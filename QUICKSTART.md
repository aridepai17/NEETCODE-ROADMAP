# 🚀 Quick Start Guide

Get started with the NeetCode Roadmap in 5 minutes!

## For Complete Beginners

### Step 1: Verify Python Installation

Open your terminal/command prompt and run:

```bash
python --version
```

If you see `Python 3.7.x` or higher, you're good to go! If not, [download Python here](https://www.python.org/downloads/).

### Step 2: Navigate to the Repository

```bash
cd "NEETCODE ROADMAP"
```

### Step 3: Run Your First Solution

```bash
cd "ARRAYS AND HASHING"
python twosum.py
```

You should see output like:
```
[0, 1]
[1, 2]
[0, 1]
...
```

Congratulations! 🎉 You just ran your first solution!

## Understanding a Solution File

Let's break down the structure using `twosum.py` as an example:

### 1. Problem Title
```python
# TWO SUM
```
The name of the LeetCode problem.

### 2. Problem Description
```python
'''
Given an array of integers nums and an integer target,
return indices of the two numbers such that they add up to target.
'''
```
Explains what the problem asks you to do.

### 3. Solution Function
```python
def twoSum(nums, target):
    hashMap = {}
    
    for i in range(len(nums)):
        diff = target - nums[i]
        
        if diff in hashMap:
            return [hashMap[diff], i]
        
        hashMap[nums[i]] = i
        
    return []
```
The actual implementation that solves the problem.

### 4. Complexity Analysis
```python
'''
Time Complexity: O(n)
Space Complexity: O(n)
'''
```
Explains how efficient the solution is.

### 5. Test Cases
```python
nums1 = [2, 7, 11, 15]
target1 = 9
print(twoSum(nums1, target1))  # Output: [0, 1]
```
Examples that verify the solution works correctly.

## Your First Week Plan

### Day 1-2: Arrays and Hashing Basics
- [ ] Two Sum
- [ ] Contains Duplicate
- [ ] Valid Anagram

### Day 3-4: More Array Problems
- [ ] Group Anagrams
- [ ] Top K Frequent Elements
- [ ] Product of Array Except Self

### Day 5-7: Two Pointers Introduction
- [ ] Valid Palindrome
- [ ] Two Sum II
- [ ] 3Sum

## How to Practice Effectively

### 1. Read the Problem
Spend 2-3 minutes understanding what's being asked.

### 2. Think Before Coding
Spend 5-10 minutes thinking about possible approaches:
- What data structures could help?
- Have I seen a similar problem?
- What's the brute force solution?

### 3. Implement
Write your solution. Don't worry about perfection!

### 4. Test
Run the test cases. Debug if needed.

### 5. Analyze
Look at the provided solution and complexity analysis:
- Is your approach similar?
- Is there a more efficient way?
- What did you learn?

### 6. Review
Come back to the problem after 3 days and solve it again from scratch.

## Common Beginner Mistakes

### ❌ Mistake 1: Jumping to Code Too Quickly
**Solution**: Always spend time understanding the problem first.

### ❌ Mistake 2: Not Testing Edge Cases
**Solution**: Think about empty inputs, single elements, duplicates, etc.

### ❌ Mistake 3: Ignoring Time Complexity
**Solution**: Always ask "Can I do better?" after your first solution.

### ❌ Mistake 4: Memorizing Solutions
**Solution**: Focus on understanding patterns, not memorizing code.

### ❌ Mistake 5: Giving Up Too Quickly
**Solution**: Struggle for 20-30 minutes before looking at the solution.

## Debugging Tips

### If Your Code Doesn't Run:

1. **Check for syntax errors**
   - Missing colons `:`
   - Incorrect indentation
   - Mismatched parentheses

2. **Print intermediate values**
   ```python
   print(f"Current value: {variable}")
   ```

3. **Test with simple inputs**
   ```python
   # Start with the smallest possible input
   print(twoSum([1, 2], 3))  # Should return [0, 1]
   ```

### If Your Output is Wrong:

1. **Trace through manually**
   - Use pen and paper
   - Follow your code step by step

2. **Check boundary conditions**
   - First element
   - Last element
   - Empty array

3. **Compare with expected output**
   - Look at the test cases
   - Understand why they expect that result

## Next Steps

Once you're comfortable with the basics:

1. **Move to Medium problems** in the same category
2. **Time yourself** (aim for 20-30 minutes per problem)
3. **Explain solutions out loud** (practice for interviews)
4. **Join coding communities** (LeetCode forums, Reddit, Discord)
5. **Track your progress** using the checklist in README.md

## Resources for Beginners

### Python Basics
- [Python Official Tutorial](https://docs.python.org/3/tutorial/)
- [Python for Beginners](https://www.python.org/about/gettingstarted/)

### Data Structures
- [Python Data Structures](https://docs.python.org/3/tutorial/datastructures.html)
- Lists, Dictionaries, Sets, Tuples

### Algorithm Basics
- [Big-O Notation](https://www.bigocheatsheet.com/)
- [Algorithm Visualizations](https://visualgo.net/)

## Getting Help

- **Read the code comments** - They explain the logic
- **Watch NeetCode videos** - Visual explanations help
- **Ask in communities** - Don't struggle alone
- **Open an issue** - We're here to help!

## Motivation

> "The expert in anything was once a beginner."

Every programmer you admire struggled with these problems once. The difference is they kept going. You can do this! 💪

---

**Ready to start?** Go back to the main [README.md](README.md) and pick your first problem!

**Questions?** Open an issue with the `question` label.

**Happy Coding!** 🚀
