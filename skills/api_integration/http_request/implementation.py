"""
HTTP Request Skill

This skill makes HTTP requests with comprehensive options and error handling.
"""

from typing import Dict, Any, Optional
import json


def http_request(
    url: str,
    method: str = "GET",
    headers: Optional[Dict[str, str]] = None,
    data: Optional[Dict[str, Any]] = None,
    params: Optional[Dict[str, Any]] = None,
    timeout: int = 30
) -> Dict[str, Any]:
    """
    Make an HTTP request with specified parameters.
    
    Args:
        url (str): The URL to make the request to
        method (str): HTTP method (GET, POST, PUT, DELETE, PATCH)
        headers (dict): HTTP headers as key-value pairs
        data (dict): Request body data (for POST, PUT, PATCH)
        params (dict): URL query parameters
        timeout (int): Request timeout in seconds
    
    Returns:
        dict: Response object with status_code, headers, and body
        
    Raises:
        requests.RequestException: For network-related errors
        ValueError: For invalid parameters
    
    Examples:
        >>> # GET request
        >>> response = http_request("https://api.example.com/data")
        >>> print(response['status_code'])
        
        >>> # POST request with JSON data
        >>> response = http_request(
        ...     "https://api.example.com/users",
        ...     method="POST",
        ...     headers={"Content-Type": "application/json"},
        ...     data={"name": "John", "email": "john@example.com"}
        ... )
    """
    try:
        import requests
    except ImportError:
        raise ImportError(
            "The 'requests' library is required. Install it with: pip install requests"
        )
    
    # Validate method
    valid_methods = ["GET", "POST", "PUT", "DELETE", "PATCH", "HEAD", "OPTIONS"]
    method = method.upper()
    if method not in valid_methods:
        raise ValueError(f"Invalid HTTP method: {method}")
    
    # Set default headers
    if headers is None:
        headers = {}
    
    # Prepare request kwargs
    request_kwargs = {
        "timeout": timeout,
        "headers": headers
    }
    
    if params:
        request_kwargs["params"] = params
    
    if data and method in ["POST", "PUT", "PATCH"]:
        # If Content-Type is JSON, serialize the data
        if headers.get("Content-Type") == "application/json":
            request_kwargs["json"] = data
        else:
            request_kwargs["data"] = data
    
    try:
        # Make the request
        response = requests.request(method, url, **request_kwargs)
        
        # Try to parse JSON response
        try:
            body = response.json()
        except json.JSONDecodeError:
            body = response.text
        
        # Return structured response
        return {
            "status_code": response.status_code,
            "headers": dict(response.headers),
            "body": body,
            "ok": response.ok,
            "url": response.url
        }
        
    except requests.Timeout:
        raise TimeoutError(f"Request to {url} timed out after {timeout} seconds")
    except requests.ConnectionError as e:
        raise ConnectionError(f"Failed to connect to {url}: {str(e)}")
    except requests.RequestException as e:
        raise requests.RequestException(f"Request failed: {str(e)}")


if __name__ == "__main__":
    # Example usage
    print("HTTP Request Skill Examples\n")
    
    # Example 1: Simple GET request (using a public API)
    print("Example 1: GET request")
    try:
        response = http_request(
            "https://jsonplaceholder.typicode.com/posts/1"
        )
        print(f"Status: {response['status_code']}")
        print(f"Data: {response['body']}\n")
    except Exception as e:
        print(f"Error: {e}\n")
    
    # Example 2: POST request
    print("Example 2: POST request")
    try:
        response = http_request(
            "https://jsonplaceholder.typicode.com/posts",
            method="POST",
            headers={"Content-Type": "application/json"},
            data={
                "title": "Test Post",
                "body": "This is a test",
                "userId": 1
            }
        )
        print(f"Status: {response['status_code']}")
        print(f"Created: {response['body']}\n")
    except Exception as e:
        print(f"Error: {e}\n")
    
    # Example 3: GET with query parameters
    print("Example 3: GET with query parameters")
    try:
        response = http_request(
            "https://jsonplaceholder.typicode.com/posts",
            params={"userId": 1}
        )
        print(f"Status: {response['status_code']}")
        print(f"Found {len(response['body'])} posts\n")
    except Exception as e:
        print(f"Error: {e}\n")
