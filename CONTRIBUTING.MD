# Contributing to ScrapeGen

Thank you for your interest in contributing to ScrapeGen! This document provides guidelines and information about contributing to this project.

## Table of Contents

- [Code of Conduct](#code-of-conduct)
- [Getting Started](#getting-started)
- [Development Process](#development-process)
- [Pull Request Process](#pull-request-process)
- [Coding Standards](#coding-standards)
- [Testing Guidelines](#testing-guidelines)
- [Documentation](#documentation)
- [Issue Reporting](#issue-reporting)
- [Security Issues](#security-issues)

## Code of Conduct

By participating in this project, you agree to abide by our Code of Conduct:

- Use welcoming and inclusive language
- Be respectful of different viewpoints and experiences
- Gracefully accept constructive criticism
- Focus on what is best for the community
- Show empathy towards other community members

## Getting Started

1. Fork the repository on GitHub
2. Clone your fork locally:

```bash
git clone https://github.com/your-username/scrapegen.git
cd scrapegen
```

3. Create a virtual environment and install dependencies:

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -e ".[dev]"
```

4. Create a branch for your work:

```bash
git checkout -b feature/your-feature-name
```

## Development Process

1. Choose an issue to work on or create a new one
2. Comment on the issue to let others know you're working on it
3. Write your code following our coding standards
4. Add tests for your changes
5. Update documentation as needed
6. Submit a pull request

### Environment Setup

```bash
# Install pre-commit hooks
pip install pre-commit
pre-commit install

# Install development dependencies
pip install -e ".[dev]"
```

## Pull Request Process

1. Update the README.md with details of changes if needed
2. Update the documentation with details of changes if needed
3. Add your changes to the CHANGELOG.md under "Unreleased"
4. Ensure all tests pass and code style checks succeed
5. Include a clear description of the changes in your PR
6. Link any relevant issues in your PR description

### PR Title Format

- feat: Add new feature
- fix: Bug fix
- docs: Documentation changes
- style: Code style changes (formatting, etc)
- refactor: Code refactoring
- test: Adding tests
- chore: Maintenance tasks

## Coding Standards

### Python Style Guide

- Follow PEP 8 guidelines
- Use type hints for all function arguments and return values
- Write docstrings for all public modules, functions, classes, and methods
- Maximum line length is 88 characters (using Black formatter)

### Code Formatting

```bash
# Format code
black src tests

# Sort imports
isort src tests

# Run type checking
mypy src
```

### Naming Conventions

- Classes: PascalCase
- Functions and variables: snake_case
- Constants: UPPERCASE_WITH_UNDERSCORES
- Private attributes/methods: _leading_underscore

## Testing Guidelines

- Write unit tests for all new functionality
- Maintain test coverage above 90%
- Use pytest for testing
- Place tests in the `tests/` directory
- Name test files with `test_` prefix

```bash
# Run tests
pytest

# Run tests with coverage
pytest --cov=src/scrapegen tests/

# Run specific test file
pytest tests/test_specific_file.py
```

## Documentation

- Use Google-style docstrings
- Update documentation for any new features or changes
- Include examples in docstrings
- Keep API documentation up to date

Example docstring:

```python
def function_name(param1: str, param2: int) -> bool:
    """Short description of function.

    Longer description of function if needed.

    Args:
        param1: Description of param1
        param2: Description of param2

    Returns:
        Description of return value

    Raises:
        ValueError: Description of when this error occurs
    """
```

## Issue Reporting

### Bug Reports

When reporting bugs, please include:

1. Description of the bug
2. Steps to reproduce
3. Expected behavior
4. Actual behavior
5. Environment information:
   - Python version
   - ScrapeGen version
   - Operating system
   - Any relevant dependencies

### Feature Requests

When requesting features, please include:

1. Clear description of the feature
2. Use cases
3. Expected behavior
4. Alternative solutions considered
5. Example implementation if possible

## Recognition

Contributors will be recognized in the following ways:

1. Added to CONTRIBUTORS.md file
2. Mentioned in release notes for significant contributions
3. Listed in the project documentation

## Questions?

If you have questions about contributing, please:

1. Check the documentation
2. Search existing issues
3. Open a new issue with the "question" label
4. Join our community chat/forum

Thank you for contributing to ScrapeGen
