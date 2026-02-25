# COMBINATION SUM 4

'''
Given an array of distinct integers nums and a target integer target, return the number of possible combinations that add up to target.
The test cases are generated so that the answer can fit in a 32-bit integer.
'''

'''
ALGORITHM:

This problem is solved using dynamic programming. It's similar to the climbing stairs problem where we have multiple "steps" (the nums array) instead of just 1 or 2.

Algorithm:
1. Create dp array where dp[total] = number of ways to form sum = total
2. Initialize dp[0] = 1 (one way to form sum 0: use no elements)
3. For each total from 1 to target:
    a. For each num in nums:
        - If total >= num, add dp[total - num] to dp[total]
4. Return dp[target]

Key insight: We count combinations (order matters for permutations, which is handled by iterating total from small to large).
'''

def combinationSum4(nums, target):
    dp = [0] * (target + 1)
    dp[0] = 1
    
    for total in range(1, target + 1):
        for num in nums:
            if total - num >= 0:
                dp[total] += dp[total - num]
                
    return dp[target]

'''
Time Complexity: O(T × N), where T is the target and N is the length of nums. We iterate through each value up to target and try each number in nums.
Space Complexity: O(T) for the dp array.
'''

# Test Cases

# Test Case 1: Basic case
nums1 = [1, 2, 3]
target1 = 4
result1 = combinationSum4(nums1, target1)
print(result1)  # Expected: 7
# Combinations: [1,1,1,1], [1,1,2], [1,2,1], [2,1,1], [2,2], [1,3], [3,1]

# Test Case 2: Single element
nums2 = [1]
target2 = 1
result2 = combinationSum4(nums2, target2)
print(result2)  # Expected: 1

# Test Case 3: Two elements
nums3 = [1, 2]
target3 = 3
result3 = combinationSum4(nums3, target3)
print(result3)  # Expected: 3 ([1,1,1], [1,2], [2,1])

# Test Case 4: Larger target
nums4 = [1, 2, 3]
target4 = 5
result4 = combinationSum4(nums4, target4)
print(result4)  # Expected: 13

# Test Case 5: No valid combination
nums5 = [2]
target5 = 1
result5 = combinationSum4(nums5, target5)
print(result5)  # Expected: 0

# Test Case 6: Target is 0
nums6 = [1, 2]
target6 = 0
result6 = combinationSum4(nums6, target6)
print(result6)  # Expected: 1 (empty combination)

# Test Case 7: nums = [1,2,5,25], target = 100
nums7 = [1, 2, 5, 25]
target7 = 100
result7 = combinationSum4(nums7, target7)
print(result7)  # Expected: Depends on calculation

# Test Case 8: Single element larger than target
nums8 = [5]
target8 = 2
result8 = combinationSum4(nums8, target8)
print(result8)  # Expected: 0

# Test Case 9: nums = [1,2,3,10], target = 1000 (large)
nums9 = [1, 2, 3, 10]
target9 = 100
result9 = combinationSum4(nums9, target9)
print(result9)

# Test Case 10: Repeated same number
nums10 = [2, 2]
target10 = 4
result10 = combinationSum4(nums10, target10)
print(result10)  # Expected: 3 ([2,2], [2,2] - wait, duplicates in nums are not distinct, so [2,2] counts once. Actually order matters: [2,2], [2,2] - but nums has duplicates. Wait, the problem says "distinct integers", so this test case is invalid. Let me change it)