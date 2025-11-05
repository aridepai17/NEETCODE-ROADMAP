# CONTINUOUS SUBARRAY SUM

'''
Given an integer array nums and an integer k, return true if nums has a good subarray or false otherwise.
A good subarray is a subarray where:
- its length is at least two, and
- the sum of the elements of the subarray is a multiple of k.
Note that:
- A subarray is a contiguous part of the array.
- An integer x is a multiple of k if there exists an integer n such that x = n * k. 0 is always a multiple of k.
'''

def continuousSubarraySum(nums, k):
    hashMap = { 0 : -1 } # Remainder -> Index
    total = 0
    
    for index in range(len(nums)):
        number = nums[index]
        total += number
        remainder = total % k
        
        if remainder not in hashMap:
            hashMap[remainder] = index
        elif index - hashMap[remainder] > 1:
            return True
        
    return False

'''
Time Complexity: O(N)
- Let N be the number of elements in the input array `nums`.
- The algorithm iterates through the `nums` array exactly once using a for loop.
- Inside the loop, all operations (addition, modulo, dictionary lookup, dictionary assignment, subtraction, comparison) are performed in constant time, O(1).
- Therefore, the total time complexity is O(N).

Space Complexity: O(min(N, K))
- The algorithm uses a dictionary `hashMap` to store remainder-to-index mappings.
- The number of possible remainders when dividing by `k` is at most `k` (remainders range from 0 to k-1).
- In the worst case, if k is very large, we might store up to N different remainders (one for each prefix sum).
- However, if k is small, the maximum number of entries in the dictionary is limited to k.
- Therefore, the space complexity is O(min(N, K)), where K is the value of `k`.
'''

# Test Cases
nums1 = [23,2,4,6,7], k1 = 6
print(continuousSubarraySum(nums1, k1)) # Output: True

nums2 = [23,2,6,4,7]
k2 = 6
print(continuousSubarraySum(nums2, k2)) # Output: True

nums3 = [23,2,6,4,7]
k3 = 13
print(continuousSubarraySum(nums3, k3)) # Output: False

nums4 = [0,0]
k4 = 1
print(continuousSubarraySum(nums4, k4)) # Output: True

nums5 = [5,0,0,0]
k5 = 3
print(continuousSubarraySum(nums5, k5)) # Output: True

nums6 = [1,0]
k6 = 2
print(continuousSubarraySum(nums6, k6)) # Output: False

nums7 = [1,2,3]
k7 = 5
print(continuousSubarraySum(nums7, k7)) # Output: True

nums8 = [1,2,12]
k8 = 6
print(continuousSubarraySum(nums8, k8)) # Output: False

nums9 = [23,2,4,6,6]
k9 = 7
print(continuousSubarraySum(nums9, k9)) # Output: True

nums10 = [5,2,4]
k10 = 5
print(continuousSubarraySum(nums10, k10)) # Output: False