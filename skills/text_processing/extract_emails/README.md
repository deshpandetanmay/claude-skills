# Extract Emails Skill

## Description
Extract email addresses from text using regular expressions. This skill can find all email addresses in a given text and optionally return only unique addresses.

## Use Cases
- Parsing contact information from documents
- Extracting recipient lists from email threads
- Finding email addresses in web scraped content
- Data cleaning and validation
- Contact list generation

## Parameters

### text (required)
- **Type**: string
- **Description**: The text to extract email addresses from
- **Example**: `"Contact us at support@example.com"`

### unique (optional)
- **Type**: boolean
- **Default**: `true`
- **Description**: Whether to return only unique email addresses
- **Example**: `true`

## Returns
- **Type**: array of strings
- **Description**: List of email addresses found in the text
- **Example**: `["support@example.com", "sales@example.com"]`

## Examples

### Example 1: Basic Usage
```python
from implementation import extract_emails

text = "Contact us at support@example.com or sales@example.com"
emails = extract_emails(text)
print(emails)
# Output: ['support@example.com', 'sales@example.com']
```

### Example 2: With Duplicates
```python
text = """
For support: support@example.com
Sales: sales@example.com
Also support: support@example.com
"""

# Get unique emails (default)
unique_emails = extract_emails(text, unique=True)
print(unique_emails)
# Output: ['support@example.com', 'sales@example.com']

# Get all emails including duplicates
all_emails = extract_emails(text, unique=False)
print(all_emails)
# Output: ['support@example.com', 'sales@example.com', 'support@example.com']
```

### Example 3: Complex Text
```python
text = """
Team contacts:
- John Doe: john.doe@company.com
- Jane Smith: jane.smith@company.com
- Support Team: support+urgent@company.co.uk

Please CC admin@company.com on all correspondence.
"""

emails = extract_emails(text)
print(emails)
# Output: ['john.doe@company.com', 'jane.smith@company.com', 
#          'support+urgent@company.co.uk', 'admin@company.com']
```

## Error Handling

### Common Issues
1. **Empty String**: Returns empty list
2. **No Emails Found**: Returns empty list
3. **Invalid Email Format**: Skipped automatically by regex pattern

### Pattern Limitations
- May not catch all obscure email formats
- Assumes standard email format: `user@domain.tld`
- Validates basic structure but not deliverability

## Dependencies
- Python 3.6+
- Standard library `re` module (no external dependencies)

## Implementation Notes
- Uses standard email regex pattern
- Preserves order of first occurrence when `unique=True`
- Case-sensitive matching
- Handles common email formats including:
  - Standard: `user@domain.com`
  - With dots: `first.last@domain.com`
  - With plus: `user+tag@domain.com`
  - With hyphens: `user-name@domain.com`
  - Subdomains: `user@mail.domain.com`
  - Country codes: `user@domain.co.uk`

## Testing
Run the implementation directly to see examples:
```bash
python implementation.py
```

## Performance
- **Time Complexity**: O(n) where n is the length of the text
- **Space Complexity**: O(m) where m is the number of emails found
- **Suitable for**: Texts up to several MB in size

## Version History
- **1.0.0** (2026-01-31): Initial release
