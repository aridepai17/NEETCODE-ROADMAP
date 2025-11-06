# SUBARRAY SUMS DIVISIBLE BY K

'''
Given an integer array nums and an integer k, return the number of non-empty subarrays that have a sum divisible by k.
A subarray is a contiguous part of an array.
'''

def subarraysDivByK(nums, k):
    prefixSum = 0
    result = 0
    hashMap = {0 : 1} # Remainder -> Count
    
    for num in nums:
        prefixSum += num
        remainder = prefixSum % k
        result += hashMap.get(remainder, 0)
        hashMap[remainder] = hashMap.get(reaminder, 0) + 1
        
    return result

'''
Time Complexity: O(N)
- Let N be the number of elements in the input array `nums`.
- The algorithm iterates through the `nums` array exactly once using a for loop.
- Inside the loop, all operations (addition, modulo, dictionary lookup, dictionary assignment) are performed in constant time, O(1).
- Therefore, the total time complexity is O(N).

Space Complexity: O(min(N, K))
- The algorithm uses a dictionary `hashMap` to store remainder-to-count mappings.
- The number of possible remainders when dividing by `k` is at most `k` (remainders range from 0 to k-1).
- In the worst case, if k is very large, we might store up to N different remainders (one for each prefix sum).
- However, if k is small, the maximum number of entries in the dictionary is limited to k.
- Therefore, the space complexity is O(min(N, K)), where K is the value of `k`.
'''

# Test Cases
nums1 = [4, 5, 0, -2, -3, 1 ]
k1 = 5
print(subarraysDivByK(nums1, k1)) # Output: 7

nums2 = [5]
k2 = 9
print(subarraysDivByK(nums2, k2)) # Output: 0

nums3 = [-1, 2, 9]
k3 = 2
print(subarraysDivByK(nums3, k3)) # Output: 2

nums4 = [2, -2, 2, -4]
k4 = 6
print(subarraysDivByK(nums4, k4)) # Output: 2

nums5 = [1, 1, 1]
k5 = 3
print(subarraysDivByK(nums5, k5)) # Output: 3

nums6 = [0, 0, 0]
k6 = 1
print(subarraysDivByK(nums6, k6)) # Output: 6

nums7 = [7, -5, 3, -2, 1]
k7 = 4
print(subarraysDivByK(nums7, k7)) # Output: 4

nums8 = [-5, -5, -5, -5]
k8 = 5
print(subarraysDivByK(nums8, k8)) # Output: 10

nums9 = [3, 1, 2, 5, 1]
k9 = 3
print(subarraysDivByK(nums9, k9)) # Output: 6

nums10 = [8, 9, 7, 10, 6]
k10 = 5
print(subarraysDivByK(nums10, k10)) # Output: 5