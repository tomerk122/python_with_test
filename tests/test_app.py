import pytest
from app import get_website_status

def test_get_website_status():
    assert get_website_status("https://www.github.com") == 200
