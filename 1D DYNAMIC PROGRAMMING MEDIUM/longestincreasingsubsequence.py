# LONGEST INCREASING SUBSEQUENCE

'''
Given an integer array nums, return the length of the longest strictly increasing subsequence.
'''

def lengthofLIS(nums):
    LIS = [1] * len(nums)
    
    for i in range(len(nums) - 1, -1, -1):
        for j in range(i + 1, len(nums)):
            if nums[i] < nums[j]:
                LIS[i] = max(LIS[i], 1 + LIS[j])
                
    return max(LIS)

'''
ALGORITHM:

This problem is solved using dynamic programming where LIS[i] represents the length of the longest increasing subsequence starting at index i.

Algorithm:
1. Initialize LIS array with all 1s (each element is a subsequence of length 1)
2. Iterate from right to left (i from len(nums)-1 to 0):
    a. For each i, check all j > i:
        - If nums[i] < nums[j], we can extend the subsequence: LIS[i] = max(LIS[i], 1 + LIS[j])
3. Return max(LIS)

Key insight: We build solutions from right to left, considering each element as a potential starting point of an increasing subsequence.
'''

'''
Time Complexity: O(N²), where N is the length of the array. We use nested loops to compare each pair of elements.
Space Complexity: O(N) for the LIS array.
'''

# Test Cases

# Test Case 1: Basic case
nums1 = [10, 9, 2, 5, 3, 7, 101, 18]
result1 = lengthofLIS(nums1)
print(result1)  # Expected: 4 (2, 3, 7, 101 or 2, 3, 7, 18)

# Test Case 2: Single element
nums2 = [1]
result2 = lengthofLIS(nums2)
print(result2)  # Expected: 1

# Test Case 3: All decreasing
nums3 = [5, 4, 3, 2, 1]
result3 = lengthofLIS(nums3)
print(result3)  # Expected: 1

# Test Case 4: All increasing
nums4 = [1, 2, 3, 4, 5]
result4 = lengthofLIS(nums4)
print(result4)  # Expected: 5

# Test Case 5: Two elements
nums5 = [2, 2]
result5 = lengthofLIS(nums5)
print(result5)  # Expected: 1 (cannot have strictly increasing with duplicates)

# Test Case 6: Contains zeros and negatives
nums6 = [0, 1, 0, 3, 2, 3]
result6 = lengthofLIS(nums6)
print(result6)  # Expected: 4 (0, 1, 2, 3)

# Test Case 7: Large values
nums7 = [7, 7, 7, 7, 7]
result7 = lengthofLIS(nums7)
print(result7)  # Expected: 1

# Test Case 8: Long array with pattern
nums8 = [1, 3, 6, 7, 9, 4, 10, 5, 6]
result8 = lengthofLIS(nums8)
print(result8)  # Expected: 6 (1, 3, 6, 7, 9, 10)

# Test Case 9: Empty array
nums9 = []
result9 = lengthofLIS(nums9)
print(result9)  # Expected: 0 (will cause error with max of empty list, let's handle this)

# Test Case 10: Alternating values
nums10 = [1, 5, 2, 3, 4, 6]
result10 = lengthofLIS(nums10)
print(result10)  # Expected: 5 (1, 2, 3, 4, 6)

