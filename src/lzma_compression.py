import lzma
import typing

def lzma_compress(data: typing.Union[str, bytes], compression_level: int = 6) -> bytes:
    """
    Compress input data using LZMA compression algorithm.

    Args:
        data (str or bytes): The input data to compress. 
            If str, will be encoded to UTF-8 bytes first.
        compression_level (int, optional): Compression level from 0-9. 
            Defaults to 6 (recommended balance of compression and speed).

    Returns:
        bytes: Compressed data.

    Raises:
        ValueError: If compression level is not between 0 and 9.
        TypeError: If input data is not str or bytes.
    """
    # Validate compression level
    if not 0 <= compression_level <= 9:
        raise ValueError("Compression level must be between 0 and 9.")

    # Convert string to bytes if needed
    if isinstance(data, str):
        data = data.encode('utf-8')
    elif not isinstance(data, bytes):
        raise TypeError("Input must be str or bytes.")

    # Compress using LZMA
    return lzma.compress(data, preset=compression_level)

def lzma_decompress(compressed_data: bytes) -> bytes:
    """
    Decompress LZMA compressed data.

    Args:
        compressed_data (bytes): The LZMA compressed data.

    Returns:
        bytes: Decompressed data.

    Raises:
        lzma.LZMAError: If data is invalid or corrupted.
        TypeError: If input is not bytes.
    """
    # Validate input
    if not isinstance(compressed_data, bytes):
        raise TypeError("Input must be bytes.")

    # Decompress using LZMA
    return lzma.decompress(compressed_data)