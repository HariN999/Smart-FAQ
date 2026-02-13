from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017")
db = client["smartfaq"]
faq_collection = db["faqs"]
