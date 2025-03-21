# src/utils/advanced_shortener.py
import hashlib
import base64

def generate_short_code_improved(url, length=6):
    """
    An improved algorithm that uses base64 encoding of a hash.
    
    Args:
        url (str): The original URL to shorten
        length (int): Length of the short code
        
    Returns:
        str: A unique short code
    """
    # Create a SHA-256 hash of the URL (more collision-resistant than MD5)
    url_hash = hashlib.sha256(url.encode()).digest()
    
    # Use base64 encoding for more efficient character usage
    # Replace characters that might cause issues in URLs
    encoded = base64.urlsafe_b64encode(url_hash).decode('utf-8')
    
    # Take just what we need and remove any padding
    short_code = encoded.replace('=', '').replace('-', 'a').replace('_', 'Z')[:length]
    
    return short_code