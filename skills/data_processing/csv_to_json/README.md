# CSV to JSON Conversion Skill

## Description
Convert CSV (Comma-Separated Values) data to JSON format. This skill handles various CSV formats including different delimiters, with or without headers, and provides clean JSON output.

## Use Cases
- Data format conversion for APIs
- Processing CSV exports from databases
- Converting spreadsheet data to JSON
- Preparing data for web applications
- ETL (Extract, Transform, Load) operations
- Data migration between systems

## Parameters

### csv_data (required)
- **Type**: string
- **Description**: CSV data as a string (can include newlines)
- **Example**: `"name,age\nJohn,30\nJane,25"`

### delimiter (optional)
- **Type**: string
- **Default**: `","`
- **Description**: Character used to separate values in CSV
- **Options**: `,` (comma), `;` (semicolon), `\t` (tab), `|` (pipe)
- **Example**: `";"`

### has_header (optional)
- **Type**: boolean
- **Default**: `true`
- **Description**: Whether the first row contains column headers
- **Example**: `true`

## Returns
- **Type**: array of objects
- **Description**: Array of JSON objects, each representing a CSV row
- **Example**:
  ```json
  [
    {"name": "John", "age": "30"},
    {"name": "Jane", "age": "25"}
  ]
  ```

## Examples

### Example 1: Basic CSV with Headers
```python
from implementation import csv_to_json
import json

csv_data = """name,age,city
John Doe,30,New York
Jane Smith,25,Los Angeles"""

result = csv_to_json(csv_data)
print(json.dumps(result, indent=2))
```

Output:
```json
[
  {
    "name": "John Doe",
    "age": "30",
    "city": "New York"
  },
  {
    "name": "Jane Smith",
    "age": "25",
    "city": "Los Angeles"
  }
]
```

### Example 2: CSV Without Headers
```python
csv_data = """John,30,Engineer
Jane,25,Designer
Bob,35,Manager"""

result = csv_to_json(csv_data, has_header=False)
print(json.dumps(result, indent=2))
```

Output:
```json
[
  {
    "column_0": "John",
    "column_1": "30",
    "column_2": "Engineer"
  },
  {
    "column_0": "Jane",
    "column_1": "25",
    "column_2": "Designer"
  },
  {
    "column_0": "Bob",
    "column_1": "35",
    "column_2": "Manager"
  }
]
```

### Example 3: Semicolon Delimiter
```python
csv_data = """name;email;department
Alice;alice@example.com;Sales
Bob;bob@example.com;Engineering"""

result = csv_to_json(csv_data, delimiter=';')
print(json.dumps(result, indent=2))
```

### Example 4: Tab-Delimited Data
```python
csv_data = "product\tprice\tstock\nLaptop\t999\t15\nMouse\t25\t100"

result = csv_to_json(csv_data, delimiter='\t')
print(json.dumps(result, indent=2))
```

### Example 5: Reading from File
```python
with open('data.csv', 'r') as file:
    csv_content = file.read()

result = csv_to_json(csv_content)
print(f"Converted {len(result)} rows")
```

### Example 6: Pipe-Delimited Data
```python
csv_data = """id|name|status
1|Project A|Active
2|Project B|Completed"""

result = csv_to_json(csv_data, delimiter='|')
```

## Error Handling

### Empty Data
```python
csv_data = ""
result = csv_to_json(csv_data)
print(result)  # Returns []
```

### Inconsistent Columns
If a row has more columns than headers, extra columns are named automatically:
```python
csv_data = """a,b
1,2,3
4,5"""

result = csv_to_json(csv_data)
# First row will have keys: 'a', 'b', 'column_2'
```

### Empty Rows
Empty rows are automatically skipped:
```python
csv_data = """name,age
John,30

Jane,25"""

result = csv_to_json(csv_data)
# Returns only 2 objects (empty row skipped)
```

## Dependencies
- Python 3.6+
- Standard library `csv` and `io` modules (no external dependencies)

## Implementation Notes
- Uses Python's built-in `csv` module for robust parsing
- Handles quoted values with commas inside
- Skips empty rows automatically
- Preserves value order in JSON objects
- All values are returned as strings (no type conversion)
- Generates generic column names when no header is present
- Handles rows with varying column counts gracefully

## Data Type Handling
This skill returns all values as strings. For type conversion:

```python
result = csv_to_json(csv_data)

# Convert numeric fields
for item in result:
    if 'age' in item:
        item['age'] = int(item['age'])
    if 'price' in item:
        item['price'] = float(item['price'])
```

## Performance
- **Time Complexity**: O(n × m) where n is rows and m is columns
- **Space Complexity**: O(n × m) for storing result
- **Suitable for**: Files up to several million rows (limited by memory)

## Best Practices
1. Validate CSV data before conversion
2. Handle empty or malformed data gracefully
3. Consider data types and convert as needed
4. Use appropriate delimiter for your data format
5. Be aware that all values are strings initially
6. Test with sample data before processing large files

## Testing
Run the implementation directly to see examples:
```bash
python implementation.py
```

## Version History
- **1.0.0** (2026-01-31): Initial release

## Related Skills
- `json_to_csv`: Convert JSON back to CSV format
- `parse_csv_file`: Read CSV directly from files
- `validate_csv`: Validate CSV structure
- `csv_filter`: Filter CSV data by criteria
