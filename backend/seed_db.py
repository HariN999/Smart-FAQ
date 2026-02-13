from pymongo import MongoClient
import json

# 🔧 Change DB name if yours is different
client = MongoClient("mongodb://localhost:27017")
db = client["smartfaq"]
collection = db["faqs"]

with open("data/seed_faqs.json") as f:
    faqs = json.load(f)

collection.insert_many(faqs)

print("✅ Database seeded successfully!")
