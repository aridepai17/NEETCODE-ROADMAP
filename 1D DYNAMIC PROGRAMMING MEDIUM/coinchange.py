# COIN CHANGE

'''
You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.
Return the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.
You may assume that you have an infinite number of each kind of coin.
'''

'''
ALGORITHM:

This is a classic dynamic programming problem (Unbounded Knapsack). We use bottom-up DP where dp[i] represents the minimum number of coins needed to make amount i.

The recurrence relation is:
- dp[i] = min(dp[i - coin] + 1) for all coins where i - coin >= 0

We initialize dp array with amount + 1 (a value larger than any possible answer) to represent "infinity".
- dp[0] = 0 (0 coins needed to make amount 0)

Algorithm:
1. Initialize dp array of size (amount + 1) with value amount + 1
2. Set dp[0] = 0
3. For each amount i from 1 to amount:
    - For each coin in coins:
        - If i - coin >= 0, update dp[i] = min(dp[i], 1 + dp[i - coin])
4. If dp[amount] is still amount + 1, return -1 (impossible)
5. Otherwise, return dp[amount]
'''

def coinChange(coins, amount):
    dp = [amount + 1] * (amount + 1)
    dp[0] = 0
    
    for a in range(1, amount + 1):
        for c in coins:
            if a - c >= 0:
                dp[a] = min(dp[a], 1 + dp[a - c])
                
    if dp[amount] != amount + 1:
        return dp[amount]
    else:
        return -1

'''
Time Complexity: O(N * A), where N is the number of coins and A is the amount. We iterate through all amounts and for each amount, we try all coins.
Space Complexity: O(A) for the dp array.
'''

# Test Cases

# Test Case 1: Basic case
coins1 = [1, 2, 5]
amount1 = 11
result1 = coinChange(coins1, amount1)
print(result1) # Expected: 3 (5 + 5 + 1)

# Test Case 2: Amount is 0
coins2 = [1]
amount2 = 0
result2 = coinChange(coins2, amount2)
print(result2) # Expected: 0

# Test Case 3: Impossible case
coins3 = [2]
amount3 = 1
result3 = coinChange(coins3, amount3)
print(result3) # Expected: -1

# Test Case 4: Single coin type
coins4 = [1]
amount4 = 10
result4 = coinChange(coins4, amount4)
print(result4) # Expected: 10

# Test Case 5: Two coin types
coins5 = [1, 2]
amount5 = 3
result5 = coinChange(coins5, amount5)
print(result5) # Expected: 2 (1 + 2)

# Test Case 6: Large amount
coins6 = [1, 2, 5]
amount6 = 100
result6 = coinChange(coins6, amount6)
print(result6) # Expected: 20

# Test Case 7: Coin value larger than amount
coins7 = [5, 10]
amount7 = 3
result7 = coinChange(coins7, amount7)
print(result7) # Expected: -1

# Test Case 8: Multiple of largest coin
coins8 = [1, 5, 10, 25]
amount8 = 50
result8 = coinChange(coins8, amount8)
print(result8) # Expected: 2 (25 + 25)

# Test Case 9: Greedy fails, DP works
coins9 = [1, 5, 6, 9]
amount9 = 11
result9 = coinChange(coins9, amount9)
print(result9) # Expected: 2 (5 + 6)

# Test Case 10: All coins available
coins10 = [1, 2, 5, 10, 20]
amount10 = 99
result10 = coinChange(coins10, amount10)
print(result10) # Expected: 9 (20+20+20+20+10+5+2+2)