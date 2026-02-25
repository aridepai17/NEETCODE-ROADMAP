# PARTITION EQUAL SUBSET SUM

'''
Given an integer array nums, return true if you can partition the array into two subsets such that the sum of the elements in both subsets is equal or false otherwise.
'''

'''
ALGORITHM:

This problem is solved using dynamic programming, treating it as a subset sum problem. We need to find if we can form a subset with sum = total/2.

Algorithm:
1. Calculate total sum of array. If odd, return False (cannot partition into equal halves)
2. Set target = total // 2
3. Create dp array where dp[s] = True if we can form sum s using some subset of elements
4. Initialize dp[0] = True (empty set forms sum 0)
5. For each num in nums:
    a. Iterate s from target down to num (reverse to avoid using same element twice)
    b. Update dp[s] = dp[s] or dp[s - num]
6. Return dp[target]

Key insight: We use reverse iteration because each number can only be used once (0/1 knapsack).
'''

def canPartition(nums):
    total = sum(nums)
    
    if total % 2 != 0:
        return False
    
    target = total // 2
    
    dp = [False] * (target + 1)
    dp[0] = True
    
    for num in nums:
        for s in range(target, num - 1, -1):
            dp[s] = dp[s] or dp[s - num]
            
    return dp[target]

'''
Time Complexity: O(N × S), where N is the length of the array and S is the target sum (total // 2).
Space Complexity: O(S), for the dp array.
'''

# Test Cases

# Test Case 1: Basic case
nums1 = [1, 5, 11, 5]
result1 = canPartition(nums1)
print(result1)  # Expected: True ([1, 5, 5] and [11])

# Test Case 2: Cannot partition
nums2 = [1, 2, 3, 5]
result2 = canPartition(nums2)
print(result2)  # Expected: False (sum is 11, odd)

# Test Case 3: Single element
nums3 = [1]
result3 = canPartition(nums3)
print(result3)  # Expected: False

# Test Case 4: Two equal elements
nums4 = [1, 1]
result4 = canPartition(nums4)
print(result4)  # Expected: True

# Test Case 5: All same elements
nums5 = [2, 2, 2, 2]
result5 = canPartition(nums5)
print(result5)  # Expected: True ([2,2] and [2,2])

# Test Case 6: Larger numbers
nums6 = [1, 2, 3, 4, 5, 6, 7]
result6 = canPartition(nums6)
print(result6)  # Expected: True (sum=28, target=14)

# Test Case 7: Cannot form equal partition
nums7 = [3, 3, 3, 3]
result7 = canPartition(nums7)
print(result7)  # Expected: False (sum=12, target=6, can't make 6 with 3s)

# Test Case 8: Already equal
nums8 = [1, 1, 2, 2]
result8 = canPartition(nums8)
print(result8)  # Expected: True ([1,1] and [2,2])

# Test Case 9: Multiple possible partitions
nums9 = [2, 2, 2, 2, 2, 2]
result9 = canPartition(nums9)
print(result9)  # Expected: True ([2,2,2] and [2,2,2])

# Test Case 10: Large single element
nums10 = [100]
result10 = canPartition(nums10)
print(result10)  # Expected: False