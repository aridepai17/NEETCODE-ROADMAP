# 4 KEYS KEYBOARD

'''
Imagine you have a special keyboard with the following keys:
Key 1: (A): Print one 'A' on screen.
Key 2: (Ctrl-A): Select the whole screen.
Key 3: (Ctrl-C): Copy selection to buffer.
Key 4: (Ctrl-V): Print buffer on screen appending it after what has already been printed.
Now, you can only press the keyboard for N times (with the above four keys), find out the maximum numbers of 'A' you can print on screen.
'''

'''
ALGORITHM:

This problem is a classic dynamic programming problem. The key insight is:
- For N <= 6, it's optimal to just press 'A' N times (no benefit from copy-paste)
- For N > 6, we can use a combination of operations to maximize the output

The DP formula is based on the observation that the optimal sequence for large N will be:
- Press A some times to build up some As
- Then do Ctrl-A, Ctrl-C (takes 2 key presses)
- Then do Ctrl-V some times to paste the buffer (each paste takes 1 key press)

For the DP approach:
1. For i from 1 to 6: dp[i] = i (just press A)
2. For i from 7 to n:
    - dp[i] = max of:
        - dp[i-3] * 2 (do Ctrl-A, Ctrl-C, then Ctrl-V once)
        - dp[i-4] * 3 (do Ctrl-A, Ctrl-C, then Ctrl-V twice)
        - dp[i-5] * 4 (do Ctrl-A, Ctrl-C, then Ctrl-V three times)

This works because:
- To do Ctrl-A, Ctrl-C, we need 2 key presses (we're at dp[i-3])
- After that, each Ctrl-V gives us the current buffer
- If we do k Ctrl-V operations, we multiply the result by (k+1), hence 2, 3, 4 factors
'''

def maxA(n):
    if n <= 6:
        return n
    
    dp = [0] * (n + 1)
    
    for i in range(1, 7):
        dp[i] = i
    for i in range(7, n + 1):
        dp[i] = max(
            dp[i - 3] * 2,
            dp[i - 4] * 3,
            dp[i - 5] * 4
        )
        
    return dp[n]

'''
Time Complexity: O(N), where N is the number of key presses. We iterate from 1 to N exactly once.
Space Complexity: O(N) for the dp array to store intermediate results.
'''

# Test Cases

# Test Case 1: n = 1
result1 = maxA(1)
print(result1) # Expected: 1

# Test Case 2: n = 2
result2 = maxA(2)
print(result2) # Expected: 2

# Test Case 3: n = 3
result3 = maxA(3)
print(result3) # Expected: 3

# Test Case 4: n = 4
result4 = maxA(4)
print(result4) # Expected: 4

# Test Case 5: n = 5
result5 = maxA(5)
print(result5) # Expected: 5

# Test Case 6: n = 6
result6 = maxA(6)
print(result6) # Expected: 6

# Test Case 7: n = 7
result7 = maxA(7)
print(result7) # Expected: 9 (optimal: A, A, A, Ctrl-A, Ctrl-C, Ctrl-V, Ctrl-V = 3 * 3 = 9)

# Test Case 8: n = 8
result8 = maxA(8)
print(result8) # Expected: 12

# Test Case 9: n = 9
result9 = maxA(9)
print(result9) # Expected: 16

# Test Case 10: n = 10
result10 = maxA(10)
print(result10) # Expected: 20
