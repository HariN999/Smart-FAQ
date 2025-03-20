import pickle
from sentence_transformers import SentenceTransformer

# Load FAQs
faqs = [
    ("How do I reset my password?", "Go to settings > Reset password."),
    ("How to change email?", "Go to account settings and update email."),
]

model = SentenceTransformer("all-MiniLM-L6-v2")

questions = [q[0] for q in faqs]
answers = [q[1] for q in faqs]
question_embeddings = model.encode(questions)

# Save model
with open("faq_model.pkl", "wb") as f:
    pickle.dump((model, questions, answers, question_embeddings), f)
