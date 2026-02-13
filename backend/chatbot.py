"""
Chatbot Module - Semantic FAQ Matching
Uses sentence transformers to find the most relevant FAQ answer for user questions.
Implements cosine similarity for semantic search.
"""

from sentence_transformers import SentenceTransformer, util
from database import faq_collection

# Load the sentence transformer model for generating embeddings
# all-MiniLM-L6-v2 is a lightweight, fast model that produces 384-dimensional embeddings
# Good balance between speed and quality for FAQ matching
model = SentenceTransformer("all-MiniLM-L6-v2")


def load_faqs() -> list:
    """
    Load all FAQ documents from the MongoDB database.
    
    Returns:
        list: List of FAQ dictionaries containing 'question' and 'answer' fields
              The _id field is excluded from results
              
    Example:
        >>> faqs = load_faqs()
        >>> # Returns: [{"question": "What is...", "answer": "It is..."}, ...]
    """
    # Query all FAQs from database, exclude MongoDB _id field
    return list(faq_collection.find({}, {"_id": 0}))


def get_best_faq(user_question: str) -> tuple[str, float]:
    """
    Find the most semantically similar FAQ answer for a given question.
    
    This function:
        1. Loads all FAQs from database
        2. Converts FAQ questions and user question to embeddings (vectors)
        3. Computes cosine similarity between user question and all FAQ questions
        4. Returns the answer with highest similarity score
    
    How it works:
        - Sentence embeddings capture semantic meaning beyond keyword matching
        - Cosine similarity measures how "close" two embeddings are (0 to 1)
        - Higher score = more similar meaning
        
    Args:
        user_question: The question asked by the user
        
    Returns:
        tuple: (answer, confidence_score)
            - answer (str): The best matching FAQ answer
            - confidence_score (float): Similarity score between 0 and 1
            
    Example:
        >>> answer, confidence = get_best_faq("How do I reset my password?")
        >>> print(f"Answer: {answer}, Confidence: {confidence}")
        # Output: Answer: Click forgot password..., Confidence: 0.856
    """
    # Load all available FAQs from database
    faqs = load_faqs()

    # Handle case when database has no FAQs
    if not faqs:
        return "No FAQs available", 0.0

    # Extract just the question text from each FAQ document
    faq_questions = [faq["question"] for faq in faqs]

    # Convert all FAQ questions to embeddings (numerical vector representations)
    # convert_to_tensor=True enables GPU acceleration if available
    faq_embeddings = model.encode(faq_questions, convert_to_tensor=True)
    
    # Convert user's question to an embedding using the same model
    query_embedding = model.encode(user_question, convert_to_tensor=True)

    # Calculate cosine similarity between user question and all FAQ questions
    # Returns a tensor of scores, one for each FAQ
    # Score ranges from -1 (opposite) to 1 (identical)
    # In practice, scores are usually between 0 and 1 for natural language
    scores = util.cos_sim(query_embedding, faq_embeddings)[0]

    # Find the index of the FAQ with the highest similarity score
    best_idx = scores.argmax().item()
    
    # Get the actual similarity score and round to 3 decimal places
    # Convert from tensor to Python float for JSON serialization
    best_score = round(float(scores[best_idx]), 3)

    # Retrieve the answer from the best matching FAQ
    best_answer = faqs[best_idx]["answer"]

    # Return both the answer and confidence score as a tuple
    return best_answer, best_score