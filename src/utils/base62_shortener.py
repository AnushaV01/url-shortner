# src/utils/base62_shortener.py
import hashlib

def generate_short_code_base62(url, length=6):
    """
    Generate a short code using base62 encoding (A-Z, a-z, 0-9).
    Most efficient and don't need  clean up
    Args:
        url (str): The original URL to shorten
        length (int): Length of the short code   
    Returns:
        str: A unique short code
    """
    # Create a SHA-256 hash of the URL
    url_hash = hashlib.sha256(url.encode()).digest()
    
    # Convert the hash to an integer
    hash_int = int.from_bytes(url_hash, byteorder='big')
    
    # Define the characters for base62
    chars = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    
    # Convert to base62
    result = ""
    while hash_int > 0 and len(result) < length:
        result = chars[hash_int % 62] + result
        hash_int //= 62
    
    # Pad with characters if needed
    while len(result) < length:
        # Add padding based on another part of the hash
        padding_index = hash_int % 62 if hash_int > 0 else 0
        result = chars[padding_index] + result
        hash_int //= 62 if hash_int > 0 else 1
    
    return result