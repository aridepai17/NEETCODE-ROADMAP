# SQRT(X)

'''
Given a non-negative integer x, return the square root of x rounded down to the nearest integer.
The returned integer should be non-negative as well.
You must not use any built-in exponent function or operator.
For example, do not use pow(x, 0.5) in c++ or x ** 0.5 in python.
'''

# Brute Force Solution
def mySqrt1(x):
    for i in range(1, x + 1):
        if i * i == x:
            return i
        if i * i > x:
            return i - 1
        
'''
Time Complexity: O(√x)
Let x be the input number.
- The algorithm iterates through numbers from 1 to x in the worst case.
- However, the loop terminates early when i * i > x, which occurs when i > √x.
- Therefore, the loop runs at most √x iterations.
- Each iteration performs constant time operations: multiplication and comparison.
- Thus, the overall time complexity is O(√x).

Space Complexity: O(1)
- The algorithm uses only a constant amount of extra space for the loop variable i.
- No additional data structures are created that scale with the input size.
- Therefore, the space complexity is O(1).
'''

# Binary Search Solution
def mySqrt2(x):
    left = 1
    right = x
    
    while left <= right:
        mid = (left + right) // 2
        if mid * mid < x:
            left = mid + 1
        elif mid * mid > x:
            right = mid - 1
        else:
            return mid
        
    return right

'''
Time Complexity: O(log x)
Let x be the input number.
- The algorithm uses binary search on the range [1, x].
- In each iteration, we calculate the midpoint and check if mid * mid equals, is less than, or is greater than x.
- The search space is halved in each iteration by adjusting either `left` or `right`.
- The loop continues until `left > right`, which takes at most log₂(x) iterations.
- All operations inside the loop (calculating mid, multiplication, comparisons) are O(1).
- Therefore, the overall time complexity is O(log x).

Space Complexity: O(1)
- The algorithm uses a constant amount of extra space for variables: `left`, `right`, and `mid`.
- No additional data structures are created that scale with the input size.
- Therefore, the space complexity is O(1).
'''

# Test Cases
x1 = 4
print(mySqrt2(x1)) # Output: 2

x2 = 8
print(mySqrt2(x2)) # Output: 2

x3 = 1
print(mySqrt2(x3)) # Output: 1

x4 = 16
print(mySqrt2(x4)) # Output: 4

x5 = 25
print(mySqrt2(x5)) # Output: 5

x6 = 100
print(mySqrt2(x6)) # Output: 10

x7 = 101
print(mySqrt2(x7)) # Output: 10

x8 = 144
print(mySqrt2(x8)) # Output: 12

x9 = 0
print(mySqrt2(x9)) # Output: 0

x10 = 2
print(mySqrt2(x10)) # Output: 1