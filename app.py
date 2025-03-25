import mysql.connector
from flask import Flask, render_template, request, jsonify
from chatbot import get_best_faq, classify_domain

app = Flask(__name__)

# Database configuration
db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'mysql',
    'database': 'smartfaq'
}
if not os.path.exists('model.pkl'):
    model_url = 'https://drive.google.com/uc?id=1gB4-RxlQrgNqGeSd2b0VkxAuNPFVtwXW'
    gdown.download(model_url, 'model.pkl', quiet=False)
def get_db_connection():
    return mysql.connector.connect(**db_config)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/domains")
def get_domains():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT DISTINCT domain FROM faqs")
    domains = [row[0] for row in cursor.fetchall()]
    conn.close()

    # Ensure "General" appears first in the list
    if "General" in domains:
        domains.remove("General")
        domains.insert(0, "General")

    return jsonify({"domains": domains})


@app.route("/faq/<domain>")
def get_faqs(domain):
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT question, answer FROM faqs WHERE domain = %s", (domain,))
    faqs = cursor.fetchall()
    conn.close()
    return jsonify({"faqs": faqs})

@app.route("/chatbot", methods=["POST"])
def chatbot():
    user_query = request.json.get("query", "").strip()
    
    if not user_query:
        return jsonify({
            "question": "Empty query",
            "answer": "Please enter a question.",
            "status": "error"
        })
    
    try:
        # Get best matching FAQ
        matched_question, response = get_best_faq(user_query)
        
        # Classify domain
        domain = classify_domain(user_query)
        
        # Store in database
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO faqs (question, answer, domain) VALUES (%s, %s, %s)",
            (user_query, response, domain)
        )
        conn.commit()
        conn.close()
        
        return jsonify({
            "question": matched_question,
            "answer": response,
            "domain": domain,
            "status": "success"
        })
        
    except Exception as e:
        print(f"Error in chatbot: {str(e)}")
        return jsonify({
            "question": "Error",
            "answer": "Sorry, I encountered an error. Please try again.",
            "status": "error"
        })

if __name__ == "__main__":
    app.run(debug=True)
