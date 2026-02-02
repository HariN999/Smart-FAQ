from sentence_transformers import SentenceTransformer, util
import json

model = SentenceTransformer("all-MiniLM-L6-v2")

with open("data/faq_sample.json") as f:
    faqs = json.load(f)

questions = [x["question"] for x in faqs]
answers = [x["answer"] for x in faqs]

question_embeddings = model.encode(questions, convert_to_tensor=True)

def get_best_faq(user_question):
    user_embedding = model.encode(user_question, convert_to_tensor=True)
    scores = util.cos_sim(user_embedding, question_embeddings)[0]
    best_idx = int(scores.argmax())
    return answers[best_idx]
