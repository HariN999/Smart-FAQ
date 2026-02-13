# 🧠 Smart-FAQ

AI-powered semantic FAQ system built with **FastAPI, React, MongoDB, and SentenceTransformers**.
Instead of keyword matching, Smart-FAQ understands the *meaning* of a question using embeddings and returns the most relevant answer with a confidence score.

---

## 🚀 Overview

Smart-FAQ is a full-stack AI application that allows users to ask natural-language questions and receive intelligent responses from a semantic FAQ database.

The system includes:

* ⚡ FastAPI backend
* 🎨 React frontend
* 🔐 JWT-based admin authentication
* 🧠 Semantic search using embeddings
* 🍃 MongoDB database

Admins can manage FAQs through a protected dashboard, while users interact with a clean AI-style interface.

---

## ✨ Features

* Semantic question matching (not keyword search)
* Confidence score with each answer
* Low-confidence fallback message
* Admin dashboard (Add/Delete FAQs)
* JWT-protected routes
* MongoDB storage
* Responsive modern UI

---

## 🧠 Architecture

Frontend (React)
→ sends request to FastAPI

FastAPI Backend
→ generates embeddings
→ queries MongoDB
→ finds best semantic match

MongoDB
→ stores FAQ documents

Embedding Model
→ SentenceTransformers (`all-MiniLM-L6-v2`)

---

## 🛠 Tech Stack

**Frontend**

* React (Vite)
* Fetch API
* CSS (Glass-style UI)

**Backend**

* FastAPI
* Uvicorn
* SentenceTransformers
* PyTorch
* JWT Authentication

**Database**

* MongoDB

---

## ⚙️ Setup Instructions

### 🔧 Backend Setup

```bash
cd backend
pip install -r requirements.txt
```

Start MongoDB locally.

Seed demo data:

```bash
python seed_db.py
```

Run backend:

```bash
uvicorn app:app --reload
```

API Docs:

```
http://127.0.0.1:8000/docs
```

---

### 🎨 Frontend Setup

```bash
cd frontend/smartfaq-frontend
npm install
npm run dev
```

Frontend runs at:

```
http://localhost:5173
```

---

## 🔌 API Endpoints

### Public

* `GET /` — Health check
* `POST /ask` — Ask semantic question

### Admin (JWT Protected)

* `POST /admin/login`
* `GET /admin/faqs`
* `POST /admin/faqs`
* `DELETE /admin/faqs/{faq_id}`

---

## 🔐 Admin Access

Admin authentication uses JWT tokens.

Login through the Admin Mode UI or via:

```
POST /admin/login
```

Token is required for protected routes.

---

## 🌱 Seed Database

To populate MongoDB with demo FAQs:

```bash
python seed_db.py
```

This loads sample FAQs from:

```
backend/data/seed_faqs.json
```

---

## 📸 Screenshots

### User Interface

![User UI](screenshots/User.png)

### Admin Dashboard

![Admin UI](screenshots/Admin.png)

### API Documentation

![Swagger](screenshots/Swagger.png)

---

## 🎯 Future Improvements

* Vector database integration
* Role-based admin permissions
* FAQ categories and filtering
* Deployment with Docker

---

## 📄 License

MIT License

---

## 👤 Author

Hariharan Narlakanti

