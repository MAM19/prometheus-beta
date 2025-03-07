"""
LZRW (Lempel-Ziv Ross Williams) Compression Algorithm Implementation

This module provides a simplified LZ-style compression algorithm.
"""

def compress(input_data):
    """
    Compress input data using a simplified LZ-style compression algorithm.
    
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
        # Find longest match
        longest_match = input_data[current_pos:current_pos+1]
        match_pos = current_pos
        
        # Explore possible longer matches
        for length in range(1, min(16, len(input_data) - current_pos)):
            current_sequence = input_data[current_pos:current_pos+length]
            
            # Check if sequence exists in dictionary
            if current_sequence in dictionary:
                longest_match = current_sequence
                match_pos = dictionary[current_sequence]
            else:
                break
        
        # Update dictionary with current sequence
        dictionary[longest_match] = current_pos
        
        # Encode match or literal
        if len(longest_match) > 1:
            # Compressed token: offset and length
            offset = current_pos - match_pos
            length = len(longest_match)
            
            # First byte is literal before compression token
            output.append(input_data[current_pos])
            
            # Compression token
            compressed_token = ((offset & 0xFFF) << 4) | (length & 0x0F)
            output.append((compressed_token >> 8) | 0x80)  # High byte with compression flag
            output.append(compressed_token & 0xFF)  # Low byte
            
            current_pos += length
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
        # Ensure we have at least 3 bytes to process
        if current_pos + 2 >= len(compressed_data):
            output.extend(compressed_data[current_pos:])
            break
        
        # Check current bytes
        literal_byte = compressed_data[current_pos]
        token_byte1 = compressed_data[current_pos + 1]
        token_byte2 = compressed_data[current_pos + 2]
        
        # Check compression flag
        if token_byte1 & 0x80:
            # Compressed token: literal byte + compression
            output.append(literal_byte)
            
            # Reconstruct token
            token = ((token_byte1 & 0x7F) << 8) | token_byte2
            
            # Extract offset and length
            offset = (token >> 4) & 0xFFF
            length = token & 0x0F
            
            # Validate offset and length
            if offset == 0 or length == 0 or offset > len(output):
                output.append(token_byte1)
                current_pos += 1
                continue
            
            # Find start of match
            match_start = len(output) - offset
            
            # Copy matched sequence
            for _ in range(length):
                output.append(output[match_start])
                match_start += 1
            
            current_pos += 3
        else:
            # Literal byte
            output.append(literal_byte)
            current_pos += 1
    
    return bytes(output)