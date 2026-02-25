# INTEGER BREAK

'''
Given an integer n, break it into the sum of k positive integers, where k >= 2, and maximize the product of those integers.
Return the maximum product you can get.
'''

'''
ALGORITHM:

This problem can be solved using either dynamic programming or mathematical optimization.

DYNAMIC PROGRAMMING SOLUTION:
1. dp[i] represents the maximum product for breaking integer i
2. Initialize dp[1] = 1 (base case)
3. For each i from 2 to n:
    a. Try all possible first numbers j from 1 to i-1:
        - j * (i - j): break into j and (i - j)
        - j * dp[i - j]: break j and further break (i - j)
    b. Take the maximum
4. Return dp[n]
'''

# Dynamic Programming Solution
def integerBreak(n):
    dp = [0] * (n + 1)
    dp[1] = 1
    
    for i in range(2, n + 1):
        for j in range(1, i):
            dp[i] = max(
                dp[i],
                j * (i - j),
                j * dp[i - j]
            )
            
    return dp[n]

'''
MATHEMATICAL OPTIMIZATION:
Key insight: For maximum product, break n into as many 3s as possible.
- When we break 3 into 1+2, product is 3
- When we break 3 into 1+1+1, product is 1
- So we want as many 3s as possible, but avoid ending with 1
- If n > 4, we can always use more 3s
- The remainder can be 2, 3, or 4 (if 4, use two 2s)

Algorithm:
1. If n <= 3, return n - 1 (special cases: 2->1, 3->2)
2. Multiply by 3 while n > 4
3. Return result * n
'''

# Optimal Solution using Math
def integerBreak_Optimal(n):
    if n <= 3:
        return n - 1
    
    result = 1
    
    while n > 4:
        result *= 3
        n -= 3
        
    return result * n

'''
Time and Space Complexity:
DYNAMIC PROGRAMMING SOLUTION:
Time Complexity: O(N²) - nested loops to consider all partitions
Space Complexity: O(N) for the dp array

MATHEMATICAL OPTIMIZATION:
Time Complexity: O(N) for the while loop (but iterations are N/3, so effectively O(N))
Space Complexity: O(1) - constant space
'''

# Test Cases

# Test Case 1: n = 2
n1 = 2
result1 = integerBreak_Optimal(n1)
print(result1)  # Expected: 1 (break as 1+1)

# Test Case 2: n = 3
n2 = 3
result2 = integerBreak_Optimal(n2)
print(result2)  # Expected: 2 (break as 1+2)

# Test Case 3: n = 4
n3 = 4
result3 = integerBreak_Optimal(n3)
print(result3)  # Expected: 4 (break as 2+2)

# Test Case 4: n = 5
n4 = 5
result4 = integerBreak_Optimal(n4)
print(result4)  # Expected: 6 (break as 2+3)

# Test Case 5: n = 6
n5 = 6
result5 = integerBreak_Optimal(n5)
print(result5)  # Expected: 9 (break as 3+3)

# Test Case 6: n = 7
n6 = 7
result6 = integerBreak_Optimal(n6)
print(result6)  # Expected: 12 (break as 3+4, then 3+2+2)

# Test Case 7: n = 8
n7 = 8
result7 = integerBreak_Optimal(n7)
print(result7)  # Expected: 18 (3+3+2)

# Test Case 8: n = 9
n8 = 9
result8 = integerBreak_Optimal(n8)
print(result8)  # Expected: 27 (3+3+3)

# Test Case 9: n = 10
n9 = 10
result9 = integerBreak_Optimal(n9)
print(result9)  # Expected: 36 (3+3+4 = 3+3+2+2)

# Test Case 10: n = 58
n10 = 58
result10 = integerBreak_Optimal(n10)
print(result10)  # Expected: large number