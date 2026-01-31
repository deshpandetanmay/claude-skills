"""
Extract Email Addresses Skill

This skill extracts email addresses from text using regular expressions.
"""

import re
from typing import List


def extract_emails(text: str, unique: bool = True) -> List[str]:
    """
    Extract email addresses from text.
    
    Args:
        text (str): The text to extract email addresses from
        unique (bool): Whether to return only unique email addresses (default: True)
    
    Returns:
        List[str]: List of email addresses found in the text
    
    Examples:
        >>> extract_emails("Contact us at support@example.com or sales@example.com")
        ['support@example.com', 'sales@example.com']
        
        >>> extract_emails("Email: john@company.com, john@company.com", unique=True)
        ['john@company.com']
    """
    # Regular expression for matching email addresses
    email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    
    # Find all email addresses
    emails = re.findall(email_pattern, text)
    
    # Return unique emails if requested
    if unique:
        return list(dict.fromkeys(emails))  # Preserves order
    
    return emails


if __name__ == "__main__":
    # Example usage
    sample_text = """
    For support, contact us at support@example.com.
    Sales inquiries: sales@example.com
    General info: info@example.com
    Duplicate: support@example.com
    """
    
    print("All emails:", extract_emails(sample_text, unique=False))
    print("Unique emails:", extract_emails(sample_text, unique=True))
