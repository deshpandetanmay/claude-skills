# Parse JSON File Skill

## Description
Read and parse JSON files with comprehensive error handling and validation. This skill safely loads JSON data from files and provides clear error messages for common issues.

## Use Cases
- Loading configuration files
- Reading API response data from files
- Processing JSON exports
- Data pipeline input processing
- Configuration management

## Parameters

### file_path (required)
- **Type**: string
- **Description**: Path to the JSON file to parse (absolute or relative)
- **Example**: `"config.json"` or `"/path/to/data.json"`

### encoding (optional)
- **Type**: string
- **Default**: `"utf-8"`
- **Description**: Character encoding of the file
- **Example**: `"utf-8"`, `"latin-1"`, `"ascii"`

### strict (optional)
- **Type**: boolean
- **Default**: `true`
- **Description**: Whether to use strict JSON parsing (disallows control characters)
- **Example**: `true`

## Returns
- **Type**: object or array
- **Description**: Parsed JSON data as Python dictionary or list
- **Example**: `{"key": "value", "items": [1, 2, 3]}`

## Examples

### Example 1: Basic Usage
```python
from implementation import parse_json_file

# Parse a configuration file
config = parse_json_file("config.json")
print(config['database']['host'])
```

### Example 2: With Custom Encoding
```python
# Parse a file with different encoding
data = parse_json_file("data.json", encoding="latin-1")
```

### Example 3: Non-Strict Parsing
```python
# Allow control characters in strings
data = parse_json_file("relaxed.json", strict=False)
```

### Example 4: Error Handling
```python
import json

try:
    data = parse_json_file("data.json")
    print("Successfully parsed:", data)
except FileNotFoundError as e:
    print(f"File not found: {e}")
except json.JSONDecodeError as e:
    print(f"Invalid JSON: {e}")
except PermissionError as e:
    print(f"Permission denied: {e}")
```

## Error Handling

### Common Errors

#### FileNotFoundError
**Cause**: The specified file doesn't exist
**Solution**: Check the file path and ensure the file exists

```python
try:
    data = parse_json_file("missing.json")
except FileNotFoundError as e:
    print(f"File not found: {e}")
```

#### JSONDecodeError
**Cause**: The file contains invalid JSON syntax
**Solution**: Validate and fix the JSON structure

```python
try:
    data = parse_json_file("invalid.json")
except json.JSONDecodeError as e:
    print(f"Invalid JSON at position {e.pos}: {e.msg}")
```

#### PermissionError
**Cause**: Insufficient permissions to read the file
**Solution**: Check file permissions and access rights

```python
try:
    data = parse_json_file("protected.json")
except PermissionError as e:
    print(f"Cannot read file: {e}")
```

#### ValueError
**Cause**: Path points to a directory instead of a file
**Solution**: Ensure the path points to a file

## Dependencies
- Python 3.6+
- Standard library `json` and `os` modules (no external dependencies)

## Implementation Notes
- Uses context manager for safe file handling
- Automatically closes file handles
- Validates file existence before parsing
- Distinguishes between files and directories
- Provides detailed error messages with context
- Supports all standard JSON data types:
  - Objects (dictionaries)
  - Arrays (lists)
  - Strings
  - Numbers
  - Booleans
  - null (None)

## Testing
Run the implementation directly to see examples:
```bash
python implementation.py
```

This will create a temporary JSON file, parse it, and display the results.

## Performance
- **Time Complexity**: O(n) where n is the size of the JSON file
- **Space Complexity**: O(n) for storing parsed data
- **Suitable for**: Files up to several hundred MB (depending on available memory)

## Best Practices
1. Always use try-except blocks for error handling
2. Validate file paths before parsing
3. Use appropriate encoding for your data
4. Consider memory constraints for large files
5. Use strict mode for security-sensitive applications

## Version History
- **1.0.0** (2026-01-31): Initial release

## Related Skills
- `write_json_file`: Write data to JSON files
- `validate_json_schema`: Validate JSON against a schema
- `merge_json_files`: Merge multiple JSON files
