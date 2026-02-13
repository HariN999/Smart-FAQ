"""
Smart FAQ API - Main Application File
This FastAPI application provides endpoints for FAQ question answering and admin management.
"""

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


# Initialize HTTP Bearer security scheme for JWT token authentication
security = HTTPBearer()

def verify_token(credentials=Depends(security)):
    """
    Dependency function to verify JWT tokens for protected routes.
    
    Args:
        credentials: HTTPBearer credentials containing the JWT token
        
    Raises:
        HTTPException: 403 error if token is invalid or expired
    """
    try:
        # Attempt to decode and validate the JWT token
        decode_token(credentials.credentials)
    except Exception:
        # If decoding fails (invalid/expired token), raise 403 Forbidden
        raise HTTPException(status_code=403, detail="Invalid token")


# Initialize FastAPI application with title
app = FastAPI(title="Smart-FAQ API")

# Configure CORS middleware to allow cross-origin requests from frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # TODO: Restrict to specific origins in production for security
    allow_credentials=True,  # Allow cookies and authorization headers
    allow_methods=["*"],  # Allow all HTTP methods (GET, POST, DELETE, etc.)
    allow_headers=["*"],  # Allow all headers
)

# Configuration constants for low confidence handling (Issue #5)
LOW_CONFIDENCE_THRESHOLD = 0.4  # Minimum confidence score to return the answer
LOW_CONFIDENCE_MESSAGE = "Sorry, I couldn't find a confident answer. Try rephrasing your question."


# -----------------------------
# Request / Response Schemas
# -----------------------------

class QuestionRequest(BaseModel):
    """Schema for incoming user questions."""
    question: str  # The user's question text


class AnswerResponse(BaseModel):
    """Schema for FAQ answer responses."""
    answer: str  # The answer text to return to user
    confidence: float | None = None  # Confidence score (0-1), prepares Issue #7


# -----------------------------
# API ROUTES (Issue #9)
# -----------------------------

@app.get("/")
def root():
    """
    Health check endpoint to verify API is running.
    
    Returns:
        dict: Simple message confirming API status
    """
    return {"message": "Smart-FAQ FastAPI running"}


@app.post("/ask", response_model=AnswerResponse)
def ask_question(data: QuestionRequest):
    """
    Main endpoint for users to ask questions and receive FAQ answers.
    Uses semantic similarity to find the best matching FAQ.
    
    Args:
        data: QuestionRequest containing the user's question
        
    Returns:
        AnswerResponse: Contains the answer text and confidence score
        
    Logic:
        1. Find best matching FAQ using sentence embeddings
        2. Check if confidence meets threshold (Issue #5)
        3. Return answer or low confidence message
    """
    # Get the best matching FAQ from the chatbot module
    result = get_best_faq(data.question)

    # Handle different return formats (with or without confidence score)
    if isinstance(result, tuple):
        # If tuple returned, unpack answer and confidence
        answer, confidence = result
    else:
        # If only answer returned (legacy format), set confidence to None
        answer = result
        confidence = None

    # Issue #5: If confidence is below threshold, return generic message
    if confidence is not None and confidence < LOW_CONFIDENCE_THRESHOLD:
        answer = LOW_CONFIDENCE_MESSAGE

    return {
        "answer": answer,
        "confidence": confidence
    }


# -----------------------------
# Admin Authentication Routes
# -----------------------------

@app.post("/admin/login")
def login():
    """
    Admin login endpoint that generates a JWT token.
    
    Note: This is a simplified auth system. In production, you should:
        - Verify username/password credentials
        - Implement rate limiting
        - Use secure password hashing
        
    Returns:
        dict: Contains the JWT access token
    """
    # Create a JWT token for the "admin" user (hardcoded for simplicity)
    token = create_token("admin")
    return {"access_token": token}


@app.get("/admin/protected")
def protected_route(user=Depends(verify_token)):
    """
    Test endpoint to verify admin authentication is working.
    Requires valid JWT token in Authorization header.
    
    Args:
        user: Injected by verify_token dependency (unused but validates token)
        
    Returns:
        dict: Confirmation message if token is valid
    """
    return {"message": "Admin access granted"}


# -----------------------------
# Admin FAQ Management Routes
# -----------------------------

@app.get("/admin/faqs")
def get_faqs(user=Depends(verify_token)):
    """
    Retrieve all FAQs from the database.
    Protected endpoint - requires admin authentication.
    
    Args:
        user: Injected by verify_token dependency
        
    Returns:
        list: All FAQ documents with _id converted to string
    """
    # Fetch all FAQ documents from MongoDB
    faqs = list(faq_collection.find())
    
    # Convert MongoDB ObjectId to string for JSON serialization
    for f in faqs:
        f["_id"] = str(f["_id"])
    
    return faqs


@app.post("/admin/faqs")
def add_faq(data: dict = Body(...), user=Depends(verify_token)):
    """
    Add a new FAQ to the database.
    Protected endpoint - requires admin authentication.
    
    Args:
        data: Dictionary containing 'question' and 'answer' fields
        user: Injected by verify_token dependency
        
    Returns:
        dict: Success message
    """
    # Insert new FAQ document into MongoDB
    faq_collection.insert_one({
        "question": data["question"],
        "answer": data["answer"]
    })
    return {"message": "FAQ added"}


@app.delete("/admin/faqs/{faq_id}")
def delete_faq(faq_id: str, user=Depends(verify_token)):
    """
    Delete an FAQ by its ID.
    Protected endpoint - requires admin authentication.
    
    Args:
        faq_id: MongoDB ObjectId as string
        user: Injected by verify_token dependency
        
    Returns:
        dict: Success message
    """
    # Convert string ID to ObjectId and delete from MongoDB
    faq_collection.delete_one({"_id": ObjectId(faq_id)})
    return {"message": "FAQ deleted"}