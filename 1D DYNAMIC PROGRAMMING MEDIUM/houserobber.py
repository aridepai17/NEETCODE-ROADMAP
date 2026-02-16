# HOUSE ROBBER

'''
You are a professional robber planning to rob houses along a street. 
Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security systems connected and it will automatically contact the police if two adjacent houses were broken into on the same night.
Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.
'''

'''
ALGORITHM:

This is a classic dynamic programming problem. At each house, we have two choices:
1. Rob this house: Then we can't rob the previous house, so total = nums[i] + dp[i-2]
2. Don't rob this house: Then we take whatever we got from the previous house, total = dp[i-1]

We take the maximum of these two choices.

For the optimal solution:
1. Handle edge cases:
    - If n <= 2, return max(nums)

2. Initialize:
    - prev1 = nums[0] (maximum rob amount considering house 0)
    - prev2 = max(nums[0], nums[1]) (maximum considering houses 0 and 1)

3. For each house i from 2 to n-1:
    - Calculate current = max(prev2, prev1 + nums[i])
    - Update: prev1 = prev2, prev2 = current

4. Return prev2 (the maximum amount that can be robbed)
'''

# Tabulation Method
def robTabulation(nums):
    n = len(nums)
    if n <= 2:
        return max(nums)
    
    dp = [0] * (n + 1)
    dp[0] = nums[0]
    dp[1] = max(nums[0], nums[1])
    
    for i in range(2, n):
        dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])
        
    return dp[n - 1]

# Optimal Solution (O(1) space)
def rob(nums):
    n = len(nums)
    if n <= 2:
        return max(nums)
    
    prev1 = nums[0]
    prev2 = max(nums[0], nums[1])
    
    for i in range(2, n):
        current = max(prev2, prev1 + nums[i])
        prev1 = prev2
        prev2 = current
        
    return prev2

'''
Time Complexity: O(n) - We iterate through the houses once.

Space Complexity: 
- Tabulation: O(n) - For the dp array
- Optimal: O(1) - Only two variables are used
'''

# Test Cases

# Test Case 1: Basic case [1, 2, 3, 1]
nums1 = [1, 2, 3, 1]
result1 = rob(nums1)
print(result1) # Expected: 4 (rob house 0 (1) and house 2 (3) = 1 + 3 = 4)

# Test Case 2: [2, 7, 9, 3, 1]
nums2 = [2, 7, 9, 3, 1]
result2 = rob(nums2)
print(result2) # Expected: 12 (rob house 0 (2), house 2 (9), house 4 (1) = 2 + 9 + 1 = 12)

# Test Case 3: Single house [1]
nums3 = [1]
result3 = rob(nums3)
print(result3) # Expected: 1

# Test Case 4: Two houses [2, 1, 1, 2]
nums4 = [2, 1, 1, 2]
result4 = rob(nums4)
print(result4) # Expected: 4 (rob house 0 (2) and house 3 (2) = 2 + 2 = 4)

# Test Case 5: All zeros [0, 0, 0, 0]
nums5 = [0, 0, 0, 0]
result5 = rob(nums5)
print(result5) # Expected: 0

# Test Case 6: Alternating pattern [1, 3, 1, 3, 100]
nums6 = [1, 3, 1, 3, 100]
result6 = rob(nums6)
print(result6) # Expected: 104 (rob house 1 (3), house 3 (3), house 4 (100) = 3 + 3 + 100 = 104)

# Test Case 7: Decreasing values [5, 1, 1, 2, 3, 1]
nums7 = [5, 1, 1, 2, 3, 1]
result7 = rob(nums7)
print(result7) # Expected: 10 (rob house 0 (5), house 3 (2), house 4 (3) = 5 + 2 + 3 = 10)

# Test Case 8: Large array [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
nums8 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result8 = rob(nums8)
print(result8) # Expected: 30 (rob houses at indices 1, 3, 5, 7, 9 = 2+4+6+8+10 = 30)

# Test Case 9: Two houses equal [5, 5]
nums9 = [5, 5]
result9 = rob(nums9)
print(result9) # Expected: 5

# Test Case 10: All same values [3, 3, 3, 3, 3]
nums10 = [3, 3, 3, 3, 3]
result10 = rob(nums10)
print(result10) # Expected: 9 (rob houses 0, 2, 4 = 3 + 3 + 3 = 9)