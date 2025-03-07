"""
LZRW (Lempel-Ziv Ross Williams) Compression Algorithm Implementation

This module provides a simplified version of the LZRW compression algorithm.
"""

def compress(input_data):
    """
    Compress input data using a simplified LZRW-like algorithm.
    
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
        # Look for the longest match
        best_match_length = 0
        best_match_offset = 0
        
        # Generate candidate length range
        for length in range(min(15, len(input_data) - current_pos), 0, -1):
            sequence = input_data[current_pos:current_pos + length]
            
            # Check if sequence exists in dictionary
            if sequence in dictionary:
                best_match_length = length
                best_match_offset = current_pos - dictionary[sequence]
                break
        
        # Update dictionary with current sequence
        if current_pos + 3 < len(input_data):
            three_byte_sequence = input_data[current_pos:current_pos + 3]
            dictionary[three_byte_sequence] = current_pos
        
        # Encode match or literal
        if best_match_length > 2:
            # Compressed token
            output.append(input_data[current_pos])  # Literal byte
            compressed_token = ((best_match_offset & 0xFFF) << 4) | (best_match_length & 0x0F)
            output.append((compressed_token >> 8) | 0x80)  # High byte with compression flag
            output.append(compressed_token & 0xFF)  # Low byte
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
        # Ensure we have at least 2 bytes for processing
        if current_pos + 1 >= len(compressed_data):
            output.append(compressed_data[current_pos])
            break
        
        # Check the current and next byte
        current_byte = compressed_data[current_pos]
        next_byte = compressed_data[current_pos + 1]
        
        if next_byte & 0x80:
            # Compressed token
            output.append(current_byte)
            
            # Ensure we have the full compressed token
            if current_pos + 2 >= len(compressed_data):
                break
            
            # Extract token
            token = ((next_byte & 0x7F) << 8) | compressed_data[current_pos + 2]
            
            # Extract offset and length
            offset = (token >> 4) & 0xFFF
            length = token & 0x0F
            
            # Validate offset and length
            if length == 0 or offset == 0 or offset > len(output):
                output.append(next_byte)
                current_pos += 1
                continue
            
            # Copy matched sequence
            start = len(output) - offset
            for _ in range(length):
                output.append(output[start])
                start += 1
            
            current_pos += 3
        else:
            # Literal byte
            output.append(current_byte)
            current_pos += 1
    
    return bytes(output)