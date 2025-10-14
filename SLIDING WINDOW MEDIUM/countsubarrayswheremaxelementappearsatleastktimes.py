# COUNT SUBARRAYS WHERE MAX ELEMENT APPEARS AT LEAST K TIMES

'''
You are given an integer array nums and a positive integer k.
Return the number of subarrays where the maximum element of nums appears at least k times in that subarray.
A subarray is a contiguous sequence of elements within an array.
'''

def countSubarrays(nums, k):
    maxNumber = max(nums)
    maxCount = 0
    result = 0
    left = 0
    
    for right in range(len(nums)):
        if nums[right] == maxNumber:
            maxCount += 1
            
        while maxCount == k:
            if nums[left] == maxNumber:
                maxCount -= 1
            left += 1
        result += left
        
    return result

'''
Time Complexity: O(n)
The algorithm consists of two main parts: finding the maximum element and the sliding window traversal.
1. Finding the maximum element `max(nums)` takes O(n) time as it requires iterating through the entire array once.
2. The sliding window approach involves two pointers, `left` and `right`. The `right` pointer iterates through the array from beginning to end, which is n steps. The `left` pointer also moves forward and will traverse the array at most once.
Since each element is visited by the `right` and `left` pointers at most a constant number of times, the time complexity of the sliding window part is O(n).
Combining these, the total time complexity is O(n) + O(n) = O(n), where n is the number of elements in `nums`.

Space Complexity: O(1)
The algorithm uses a fixed number of variables (`maxNumber`, `maxCount`, `result`, `left`, `right`) to store the maximum number, its count in the current window, the total count of valid subarrays, and the window boundaries.
The amount of memory used does not depend on the size of the input array `nums`.
Therefore, the space complexity is O(1).
'''

# Test Cases
nums1 = [1, 3, 2, 3, 3], k1 = 2
print(countSubarrays(nums1, k1)) # Output: 6

nums2 = [1, 4, 2, 1], k2 = 1
print(countSubarrays(nums2, k2)) # Output: 6

nums3 = [1, 2, 3, 4, 5], k3 = 2
print(countSubarrays(nums3, k3)) # Output: 0

nums4 = [5, 5, 5, 5, 5], k4 = 3
print(countSubarrays(nums4, k4)) # Output: 6

nums5 = [10, 1, 2, 10, 3, 10], k5 = 2
print(countSubarrays(nums5, k5)) # Output: 6

nums6 = [1, 2, 3, 10, 10], k6 = 2
print(countSubarrays(nums6, k6)) # Output: 4

nums7 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1], k7 = 10
print(countSubarrays(nums7, k7)) # Output: 1

nums8 = [-1, -5, -1, -2, -1], k8 = 2
print(countSubarrays(nums8, k8)) # Output: 5

nums9 = [2, 2, 1, 2, 1], k9 = 4
print(countSubarrays(nums9, k9)) # Output: 0

nums10 = [6, 1, 3, 6, 2, 6, 6], k10 = 3
print(countSubarrays(nums10, k10)) # Output: 5