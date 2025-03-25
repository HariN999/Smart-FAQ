import pickle
import pymysql
from sentence_transformers import SentenceTransformer

# Load the trained model
MODEL_PATH = "faq_model.pkl"

def load_model():
    """Load the trained model and stored embeddings."""
    with open(MODEL_PATH, "rb") as f:
        model, questions, answers, question_embeddings = pickle.load(f)
    return model, questions, answers, question_embeddings

def connect_db():
    """Establish connection with MySQL database."""
    return pymysql.connect(
        host="localhost",
        user="root",
        password="mysql",
        database="smartfaq",
        charset="utf8mb4",
        cursorclass=pymysql.cursors.DictCursor
    )

def fetch_faqs():
    """Fetch all FAQs from the MySQL database."""
    connection = connect_db()
    with connection.cursor() as cursor:
        cursor.execute("SELECT question, answer FROM faq_table")
        faqs = cursor.fetchall()
    connection.close()
    return [(faq["question"], faq["answer"]) for faq in faqs]

def update_faq_model():
    """Update the FAQ model with new questions and answers from the database."""
    print("Fetching updated FAQs from the database...")
    faqs = fetch_faqs()
    
    if not faqs:
        print("No FAQs found in the database.")
        return
    
    questions, answers = zip(*faqs)

    # Load the sentence transformer model
    model = SentenceTransformer("all-MiniLM-L6-v2")
    question_embeddings = model.encode(questions, convert_to_tensor=True)

    # Save the updated model
    with open(MODEL_PATH, "wb") as f:
        pickle.dump((model, questions, answers, question_embeddings), f)

    print("FAQ model updated successfully!")

if __name__ == "__main__":
    update_faq_model()
