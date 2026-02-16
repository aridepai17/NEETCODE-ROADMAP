# CLIMBING STAIRS

'''
You are climbing a staircase. It takes n steps to reach the top.
Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
'''

'''
ALGORITHM:

This problem is essentially finding the n-th Fibonacci number.

For the optimal solution (using constant space):
1. Base cases:
    - If n == 1, return 1 (only one way: take 1 step)
    - If n == 2, return 2 (two ways: take 1+1 or take 2)

2. Initialize:
    - prev = 1 (ways to reach step 1)
    - current = 2 (ways to reach step 2)

3. For each step from 3 to n:
    - Calculate new ways = prev + current
    - Update prev = current
    - Update current = new ways

4. Return current (which now holds the answer for step n)

The reasoning:
- To reach step n, you can come from step n-1 (take 1 step) or from step n-2 (take 2 steps)
- So ways(n) = ways(n-1) + ways(n-2)
- This is the Fibonacci sequence!
'''

# Recursive Solution (Inefficient - O(2^n) time)
def climbStairsRecursive(n):
    if n == 1:
        return 1
    if n == 2:
        return 2
    return climbStairsRecursive(n - 1) + climbStairsRecursive(n - 2)


# Tabulation Solution (Bottom-up DP - O(n) time, O(n) space)
def climbStairsTabulation(n):
    if n == 1:
        return 1
    if n == 2:
        return 2
    dp = [0] * (n + 1)
    dp[1] = 1
    dp[2] = 2
    for i in range(3, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    return dp[n]


# Optimal Solution (Bottom-up DP with constant space - O(n) time, O(1) space)
def climbStairs(n):
    if n == 1:
        return 1
    if n == 2:
        return 2
    
    prev, current = 1, 2
    for i in range(3, n + 1):
        prev, current = current, prev + current
        
    return current

'''
Time Complexity: O(n) - We iterate from 2 to n exactly once.

Space Complexity: 
- Recursive: O(n) - Due to recursion stack (also O(2^n) time)
- Tabulation: O(n) - For the dp array
- Optimal: O(1) - Only two variables are used
'''

# Test Cases

# Test Case 1: n = 1
result1 = climbStairs(1)
print(result1) # Expected: 1

# Test Case 2: n = 2
result2 = climbStairs(2)
print(result2) # Expected: 2

# Test Case 3: n = 3
result3 = climbStairs(3)
print(result3) # Expected: 3 (1+1+1, 1+2, 2+1)

# Test Case 4: n = 4
result4 = climbStairs(4)
print(result4) # Expected: 5

# Test Case 5: n = 5
result5 = climbStairs(5)
print(result5) # Expected: 8

# Test Case 6: n = 10
result6 = climbStairs(10)
print(result6) # Expected: 89

# Test Case 7: n = 20
result7 = climbStairs(20)
print(result7) # Expected: 10946

# Test Case 8: n = 30
result8 = climbStairs(30)
print(result8) # Expected: 1346269

# Test Case 9: n = 40
result9 = climbStairs(40)
print(result9) # Expected: 165580141

# Test Case 10: n = 45
result10 = climbStairs(45)
print(result10) # Expected: 1836311903