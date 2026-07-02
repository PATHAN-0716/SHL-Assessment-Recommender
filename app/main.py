from fastapi import FastAPI
from app.api.routes import router

app = FastAPI(
    title="SHL Assessment Recommendation API",
)


@app.get("/")
def home():
    return {
        "message": "SHL Assessment Recommendation API is running."
    }


app.include_router(router)