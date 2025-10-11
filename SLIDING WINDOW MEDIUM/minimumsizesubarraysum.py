# MINIMUM SIZE SUBARRAY SUM

'''
Given an array of positive integers nums and a positive integer target, return the minimal length of a subarray whose sum is greater than or equal to target. 
If there is no such subarray, return 0 instead.
'''

def minSubarraySum(target, nums):
    minimum = float('inf')
    currentSum = 0
    left = 0
    
    for right in range(len(nums)):
        currentSum += nums[right]
        while currentSum >= target:
            minimum = min(minimum, right - left + 1)
            currentSum -= nums[left]
            left += 1
            
    if minimum == float('inf'):
        return 0
    else:
        return minimum
    
'''
Time Complexity: O(n)
The algorithm uses a sliding window approach with two pointers, `left` and `right`.
The `right` pointer iterates through the `nums` array from the beginning to the end, which takes O(n) time.
The `left` pointer also moves forward, and each element is visited at most once by `left`.
Since each element of the `nums` array is processed by both pointers at most once, the overall time complexity is linear, O(n), where 'n' is the length of the `nums` array.

Space Complexity: O(1)
The algorithm uses a constant amount of extra space for variables like `minimum`, `currentSum`, `left`, and `right`.
The space required does not depend on the size of the input array, so the space complexity is O(1).
'''

# Test Cases
target1 = 7, nums1 = [2, 3, 1, 2, 4, 3]
print(minSubarraySum(target1, nums1)) # Output: 2

target2, nums2 = 11, [1, 2, 3, 4, 5]
print(minSubarraySum(target2, nums2)) # Output: 3

target3, nums3 = 15, [1, 1, 1, 1, 1]
print(minSubarraySum(target3, nums3)) # Output: 0

target4, nums4 = 4, [1, 4, 4]
print(minSubarraySum(target4, nums4)) # Output: 1

target5, nums5 = 5, []
print(minSubarraySum(target5, nums5)) # Output: 0

target6, nums6 = 5, [10]
print(minSubarraySum(target6, nums6)) # Output: 1

target7, nums7 = 5, [3]
print(minSubarraySum(target7, nums7)) # Output: 0

target8, nums8 = 20, [2, 1, 5, 2, 8, 10, 4]
print(minSubarraySum(target8, nums8)) # Output: 3

target9, nums9 = 6, [10, 2, 3]
print(minSubarraySum(target9, nums9)) # Output: 1

target10, nums10 = 7, [2, 2, 2, 2, 2, 2]
print(minSubarraySum(target10, nums10)) # Output: 4