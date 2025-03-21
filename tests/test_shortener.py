# tests/test_shortener.py
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.utils.shortener import generate_short_code

def test_generate_short_code():
    # Test that the function returns a string of the correct length
    url = "https://www.example.com/very/long/url/that/needs/shortening"
    short_code = generate_short_code(url, length=6)
    assert isinstance(short_code, str)
    assert len(short_code) == 6
    print(short_code)
    
    # Test that different URLs get different codes
    url2 = "https://www.example.com/another/different/url"
    short_code2 = generate_short_code(url2, length=6)
    assert short_code != short_code2
    print(short_code2)

if __name__ == "__main__":
    test_generate_short_code()
    print("All tests passed!")