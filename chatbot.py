import pickle
import torch
from sentence_transformers import util

# Load trained model
with open("faq_model.pkl", "rb") as f:
    model, questions, answers, question_embeddings = pickle.load(f)

def get_best_faq(user_query):
    """Find the most relevant FAQ response using semantic similarity"""
    try:
        # Encode the user query
        query_embedding = model.encode(user_query, convert_to_tensor=True)
        
        # Calculate similarity scores
        scores = util.pytorch_cos_sim(query_embedding, question_embeddings)[0]
        
        # Get the index of the highest scoring question
        best_match_idx = torch.argmax(scores).item()
        
        return questions[best_match_idx], answers[best_match_idx]
    except Exception as e:
        print(f"Error in get_best_faq: {str(e)}")
        return user_query, "I couldn't find a good answer to that question."

def classify_domain(query):
    """Classify the query into a domain based on keywords"""
    query = query.lower()
    
    domain_keywords = {
        'account': ['password', 'login', 'account', 'sign in', 'register'],
        'billing': ['payment', 'credit', 'card', 'bill', 'invoice', 'price'],
        'technical': ['error', 'bug', 'crash', 'technical', 'issue', 'problem'],
        'features': ['how to', 'use', 'feature', 'guide', 'tutorial', 'instruction']
    }
    
    for domain, keywords in domain_keywords.items():
        if any(keyword in query for keyword in keywords):
            return domain.capitalize()
    
    return 'General'
