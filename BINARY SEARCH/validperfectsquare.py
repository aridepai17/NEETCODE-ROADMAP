# VALID PERFECT SQUARE

'''
Given a positive integer num, return true if num is a perfect square or false otherwise.
A perfect square is an integer that is the square of an integer. 
In other words, it is the product of some integer with itself.
You must not use any built-in library function, such as sqrt.
'''

# Brute Force Solution
from tkinter import N


def validPerfectSquare1(num):
    for i in range(1, num + 1):
        if i * i == num:
            return True
        if i * i > num:
            return False

'''
Time Complexity: O(√N)
Let N be the input number `num`.
- The algorithm iterates through numbers from 1 to `num` in the worst case.
- However, the loop terminates early when `i * i > num`, which occurs when `i > √N`.
- Therefore, the loop runs at most √N iterations.
- Each iteration performs constant time operations: multiplication and comparison.
- Thus, the overall time complexity is O(√N).

Space Complexity: O(1)
- The algorithm uses only a constant amount of extra space for the loop variable `i`.
- No additional data structures are created that scale with the input size.
- Therefore, the space complexity is O(1).
'''

# Binary Search Solution
def validPerfectSquare2(num):
    left = 1
    right = N
    
    while left <= right:
        mid = (left + right) // 2
        if mid * mid < num:
            left = mid + 1
        elif mid * mid > num:
            right = mid - 1
        else:
            return True
        
    return False

'''
Time Complexity: O(log N)
Let N be the input number `num`.
- The algorithm uses binary search on the range [1, N].
- In each iteration, we calculate the midpoint and check if mid * mid equals num.
- The search space is halved in each iteration by adjusting either `left` or `right`.
- The loop continues until `left > right`, which takes at most log₂(N) iterations.
- All operations inside the loop (calculating mid, multiplication, comparisons) are O(1).
- Therefore, the overall time complexity is O(log N).

Space Complexity: O(1)
- The algorithm uses a constant amount of extra space for variables: `left`, `right`, and `mid`.
- No additional data structures are created that scale with the input size.
- Therefore, the space complexity is O(1).
'''

# Test Cases
num1 = 15
print(validPerfectSquare2(num1)) # Output: False

num2 = 16
print(validPerfectSquare2(num2)) # Output: True

num3 = 1
print(validPerfectSquare2(num3)) # Output: True

num4 = 4
print(validPerfectSquare2(num4)) # Output: True

num5 = 100
print(validPerfectSquare2(num5)) # Output: True

num6 = 101
print(validPerfectSquare2(num6)) # Output: False

num7 = 144
print(validPerfectSquare2(num7)) # Output: True

num8 = 1000
print(validPerfectSquare2(num8)) # Output: False

num9 = 625
print(validPerfectSquare2(num9)) # Output: True

num10 = 2
print(validPerfectSquare2(num10)) # Output: False