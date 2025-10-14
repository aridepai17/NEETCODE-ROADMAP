# MAXIMUM SUM OF DISTINCT SUBARRAYS WITH LENGTH K

'''
You are given an integer array nums and an integer k. 
Find the maximum subarray sum of all the subarrays of nums that meet the following conditions:
- The length of the subarray is k, and
- All the elements of the subarray are distinct.
Return the maximum subarray sum of all the subarrays that meet the conditions. If no subarray meets the conditions, return 0.
A subarray is a contiguous non-empty sequence of elements within an array.
'''

def maximumSubarraySum(nums, k):
    hashMap = {}
    currentSum = 0
    result = 0
    left = 0
    
    for right in range(len(nums)):
        hashMap[nums[right]] = hashMap.get(nums[right], 0) + 1
        currentSum += nums[right]
        
        if right - left + 1 > k:
            hashMap[nums[left]] -= 1
            if hashMap[nums[left]] == 0:
                hashMap.pop(nums[left])
            currentSum -= nums[left]
            left += 1
            
        if len(hashMap) == (right - left + 1) == k:
            result = max(result, currentSum)
            
    return result

'''
Time Complexity: O(n)
We iterate through the input array `nums` once using a sliding window approach. 
The `right` pointer moves from the beginning to the end of the array, and the `left` pointer also traverses the array at most once. 
All operations inside the loop (dictionary access, arithmetic operations) take constant time on average. 
Therefore, the time complexity is linear with respect to the size of the input array, n.

Space Complexity: O(k)
The space complexity is determined by the `hashMap` used to store the frequency of elements within the current window. 
The size of the window is at most `k`. In the worst case, the window contains `k` distinct elements, so the hash map will store up to `k` key-value pairs. 
Thus, the space required is proportional to `k`.
'''

# Test Cases
nums1 = [1,5,4,2,9,9,9], k1 = 3
print(maximumSubarraySum(nums1, k1)) # Output: 15

nums2 = [4,4,4], k2 = 2
print(maximumSubarraySum(nums2, k2)) # Output: 0

nums3 = [1,1,1,1,1], k3 = 3
print(maximumSubarraySum(nums3, k3)) # Output: 0

nums4 = [9,9,9,1,2,3], k4 = 3
print(maximumSubarraySum(nums4, k4)) # Output: 12

nums5 = [1,2,3,4,5], k5 = 5
print(maximumSubarraySum(nums5, k5)) # Output: 15

nums6 = [1,2,3,4,1], k6 = 5
print(maximumSubarraySum(nums6, k6)) # Output: 0

nums7 = [10], k7 = 1
print(maximumSubarraySum(nums7, k7)) # Output: 10

nums8 = [1, -1, 2, -2, 3, -3], k8 = 3
print(maximumSubarraySum(nums8, k8)) # Output: 3

nums9 = [], k9 = 1
print(maximumSubarraySum(nums9, k9)) # Output: 0

nums10 = [1,2,3], k10 = 4
print(maximumSubarraySum(nums10, k10)) # Output: 0