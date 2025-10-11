# SUBARRAY PRODUCT LESS THAN K

'''
Given an array of integers nums and an integer k, return the number of contiguous subarrays where the product of all the elements in the subarray is strictly less than k.
'''

def numSubarrayProductLessThanK(nums, k):
    if k <= 1:
        return 0
    
    left = 0
    currentProduct = 1
    total = 0
    
    for right in range(len(nums)):
        currentProduct *= nums[right]
        while currentProduct >= k:
            currentProduct //= nums[left]
            left += 1
        total += (right - left + 1)
        
    return total

'''
Time Complexity: O(n)
The algorithm uses a sliding window approach with two pointers, `left` and `right`.
The `right` pointer iterates through the `nums` array from the beginning to the end, which takes O(n) time.
The `left` pointer also moves forward, and each element is visited at most once by `left`.
Since each element of the `nums` array is processed by both pointers at most once (multiplied by `right` and divided by `left`), the overall time complexity is linear, O(n), where 'n' is the length of the `nums` array.

Space Complexity: O(1)
The algorithm uses a constant amount of extra space for variables like `left`, `currentProduct`, `total`, and `right`.
The space required does not depend on the size of the input array, so the space complexity is O(1).
'''

# Test Cases
nums1 = [10, 5, 2, 6], k1 = 100
print(numSubarrayProductLessThanK(nums1, k1)) # Output: 8

nums2 = [1, 2, 3], k2 = 0
print(numSubarrayProductLessThanK(nums2, k2)) # Output: 0

nums3 = [1, 1, 1], k3 = 2
print(numSubarrayProductLessThanK(nums3, k3)) # Output: 6

nums4 = [5, 4, 3, 2, 1], k4 = 50
print(numSubarrayProductLessThanK(nums4, k4)) # Output: 12

nums5 = [100, 200, 300], k5 = 100
print(numSubarrayProductLessThanK(nums5, k5)) # Output: 0

nums6 = [], k6 = 100
print(numSubarrayProductLessThanK(nums6, k6)) # Output: 0

nums7 = [1, 2, 3, 4, 5], k7 = 1
print(numSubarrayProductLessThanK(nums7, k7)) # Output: 0

nums8 = [2, 3, 5, 7], k8 = 10
print(numSubarrayProductLessThanK(nums8, k8)) # Output: 5

nums9 = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1], k9 = 1000
print(numSubarrayProductLessThanK(nums9, k9)) # Output: 34

nums10 = [4, 2, 10, 5], k10 = 25
print(numSubarrayProductLessThanK(nums10, k10)) # Output: 7