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

def test_simple_compression_decompression():
    """Test basic compression and decompression."""
    test_data = b'hello world hello world'
    compressed = compress(test_data)
    assert compressed != test_data  # Ensure some compression occurs
    decompressed = decompress(compressed)
    assert decompressed == test_data

def test_repeated_pattern():
    """Test compression of data with repeated patterns."""
    test_data = b'AAAAAAAAAAAAAAAA'
    compressed = compress(test_data)
    assert len(compressed) < len(test_data)  # Ensure compression
    decompressed = decompress(compressed)
    assert decompressed == test_data

def test_random_data():
    """Test compression of random-like data."""
    test_data = os.urandom(1024)
    compressed = compress(test_data)
    decompressed = decompress(compressed)
    assert decompressed == test_data

def test_error_handling():
    """Test error handling for invalid inputs."""
    with pytest.raises(TypeError):
        compress("not bytes")
    
    with pytest.raises(TypeError):
        decompress("not bytes")
    
    # Malformed compressed data
    with pytest.raises(ValueError):
        decompress(b'\xFF\xFF')  # Invalid compressed token

def test_reversibility():
    """Ensure multiple rounds of compression and decompression work."""
    test_data = b'This is a test string with some repeated content repeated content'
    compressed1 = compress(test_data)
    decompressed1 = decompress(compressed1)
    
    compressed2 = compress(decompressed1)
    decompressed2 = decompress(compressed2)
    
    assert decompressed1 == test_data
    assert decompressed2 == test_data