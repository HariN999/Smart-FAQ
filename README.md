# 🚀 Smart-FAQ – AI Powered Question Answering System

Smart-FAQ is an **AI-powered Frequently Asked Questions (FAQ) system** that uses Natural Language Processing (NLP) to understand user queries and return the most relevant answers from a predefined knowledge base.

It enables organizations to automate customer support, reduce response time, and provide instant, accurate answers to users.

---

## 📌 Problem Statement

Traditional FAQ systems rely on keyword matching, which often fails when users phrase questions differently.

Smart-FAQ solves this problem by using **semantic similarity and NLP techniques** so that even if a question is phrased differently, the system can still understand the intent and return the correct answer.

---

## ✅ Features

* Accepts natural language questions
* Finds the most relevant answer using semantic similarity
* Easy to extend with new FAQ data
* Simple and clean interface
* Fast response time

---

## 🛠 Tech Stack

* **Programming Language:** Python
* **Backend:** Flask
* **NLP Libraries:**

  * Scikit-learn
  * NLTK / SpaCy (if used)
* **Frontend:** HTML, CSS, JavaScript

---

## 📂 Project Structure

```
Smart-FAQ/
│
├── app.py                # Main Flask application
├── faq_data.csv / json   # FAQ dataset
├── requirements.txt      # Python dependencies
├── templates/
│   └── index.html        # Frontend UI
├── static/
│   ├── style.css
│   └── script.js
└── README.md
```

---

## ⚙️ Installation & Setup

### 1. Clone the Repository

```bash
git clone https://github.com/HariN999/Smart-FAQ.git
cd Smart-FAQ
```

### 2. Create Virtual Environment (Optional but Recommended)

```bash
python -m venv venv
source venv/bin/activate     # macOS / Linux
venv\Scripts\activate        # Windows
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the Application

```bash
python app.py
```

### 5. Open in Browser

```
http://127.0.0.1:5000
```

---

## 🧪 Example Usage

**User Question:**

```
How can I reset my password?
```

**System Response:**

```
To reset your password, go to settings and click on "Reset Password".
```

---

## 📈 Future Enhancements

* Add database instead of file-based FAQ storage
* Support voice input
* Multilingual support
* Integrate transformer-based models (BERT / Sentence Transformers)
* Admin dashboard to manage FAQs

---

## 🎯 Learning Outcomes

* Practical experience with NLP
* Flask backend development
* Semantic similarity and text preprocessing
* Building AI-powered web applications

---

## 🤝 Contributing

Contributions are welcome!

1. Fork the repository
2. Create a new branch
3. Make your changes
4. Submit a pull request

---

## 📜 License

This project is open-source and available under the **MIT License**.

---

## 👨‍💻 Author

**Hariharan**
GitHub: [https://github.com/HariN999](https://github.com/HariN999)
