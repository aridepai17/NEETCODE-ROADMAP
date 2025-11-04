# Contributing to NeetCode Roadmap

First off, thank you for considering contributing to this project! 🎉

## Table of Contents

- [Code of Conduct](#code-of-conduct)
- [How Can I Contribute?](#how-can-i-contribute)
- [Style Guidelines](#style-guidelines)
- [Commit Guidelines](#commit-guidelines)
- [Pull Request Process](#pull-request-process)

## Code of Conduct

This project and everyone participating in it is governed by our commitment to providing a welcoming and inspiring community for all. Please be respectful and constructive in your interactions.

## How Can I Contribute?

### Reporting Bugs

Before creating bug reports, please check existing issues to avoid duplicates. When creating a bug report, include:

- **Clear title and description**
- **Steps to reproduce** the issue
- **Expected vs actual behavior**
- **Code snippet** demonstrating the problem
- **Python version** you're using

### Suggesting Enhancements

Enhancement suggestions are tracked as GitHub issues. When creating an enhancement suggestion, include:

- **Clear title and description**
- **Use case** explaining why this would be useful
- **Example implementation** if possible

### Adding New Solutions

1. **Choose a problem** from LeetCode that fits the repository structure
2. **Follow the existing format**:
   ```python
   # PROBLEM TITLE

   '''
   Problem description from LeetCode
   '''

   def solution(params):
       # Your implementation
       pass

   '''
   Time Complexity: O(?)
   Explanation...

   Space Complexity: O(?)
   Explanation...
   '''

   # Test Cases
   # At least 5-10 test cases
   ```

3. **Place in correct folder** based on topic and difficulty
4. **Name file appropriately** (lowercase, no spaces)

### Improving Existing Solutions

- **Optimize** time or space complexity
- **Add alternative approaches**
- **Improve code readability**
- **Add more test cases**
- **Enhance complexity explanations**

## Style Guidelines

### Python Code Style

- Follow **PEP 8** style guide
- Use **4 spaces** for indentation (no tabs)
- Maximum line length: **79 characters** for code, **72 for comments**
- Use **descriptive variable names**
- Add **comments** for complex logic
- Include **docstrings** for functions (optional but recommended)

### Documentation Style

- Use **Markdown** for all documentation
- Keep explanations **clear and concise**
- Use **code blocks** with syntax highlighting
- Include **examples** where helpful

### Complexity Analysis

Always include both time and space complexity:

```python
'''
Time Complexity: O(n)
- Explain why: "We iterate through the array once..."
- Mention dominant operations
- Consider best, average, and worst cases if relevant

Space Complexity: O(1)
- Explain auxiliary space used
- Don't count input/output space
- Mention any data structures used
'''
```

## Commit Guidelines

### Commit Message Format

```
<type>: <subject>

<body (optional)>
```

### Types

- **Add**: New solution or file
- **Fix**: Bug fix in existing solution
- **Improve**: Optimization or enhancement
- **Docs**: Documentation changes
- **Style**: Code formatting (no logic change)
- **Refactor**: Code restructuring (no behavior change)
- **Test**: Adding or updating test cases

### Examples

```
Add: Two Sum solution in Arrays and Hashing

Implemented O(n) solution using hash map approach.
Includes 10 test cases covering edge cases.
```

```
Fix: Correct time complexity in Valid Palindrome

The previous analysis incorrectly stated O(n^2).
Updated to O(n) with detailed explanation.
```

```
Improve: Optimize space complexity in Group Anagrams

Reduced space from O(n*k) to O(n) by using tuple keys.
```

## Pull Request Process

1. **Fork the repository** and create your branch from `main`
   ```bash
   git checkout -b feature/your-feature-name
   ```

2. **Make your changes** following the style guidelines

3. **Test your code** - ensure all solutions run without errors
   ```bash
   python your_solution.py
   ```

4. **Update documentation** if needed (README, comments, etc.)

5. **Commit your changes** with clear commit messages

6. **Push to your fork**
   ```bash
   git push origin feature/your-feature-name
   ```

7. **Open a Pull Request** with:
   - **Clear title** describing the change
   - **Description** of what and why
   - **Reference to issues** if applicable
   - **Test results** showing your code works

### Pull Request Checklist

- [ ] Code follows the style guidelines
- [ ] Solution includes complexity analysis
- [ ] Test cases are comprehensive
- [ ] File is in the correct folder
- [ ] Commit messages are clear
- [ ] Documentation is updated if needed
- [ ] Code runs without errors

## Questions?

Feel free to open an issue with the label `question` if you need clarification on anything.

---

Thank you for contributing! 🙏
