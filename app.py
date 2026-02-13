from fastapi import FastAPI, Form
from fastapi.responses import HTMLResponse
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from chatbot import get_best_faq

app = FastAPI(title="Smart-FAQ API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # change later in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# -----------------------------
# Request / Response Schemas
# -----------------------------
class QuestionRequest(BaseModel):
    question: str


class AnswerResponse(BaseModel):
    answer: str
    confidence: float | None = None   # prepares Issue #7


# -----------------------------
# API ROUTES (Issue #9)
# -----------------------------
@app.get("/")
def root():
    return {"message": "Smart-FAQ FastAPI running"}


@app.post("/ask", response_model=AnswerResponse)
def ask_question(data: QuestionRequest):
    """
    Main semantic FAQ endpoint
    """
    result = get_best_faq(data.question)

    # Support future upgrade where chatbot returns (answer, confidence)
    if isinstance(result, tuple):
        answer, confidence = result
    else:
        answer = result
        confidence = None

    return {
        "answer": answer,
        "confidence": confidence
    }
