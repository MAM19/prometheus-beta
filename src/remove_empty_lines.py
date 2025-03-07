def remove_empty_lines(input_file, output_file=None):
    """
    Remove empty lines from a given file.

    Args:
        input_file (str): Path to the input file to remove empty lines from.
        output_file (str, optional): Path to save the file without empty lines. 
                                     If not provided, overwrites the input file.

    Returns:
        int: Number of empty lines removed.

    Raises:
        FileNotFoundError: If the input file does not exist.
        PermissionError: If there are permission issues reading/writing files.
        TypeError: If input arguments are not strings.
    """
    # Validate input types
    if not isinstance(input_file, str):
        raise TypeError("input_file must be a string")
    
    if output_file is not None and not isinstance(output_file, str):
        raise TypeError("output_file must be a string")
    
    # Use input_file as output_file if not specified
    if output_file is None:
        output_file = input_file
    
    # Track number of empty lines removed
    empty_lines_count = 0
    
    try:
        # Read input file
        with open(input_file, 'r') as infile:
            lines = infile.readlines()
        
        # Filter out empty lines (including lines with only whitespace)
        non_empty_lines = [line for line in lines if line.strip()]
        
        # Calculate empty lines
        empty_lines_count = len(lines) - len(non_empty_lines)
        
        # Write non-empty lines to output file
        with open(output_file, 'w') as outfile:
            outfile.writelines(non_empty_lines)
        
        return empty_lines_count
    
    except FileNotFoundError:
        raise FileNotFoundError(f"Input file not found: {input_file}")
    except PermissionError:
        raise PermissionError(f"Permission denied when accessing file: {input_file}")