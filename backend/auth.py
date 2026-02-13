"""
Authentication Module - JWT Token Management
Handles creation and validation of JSON Web Tokens for admin authentication.
"""

from jose import jwt
from datetime import datetime, timedelta

# Secret key used to sign JWT tokens - MUST be kept secure
# TODO: Move to environment variable in production for security
SECRET_KEY = "super_secret_key"

# Algorithm used for JWT encoding/decoding
ALGORITHM = "HS256"  # HMAC with SHA-256


def create_token(username: str) -> str:
    """
    Generate a JWT access token for a user.
    
    The token contains:
        - sub (subject): The username
        - exp (expiration): Token validity timestamp
    
    Args:
        username: The username to encode in the token (e.g., "admin")
        
    Returns:
        str: Encoded JWT token as a string
        
    Example:
        >>> token = create_token("admin")
        >>> # Returns: "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..."
    """
    # Create the token payload with username and expiration time
    payload = {
        "sub": username,  # Subject (username) - standard JWT claim
        "exp": datetime.utcnow() + timedelta(hours=2)  # Token expires in 2 hours
    }
    
    # Encode the payload into a JWT token using the secret key
    return jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)


def decode_token(token: str) -> dict:
    """
    Decode and validate a JWT token.
    
    This function will:
        1. Verify the token signature using SECRET_KEY
        2. Check if the token has expired
        3. Return the decoded payload if valid
    
    Args:
        token: The JWT token string to decode
        
    Returns:
        dict: Decoded token payload containing 'sub' and 'exp'
        
    Raises:
        jose.exceptions.JWTError: If token is invalid or expired
        
    Example:
        >>> payload = decode_token(token)
        >>> print(payload["sub"])  # Prints: "admin"
    """
    # Decode and verify the token
    # This will raise an exception if:
    #   - Token signature is invalid
    #   - Token has expired
    #   - Token format is malformed
    return jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])