# COUNT NUMBER OF NICE SUBARRAYS

'''
Given an array of integers nums and an integer k. 
A continuous subarray is called nice if there are k odd numbers on it.
Return the number of nice sub-arrays.
'''

def numberOfSubarrays(nums, k):
    result = 0
    left = 0
    middle = 0
    odd = 0
    
    for right in range(len(nums)):
        if nums[right] % 2 == 1:
            odd += 1
        while odd > k:
            if nums[left] % 2 == 1:
                odd -= 1
            left += 1
            middle = left
        if odd == k:
            while not nums[middle] % 2 == 1:
                middle += 1
            result += (middle + left) + 1
            
    return result

'''
Time Complexity: O(n)
The algorithm uses a sliding window approach with three pointers: left, middle, and right.
The 'right' pointer iterates through the array from beginning to end once, which takes O(n) time.
The 'left' and 'middle' pointers also only move forward through the array. Although they are in `while` loops,
the total number of times they are incremented across all iterations of the outer `for` loop is bounded by n.
Each element of the array is visited a constant number of times by these pointers.
Thus, the overall time complexity is linear, O(n).

Space Complexity: O(1)
The algorithm uses a fixed number of variables (result, left, middle, odd, right) to store state.
The amount of extra space required does not depend on the size of the input array `nums`.
Therefore, the space complexity is constant, O(1).
'''

# Test Cases
nums1 = [1,1,2,1,1], k1 = 3
print(numberOfSubarrays(nums1, k1)) # Output: 2

nums2 = [2,4,6], k2 = 1
print(numberOfSubarrays(nums2, k2)) # Output: 0

nums3 = [2,2,2,1,2,2,1,2,2,2], k3 = 2
print(numberOfSubarrays(nums3, k3)) # Output: 16

nums4 = [1,1,1,1,1], k4 = 1
print(numberOfSubarrays(nums4, k4)) # Output: 5

nums5 = [1,1,1,1,1], k5 = 5
print(numberOfSubarrays(nums5, k5)) # Output: 1

nums6 = [1,2,3,4,5], k6 = 2
print(numberOfSubarrays(nums6, k6)) # Output: 4

nums7 = [2,1,2,1,2,1,2], k7 = 2
print(numberOfSubarrays(nums7, k7)) # Output: 8

nums8 = [4,3,2,3,4], k8 = 1
print(numberOfSubarrays(nums8, k8)) # Output: 8

nums9 = [1], k9 = 1
print(numberOfSubarrays(nums9, k9)) # Output: 1

nums10 = [1,1,1,1,1], k10 = 6
print(numberOfSubarrays(nums10, k10)) # Output: 0