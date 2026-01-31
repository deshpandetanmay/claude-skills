# Claude Skills Library

A comprehensive library of reusable skills for AI agents, designed to be used with [agentskills.io](https://agentskills.io/home).

## Overview

This library provides a collection of well-documented, modular skills that AI agents can utilize to perform various tasks. Each skill is designed to be:

- **Modular**: Self-contained and reusable
- **Well-documented**: Clear descriptions, parameters, and examples
- **Tested**: Reliable and production-ready
- **Standardized**: Follows consistent formatting and structure

## Quick Start

### Browse Skills

Use the interactive skill browser:
```bash
python browse_skills.py
```

Or explore the [skills directory](skills/) manually.

### Using a Skill

1. Navigate to the skill directory (e.g., `skills/text_processing/extract_emails/`)
2. Read the `README.md` for documentation
3. Review `skill.json` for metadata and parameters
4. Import and use the implementation:

```python
# Example: Using the extract_emails skill
from skills.text_processing.extract_emails.implementation import extract_emails

text = "Contact us at support@example.com or sales@example.com"
emails = extract_emails(text)
print(emails)  # ['support@example.com', 'sales@example.com']
```

### Available Skills

- **[extract_emails](skills/text_processing/extract_emails/)** - Extract email addresses from text
- **[parse_json_file](skills/file_operations/parse_json_file/)** - Parse JSON files with error handling
- **[http_request](skills/api_integration/http_request/)** - Make HTTP requests to APIs
- **[csv_to_json](skills/data_processing/csv_to_json/)** - Convert CSV data to JSON format

See the full [skills catalog](skills/catalog.json) for details.

## Skills Categories

### 📊 Data Processing
Skills for manipulating, transforming, and analyzing data.

### 🌐 Web Automation
Skills for web scraping, browser automation, and web interactions.

### 📁 File Operations
Skills for file management, reading, writing, and processing files.

### 📝 Text Processing
Skills for text manipulation, parsing, and natural language processing.

### 🔌 API Integration
Skills for interacting with external APIs and services.

## Skill Structure

Each skill follows this standard structure:

```
skills/
└── category/
    └── skill_name/
        ├── README.md          # Skill documentation
        ├── skill.json         # Skill metadata
        ├── implementation.py  # Implementation (or .js, .sh, etc.)
        └── examples/          # Usage examples
```

## Skill Metadata Format

Each skill includes a `skill.json` file with the following structure:

```json
{
  "name": "skill_name",
  "description": "Brief description of what the skill does",
  "category": "category_name",
  "version": "1.0.0",
  "author": "Author Name",
  "parameters": [
    {
      "name": "param_name",
      "type": "string",
      "required": true,
      "description": "Parameter description"
    }
  ],
  "returns": {
    "type": "object",
    "description": "Return value description"
  },
  "examples": [
    {
      "description": "Example usage",
      "code": "example code"
    }
  ]
}
```

## Usage

### For AI Agents

AI agents can discover and utilize skills from this library by:

1. Browsing the skills directory structure
2. Reading skill metadata from `skill.json` files
3. Following implementation guidelines in README files
4. Adapting examples to specific use cases

### For Developers

To contribute a new skill:

1. Choose the appropriate category or create a new one
2. Create a directory for your skill
3. Add `skill.json` with complete metadata
4. Implement the skill in your preferred language
5. Document usage in README.md
6. Provide examples
7. Submit a pull request

## Contributing

We welcome contributions! Please see [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Support

For issues, questions, or suggestions, please open an issue on GitHub.

## Roadmap

- [ ] Add more skills across all categories
- [ ] Implement skill testing framework
- [ ] Create skill discovery API
- [ ] Add skill versioning system
- [ ] Develop skill composition examples
- [ ] Build interactive documentation site 
