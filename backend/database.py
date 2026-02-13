"""
Database Module - MongoDB Connection Setup
Establishes connection to MongoDB and provides access to collections.
"""

from pymongo import MongoClient

# Create MongoDB client connection to local instance
# Connection string format: mongodb://[host]:[port]
# Default MongoDB port is 27017
# TODO: In production, use environment variables for connection string
#       and consider authentication with username/password
client = MongoClient("mongodb://localhost:27017")

# Select the database named "smartfaq"
# If database doesn't exist, MongoDB will create it on first write operation
db = client["smartfaq"]

# Get reference to the "faqs" collection within the smartfaq database
# Collections are similar to tables in relational databases
# If collection doesn't exist, MongoDB will create it on first insert
faq_collection = db["faqs"]

# Example FAQ document structure in this collection:
# {
#     "_id": ObjectId("..."),           # MongoDB auto-generated unique ID
#     "question": "What is your name?", # The FAQ question text
#     "answer": "I am SmartFAQ bot."    # The FAQ answer text
# }