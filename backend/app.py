from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from chatbot import get_best_faq
from auth import create_token, decode_token
from fastapi import Depends, HTTPException
from fastapi.security import HTTPBearer
from jose import jwt
from database import faq_collection
from fastapi import Body
from bson import ObjectId


security = HTTPBearer()

def verify_token(credentials=Depends(security)):
    try:
        decode_token(credentials.credentials)
    except Exception:
        raise HTTPException(status_code=403, detail="Invalid token")


app = FastAPI(title="Smart-FAQ API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # change later in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
LOW_CONFIDENCE_THRESHOLD = 0.4
LOW_CONFIDENCE_MESSAGE = "Sorry, I couldn't find a confident answer. Try rephrasing your question."


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

    result = get_best_faq(data.question)

    if isinstance(result, tuple):
        answer, confidence = result
    else:
        answer = result
        confidence = None

    # 🔥 Issue #5 logic
    if confidence is not None and confidence < LOW_CONFIDENCE_THRESHOLD:
        answer = LOW_CONFIDENCE_MESSAGE

    return {
        "answer": answer,
        "confidence": confidence
    }

@app.post("/admin/login")
def login():
    token = create_token("admin")
    return {"access_token": token}

@app.get("/admin/protected")
def protected_route(user=Depends(verify_token)):
    return {"message": "Admin access granted"}

@app.get("/admin/faqs")
def get_faqs(user=Depends(verify_token)):
    faqs = list(faq_collection.find())
    for f in faqs:
        f["_id"] = str(f["_id"])
    return faqs

@app.post("/admin/faqs")
def add_faq(data: dict = Body(...), user=Depends(verify_token)):
    faq_collection.insert_one({
        "question": data["question"],
        "answer": data["answer"]
    })
    return {"message": "FAQ added"}

@app.delete("/admin/faqs/{faq_id}")
def delete_faq(faq_id: str, user=Depends(verify_token)):
    faq_collection.delete_one({"_id": ObjectId(faq_id)})
    return {"message": "FAQ deleted"}
