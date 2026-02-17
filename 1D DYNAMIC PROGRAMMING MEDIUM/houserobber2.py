# HOUSE ROBBER 2

'''
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed. 
All houses at this place are arranged in a circle. 
That means the first house is the neighbor of the last one. 
Meanwhile, adjacent houses have a security system connected, and it will automatically contact the police if two adjacent houses were broken into on the same night.
Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.
'''

'''
ALGORITHM:

This problem is an extension of House Robber. Since houses are arranged in a circle:
- If you rob the first house, you cannot rob the last house
- If you don't rob the first house, you can consider robbing the last house

The solution handles this by considering two cases:
1. Rob houses from index 0 to n-2 (excluding the last house)
2. Rob houses from index 1 to n-1 (excluding the first house)

For the helper function `robHouse(nums)`:
1. Initialize prev2 = 0, prev1 = 0
2. For each house:
    - current = max(prev2, prev1 + nums[i])
    - prev2 = prev1
    - prev1 = current
3. Return prev1

The main function:
- If n == 1, return nums[0]
- Otherwise, return max(robHouse(nums[1:]), robHouse(nums[:-1]))
'''

def rob(nums):
    n = len(nums)
    if n == 1:
        return nums[0]
    
    def robHouse(nums):
        n = len(nums)
        prev2, prev1 = 0, 0
        
        for i in range(n):
            current = max(prev2, prev1 + nums[i])
            prev2 = prev1
            prev1 = current
            
        return prev1
    
    return max(robHouse(nums[1:]), robHouse(nums[:-1]))

'''
Time Complexity: O(n) - We traverse the array twice (once for each case).
Space Complexity: O(1) - Only using constant extra space for the helper function.
'''

# Test Cases

# Test Case 1: Basic case [2, 3, 2]
nums1 = [2, 3, 2]
result1 = rob(nums1)
print(result1) # Expected: 3 (rob house 1 (3))

# Test Case 2: [1, 2, 3, 1]
nums2 = [1, 2, 3, 1]
result2 = rob(nums2)
print(result2) # Expected: 4 (rob house 1 (2) and house 3 (1) or house 0 (1) and house 2 (3))

# Test Case 3: Single house [1]
nums3 = [1]
result3 = rob(nums3)
print(result3) # Expected: 1

# Test Case 4: Two houses [2, 3]
nums4 = [2, 3]
result4 = rob(nums4)
print(result4) # Expected: 3 (rob house 1)

# Test Case 5: Two houses [3, 2, 3]
nums5 = [3, 2, 3]
result5 = rob(nums5)
print(result5) # Expected: 3 (rob house 0 or house 2)

# Test Case 6: All same values [1, 1, 1, 1, 1]
nums6 = [1, 1, 1, 1, 1]
result6 = rob(nums6)
print(result6) # Expected: 3

# Test Case 7: Large first and last [10, 1, 1, 10]
nums7 = [10, 1, 1, 10]
result7 = rob(nums7)
print(result7) # Expected: 20 (rob house 0 and house 3)

# Test Case 8: Zigzag [1, 3, 1, 3, 100]
nums8 = [1, 3, 1, 3, 100]
result8 = rob(nums8)
print(result8) # Expected: 104 (rob house 1, 3, and 4)

# Test Case 9: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
nums9 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result9 = rob(nums9)
print(result9) # Expected: 30 (rob houses at indices 1, 3, 5, 7, 9 = 2+4+6+8+10)

# Test Case 10: Zeros [0, 0, 0, 0, 0]
nums10 = [0, 0, 0, 0, 0]
result10 = rob(nums10)
print(result10) # Expected: 0