# Skills Directory

This directory contains all the skills available in the Claude Skills Library, organized by category.

## Quick Navigation

- [📊 Data Processing](#data-processing)
- [🌐 Web Automation](#web-automation)
- [📁 File Operations](#file-operations)
- [📝 Text Processing](#text-processing)
- [🔌 API Integration](#api-integration)

---

## Data Processing

Skills for manipulating, transforming, and analyzing data.

### Available Skills

| Skill | Description | Difficulty | Language |
|-------|-------------|------------|----------|
| [csv_to_json](data_processing/csv_to_json/) | Convert CSV data to JSON format | Easy | Python |

---

## Web Automation

Skills for web scraping, browser automation, and web interactions.

### Available Skills

*Coming soon!*

---

## File Operations

Skills for file management, reading, writing, and processing files.

### Available Skills

| Skill | Description | Difficulty | Language |
|-------|-------------|------------|----------|
| [parse_json_file](file_operations/parse_json_file/) | Read and parse JSON files with error handling | Easy | Python |

---

## Text Processing

Skills for text manipulation, parsing, and natural language processing.

### Available Skills

| Skill | Description | Difficulty | Language |
|-------|-------------|------------|----------|
| [extract_emails](text_processing/extract_emails/) | Extract email addresses from text | Easy | Python |

---

## API Integration

Skills for interacting with external APIs and services.

### Available Skills

| Skill | Description | Difficulty | Language |
|-------|-------------|------------|----------|
| [http_request](api_integration/http_request/) | Make HTTP requests with various options | Medium | Python |

---

## Using Skills

Each skill directory contains:

- **README.md**: Comprehensive documentation with examples
- **skill.json**: Metadata and parameter specifications
- **implementation**: Code implementation (e.g., implementation.py)
- **examples/**: Usage examples and test cases

## Contributing New Skills

See the main [CONTRIBUTING.md](../CONTRIBUTING.md) for guidelines on adding new skills.

## Skill Discovery

Use the [catalog.json](catalog.json) file to programmatically discover and access skills:

```python
import json

# Load the catalog
with open('skills/catalog.json', 'r') as f:
    catalog = json.load(f)

# List all skills
for skill in catalog['skills']:
    print(f"{skill['name']}: {skill['description']}")

# Find skills by category
api_skills = [s for s in catalog['skills'] if s['category'] == 'api_integration']

# Find skills by tag
email_skills = [s for s in catalog['skills'] if 'email' in s['tags']]
```

## Stats

- **Total Skills**: 4
- **Categories**: 5
- **Languages**: Python
- **Last Updated**: 2026-01-31

## Roadmap

Planned skill categories and examples:

### Future Skills
- **Data Processing**: JSON to CSV, XML parser, data validator
- **Web Automation**: Selenium wrapper, web scraper, form filler
- **File Operations**: File compressor, image processor, PDF reader
- **Text Processing**: Sentiment analysis, text summarizer, markdown parser
- **API Integration**: GraphQL client, OAuth handler, webhook processor
- **Database**: SQL query builder, MongoDB client, Redis cache
- **Utilities**: Date formatter, UUID generator, hash calculator
- **Security**: Password validator, encryption/decryption, JWT handler
- **Image Processing**: Resize, crop, filter images
- **Audio/Video**: Audio transcription, video metadata extractor

## Support

For questions or issues with specific skills, please:
1. Check the skill's README.md file
2. Review the examples directory
3. Open an issue on GitHub with the skill name in the title
