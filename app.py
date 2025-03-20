import mysql.connector
from flask import Flask, render_template, request, jsonify
from models import get_faqs, add_faq, get_domains
from chatbot import get_best_faq

app = Flask(__name__)

@app.route("/")
def home():
    domains = get_domains()
    return render_template("index.html", domains=domains)

@app.route("/faq/<domain>")
def faq_page(domain):
    faqs = get_faqs(domain)
    return render_template("faq.html", faqs=faqs, domain=domain)

@app.route("/chatbot", methods=["POST"])
def chatbot():
    user_query = request.json.get("query")
    matched_question, response = get_best_faq(user_query)
    add_faq(matched_question, response, "General")  # Store new FAQs
    return jsonify({"question": matched_question, "answer": response})

if __name__ == "__main__":
    app.run(debug=True)
