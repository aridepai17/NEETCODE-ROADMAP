# PERFECT SQUARES

'''
Given an integer n, return the least number of perfect square numbers that sum to n.
A perfect square is an integer that is the square of an integer; in other words, it is the product of some integer with itself.
For example, 1, 4, 9, and 16 are perfect squares while 3 and 11 are not.
'''

'''
ALGORITHM:

This problem is solved using dynamic programming based on Lagrange's Theorem, which states that any natural number can be represented as the sum of at most 4 perfect squares.

Algorithm:
1. Generate all perfect squares up to n: 1, 4, 9, 16, ...
2. Initialize dp array where dp[i] = minimum number of perfect squares that sum to i
3. Set initial values: dp[0] = 0, dp[1...n] = 4 (worst case by Lagrange's theorem)
4. For each total from 1 to n:
    a. For each square in squares (that is <= total):
        - dp[total] = min(dp[total], 1 + dp[total - square])
5. Return dp[n]

Key insight: Using Lagrange's theorem, we know the answer is at most 4, so we initialize with 4 and try to find smaller solutions.
'''

def perfectSquares(n):
    squares = []
    i = 1
    while i * i <= n:
        squares.append(i * i)
        i += 1
        
    # Lagrange Theorem
    dp = [4] * (n + 1)
    dp[0] = 0
    
    for total in range(1, n + 1):
        for square in squares:
            if square > total:
                break
            dp[total] = min(dp[total], 1 + dp[total - square])
            
    return dp[n]

'''
Time Complexity: O(N × sqrt(N)), where N is the input number. We iterate through all numbers from 1 to N, and for each we iterate through all perfect squares up to that number.
Space Complexity: O(N) for the dp array.
'''

# Test Cases

# Test Case 1: Basic case
n1 = 12
result1 = perfectSquares(n1)
print(result1)  # Expected: 3 (4 + 4 + 4)

# Test Case 2: Already a perfect square
n2 = 16
result2 = perfectSquares(n2)
print(result2)  # Expected: 1 (16)

# Test Case 3: n = 1
n3 = 1
result3 = perfectSquares(n3)
print(result3)  # Expected: 1 (1)

# Test Case 4: n = 2
n4 = 2
result4 = perfectSquares(n4)
print(result4)  # Expected: 2 (1 + 1)

# Test Case 5: n = 3
n5 = 3
result5 = perfectSquares(n5)
print(result5)  # Expected: 3 (1 + 1 + 1)

# Test Case 6: Classic case 13 = 4 + 9
n6 = 13
result6 = perfectSquares(n6)
print(result6)  # Expected: 2

# Test Case 7: n = 100
n7 = 100
result7 = perfectSquares(n7)
print(result7)  # Expected: 1 (10^2)

# Test Case 8: n = 99
n8 = 99
result8 = perfectSquares(n8)
print(result8)  # Expected: 3 (9 + 9 + 81)

# Test Case 9: n = 48
n9 = 48
result9 = perfectSquares(n9)
print(result9)  # Expected: 3 (16 + 16 + 16)

# Test Case 10: Large n
n10 = 10000
result10 = perfectSquares(n10)
print(result10)  # Expected: 1 (100^2)