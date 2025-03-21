# tests/test_base62_shortener.py
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.utils.base62_shortener import generate_short_code_base62

def test_generate_short_code_base62():
    # Test that the function returns a string of the correct length
    url = "https://www.example.com/very/long/url/that/needs/shortening"
    short_code = generate_short_code_base62(url, length=6)
    assert isinstance(short_code, str)
    assert len(short_code) == 6
    
    # Test that different URLs get different codes
    url2 = "https://www.example.com/another/different/url"
    short_code2 = generate_short_code_base62(url2, length=6)
    assert short_code != short_code2
    
    # Test that the same URL always gives the same code (deterministic)
    url3 = "https://www.example.com/very/long/url/that/needs/shortening"
    short_code3 = generate_short_code_base62(url3, length=6)
    assert short_code == short_code3
    
    # Test that only valid Base62 characters are used
    valid_chars = set("0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz")
    assert all(c in valid_chars for c in short_code)

if __name__ == "__main__":
    test_generate_short_code_base62()
    print("All tests passed!")