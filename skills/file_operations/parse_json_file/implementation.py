"""
Parse JSON File Skill

This skill reads and parses JSON files with proper error handling.
"""

import json
import os
from typing import Union, Dict, List


def parse_json_file(
    file_path: str,
    encoding: str = 'utf-8',
    strict: bool = True
) -> Union[Dict, List]:
    """
    Read and parse a JSON file.
    
    Args:
        file_path (str): Path to the JSON file to parse
        encoding (str): File encoding (default: 'utf-8')
        strict (bool): Whether to use strict JSON parsing (default: True)
    
    Returns:
        Union[Dict, List]: Parsed JSON data
    
    Raises:
        FileNotFoundError: If the file doesn't exist
        json.JSONDecodeError: If the file contains invalid JSON
        PermissionError: If there are insufficient permissions to read the file
    
    Examples:
        >>> data = parse_json_file("config.json")
        >>> print(data['setting'])
        
        >>> data = parse_json_file("data.json", encoding="utf-8", strict=False)
    """
    # Check if file exists
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File not found: {file_path}")
    
    # Check if it's a file (not a directory)
    if not os.path.isfile(file_path):
        raise ValueError(f"Path is not a file: {file_path}")
    
    try:
        with open(file_path, 'r', encoding=encoding) as file:
            data = json.load(file, strict=strict)
            return data
    except json.JSONDecodeError as e:
        raise json.JSONDecodeError(
            f"Invalid JSON in {file_path}: {e.msg}",
            e.doc,
            e.pos
        )
    except PermissionError as e:
        raise PermissionError(f"Permission denied reading {file_path}: {e}")
    except Exception as e:
        raise Exception(f"Error reading {file_path}: {str(e)}")


if __name__ == "__main__":
    # Example usage
    import tempfile
    
    # Create a temporary JSON file for demonstration
    with tempfile.NamedTemporaryFile(mode='w', suffix='.json', delete=False) as f:
        example_data = {
            "name": "Example",
            "version": "1.0.0",
            "settings": {
                "enabled": True,
                "count": 42
            },
            "items": ["item1", "item2", "item3"]
        }
        json.dump(example_data, f, indent=2)
        temp_file = f.name
    
    try:
        # Parse the JSON file
        data = parse_json_file(temp_file)
        print("Parsed data:")
        print(json.dumps(data, indent=2))
        
        # Access nested data
        print(f"\nName: {data['name']}")
        print(f"Enabled: {data['settings']['enabled']}")
        print(f"Items: {data['items']}")
    finally:
        # Clean up
        os.unlink(temp_file)
