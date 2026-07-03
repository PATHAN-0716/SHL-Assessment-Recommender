"""
Purpose:
Evaluates the SHL chatbot using all conversation traces.

Run:
    python -m tests.evaluate
"""

import json
import time
from pathlib import Path

import requests

API_URL = "http://127.0.0.1:8000/chat"

TRACE_DIR = Path("tests/traces")
OUTPUT_FILE = Path("tests/evaluation_report.json")


def grounded(response: str, retrieved: list[str]) -> bool:
    """
    Returns True if at least one retrieved assessment appears
    in the generated response.
    """
    response = response.lower()

    for assessment in retrieved:
        if assessment.lower() in response:
            return True

    return False


results = []
latencies = []
grounded_count = 0

trace_files = sorted(TRACE_DIR.glob("*.md"))

for trace in trace_files:

    conversation = trace.read_text(
        encoding="utf-8"
    ).strip()

    payload = {
        "session_id": trace.stem,
        "message": conversation,
    }

    start = time.perf_counter()

    try:

        response = requests.post(
            API_URL,
            json=payload,
            timeout=120,
        )

        latency = round(
            (time.perf_counter() - start) * 1000,
            2,
        )

        latencies.append(latency)

        if response.status_code != 200:

            results.append(
                {
                    "conversation": trace.name,
                    "status": "FAILED",
                    "status_code": response.status_code,
                }
            )

            continue

        data = response.json()

        reply = data.get("response", "")

        retrieved = data.get(
            "retrieved_assessments",
            [],
        )

        is_grounded = grounded(
            reply,
            retrieved,
        )

        if is_grounded:
            grounded_count += 1

        results.append(
            {
                "conversation": trace.name,
                "status": "PASS",
                "latency_ms": latency,
                "retrieved_assessments": retrieved,
                "grounded": is_grounded,
                "response": reply,
            }
        )

    except Exception as e:

        results.append(
            {
                "conversation": trace.name,
                "status": "FAILED",
                "error": str(e),
            }
        )

summary = {
    "total_conversations": len(trace_files),
    "passed": len(
        [r for r in results if r["status"] == "PASS"]
    ),
    "failed": len(
        [r for r in results if r["status"] == "FAILED"]
    ),
    "average_latency_ms": round(
        sum(latencies) / len(latencies),
        2,
    )
    if latencies
    else 0,
    "retrieval_success_rate": round(
        (
            len(
                [
                    r
                    for r in results
                    if r.get("retrieved_assessments")
                ]
            )
            / len(trace_files)
        )
        * 100,
        2,
    )
    if trace_files
    else 0,
    "groundedness_rate": round(
        (grounded_count / len(trace_files)) * 100,
        2,
    )
    if trace_files
    else 0,
    "results": results,
}

OUTPUT_FILE.write_text(
    json.dumps(summary, indent=4),
    encoding="utf-8",
)

print("\n" + "=" * 60)
print("SHL CHATBOT EVALUATION")
print("=" * 60)
print(f"Total Conversations : {summary['total_conversations']}")
print(f"Passed              : {summary['passed']}")
print(f"Failed              : {summary['failed']}")
print(f"Avg Latency (ms)    : {summary['average_latency_ms']}")
print(f"Retrieval Success   : {summary['retrieval_success_rate']}%")
print(f"Groundedness        : {summary['groundedness_rate']}%")
print("=" * 60)
print(f"Report saved to: {OUTPUT_FILE}")