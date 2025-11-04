# 🚀 NeetCode Roadmap - Complete DSA Solutions

[![Python](https://img.shields.io/badge/Python-3.7+-blue.svg)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](CONTRIBUTING.md)

> A comprehensive collection of Data Structures and Algorithms solutions following the NeetCode roadmap. Perfect for interview preparation, learning, and mastering problem-solving patterns.

---

## 📋 Table of Contents

- [Overview](#-overview)
- [Repository Structure](#-repository-structure)
- [Problem Categories](#-problem-categories)
- [Getting Started](#-getting-started)
- [How to Use This Repository](#-how-to-use-this-repository)
- [Code Structure](#-code-structure)
- [Learning Path](#-learning-path)
- [Contributing](#-contributing)
- [Resources](#-resources)
- [FAQ](#-faq)
- [License](#-license)

---

## 🎯 Overview

This repository contains **150+ LeetCode problems** organized by topic and difficulty level, following the popular [NeetCode roadmap](https://neetcode.io/roadmap). Each solution includes:

- ✅ **Clean, readable Python code** with descriptive variable names
- 📝 **Detailed problem descriptions** from LeetCode
- 🧠 **Multiple solution approaches** (when applicable)
- ⏱️ **Time and Space complexity analysis** for each approach
- 🧪 **Comprehensive test cases** with expected outputs
- 💡 **In-line comments** explaining the logic

### Why This Repository?

- **Beginner-Friendly**: Each solution is self-contained and easy to understand
- **Interview-Ready**: Covers all major DSA patterns asked in FAANG interviews
- **Progressive Learning**: Organized from Easy → Medium → Hard difficulty
- **Pattern Recognition**: Learn to identify and apply common problem-solving patterns
- **Production-Quality**: Code follows best practices and PEP 8 style guidelines

---

## 📁 Repository Structure

```
NEETCODE ROADMAP/
│
├── ARRAYS AND HASHING/              # Easy problems (68 solutions)
├── ARRAYS AND HASHING MEDIUM/       # Medium problems (33 solutions)
│
├── TWO POINTERS/                    # Easy problems (16 solutions)
├── TWO POINTERS MEDIUM/             # Medium problems (18 solutions)
│
├── SLIDING WINDOW/                  # Easy problems (5 solutions)
├── SLIDING WINDOW MEDIUM/           # Medium problems (27 solutions)
├── SLIDING WINDOW HARD/             # Hard problems (2 solutions)
│
├── STACK/                           # Easy problems (7 solutions)
├── STACK MEDIUM/                    # Medium problems (14 solutions)
│
└── README.md                        # This file
```

### File Naming Convention

All files follow a consistent naming pattern:
- **Lowercase with no spaces**: `twosum.py`, `validpalindrome.py`
- **Descriptive names**: Match the LeetCode problem title
- **Easy to search**: Use Ctrl+F to find problems quickly

---

## 🗂️ Problem Categories

### 1. Arrays and Hashing
**Total: 101 problems** (68 Easy + 33 Medium)

Core concepts covered:
- Hash Maps and Hash Sets
- Frequency counting
- Prefix sums
- Array manipulation
- String processing

**Key Problems:**
- Two Sum
- Group Anagrams
- Valid Anagram
- Contains Duplicate
- Top K Frequent Elements

---

### 2. Two Pointers
**Total: 34 problems** (16 Easy + 18 Medium)

Core concepts covered:
- Left-right pointer technique
- Fast-slow pointer (Floyd's algorithm)
- Sliding window variations
- In-place array modifications

**Key Problems:**
- Valid Palindrome
- Two Sum II
- Container With Most Water
- Trapping Rain Water

---

### 3. Sliding Window
**Total: 34 problems** (5 Easy + 27 Medium + 2 Hard)

Core concepts covered:
- Fixed-size windows
- Variable-size windows
- Optimization problems
- Substring problems

**Key Problems:**
- Best Time to Buy and Sell Stock
- Longest Substring Without Repeating Characters
- Minimum Window Substring
- Sliding Window Maximum

---

### 4. Stack
**Total: 21 problems** (7 Easy + 14 Medium)

Core concepts covered:
- LIFO (Last In First Out) operations
- Monotonic stacks
- Expression evaluation
- Parentheses matching

**Key Problems:**
- Valid Parentheses
- Min Stack
- Daily Temperatures
- Largest Rectangle in Histogram

---

## 🚀 Getting Started

### Prerequisites

- **Python 3.7 or higher** installed on your system
- Basic understanding of Python syntax
- A code editor (VS Code, PyCharm, or any text editor)

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/aridepai17/neetcode-roadmap.git
   cd neetcode-roadmap
   ```

2. **No dependencies required!**
   All solutions use Python's standard library only. No external packages needed.

3. **Verify Python installation**
   ```bash
   python --version
   # Should output: Python 3.7.x or higher
   ```

---

## 💻 How to Use This Repository

### For Beginners

1. **Start with Easy problems** in the `ARRAYS AND HASHING` folder
2. **Read the problem description** at the top of each file
3. **Try solving it yourself** before looking at the solution
4. **Study the solution** and understand the approach
5. **Analyze the complexity** to understand efficiency
6. **Run the test cases** to verify your understanding

### Running a Solution

```bash
# Navigate to any folder
cd "ARRAYS AND HASHING"

# Run any Python file
python twosum.py
```

**Expected Output:**
```
[0, 1]
[1, 2]
[0, 1]
...
```

### For Interview Preparation

1. **Focus on patterns**, not memorization
2. **Time yourself** (aim for 20-30 minutes per problem)
3. **Practice explaining** your solution out loud
4. **Review complexity analysis** for each solution
5. **Revisit problems** after a few days to reinforce learning

### For Advanced Users

- Compare multiple solution approaches
- Optimize space/time complexity
- Implement solutions in other languages
- Add edge case test scenarios
- Contribute improvements via Pull Requests

---

## 📝 Code Structure

Every solution file follows this consistent structure:

```python
# PROBLEM TITLE

'''
Problem Description:
Detailed explanation of what the problem asks for,
including constraints and requirements.
'''

def solutionFunction(params):
    # Implementation with clear logic
    # Step-by-step approach
    # Efficient algorithm
    pass

'''
Time Complexity: O(n)
Detailed explanation of why this complexity...

Space Complexity: O(1)
Detailed explanation of space usage...
'''

# Test Cases
testCase1 = [...]
print(solutionFunction(testCase1))  # Output: expected_result
```

### Code Quality Standards

- ✅ **PEP 8 compliant**: Follows Python style guidelines
- ✅ **Descriptive naming**: Variables and functions have clear names
- ✅ **Comments**: Complex logic is explained
- ✅ **Type hints**: (where applicable) for better code clarity
- ✅ **Edge cases**: Test cases cover normal and edge scenarios

---

## 🎓 Learning Path

### Recommended Study Order

```
Week 1-2: Arrays and Hashing (Easy)
  ↓
Week 3-4: Two Pointers (Easy)
  ↓
Week 5-6: Sliding Window (Easy → Medium)
  ↓
Week 7-8: Stack (Easy → Medium)
  ↓
Week 9-10: Arrays and Hashing (Medium)
  ↓
Week 11-12: Two Pointers (Medium)
  ↓
Week 13+: Advanced topics and Hard problems
```

### Study Tips

1. **Consistency over intensity**: Solve 2-3 problems daily
2. **Understand, don't memorize**: Focus on the "why" behind solutions
3. **Write it out**: Code solutions from scratch without copy-paste
4. **Review regularly**: Revisit solved problems weekly
5. **Join communities**: Discuss solutions with peers

### Pattern Recognition Guide

| Pattern | When to Use | Example Problems |
|---------|-------------|------------------|
| **Hash Map** | Need O(1) lookup, counting frequency | Two Sum, Group Anagrams |
| **Two Pointers** | Sorted array, palindrome check | Valid Palindrome, Container With Most Water |
| **Sliding Window** | Subarray/substring problems | Longest Substring, Max Sum Subarray |
| **Stack** | Matching pairs, next greater element | Valid Parentheses, Daily Temperatures |

---

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

### Ways to Contribute

- 🐛 **Report bugs** or issues in solutions
- 💡 **Suggest optimizations** or alternative approaches
- 📚 **Add more test cases** for edge scenarios
- 🌐 **Translate solutions** to other languages
- 📖 **Improve documentation** and explanations
- ✨ **Add new problems** following the existing structure

### Contribution Guidelines

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/improvement`)
3. Follow the existing code structure and style
4. Add test cases for new solutions
5. Update README if adding new categories
6. Commit with clear messages (`git commit -m "Add: Two Sum solution"`)
7. Push to your branch (`git push origin feature/improvement`)
8. Open a Pull Request

---

## 📚 Resources

### Learning Materials

- **[NeetCode.io](https://neetcode.io/)** - Video explanations for each problem
- **[LeetCode](https://leetcode.com/)** - Original problem statements and online judge
- **[Big-O Cheat Sheet](https://www.bigocheatsheet.com/)** - Time/space complexity reference
- **[Python Documentation](https://docs.python.org/3/)** - Official Python docs

### Recommended Books

- *Cracking the Coding Interview* by Gayle Laakmann McDowell
- *Elements of Programming Interviews in Python* by Aziz, Lee, Prakash
- *Introduction to Algorithms* by CLRS

### YouTube Channels

- [NeetCode](https://www.youtube.com/@NeetCode) - Problem walkthroughs
- [Abdul Bari](https://www.youtube.com/@abdul_bari) - Algorithm fundamentals
- [Back To Back SWE](https://www.youtube.com/@BackToBackSWE) - In-depth explanations

---

## ❓ FAQ

### Q: Do I need to know advanced Python to use this repository?
**A:** No! Basic Python knowledge (loops, conditionals, functions) is sufficient. Each solution is beginner-friendly.

### Q: How long will it take to complete all problems?
**A:** At 2-3 problems per day, approximately 2-3 months. Focus on understanding over speed.

### Q: Can I use these solutions for LeetCode submissions?
**A:** Yes, but we encourage you to understand and type them yourself rather than copy-paste.

### Q: Why Python instead of other languages?
**A:** Python's clean syntax makes it ideal for learning algorithms. The logic translates easily to other languages.

### Q: Are there solutions for Hard difficulty problems?
**A:** Currently, the repository focuses on Easy and Medium problems. Hard problems will be added progressively.

### Q: How do I track my progress?
**A:** Create a checklist or use the GitHub issues feature to mark completed problems.

### Q: What if I don't understand a solution?
**A:** Check the NeetCode video explanation, or open an issue asking for clarification. Community help is available!

---

## 📊 Progress Tracker

Track your journey through the roadmap:

- [ ] Arrays and Hashing - Easy (68 problems)
- [ ] Arrays and Hashing - Medium (33 problems)
- [ ] Two Pointers - Easy (16 problems)
- [ ] Two Pointers - Medium (18 problems)
- [ ] Sliding Window - Easy (5 problems)
- [ ] Sliding Window - Medium (27 problems)
- [ ] Sliding Window - Hard (2 problems)
- [ ] Stack - Easy (7 problems)
- [ ] Stack - Medium (14 problems)

**Total Progress: 0 / 190 problems completed** 🎯

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 🌟 Acknowledgments

- **[NeetCode](https://neetcode.io/)** for the excellent roadmap and video explanations
- **[LeetCode](https://leetcode.com/)** for providing the problem platform
- **The coding community** for continuous learning and support

---

## 📞 Contact & Support

- **Issues**: [GitHub Issues](https://github.com/yourusername/neetcode-roadmap/issues)
- **Discussions**: [GitHub Discussions](https://github.com/yourusername/neetcode-roadmap/discussions)
- **Email**: your.email@example.com

---

<div align="center">

### ⭐ Star this repository if you find it helpful!

**Happy Coding! 🚀**

*Remember: The goal is not to solve all problems, but to understand the patterns and think algorithmically.*

</div>

---

## 🔄 Recent Updates

- **Nov 2024**: Initial repository setup with 190+ problems
- Added comprehensive documentation
- Organized problems by difficulty and topic
- Included complexity analysis for all solutions