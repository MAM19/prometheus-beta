"""
LZRW (Lempel-Ziv Ross Williams) Compression Algorithm Implementation

This module provides functions for LZRW compression and decompression.
"""

def compress(input_data):
    """
    Compress input data using a LZRW-like compression algorithm.
    
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
    window_size = 4096
    current_pos = 0
    
    while current_pos < len(input_data):
        # Find longest match
        best_length = 0
        best_offset = 0
        
        # Search back in the sliding window
        search_start = max(0, current_pos - window_size)
        for start in range(search_start, current_pos):
            match_length = 0
            
            # Check how long the match continues
            while (current_pos + match_length < len(input_data) and 
                   match_length < 15 and  # 4-bit length limit
                   input_data[start + match_length] == input_data[current_pos + match_length]):
                match_length += 1
            
            # Update best match
            if match_length > best_length:
                best_length = match_length
                best_offset = current_pos - start
        
        # Encode match or literal
        if best_length > 2:
            # Compressed token
            compressed_token = ((best_offset & 0xFFF) << 4) | (best_length & 0x0F)
            output.append(input_data[current_pos])  # Literal byte before compressed token
            output.append((compressed_token >> 8) | 0x80)  # High byte with compression flag
            output.append(compressed_token & 0xFF)  # Low byte
            current_pos += best_length
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
        # Ensure data is available
        if current_pos + 1 >= len(compressed_data):
            break
        
        # Check if current byte is a literal or potential compression token
        current_byte = compressed_data[current_pos]
        next_byte = compressed_data[current_pos + 1]
        
        # Check if it's a compressed token
        if next_byte & 0x80:
            # First byte is a literal, next is a compressed token
            output.append(current_byte)
            
            # Extract compressed token
            token = ((next_byte & 0x7F) << 8) | compressed_data[current_pos + 2]
            current_pos += 3
            
            # Extract offset and length
            offset = (token >> 4) & 0xFFF
            length = token & 0x0F
            
            # Validate offset and length
            if offset == 0 or length == 0 or offset > len(output):
                output.append(next_byte)
                continue
            
            # Copy matched sequence
            start = len(output) - offset
            for i in range(length):
                output.append(output[start + i])
        else:
            # Literal byte
            output.append(current_byte)
            current_pos += 1
    
    return bytes(output)