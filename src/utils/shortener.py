# src/utils/shortener.py
import random
import string
import hashlib

def generate_short_code(url, length=6):
    '''
    Generate a short code for a given URL.
    
    Args:
        url (str): The original URL to shorten
        length (int): Length of the short code
        
    Returns:
        str: A unique short code
    '''
    # Create a hash of the URL
    url_hash = hashlib.md5(url.encode()).hexdigest()
    
    # Take the first 'length' characters of the hash
    # Convert to base62 (a-z, A-Z, 0-9) for better readability
    chars = string.ascii_letters + string.digits
    short_code = ''.join(random.choice(chars) for _ in range(length))
    
    return short_code