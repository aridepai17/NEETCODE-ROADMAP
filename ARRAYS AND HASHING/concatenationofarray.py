# CONCATENATION OF ARRAY

'''
Given an integer array nums of length n, you want to create an array ans of length 2n where,
ans[i] == nums[i] and ans[i + n] == nums[i] for 0 <= i < n (0-indexed).
Specifically, ans is the concatenation of two nums arrays.
Return the array ans.
'''

def getConcatenation(nums):
    return nums + nums

# Test Cases
nums1 = [1, 2, 1]
print(f"Input: {nums1}")
print(f"Output: {getConcatenation(nums1)}") # Expected: [1, 2, 1, 1, 2, 1]

# Additional test cases
nums2 = [1, 3, 2, 1]
print(f"\nInput: {nums2}")
print(f"Output: {getConcatenation(nums2)}") # Expected: [1, 3, 2, 1, 1, 3, 2, 1]

nums3 = [5]
print(f"\nInput: {nums3}")
print(f"Output: {getConcatenation(nums3)}") # Expected: [5, 5]

nums4 = [0, 0, 0]
print(f"\nInput: {nums4}")
print(f"Output: {getConcatenation(nums4)}") # Expected: [0, 0, 0, 0, 0, 0]

nums5 = [-1, -2, -3]
print(f"\nInput: {nums5}")
print(f"Output: {getConcatenation(nums5)}") # Expected: [-1, -2, -3, -1, -2, -3]

nums6 = [10, 20, 30, 40, 50]
print(f"\nInput: {nums6}")
print(f"Output: {getConcatenation(nums6)}") # Expected: [10, 20, 30, 40, 50, 10, 20, 30, 40, 50]

nums7 = []
print(f"\nInput: {nums7}")
print(f"Output: {getConcatenation(nums7)}") # Expected: []

nums8 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(f"\nInput: {nums8}")
print(f"Output: {getConcatenation(nums8)}") # Expected: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]