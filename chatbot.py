from sentence_transformers import SentenceTransformer, util

# load model once
model = SentenceTransformer("all-MiniLM-L6-v2")

# example FAQ structure
faqs = [
    {"question": "What is fertilizer?", "answer": "Fertilizer helps plants grow."},
    {"question": "How to water plants?", "answer": "Water early morning."}
]

faq_questions = [faq["question"] for faq in faqs]
faq_embeddings = model.encode(faq_questions, convert_to_tensor=True)


def get_best_faq(user_question: str):
    # Encode user query
    query_embedding = model.encode(user_question, convert_to_tensor=True)

    # Compute similarity scores
    scores = util.cos_sim(query_embedding, faq_embeddings)[0]

    # Get best match
    best_idx = scores.argmax().item()
    best_score = round(float(scores[best_idx]), 3)

    best_answer = faqs[best_idx]["answer"]

    #  NEW: return tuple
    return best_answer, best_score
