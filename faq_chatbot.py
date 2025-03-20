import torch
import pickle
from sentence_transformers import util

# Load the trained model & embeddings
with open("faq_model.pkl", "rb") as f:
    model, questions, answers, question_embeddings = pickle.load(f)

def get_best_faq(user_query):
    """Find the most relevant FAQ response."""
    query_embedding = model.encode(user_query, convert_to_tensor=True)
    scores = util.pytorch_cos_sim(query_embedding, question_embeddings)[0]
    best_match_idx = torch.argmax(scores).item()
    
    return questions[best_match_idx], answers[best_match_idx]

# Example usage
user_input = "How do I reset my password?"
matched_question, response = get_best_faq(user_input)

print(f"Matched FAQ: {matched_question}")
print(f"Response: {response}")
