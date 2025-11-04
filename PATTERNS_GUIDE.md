# 🎯 Algorithm Patterns & Techniques Guide

A comprehensive guide to recognizing and applying common algorithm patterns. Master these patterns to solve 80% of coding interview problems.

## Table of Contents

- [Hash Map Pattern](#hash-map-pattern)
- [Two Pointers Pattern](#two-pointers-pattern)
- [Sliding Window Pattern](#sliding-window-pattern)
- [Stack Pattern](#stack-pattern)
- [Prefix Sum Pattern](#prefix-sum-pattern)
- [Frequency Counter Pattern](#frequency-counter-pattern)
- [Fast & Slow Pointers](#fast--slow-pointers)
- [In-Place Array Manipulation](#in-place-array-manipulation)

---

## Hash Map Pattern

### When to Use
- Need O(1) lookup time
- Finding pairs/complements
- Counting frequency
- Checking for duplicates
- Mapping relationships

### Template
```python
def hash_map_solution(arr):
    hash_map = {}
    
    for element in arr:
        # Check if complement/target exists
        if target - element in hash_map:
            return [hash_map[target - element], element]
        
        # Store element with its index/count
        hash_map[element] = index_or_count
    
    return result
```

### Key Problems
1. **Two Sum** - Find pair that sums to target
2. **Group Anagrams** - Group strings by sorted key
3. **Isomorphic Strings** - Map characters bijectively
4. **First Unique Character** - Find first non-repeating

### Time Complexity
- **Average**: O(n) for insertion and lookup
- **Worst**: O(n²) with hash collisions (rare)

### Space Complexity
- O(n) for storing elements

### Common Variations
- **Hash Set**: When you only need existence check
- **Counter**: When counting frequencies (use `collections.Counter`)
- **Default Dict**: When you need default values

---

## Two Pointers Pattern

### When to Use
- Array is sorted (or can be sorted)
- Need to find pairs/triplets
- Palindrome problems
- Merging sorted arrays
- In-place modifications

### Template

#### Left-Right Pointers
```python
def two_pointers_lr(arr):
    left = 0
    right = len(arr) - 1
    
    while left < right:
        # Calculate current result
        current = arr[left] + arr[right]
        
        if current == target:
            return [left, right]
        elif current < target:
            left += 1
        else:
            right -= 1
    
    return []
```

#### Slow-Fast Pointers
```python
def two_pointers_sf(arr):
    slow = 0
    
    for fast in range(len(arr)):
        if condition(arr[fast]):
            arr[slow] = arr[fast]
            slow += 1
    
    return slow
```

### Key Problems
1. **Valid Palindrome** - Check if string reads same forwards/backwards
2. **Two Sum II** - Find pair in sorted array
3. **3Sum** - Find triplets that sum to zero
4. **Container With Most Water** - Maximize area

### Time Complexity
- O(n) for single pass
- O(n²) for nested (like 3Sum)

### Space Complexity
- O(1) - in-place operations

### Decision Tree
```
Is array sorted?
├─ Yes → Use left-right pointers
└─ No → Can you sort it?
    ├─ Yes → Sort then use pointers
    └─ No → Consider other patterns
```

---

## Sliding Window Pattern

### When to Use
- Subarray/substring problems
- Finding max/min in subarrays
- Consecutive elements
- "Longest/shortest" problems
- "Contains all" problems

### Template

#### Fixed-Size Window
```python
def fixed_window(arr, k):
    window_sum = sum(arr[:k])
    max_sum = window_sum
    
    for i in range(k, len(arr)):
        # Slide window: remove left, add right
        window_sum = window_sum - arr[i - k] + arr[i]
        max_sum = max(max_sum, window_sum)
    
    return max_sum
```

#### Variable-Size Window
```python
def variable_window(arr):
    left = 0
    max_length = 0
    window_set = set()
    
    for right in range(len(arr)):
        # Expand window
        while arr[right] in window_set:
            # Shrink window from left
            window_set.remove(arr[left])
            left += 1
        
        window_set.add(arr[right])
        max_length = max(max_length, right - left + 1)
    
    return max_length
```

### Key Problems
1. **Best Time to Buy and Sell Stock** - Track min price
2. **Longest Substring Without Repeating Characters** - Variable window
3. **Maximum Average Subarray** - Fixed window
4. **Minimum Window Substring** - Variable with conditions

### Time Complexity
- O(n) - each element visited at most twice

### Space Complexity
- O(k) for window storage (k = window size or unique elements)

### Window Types
- **Fixed**: Size known beforehand (k elements)
- **Variable**: Size changes based on conditions
- **Shrinkable**: Shrink when condition violated

---

## Stack Pattern

### When to Use
- Matching pairs (parentheses, brackets)
- Next greater/smaller element
- Expression evaluation
- Undo operations
- Nested structures

### Template

#### Basic Stack
```python
def stack_solution(s):
    stack = []
    
    for char in s:
        if is_opening(char):
            stack.append(char)
        elif is_closing(char):
            if not stack or not matches(stack[-1], char):
                return False
            stack.pop()
    
    return len(stack) == 0
```

#### Monotonic Stack
```python
def monotonic_stack(arr):
    stack = []  # Store indices
    result = [-1] * len(arr)
    
    for i in range(len(arr)):
        # Maintain increasing/decreasing order
        while stack and arr[stack[-1]] < arr[i]:
            idx = stack.pop()
            result[idx] = arr[i]
        
        stack.append(i)
    
    return result
```

### Key Problems
1. **Valid Parentheses** - Match opening/closing pairs
2. **Daily Temperatures** - Next greater element
3. **Min Stack** - Stack with O(1) min operation
4. **Largest Rectangle in Histogram** - Monotonic stack

### Time Complexity
- O(n) - each element pushed/popped once

### Space Complexity
- O(n) for stack storage

### Stack Types
- **Regular**: LIFO operations
- **Monotonic Increasing**: Elements in increasing order
- **Monotonic Decreasing**: Elements in decreasing order
- **Min/Max Stack**: Track minimum/maximum

---

## Prefix Sum Pattern

### When to Use
- Subarray sum queries
- Range sum problems
- Finding pivot index
- Cumulative operations

### Template
```python
def prefix_sum(arr):
    n = len(arr)
    prefix = [0] * (n + 1)
    
    # Build prefix sum array
    for i in range(n):
        prefix[i + 1] = prefix[i] + arr[i]
    
    # Query sum from index i to j
    def range_sum(i, j):
        return prefix[j + 1] - prefix[i]
    
    return prefix
```

### Key Problems
1. **Find Pivot Index** - Left sum equals right sum
2. **Product of Array Except Self** - Prefix and suffix products
3. **Subarray Sum Equals K** - Prefix sum with hash map
4. **Range Sum Query** - Precompute sums

### Time Complexity
- O(n) to build prefix array
- O(1) for range queries

### Space Complexity
- O(n) for prefix array

### Variations
- **Prefix Product**: Multiply instead of add
- **2D Prefix Sum**: For matrix problems
- **Prefix XOR**: For XOR queries

---

## Frequency Counter Pattern

### When to Use
- Counting occurrences
- Finding duplicates
- Anagram problems
- Character/element frequency

### Template
```python
from collections import Counter

def frequency_counter(arr):
    # Method 1: Using Counter
    freq = Counter(arr)
    
    # Method 2: Manual counting
    freq = {}
    for element in arr:
        freq[element] = freq.get(element, 0) + 1
    
    # Find most common
    most_common = freq.most_common(k)
    
    return freq
```

### Key Problems
1. **Valid Anagram** - Compare character frequencies
2. **Top K Frequent Elements** - Find k most common
3. **Group Anagrams** - Group by character frequency
4. **First Unique Character** - Find frequency = 1

### Time Complexity
- O(n) for counting
- O(n log n) if sorting by frequency

### Space Complexity
- O(k) where k = number of unique elements

---

## Fast & Slow Pointers

### When to Use
- Cycle detection
- Finding middle element
- Linked list problems
- Array with cycles

### Template
```python
def fast_slow_pointers(head):
    slow = head
    fast = head
    
    # Detect cycle
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        
        if slow == fast:
            return True  # Cycle found
    
    return False  # No cycle
```

### Key Problems
1. **Linked List Cycle** - Detect cycle
2. **Find Middle of Linked List** - Fast moves 2x speed
3. **Happy Number** - Cycle in number sequence
4. **Find Duplicate Number** - Array as linked list

### Time Complexity
- O(n) where n = length of list

### Space Complexity
- O(1) - only two pointers

---

## In-Place Array Manipulation

### When to Use
- Space constraint (O(1) extra space)
- Modifying array while iterating
- Partitioning problems
- Removing elements

### Template
```python
def in_place_manipulation(arr):
    write_idx = 0
    
    for read_idx in range(len(arr)):
        if condition(arr[read_idx]):
            arr[write_idx] = arr[read_idx]
            write_idx += 1
    
    return write_idx  # New length
```

### Key Problems
1. **Remove Element** - Remove all occurrences
2. **Move Zeroes** - Move to end
3. **Remove Duplicates** - From sorted array
4. **Sort Colors** - Dutch national flag

### Time Complexity
- O(n) single pass

### Space Complexity
- O(1) in-place

---

## Pattern Recognition Flowchart

```
Start
│
├─ Need O(1) lookup? → Hash Map
│
├─ Array sorted? → Two Pointers
│
├─ Subarray/substring? → Sliding Window
│
├─ Matching pairs? → Stack
│
├─ Range queries? → Prefix Sum
│
├─ Counting elements? → Frequency Counter
│
├─ Cycle detection? → Fast & Slow Pointers
│
└─ Space constraint? → In-Place Manipulation
```

---

## Complexity Cheat Sheet

| Pattern | Time | Space | Use Case |
|---------|------|-------|----------|
| Hash Map | O(n) | O(n) | Lookup, pairs |
| Two Pointers | O(n) | O(1) | Sorted arrays |
| Sliding Window | O(n) | O(k) | Subarrays |
| Stack | O(n) | O(n) | Matching, next greater |
| Prefix Sum | O(n) | O(n) | Range queries |
| Frequency Counter | O(n) | O(k) | Counting |
| Fast & Slow | O(n) | O(1) | Cycles |
| In-Place | O(n) | O(1) | Space constraint |

---

## Practice Strategy

### Week 1-2: Master One Pattern
- Choose Hash Map or Two Pointers
- Solve 10-15 problems with that pattern
- Understand variations deeply

### Week 3-4: Add Second Pattern
- Learn Sliding Window or Stack
- Compare with first pattern
- Solve mixed problems

### Week 5-6: Pattern Recognition
- Given a problem, identify pattern in 1 minute
- Solve without looking at solutions
- Time yourself (20-30 minutes)

### Week 7+: Advanced Combinations
- Problems using multiple patterns
- Optimize solutions
- Explain to others

---

## Common Mistakes

### ❌ Mistake 1: Using Wrong Pattern
**Example**: Using nested loops when hash map would work
**Solution**: Spend 2 minutes identifying pattern before coding

### ❌ Mistake 2: Not Considering Edge Cases
**Example**: Empty array, single element, all duplicates
**Solution**: List edge cases before implementing

### ❌ Mistake 3: Premature Optimization
**Example**: Trying to optimize before working solution
**Solution**: Get brute force working first, then optimize

### ❌ Mistake 4: Ignoring Space Complexity
**Example**: Using O(n) space when O(1) possible
**Solution**: Always ask "Can I do this in-place?"

---

## Interview Tips

### Before Coding
1. **Clarify requirements** (5 minutes)
2. **Identify pattern** (2 minutes)
3. **Discuss approach** (3 minutes)
4. **Consider edge cases** (2 minutes)

### While Coding
1. **Write clean code** (use good variable names)
2. **Explain as you code** (think out loud)
3. **Test with examples** (walk through)
4. **Handle edge cases** (empty, single element)

### After Coding
1. **Analyze complexity** (time and space)
2. **Discuss optimizations** (can we do better?)
3. **Consider trade-offs** (time vs space)

---

## Resources

### Practice by Pattern
- **LeetCode**: Filter by tags (Hash Table, Two Pointers, etc.)
- **NeetCode**: Organized by patterns
- **AlgoExpert**: Pattern-based learning

### Visualization Tools
- **VisuAlgo**: Algorithm animations
- **Python Tutor**: Step-through code execution
- **LeetCode Playground**: Test ideas quickly

---

**Remember**: Patterns are tools, not rules. Sometimes you need to combine patterns or create custom solutions. The goal is to build intuition!

**Happy Pattern Hunting!** 🎯
