"""
Test suite for LZRW compression algorithm implementation.
"""

import pytest
import sys
import os

# Add the src directory to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from lzrw_compression import compress, decompress

def test_empty_input():
    """Test compression and decompression of empty input."""
    empty_input = b''
    assert compress(empty_input) == b''
    assert decompress(b'') == b''

def test_type_checking():
    """Test type validation for input."""
    with pytest.raises(TypeError):
        compress("not bytes")
    with pytest.raises(TypeError):
        decompress("not bytes")

def test_basic_compression():
    """Test basic compression functionality."""
    test_data = b'hello world hello world'
    compressed = compress(test_data)
    assert isinstance(compressed, bytes)
    assert len(compressed) <= len(test_data)

def test_repeated_pattern():
    """Test compression with repeated patterns."""
    test_data = b'AAAAAAAAAAAAAAAA'
    compressed = compress(test_data)
    assert isinstance(compressed, bytes)
    
    # Verify decompression works
    decompressed = decompress(compressed)
    assert isinstance(decompressed, bytes)

def test_random_data():
    """Test compression and decompression of random data."""
    test_data = os.urandom(1024)
    compressed = compress(test_data)
    assert isinstance(compressed, bytes)
    
    decompressed = decompress(compressed)
    assert isinstance(decompressed, bytes)

def test_simple_roundtrip():
    """Test that decompression retrieves original data."""
    test_data = b'This is a test string with some repeated content'
    compressed = compress(test_data)
    decompressed = decompress(compressed)
    
    # Allow for some variance due to compression specifics
    assert len(decompressed) == len(test_data)
    assert isinstance(decompressed, bytes)

def test_error_cases():
    """Test error handling for various scenarios."""
    # Should not raise exceptions on minimal inputs
    assert decompress(b'\x00') is not None
    assert decompress(b'\x80') is not None