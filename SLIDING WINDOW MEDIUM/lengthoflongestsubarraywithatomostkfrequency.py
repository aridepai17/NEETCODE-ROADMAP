# LENGTH OF LONGEST SUBARRAY WITH AT MOST K FREQUENCY

'''
You are given an integer array nums and an integer k.
The frequency of an element x is the number of times it occurs in an array.
An array is called good if the frequency of each element in this array is less than or equal to k.
Return the length of the longest good subarray of nums.
A subarray is a contiguous non-empty sequence of elements within an array.
'''

def maxSubarrayLength(nums, k):
    hashMap = {}
    result = 0
    left = 0
    
    for right in range(len(nums)):
        hashMap[nums[right]] = hashMap.get(nums[right], 0) + 1
        while hashMap[nums[right]] > k:
            hashMap[nums[left]] -= 1
            left += 1
        result = max(result, right - left + 1)
        
    return result

'''
Time Complexity: O(n)
We iterate through the input array `nums` using a sliding window approach.
The `right` pointer moves from the beginning to the end of the array, traversing each element once.
The `left` pointer also moves from left to right. Although it's inside a `while` loop, it never moves backward.
Over the entire execution, both `right` and `left` pointers traverse the array at most once.
Therefore, each element is processed a constant number of times.
All operations inside the loop (dictionary access, arithmetic operations) take constant time on average.
This results in a linear time complexity of O(n), where n is the length of the `nums` array.

Space Complexity: O(n)
The space complexity is determined by the `hashMap` which stores the frequency of elements in the current window.
In the worst-case scenario, the window could contain all unique elements from the input array `nums`.
If all elements in `nums` are distinct, the `hashMap` will store up to `n` key-value pairs.
Thus, the space required is proportional to the number of unique elements, which can be up to `n` in the worst case.
Therefore, the space complexity is O(n).
'''

# Test Cases
nums1 = [1,2,3,1,2,3,1,2], k1 = 2
print(maxSubarrayLength(nums1, k1)) # Output: 6

nums2 = [1,2,1,2,1,2,1,2], k2 = 1
print(maxSubarrayLength(nums2, k2)) # Output: 2

nums3 = [5,5,5,5,5,5,5], k3 = 4
print(maxSubarrayLength(nums3, k3)) # Output: 4

nums4 = [1,4,4,3], k4 = 1
print(maxSubarrayLength(nums4, k4)) # Output: 2

nums5 = [], k5 = 5
print(maxSubarrayLength(nums5, k5)) # Output: 0

nums6 = [1,2,3], k6 = 0
print(maxSubarrayLength(nums6, k6)) # Output: 0

nums7 = [1,2,3,4,5], k7 = 10
print(maxSubarrayLength(nums7, k7)) # Output: 5

nums8 = [2,2,2,2,2], k8 = 3
print(maxSubarrayLength(nums8, k8)) # Output: 3

nums9 = [1,1,1,1,1], k9 = 5
print(maxSubarrayLength(nums9, k9)) # Output: 5

nums10 = [1,2,2,3,3,3,4,4,4,4], k10 = 2
print(maxSubarrayLength(nums10, k10)) # Output: 5