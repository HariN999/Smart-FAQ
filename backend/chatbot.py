from sentence_transformers import SentenceTransformer, util
from database import faq_collection

model = SentenceTransformer("all-MiniLM-L6-v2")

def load_faqs():
    return list(faq_collection.find({}, {"_id": 0}))

def get_best_faq(user_question: str):

    faqs = load_faqs()

    if not faqs:
        return "No FAQs available", 0.0

    faq_questions = [faq["question"] for faq in faqs]

    faq_embeddings = model.encode(faq_questions, convert_to_tensor=True)
    query_embedding = model.encode(user_question, convert_to_tensor=True)

    scores = util.cos_sim(query_embedding, faq_embeddings)[0]

    best_idx = scores.argmax().item()
    best_score = round(float(scores[best_idx]), 3)

    best_answer = faqs[best_idx]["answer"]

    return best_answer, best_score
