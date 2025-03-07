"""
LZRW (Lempel-Ziv Ross Williams) Compression Algorithm Implementation

This module provides functions for LZRW compression and decompression.
The implementation follows the basic LZRW1 algorithm principles.
"""

def compress(input_data):
    """
    Compress input data using the LZRW compression algorithm.
    
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
    window_size = 4096  # Typical sliding window size
    buffer_size = 16    # Look-ahead buffer size
    
    # Track current position in input
    current_pos = 0
    
    while current_pos < len(input_data):
        # Look for longest match in previous window
        best_length = 0
        best_offset = 0
        
        # Search back in the window for longest match
        search_start = max(0, current_pos - window_size)
        search_end = current_pos
        
        for start in range(search_start, search_end):
            match_length = 0
            
            # Check how long the match continues
            while (current_pos + match_length < len(input_data) and 
                   match_length < buffer_size and 
                   input_data[start + match_length] == input_data[current_pos + match_length]):
                match_length += 1
            
            # Update best match if found
            if match_length > best_length:
                best_length = match_length
                best_offset = current_pos - start
        
        # Encode match or literal
        if best_length > 2:
            # Compressed token: offset and length
            compressed_token = ((best_offset & 0xFFF) << 4) | (best_length & 0x0F)
            output.append((compressed_token >> 8) & 0xFF)  # High byte
            output.append(compressed_token & 0xFF)        # Low byte
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
        # Check if we have enough bytes to read a token
        if current_pos + 1 >= len(compressed_data):
            break
        
        # Read token (2 bytes)
        token = (compressed_data[current_pos] << 8) | compressed_data[current_pos + 1]
        current_pos += 2
        
        # Check if it's a compressed or literal token
        if token & 0x8000:  # Compressed token
            # Extract offset and length
            offset = (token >> 4) & 0xFFF
            length = token & 0x0F
            
            # Validate offset and length
            if offset == 0 or length == 0:
                raise ValueError("Invalid compressed token")
            
            # Find start of match
            match_start = len(output) - offset
            
            # Copy matched sequence
            for i in range(length):
                output.append(output[match_start + i])
        else:
            # Literal byte
            output.append(token & 0xFF)
    
    return bytes(output)