# HTTP Request Skill

## Description
Make HTTP requests with comprehensive options including various methods, headers, authentication, and error handling. This skill provides a robust interface for interacting with REST APIs and web services.

## Use Cases
- Calling REST APIs
- Fetching data from web services
- Submitting form data
- Testing API endpoints
- Web scraping (simple cases)
- Webhook integration
- Service-to-service communication

## Parameters

### url (required)
- **Type**: string
- **Description**: The URL to make the request to
- **Example**: `"https://api.example.com/users"`

### method (optional)
- **Type**: string
- **Default**: `"GET"`
- **Options**: GET, POST, PUT, DELETE, PATCH, HEAD, OPTIONS
- **Description**: HTTP method to use
- **Example**: `"POST"`

### headers (optional)
- **Type**: object
- **Default**: `{}`
- **Description**: HTTP headers as key-value pairs
- **Example**: `{"Content-Type": "application/json", "Authorization": "Bearer token"}`

### data (optional)
- **Type**: object
- **Description**: Request body data (used with POST, PUT, PATCH)
- **Example**: `{"name": "John", "email": "john@example.com"}`

### params (optional)
- **Type**: object
- **Description**: URL query parameters
- **Example**: `{"page": 1, "limit": 10}`

### timeout (optional)
- **Type**: number
- **Default**: `30`
- **Description**: Request timeout in seconds
- **Example**: `60`

## Returns
- **Type**: object
- **Structure**:
  ```json
  {
    "status_code": 200,
    "headers": {"content-type": "application/json"},
    "body": {},
    "ok": true,
    "url": "https://api.example.com/users"
  }
  ```

## Examples

### Example 1: Simple GET Request
```python
from implementation import http_request

response = http_request("https://api.example.com/users")
print(f"Status: {response['status_code']}")
print(f"Data: {response['body']}")
```

### Example 2: POST with JSON Data
```python
response = http_request(
    url="https://api.example.com/users",
    method="POST",
    headers={"Content-Type": "application/json"},
    data={
        "name": "John Doe",
        "email": "john@example.com",
        "role": "admin"
    }
)

if response['ok']:
    print(f"User created: {response['body']['id']}")
else:
    print(f"Error: {response['status_code']}")
```

### Example 3: GET with Query Parameters
```python
response = http_request(
    url="https://api.example.com/search",
    params={
        "q": "python",
        "page": 1,
        "limit": 20
    }
)

results = response['body']['results']
print(f"Found {len(results)} results")
```

### Example 4: Authenticated Request
```python
response = http_request(
    url="https://api.example.com/profile",
    headers={
        "Authorization": "Bearer your-token-here",
        "Accept": "application/json"
    }
)

if response['status_code'] == 401:
    print("Authentication failed")
else:
    print(f"Profile: {response['body']}")
```

### Example 5: PUT Request to Update Data
```python
response = http_request(
    url="https://api.example.com/users/123",
    method="PUT",
    headers={"Content-Type": "application/json"},
    data={
        "name": "Jane Smith",
        "status": "active"
    }
)

print(f"Update status: {response['status_code']}")
```

### Example 6: DELETE Request
```python
response = http_request(
    url="https://api.example.com/users/123",
    method="DELETE",
    headers={"Authorization": "Bearer token"}
)

if response['status_code'] == 204:
    print("User deleted successfully")
```

### Example 7: Custom Timeout
```python
# For slow APIs
response = http_request(
    url="https://slow-api.example.com/process",
    timeout=120  # 2 minutes
)
```

## Error Handling

### TimeoutError
**Cause**: Request took longer than specified timeout
**Solution**: Increase timeout or check network connectivity

```python
try:
    response = http_request("https://api.example.com/data", timeout=5)
except TimeoutError as e:
    print(f"Request timed out: {e}")
```

### ConnectionError
**Cause**: Failed to establish connection to the server
**Solution**: Check URL, network connectivity, and server availability

```python
try:
    response = http_request("https://invalid-domain.example.com")
except ConnectionError as e:
    print(f"Connection failed: {e}")
```

### ValueError
**Cause**: Invalid HTTP method or parameters
**Solution**: Use valid HTTP methods (GET, POST, etc.)

```python
try:
    response = http_request("https://api.example.com", method="INVALID")
except ValueError as e:
    print(f"Invalid parameter: {e}")
```

### ImportError
**Cause**: Required 'requests' library not installed
**Solution**: Install with `pip install requests`

## Dependencies
- Python 3.6+
- `requests` library: Install with `pip install requests`

## Installation
```bash
pip install requests
```

## Implementation Notes
- Automatically parses JSON responses when possible
- Falls back to plain text for non-JSON responses
- Validates HTTP methods before making requests
- Handles both JSON and form data
- Includes response URL (useful for redirects)
- Provides both status code and boolean 'ok' flag
- Thread-safe (requests library is thread-safe)

## Performance
- **Time Complexity**: O(1) for request creation, O(n) for response parsing
- **Space Complexity**: O(n) where n is response size
- **Suitable for**: Individual API calls, not bulk operations

## Best Practices
1. Always handle timeout exceptions
2. Use appropriate timeout values for your use case
3. Check response status codes before processing data
4. Include proper authentication headers when required
5. Use HTTPS for sensitive data
6. Implement retry logic for production applications
7. Log requests for debugging
8. Validate SSL certificates in production

## Security Considerations
- Never hardcode API keys or tokens in code
- Use environment variables for sensitive credentials
- Validate SSL certificates (default behavior)
- Be cautious with user-supplied URLs
- Sanitize data before sending to APIs
- Use secure authentication methods (OAuth, JWT)

## Testing
Run the implementation directly to see examples:
```bash
python implementation.py
```

This will make several test requests to a public API.

## Version History
- **1.0.0** (2026-01-31): Initial release

## Related Skills
- `async_http_request`: For asynchronous/concurrent requests
- `graphql_query`: For GraphQL API interactions
- `websocket_connect`: For WebSocket connections
- `rate_limited_request`: For rate-limited API calls
