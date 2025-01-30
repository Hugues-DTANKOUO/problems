# Contributing to Problems

First off, thank you for considering contributing to Problems! It's people like you that make Problems such a great tool.

## Code of Conduct

This project and everyone participating in it is governed by our Code of Conduct. By participating, you are expected to uphold this code.

## How Can I Contribute?

### Reporting Bugs

Before creating bug reports, please check the issue list as you might find out that you don't need to create one. When you are creating a bug report, please include as many details as possible:

* Use a clear and descriptive title
* Describe the exact steps which reproduce the problem
* Provide specific examples to demonstrate the steps
* Describe the behavior you observed after following the steps
* Explain which behavior you expected to see instead and why
* Include screenshots and animated GIFs if possible

### Suggesting Enhancements

Enhancement suggestions are tracked as GitHub issues. When creating an enhancement suggestion, please include:

* Use a clear and descriptive title
* Provide a step-by-step description of the suggested enhancement
* Provide specific examples to demonstrate the steps
* Describe the current behavior and explain which behavior you expected to see instead
* Explain why this enhancement would be useful

### Adding New Problems

When adding new programming problems:

1. Create a new Python file in `src/problems/`
2. Follow the existing problem format:
   * Include comprehensive docstrings with examples
   * Implement the problem interface
   * Add appropriate tests
3. Update the problems list in `problems.md`

### Development Process

1. Fork the repository on GitHub
2. Clone your fork locally
3. Create your feature branch from `main`
4. If you've added code that should be tested, add tests
5. Ensure the test suite passes (`poetry run tests`)
6. Ensure your code passes all linting checks (`poetry run lint`)
7. Issue that pull request!

## Setting Up Your Development Environment

1. Install Poetry:
```bash
curl -sSL https://install.python-poetry.org | python3 -
```

2. Fork the repository on GitHub:
   * Visit https://github.com/Hugues-DTANKOUO/problems
   * Click the "Fork" button in the top-right corner
   * Wait for the forking process to complete

3. Clone your fork:
```bash
git clone https://github.com/YOUR-USERNAME/problems.git
cd problems
```

4. Install dependencies:
```bash
poetry install
```

5. Run the linting tools:
```bash
poetry run lint
```

6. Run the tests:
```bash
poetry run tests
```

7. Start the development server:
```bash
poetry run server
```

## Style Guide

* Follow PEP 8 guidelines
* Use type hints
* Write descriptive docstrings
* Keep functions focused and small
* Use meaningful variable names
* Comment complex logic

## Creating Pull Requests

1. Update the [README.md](README.md) with details of changes if needed
2. Update the [CHANGELOG.md](CHANGELOG.md) with notes on your changes
3. The PR should work for Python 3.10 and above
4. Include relevant tests
5. Make sure all linting checks pass by running:
```bash
poetry run lint
```

## Additional Notes

* Write descriptive commit messages
* Keep PRs focused - don't include unrelated changes
* Link PRs to issues where applicable
* Always run `poetry run lint` before committing your changes
* If you're updating documentation, verify the links work correctly

## Running Quality Checks

Before submitting your PR, make sure to run:

1. All tests:
```bash
poetry run tests
```

2. Linting tools:
```bash
poetry run lint
```

3. Type checking:
```bash
poetry run mypy src/problems
```

Thank you for your contribution! 🎉