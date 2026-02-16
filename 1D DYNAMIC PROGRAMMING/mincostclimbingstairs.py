# MIN COST CLIMBING STAIRS


'''
You are given an integer array cost where cost[i] is the cost of ith step on a staircase.
Once you pay the cost, you can either climb one or two steps.
You can either start from the step with index 0, or the step with index 1.
Return the minimum cost to reach the top of the floor.
'''

'''
ALGORITHM:

This is a dynamic programming problem where we need to find the minimum cost to reach the top.
The key insight is that to reach step i, we can come from either step i-1 or step i-2.

For the optimal solution:
1. Initialize:
    - prev1 = cost[0] (minimum cost to reach step 0)
    - prev2 = cost[1] (minimum cost to reach step 1)

2. For each step i from 2 to n-1:
    - Calculate current = min(prev1, prev2) + cost[i]
    - Update: prev1 = prev2, prev2 = current

3. Return min(prev1, prev2) - the minimum cost to reach the top (beyond the last step)

Note: We don't pay cost for the "top" position, only for each step we climb.
The final answer is the minimum cost to reach beyond the last step, which comes from either the last step or the second-to-last step.
'''

# Tabulation Method
def minCostClimbingStairsTabulation(cost):
    n = len(cost)
    minCost = [0] * (n + 1)
    minCost[0] = cost[0]
    minCost[1] = cost[0]
    
    for i in range(2, n + 1):
        minCost[i] = min(minCost[i - 1], minCost[i - 2]) + cost[i]
        
    return min(minCost[n - 1], minCost[n - 2])


# Optimal Solution (O(1) space)
def minCostClimbingStairs(cost):
    n = len(cost)
    prev1 = cost[0]
    prev2 = cost[1]
    
    for i in range(2, n):
        current = min(prev1, prev2) + cost[i]
        prev1 = prev2
        prev2 = current
        
    return min(prev1, prev2)

'''
Time Complexity: O(n) - We iterate through the cost array once.

Space Complexity: 
- Tabulation: O(n) - For the minCost array
- Optimal: O(1) - Only two variables are used
'''

# Test Cases

# Test Case 1: Basic case with costs [10, 15, 20]
cost1 = [10, 15, 20]
result1 = minCostClimbingStairs(cost1)
print(result1) # Expected: 15 (start at index 1: pay 15, then take 1 step to top)

# Test Case 2: Equal costs [1, 1, 1, 1]
cost2 = [1, 1, 1, 1]
result2 = minCostClimbingStairs(cost2)
print(result2) # Expected: 3

# Test Case 3: Increasing costs [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
cost3 = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
result3 = minCostClimbingStairs(cost3)
print(result3) # Expected: 6

# Test Case 4: Two steps [0, 0, 0]
cost4 = [0, 0, 0]
result4 = minCostClimbingStairs(cost4)
print(result4) # Expected: 0

# Test Case 5: Two steps [10, 10]
cost5 = [10, 10]
result5 = minCostClimbingStairs(cost5)
print(result5) # Expected: 10

# Test Case 6: Large first step [10, 1, 1, 1]
cost6 = [10, 1, 1, 1]
result6 = minCostClimbingStairs(cost6)
print(result6) # Expected: 3 (start at index 1: pay 1, then 1, then 1)

# Test Case 7: Large last step [1, 1, 100]
cost7 = [1, 1, 100]
result7 = minCostClimbingStairs(cost7)
print(result7) # Expected: 2

# Test Case 8: Single step [5]
cost8 = [5]
result8 = minCostClimbingStairs(cost8)
print(result8) # Expected: 5

# Test Case 9: Multiple zeros [0, 0, 0, 0, 0]
cost9 = [0, 0, 0, 0, 0]
result9 = minCostClimbingStairs(cost9)
print(result9) # Expected: 0

# Test Case 10: Zigzag costs [1, 100, 200, 3, 100, 5]
cost10 = [1, 100, 200, 3, 100, 5]
result10 = minCostClimbingStairs(cost10)
print(result10) # Expected: 9