from flask import Flask, render_template, request
from chatbot import get_best_faq

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    answer = ""
    if request.method == "POST":
        question = request.form["question"]
        answer = get_best_faq(question)

    return render_template("index.html", answer=answer)

if __name__ == "__main__":
    app.run(debug=True)

