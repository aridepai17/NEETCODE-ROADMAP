# PAINT HOUSE

'''
There are a row of n houses, each house can be painted with one of the three colors: red, blue or green. 
The cost of painting each house with a certain color is different. 
You have to paint all the houses such that no two adjacent houses have the same color, and you need to cost the least. 
Return the minimum cost.
The cost of painting each house with a certain color is represented by a n x 3 cost matrix. 
For example, costs[0][0] is the cost of painting house 0 with color red; costs[1][2] is the cost of painting house 1 with color green, and so on... 
Find the minimum cost to paint all houses.
'''

'''
ALGORITHM:

This is a dynamic programming problem where we need to track the minimum cost for each color at each house.

At each house, we can paint it with any color except the color used by the previous house.
- If we paint with color 0 (red), we must have painted the previous house with color 1 or 2
- If we paint with color 1 (blue), we must have painted the previous house with color 0 or 2
- If we paint with color 2 (green), we must have painted the previous house with color 0 or 1

The DP formula:
- dp[i][j] = costs[i][j] + min(dp[i-1][k]) for all k != j

For the optimal space solution:
1. Initialize dp = [0, 0, 0] to track the minimum cost ending with each color
2. For each house i:
    - Calculate new dp values:
        - dp0 = costs[i][0] + min(dp[1], dp[2]) (paint red, prev can't be red)
        - dp1 = costs[i][1] + min(dp[0], dp[2]) (paint blue, prev can't be blue)
        - dp2 = costs[i][2] + min(dp[0], dp[1]) (paint green, prev can't be green)
    - Update dp = [dp0, dp1, dp2]
3. Return min(dp) - the minimum cost to paint all houses
'''

def minCost(costs):
    # costs[i][j] => i is house no and j is color
    n = len(costs)
    if n == 0:
        return 0
    
    dp = [0, 0, 0]
    
    
    for i in range(n):
        dp0 = costs[i][0] + min(dp[1], dp[2])
        dp1 = costs[i][1] + min(dp[0], dp[2])
        dp2 = costs[i][2] + min(dp[0], dp[1])
        dp = [dp0, dp1, dp2]
        
    return min(dp)

'''
Time Complexity: O(n) - We iterate through all houses once.
Space Complexity: O(1) - Only using 3 variables to track the DP state.
'''

# Test Cases

# Test Case 1: Basic case
costs1 = [[17, 2, 17], [16, 16, 5], [14, 3, 9]]
result1 = minCost(costs1)
print(result1) # Expected: 10 (paint house 0: color 1 (2), house 1: color 2 (5), house 2: color 1 (3) = 10)

# Test Case 2: Single house
costs2 = [[1, 2, 3]]
result2 = minCost(costs2)
print(result2) # Expected: 1 (choose cheapest color for the single house)

# Test Case 3: Two houses
costs3 = [[1, 2, 3], [1, 2, 3]]
result3 = minCost(costs3)
print(result3) # Expected: 3 (house 0: color 0 (1), house 1: color 1 (2) = 3)

# Test Case 4: All same costs
costs4 = [[5, 5, 5], [5, 5, 5], [5, 5, 5]]
result4 = minCost(costs4)
print(result4) # Expected: 15

# Test Case 5: Increasing costs
costs5 = [[1, 3, 2], [4, 5, 6], [7, 8, 9]]
result5 = minCost(costs5)
print(result5) # Expected: 12

# Test Case 6: Zigzag pattern (alternating best choices)
costs6 = [[5, 8, 6], [4, 8, 3], [7, 5, 9], [3, 4, 6]]
result6 = minCost(costs6)
print(result6) # Expected: 18

# Test Case 7: Large first color
costs7 = [[100, 50, 30], [20, 70, 50], [30, 60, 40]]
result7 = minCost(costs7)
print(result7) # Expected: 100

# Test Case 8: Minimum at different positions
costs8 = [[3, 100, 100], [100, 100, 3], [3, 100, 100]]
result8 = minCost(costs8)
print(result8) # Expected: 106

# Test Case 9: Three houses
costs9 = [[17, 2, 17], [16, 16, 5], [14, 3, 9]]
result9 = minCost(costs9)
print(result9) # Expected: 10

# Test Case 10: All zeros
costs10 = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
result10 = minCost(costs10)
print(result10) # Expected: 0