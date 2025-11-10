# LARGEST RECTANGLE IN HISTOGRAM

'''
Given an array of integers heights representing the histogram's bar height where the width of each bar is 1, return the area of the largest rectangle in the histogram.
'''

def largestRectangleArea(heights):
    stack = [] # Pair: Index, Height
    maxArea = 0
    n = len(heights)
    
    for index, height in enumerate(heights):
        startIndex = index
        while stack and stack[-1][1] > height:
            prevIndex, prevHeight = stack.pop()
            width = index - prevIndex
            maxArea = max(maxArea, prevHeight * width)
            startIndex = prevIndex
        
        stack.append((startIndex, height))
        
    for index, height in stack:
        width = n - index
        maxArea = max(maxArea, height * width)
        
    return maxArea

'''
Time Complexity: O(n)
Let n be the length of the heights array.
- We iterate through the heights array once, which takes O(n) time.
- For each element, we may push it onto the stack and pop elements from the stack. However, each element can be pushed at most once and popped at most once across all iterations.
- Therefore, the total number of stack operations (push and pop) is O(n).
- The second loop processes the remaining elements in the stack. In the worst case, all n elements could be in the stack, but this loop also runs in O(n) time total.
- The overall time complexity is O(n).

Space Complexity: O(n)
- We use a stack to store pairs of (index, height). In the worst case (e.g., when heights are in increasing order), the stack can contain all n elements.
- Therefore, the space complexity is O(n).
'''

# Test Cases
heights1 = [2, 1, 5, 6, 2, 3]
print(largestRectangleArea(heights1)) # Output: 10

heights2 = [2, 4]
print(largestRectangleArea(heights2)) # Output: 4

heights3 = [1]
print(largestRectangleArea(heights3)) # Output: 1

heights4 = [0]
print(largestRectangleArea(heights4)) # Output: 0

heights5 = [2, 1, 2]
print(largestRectangleArea(heights5)) # Output: 3

heights6 = [2, 4, 3]
print(largestRectangleArea(heights6)) # Output: 6

heights7 = [2, 1, 2, 3, 1]
print(largestRectangleArea(heights7)) # Output: 5

heights8 = [2, 1, 2, 3, 1]
print(largestRectangleArea(heights8)) # Output: 5

heights9 = [2, 1, 2, 3, 1]
print(largestRectangleArea(heights9)) # Output: 5

heights10 = [2, 1, 2, 3, 1]
print(largestRectangleArea(heights10)) # Output: 5