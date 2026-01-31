"""
CSV to JSON Conversion Skill

This skill converts CSV data to JSON format with customizable options.
"""

import csv
import io
from typing import List, Dict, Any


def csv_to_json(
    csv_data: str,
    delimiter: str = ',',
    has_header: bool = True
) -> List[Dict[str, Any]]:
    """
    Convert CSV data to JSON format.
    
    Args:
        csv_data (str): CSV data as a string
        delimiter (str): CSV delimiter character (default: ',')
        has_header (bool): Whether CSV has a header row (default: True)
    
    Returns:
        List[Dict[str, Any]]: Array of JSON objects representing CSV rows
    
    Examples:
        >>> csv_data = "name,age\\nJohn,30\\nJane,25"
        >>> result = csv_to_json(csv_data)
        >>> print(result)
        [{'name': 'John', 'age': '30'}, {'name': 'Jane', 'age': '25'}]
        
        >>> # CSV without header
        >>> csv_data = "John,30\\nJane,25"
        >>> result = csv_to_json(csv_data, has_header=False)
        >>> print(result)
        [{'column_0': 'John', 'column_1': '30'}, {'column_0': 'Jane', 'column_1': '25'}]
    """
    # Create a string buffer from CSV data
    csv_buffer = io.StringIO(csv_data)
    
    # Create CSV reader
    reader = csv.reader(csv_buffer, delimiter=delimiter)
    
    # Convert to list of rows
    rows = list(reader)
    
    if not rows:
        return []
    
    result = []
    
    if has_header:
        # Use first row as headers
        headers = rows[0]
        data_rows = rows[1:]
        
        # Convert each row to a dictionary
        for row in data_rows:
            if row:  # Skip empty rows
                row_dict = {}
                for i, value in enumerate(row):
                    if i < len(headers):
                        row_dict[headers[i]] = value
                    else:
                        # Handle rows with more columns than headers
                        row_dict[f'column_{i}'] = value
                result.append(row_dict)
    else:
        # Generate generic column names
        num_columns = len(rows[0]) if rows else 0
        headers = [f'column_{i}' for i in range(num_columns)]
        
        # Convert each row to a dictionary
        for row in rows:
            if row:  # Skip empty rows
                row_dict = {}
                for i, value in enumerate(row):
                    if i < len(headers):
                        row_dict[headers[i]] = value
                    else:
                        row_dict[f'column_{i}'] = value
                result.append(row_dict)
    
    return result


if __name__ == "__main__":
    # Example 1: CSV with header
    print("Example 1: CSV with header")
    csv_with_header = """name,age,city
John Doe,30,New York
Jane Smith,25,Los Angeles
Bob Johnson,35,Chicago"""
    
    result = csv_to_json(csv_with_header)
    import json
    print(json.dumps(result, indent=2))
    print()
    
    # Example 2: CSV without header
    print("Example 2: CSV without header")
    csv_no_header = """John,30,Engineer
Jane,25,Designer
Bob,35,Manager"""
    
    result = csv_to_json(csv_no_header, has_header=False)
    print(json.dumps(result, indent=2))
    print()
    
    # Example 3: CSV with different delimiter
    print("Example 3: CSV with semicolon delimiter")
    csv_semicolon = """name;age;department
Alice;28;Sales
Charlie;32;Marketing"""
    
    result = csv_to_json(csv_semicolon, delimiter=';')
    print(json.dumps(result, indent=2))
    print()
    
    # Example 4: CSV with tab delimiter
    print("Example 4: CSV with tab delimiter")
    csv_tab = "product\tprice\tstock\nLaptop\t999\t15\nMouse\t25\t100"
    
    result = csv_to_json(csv_tab, delimiter='\t')
    print(json.dumps(result, indent=2))
