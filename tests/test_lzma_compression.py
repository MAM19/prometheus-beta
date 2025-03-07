import pytest
import lzma
from src.lzma_compression import lzma_compress, lzma_decompress

def test_lzma_compress_string():
    """Test compressing a string"""
    input_str = "Hello, world! This is a test of LZMA compression."
    compressed = lzma_compress(input_str)
    assert isinstance(compressed, bytes)
    # Ensure compressed data is not the same as original
    assert compressed != input_str.encode('utf-8')

def test_lzma_compress_bytes():
    """Test compressing bytes"""
    input_bytes = b"Raw binary data for compression"
    compressed = lzma_compress(input_bytes)
    assert isinstance(compressed, bytes)
    # Ensure compressed data is not the same as original
    assert compressed != input_bytes

def test_lzma_compress_different_levels():
    """Test compression at different levels"""
    # Use larger repeated data to make compression more predictable
    input_data = "Repeated data " * 1000
    compressed_low = lzma_compress(input_data, compression_level=1)
    compressed_high = lzma_compress(input_data, compression_level=9)
    
    # Allow for some variance, but high compression should generally be smaller
    assert len(compressed_high) <= len(compressed_low)

def test_lzma_decompress():
    """Test full compression and decompression cycle"""
    original_data = "Test data for compression and decompression"
    compressed = lzma_compress(original_data)
    decompressed = lzma_decompress(compressed)
    
    assert decompressed.decode('utf-8') == original_data

def test_lzma_compress_invalid_level():
    """Test invalid compression level"""
    with pytest.raises(ValueError, match="Compression level must be between 0 and 9."):
        lzma_compress("test", compression_level=10)

def test_lzma_compress_invalid_type():
    """Test invalid input type"""
    with pytest.raises(TypeError, match="Input must be str or bytes."):
        lzma_compress(123)

def test_lzma_decompress_invalid_type():
    """Test invalid input type for decompression"""
    with pytest.raises(TypeError, match="Input must be bytes."):
        lzma_decompress("not bytes")

def test_lzma_decompress_corrupted_data():
    """Test decompression of corrupted data"""
    with pytest.raises(lzma.LZMAError):
        lzma_decompress(b'corrupted data')

def test_empty_input():
    """Test compression and decompression of empty input"""
    empty_str = ""
    compressed = lzma_compress(empty_str)
    decompressed = lzma_decompress(compressed)
    assert decompressed.decode('utf-8') == empty_str