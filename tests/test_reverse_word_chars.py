import pytest
from src.reverse_word_chars import reverse_sentence_word_chars

def test_reverse_sentence_word_chars():
    # Test basic functionality
    assert reverse_sentence_word_chars("hello world") == "olleh dlrow"
    
    # Test empty string
    assert reverse_sentence_word_chars("") == ""
    
    # Test single word
    assert reverse_sentence_word_chars("python") == "nohtyp"
    
    # Test multiple words
    assert reverse_sentence_word_chars("abc def ghi") == "cba fed ihg"
    
    # Test words with mixed case
    assert reverse_sentence_word_chars("Hello World") == "olleH dlroW"
    
    # Test words with punctuation and numbers
    assert reverse_sentence_word_chars("hello123 world!") == "321olleh !dlrow"
    
    # Test single character words
    assert reverse_sentence_word_chars("a b c") == "a b c"

def test_input_types():
    # Test with non-string input
    with pytest.raises(AttributeError):
        reverse_sentence_word_chars(123)
    
    with pytest.raises(AttributeError):
        reverse_sentence_word_chars(None)