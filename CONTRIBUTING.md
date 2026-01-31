# Contributing to Claude Skills Library

Thank you for your interest in contributing to the Claude Skills Library! This document provides guidelines for contributing skills to the library.

## How to Contribute

### 1. Choose a Skill Category

Select an existing category or propose a new one:
- `data_processing`: Data manipulation and analysis
- `web_automation`: Web scraping and browser automation
- `file_operations`: File management and processing
- `text_processing`: Text manipulation and NLP
- `api_integration`: API interactions and integrations

### 2. Skill Requirements

Each skill must include:

#### Required Files
- `README.md`: Comprehensive documentation
- `skill.json`: Metadata in standard format
- Implementation file(s): Code in Python, JavaScript, Bash, or other languages
- `examples/`: At least one working example

#### Skill Metadata (`skill.json`)
```json
{
  "name": "skill_name",
  "description": "Clear, concise description",
  "category": "category_name",
  "version": "1.0.0",
  "author": "Your Name or GitHub Username",
  "license": "MIT",
  "tags": ["tag1", "tag2"],
  "parameters": [
    {
      "name": "param_name",
      "type": "string|number|boolean|object|array",
      "required": true|false,
      "default": "default_value",
      "description": "Parameter description"
    }
  ],
  "returns": {
    "type": "string|number|boolean|object|array",
    "description": "Return value description"
  },
  "dependencies": [],
  "examples": []
}
```

#### Documentation (`README.md`)
Your README should include:
1. **Title**: Skill name
2. **Description**: What the skill does
3. **Use Cases**: When to use this skill
4. **Parameters**: Detailed parameter documentation
5. **Returns**: What the skill returns
6. **Examples**: Multiple usage examples
7. **Error Handling**: Common errors and solutions
8. **Dependencies**: Required libraries or tools
9. **Notes**: Additional information

### 3. Code Quality Standards

- **Clean Code**: Follow language-specific best practices
- **Comments**: Add inline comments for complex logic
- **Error Handling**: Implement proper error handling
- **Testing**: Include test cases or examples
- **Security**: Avoid hardcoded credentials or sensitive data
- **Performance**: Optimize for efficiency

### 4. Submission Process

1. **Fork** the repository
2. **Create a branch**: `git checkout -b add-skill-name`
3. **Add your skill** following the structure
4. **Test** your skill thoroughly
5. **Commit**: `git commit -m "Add [skill_name] skill"`
6. **Push**: `git push origin add-skill-name`
7. **Open a Pull Request** with:
   - Clear title
   - Description of the skill
   - Use cases
   - Testing performed

### 5. Review Process

All contributions will be reviewed for:
- Code quality and standards
- Documentation completeness
- Security considerations
- Functionality and usefulness
- Compatibility with existing skills

### 6. Skill Naming Conventions

- Use lowercase with underscores: `parse_json_data`
- Be descriptive but concise
- Avoid abbreviations unless widely known
- Use verb-noun format: `extract_text`, `validate_email`

### 7. Version Guidelines

Follow semantic versioning (MAJOR.MINOR.PATCH):
- **MAJOR**: Breaking changes
- **MINOR**: New features, backward compatible
- **PATCH**: Bug fixes, backward compatible

### 8. Code of Conduct

- Be respectful and inclusive
- Provide constructive feedback
- Focus on improving the library
- Help others learn and grow

## Questions?

If you have questions or need help:
1. Check existing skills for examples
2. Review this guide thoroughly
3. Open an issue for discussion
4. Ask in pull request comments

Thank you for contributing to the Claude Skills Library! 🚀
