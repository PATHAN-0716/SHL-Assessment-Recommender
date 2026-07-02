# SHL Assessment Recommendation System

An AI-powered assessment recommendation system that recommends the most relevant SHL assessments based on a user's hiring requirements.

The application uses Retrieval-Augmented Generation (RAG) by combining semantic search over the SHL Product Catalog with Google's Gemini model to generate accurate, context-aware recommendations.

---

## Project Overview

Recruiters often describe hiring requirements in natural language rather than searching manually through hundreds of available assessments.

This project allows users to enter hiring requirements such as:

> "Need a Java Developer assessment"

The system retrieves the most relevant SHL assessments from the product catalog using semantic similarity search and generates a structured recommendation containing:

- Recommended assessments
- Assessment duration
- Remote testing availability
- Adaptive support
- Available languages
- Official SHL links
- Reason for recommendation

---

## Features

- Semantic search using FAISS vector database
- RAG-based assessment recommendation
- Google Gemini integration for response generation
- Multi-turn conversation support
- FastAPI REST API
- Structured recommendation table
- Health check endpoint
- Modular and scalable architecture

---

## Tech Stack

### Backend

- Python 3.12
- FastAPI

### AI & NLP

- Google Gemini API
- HuggingFace Embeddings
- LangChain

### Vector Search

- FAISS

### Data Processing

- JSON
- Pydantic

---

## Project Architecture

```

User Request

↓

FastAPI

↓

ChatService

↓

Conversation Manager

↓

FAISS Retriever

↓

Prompt Builder

↓

Gemini

↓

Recommendation Response

```

---

## Project Structure

```

SHL-Assessment-Recommender/

├── app/
│ ├── api/
│ ├── data/
│ ├── embeddings/
│ ├── llm/
│ ├── models/
│ ├── prompts/
│ ├── retriever/
│ └── services/
│
├── scripts/
├── vector_store/
├── requirements.txt
├── main.py
└── README.md

```

---

## Installation

### Clone the repository

```bash
git clone <repository-url>

cd SHL-Assessment-Recommender
```

### Create virtual environment

```bash
python -m venv .venv
```

### Activate virtual environment

Windows

```bash
.venv\Scripts\activate
```

Linux / Mac

```bash
source .venv/bin/activate
```

### Install dependencies

```bash
pip install -r requirements.txt
```

---

## Environment Variables

Create a `.env` file in the project root.

```env
GOOGLE_API_KEY=YOUR_API_KEY
```

---

## Build Vector Database

```bash
python -m scripts.build_index
```

---

## Run the Application

```bash
uvicorn main:app --reload
```

API Documentation

```

http://127.0.0.1:8000/docs

```

---

## API Endpoints

### POST /chat

Generates assessment recommendations.

Example Request

```json
{
  "session_id": "123",
  "message": "Need assessment"
}
```

Follow-up

```json
{
  "session_id": "123",
  "message": "Java Developer"
}
```

---

### GET /health

Returns API health status.

Example Response

```json
{
  "status": "healthy"
}
```

---

## Example Output

The system returns a structured recommendation including:

- Assessment Name
- Remote Testing
- Adaptive Support
- Duration
- Languages
- Official SHL URL
- Recommendation Reason

---

## How It Works

1. Load SHL assessment catalog.
2. Convert assessments into searchable documents.
3. Generate embeddings using HuggingFace.
4. Store embeddings in FAISS.
5. Accept user hiring requirements.
6. Retrieve the most relevant assessments.
7. Generate recommendations using Gemini.
8. Return structured recommendations through FastAPI.

---

## Future Improvements

- Support assessment comparison.
- Persistent conversation memory.
- Authentication.
- Docker deployment.
- Cloud deployment.
- Advanced filtering and ranking.

```

---

# ⭐ I would make **one addition** because recruiters like diagrams.

After **Project Architecture**, insert this:

```text
                    User
                      │
                      ▼
               FastAPI (/chat)
                      │
                      ▼
                ChatService
                      │
      ┌───────────────┼───────────────┐
      ▼               ▼               ▼
Conversation     Retriever        Memory
 Manager            │
                    ▼
             FAISS Vector Store
                    │
                    ▼
            Prompt Builder
                    │
                    ▼
               Gemini API
                    │
                    ▼
          Recommendation Response
```

It takes 10 seconds to read and immediately shows the reviewer that your architecture is modular.

---

**After the README, we'll do the final three things:**
1. Clean `requirements.txt` (remove unnecessary packages if needed).
2. Push the project to GitHub with clean commit history.
3. Verify every assignment requirement against the PDF one by one before submission.