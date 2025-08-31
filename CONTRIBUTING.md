# Contributing to Directed Graph Generator

Thank you for your interest in contributing to the Directed Graph Generator! This document provides guidelines and information for contributors.

## Table of Contents

1. [Getting Started](#getting-started)
2. [Development Setup](#development-setup)
3. [Code Style](#code-style)
4. [Testing](#testing)
5. [Submitting Changes](#submitting-changes)
6. [Reporting Issues](#reporting-issues)
7. [Feature Requests](#feature-requests)

## Getting Started

Before contributing, please:

1. **Fork the repository** on GitHub
2. **Clone your fork** locally
3. **Create a new branch** for your changes
4. **Make your changes** following the guidelines below
5. **Test your changes** thoroughly
6. **Submit a pull request**

## Development Setup

### Prerequisites

- Python 3.9 or higher
- pip (Python package installer)

### Installation

1. Clone your fork:
   ```bash
   git clone https://github.com/yourusername/Directed-Graph-Generator.git
   cd Directed-Graph-Generator
   ```

2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Install the package in development mode:
   ```bash
   pip install -e .
   ```

## Code Style

### Python Code Style

We follow [PEP 8](https://www.python.org/dev/peps/pep-0008/) for Python code style:

- Use 4 spaces for indentation (no tabs)
- Maximum line length of 79 characters
- Use descriptive variable and function names
- Add type hints where appropriate
- Write comprehensive docstrings for all public methods

### Documentation Style

- Use Google-style docstrings for all classes and methods
- Include detailed descriptions, parameters, return values, and examples
- Update the README.md and API documentation when adding new features
- Add examples to the `examples/` directory for new functionality

### Example Code Style

```python
def add_node(self, value: int) -> bool:
    """
    Adds a new node to the graph.

    Checks for duplicate values before adding the node to ensure
    each node value is unique in the graph.

    Args:
        value (int): The integer value representing the new node.

    Returns:
        bool: True if the node was successfully added, False if the value already exists.

    Example:
        >>> graph = DirectedGraph([1, 2], [(1, 2)])
        >>> graph.add_node(3)
        True
    """
    if value not in [node.value for node in self.nodes]:
        return self.__add_node(Node(value))
    return False
```

## Testing

### Running Tests

1. Install test dependencies:
   ```bash
   pip install pytest pytest-cov
   ```

2. Run tests:
   ```bash
   pytest tests/
   ```

3. Run tests with coverage:
   ```bash
   pytest tests/ --cov=directed_graph_generator
   ```

### Writing Tests

- Create test files in the `tests/` directory
- Use descriptive test function names
- Test both positive and negative cases
- Test edge cases and error conditions
- Aim for high test coverage

### Example Test

```python
def test_add_node_success():
    """Test successful node addition."""
    graph = DirectedGraph([1, 2], [(1, 2)])
    assert graph.add_node(3) is True
    assert len(graph.nodes()) == 3

def test_add_node_duplicate():
    """Test adding duplicate node."""
    graph = DirectedGraph([1, 2], [(1, 2)])
    assert graph.add_node(1) is False
    assert len(graph.nodes()) == 2
```

## Submitting Changes

### Pull Request Process

1. **Update documentation** if your changes affect the API
2. **Add tests** for new functionality
3. **Update the CHANGELOG.md** with your changes
4. **Ensure all tests pass** before submitting
5. **Write a clear description** of your changes

### Pull Request Template

```markdown
## Description
Brief description of the changes made.

## Type of Change
- [ ] Bug fix (non-breaking change which fixes an issue)
- [ ] New feature (non-breaking change which adds functionality)
- [ ] Breaking change (fix or feature that would cause existing functionality to not work as expected)
- [ ] Documentation update

## Testing
- [ ] Added tests for new functionality
- [ ] All existing tests pass
- [ ] Tested manually with examples

## Checklist
- [ ] Code follows the project's style guidelines
- [ ] Documentation has been updated
- [ ] CHANGELOG.md has been updated
- [ ] No new warnings or errors
```

## Reporting Issues

### Bug Reports

When reporting bugs, please include:

1. **Clear description** of the problem
2. **Steps to reproduce** the issue
3. **Expected behavior** vs actual behavior
4. **Environment information** (Python version, OS, etc.)
5. **Code example** that demonstrates the issue

### Issue Template

```markdown
## Bug Description
Brief description of the bug.

## Steps to Reproduce
1. Step 1
2. Step 2
3. Step 3

## Expected Behavior
What you expected to happen.

## Actual Behavior
What actually happened.

## Environment
- Python version: X.X.X
- OS: [e.g., Windows 10, macOS 12.0, Ubuntu 20.04]
- Package version: X.X.X

## Code Example
```python
# Minimal code that reproduces the issue
```

## Additional Information
Any other relevant information.
```

## Feature Requests

### Feature Request Guidelines

When requesting new features, please:

1. **Describe the feature** clearly and concisely
2. **Explain the use case** and why it's needed
3. **Provide examples** of how it would be used
4. **Consider implementation** complexity and impact

### Feature Request Template

```markdown
## Feature Description
Brief description of the requested feature.

## Use Case
Explain why this feature is needed and how it would be used.

## Proposed API
```python
# Example of how the feature would be used
```

## Implementation Considerations
Any thoughts on implementation approach or complexity.

## Additional Information
Any other relevant information.
```

## Code of Conduct

### Our Standards

- Be respectful and inclusive
- Use welcoming and inclusive language
- Be collaborative and constructive
- Focus on what is best for the community
- Show empathy towards other community members

### Enforcement

Instances of abusive, harassing, or otherwise unacceptable behavior may be reported by contacting the project maintainers.

## License

By contributing to this project, you agree that your contributions will be licensed under the MIT License.

## Questions?

If you have questions about contributing, please:

1. Check the existing documentation
2. Search existing issues and pull requests
3. Open a new issue for clarification

Thank you for contributing to the Directed Graph Generator!
