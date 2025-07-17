import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), 'src')))

from palindrome import is_palindrome

def test_is_palindrome():
    assert is_palindrome("racecar")
    assert is_palindrome("A man a plan a canal Panama")
    assert is_palindrome("madam")
    assert not is_palindrome("hello")
    assert not is_palindrome("Python")
