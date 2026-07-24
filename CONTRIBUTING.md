# Contributing to GST App

## Getting Started

1. Fork the repository
2. Clone your fork
3. Create a feature branch
4. Make your changes
5. Test your changes
6. Commit with clear messages
7. Push to your fork
8. Create a Pull Request

## Testing

All new features must include tests.

```bash
# Run tests
pytest tests/ -v

# Run specific test
pytest tests/test_auth.py::test_login -v

# Run with coverage
pytest --cov=app tests/
```

## Commit Messages

Use clear, descriptive commit messages:

```
Add GST report PDF export functionality

- Implement PDF generation using ReportLab
- Add date range filtering
- Include summary statistics
```

## Reporting Bugs

Use the issue tracker with:

1. **Clear Title**: Concise description of the bug
2. **Steps to Reproduce**: Detailed reproduction steps
3. **Expected Behavior**: What should happen
4. **Actual Behavior**: What actually happens

## Feature Requests

When requesting features:

1. **Use Case**: Describe the problem it solves
2. **Expected Behavior**: How should it work
3. **Alternatives**: Other solutions considered
