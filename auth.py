from jose import jwt
from datetime import datetime, timedelta

SECRET_KEY = "super_secret_key"
ALGORITHM = "HS256"

def create_token(username: str):
    payload = {
        "sub": username,
        "exp": datetime.utcnow() + timedelta(hours=2)
    }
    return jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)
