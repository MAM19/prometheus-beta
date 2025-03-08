def reverse_sentence_word_chars(sentence):
    """
    Reverses the characters of each word in a given sentence.
    
    Args:
        sentence (str): The input sentence to be transformed.
    
    Returns:
        str: A new sentence with the characters of each word reversed.
    
    Examples:
        >>> reverse_sentence_word_chars("hello world")
        'olleh dlrow'
        >>> reverse_sentence_word_chars("")
        ''
        >>> reverse_sentence_word_chars("a b c")
        'a b c'
    """
    # Handle empty string case
    if not sentence:
        return ""
    
    # Split the sentence into words
    words = sentence.split()
    
    # Reverse characters of each word
    reversed_words = [''.join(reversed(word)) for word in words]
    
    # Reconstruct the sentence
    return ' '.join(reversed_words)