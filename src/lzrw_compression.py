"""
LZRW (Lempel-Ziv Ross Williams) Compression Algorithm Implementation

This module provides functions for LZRW compression and decompression.
"""

def compress(input_data):
    """
    Compress input data using a LZRW-inspired compression algorithm.
    
    Args:
        input_data (bytes): The input data to be compressed.
    
    Returns:
        bytes: Compressed data.
    
    Raises:
        TypeError: If input is not bytes.
    """
    # Input validation
    if not isinstance(input_data, bytes):
        raise TypeError("Input must be bytes")
    
    # If input is empty, return empty bytes
    if not input_data:
        return b''
    
    # Initialize compression parameters
    output = bytearray()
    dictionary = {}
    current_pos = 0
    
    while current_pos < len(input_data):
        # Look for the longest match in dictionary
        best_match_length = 0
        best_match_offset = 0
        
        # Check existing sequences
        for length in range(min(15, len(input_data) - current_pos), 1, -1):
            sequence = input_data[current_pos:current_pos + length]
            
            if sequence in dictionary:
                best_match_length = length
                best_match_offset = dictionary[sequence]
                break
        
        # Update dictionary with current position
        if current_pos + 3 < len(input_data):
            key = input_data[current_pos:current_pos + 3]
            dictionary[key] = current_pos
        
        # Encode match or literal
        if best_match_length > 2:
            # Compressed token with offset and length
            compressed_token = ((best_match_offset & 0xFFF) << 4) | (best_match_length & 0x0F)
            output.append((compressed_token >> 8) | 0x80)  # Mark as compressed
            output.append(compressed_token & 0xFF)
            current_pos += best_match_length
        else:
            # Literal byte
            output.append(input_data[current_pos])
            current_pos += 1
    
    return bytes(output)

def decompress(compressed_data):
    """
    Decompress data compressed with the LZRW algorithm.
    
    Args:
        compressed_data (bytes): The compressed input data.
    
    Returns:
        bytes: Decompressed data.
    
    Raises:
        TypeError: If input is not bytes.
        ValueError: If compressed data is malformed.
    """
    # Input validation
    if not isinstance(compressed_data, bytes):
        raise TypeError("Input must be bytes")
    
    # If input is empty, return empty bytes
    if not compressed_data:
        return b''
    
    output = bytearray()
    current_pos = 0
    
    while current_pos < len(compressed_data):
        # Ensure we have at least 2 bytes
        if current_pos + 1 >= len(compressed_data):
            break
        
        # Read token
        is_compressed = bool(compressed_data[current_pos] & 0x80)
        token = ((compressed_data[current_pos] & 0x7F) << 8) | compressed_data[current_pos + 1]
        current_pos += 2
        
        if is_compressed:
            # Extract offset and length
            offset = (token >> 4) & 0xFFF
            length = token & 0x0F
            
            # Validate offset and length
            if offset == 0 or length == 0 or offset > len(output):
                raise ValueError(f"Invalid compressed token at position {current_pos}")
            
            # Copy matched sequence
            start = len(output) - offset
            for i in range(length):
                output.append(output[start + i])
        else:
            # Literal byte (first token was not compressed)
            output.append(token & 0xFF)
    
    return bytes(output)