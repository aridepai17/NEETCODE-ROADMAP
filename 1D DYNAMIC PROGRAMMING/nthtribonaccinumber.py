# NTH TRIBONACCI NUMBER

'''
The Tribonacci sequence Tn is defined as follows: 
T0 = 0, T1 = 1, T2 = 1, and Tn+3 = Tn + Tn+1 + Tn+2 for n >= 0.
Given n, return the value of Tn.
'''

'''
ALGORITHM:

The Tribonacci sequence is similar to Fibonacci but with three previous terms.
- T0 = 0
- T1 = 1
- T2 = 1
- Tn = Tn-1 + Tn-2 + Tn-3 for n >= 3

For the space-optimized solution:
1. Base cases:
    - If n == 0, return 0
    - If n <= 2, return 1

2. Initialize three variables:
    - a = 0 (represents T0)
    - b = 1 (represents T1)
    - c = 1 (represents T2)

3. For each i from 3 to n:
    - Calculate new value: a + b + c
    - Shift the variables: a = b, b = c, c = new value

4. Return c (which now holds Tn)
'''

# Recursive Solution (Inefficient - O(3^n) time)
def tribonnaciRecursive(n):
    if n == 0:
        return 0
    if n <= 2:
        return 1
    return tribonnaciRecursive(n - 1) + tribonnaciRecursive(n - 2) + tribonnaciRecursive(n - 3)

# Tabulation Method (Bottom-up DP - O(n) time, O(n) space)
def tribonnaciTabulation(n):
    if n == 0:
        return 0
    if n <= 2:
        return 1
    
    dp = [0] * (n + 1)
    dp[0] = 0
    dp[1] = 1
    dp[2] = 1
    
    for i in range(3, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3]
        
    return dp[n]

# Space Optimized Solution (Bottom-up DP with constant space - O(n) time, O(1) space)
def tribonnaci(n):
    if n == 0:
        return 0
    if n <= 2:
        return 1
    
    a, b, c = 0, 1, 1
    for i in range(3, n + 1):
        a, b, c = b, c, a + b + c
        
    return c

'''
Time Complexity: O(n) - We iterate from 3 to n exactly once.

Space Complexity: 
- Recursive: O(n) - Due to recursion stack (also O(3^n) time)
- Tabulation: O(n) - For the dp array
- Space Optimized: O(1) - Only three variables are used
'''

# Test Cases

# Test Case 1: n = 0
result1 = tribonnaci(0)
print(result1) # Expected: 0

# Test Case 2: n = 1
result2 = tribonnaci(1)
print(result2) # Expected: 1

# Test Case 3: n = 2
result3 = tribonnaci(2)
print(result3) # Expected: 1

# Test Case 4: n = 3
result4 = tribonnaci(3)
print(result4) # Expected: 2 (T0=0, T1=1, T2=1, T3=0+1+1=2)

# Test Case 5: n = 4
result5 = tribonnaci(4)
print(result5) # Expected: 4 (T4=T3+T2+T1=2+1+1=4)

# Test Case 6: n = 5
result6 = tribonnaci(5)
print(result6) # Expected: 7 (T5=T4+T3+T2=4+2+1=7)

# Test Case 7: n = 10
result7 = tribonnaci(10)
print(result7) # Expected: 149

# Test Case 8: n = 20
result8 = tribonnaci(20)
print(result8) # Expected: 35890

# Test Case 9: n = 30
result9 = tribonnaci(30)
print(result9) # Expected: 1149851

# Test Case 10: n = 37
result10 = tribonnaci(37)
print(result10) # Expected: 1134903170