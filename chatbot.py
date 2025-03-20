import pickle
import torch
from sentence_transformers import util

# Load trained model
with open("faq_model.pkl", "rb") as f:
    model, questions, answers, question_embeddings = pickle.load(f)

def get_best_faq(user_query):
    query_embedding = model.encode(user_query, convert_to_tensor=True)
    scores = util.pytorch_cos_sim(query_embedding, question_embeddings)[0]
    best_match_idx = torch.argmax(scores).item()
    return questions[best_match_idx], answers[best_match_idx]
