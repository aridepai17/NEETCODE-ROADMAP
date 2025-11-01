# SUBARRAY SUM EQUALS K

'''
Given an array of integers nums and an integer k, return the total number of subarrays whose sum equals to k.
A subarray is a contiguous non-empty sequence of elements within an array.
'''

def subarraySum(nums, k):
    prefixSum = {0 : 1}
    currentSum = 0
    result = 0
    
    for num in nums:
        currentSum += num
        diff = currentSum - k
        result += prefixSum.get(diff, 0)
        prefixSum[currentSum] = prefixSum.get(currentSum, 0) + 1
        
    return result

'''
Time Complexity: O(N)
- Let N be the number of elements in the input array `nums`.
- The algorithm iterates through the `nums` array exactly once.
- Each operation inside the loop (addition, subtraction, dictionary lookup, assignment) takes O(1) time on average.
- Therefore, the total time complexity is O(N).

Space Complexity: O(N)
- The algorithm uses a dictionary `prefixSum` to store the prefix sum frequencies.
- In the worst case, all prefix sums are different (occurs when all elements are non-zero and cumulative sums are unique), so the dictionary stores up to N different sums.
- Therefore, the space complexity is O(N).
'''

# Test Cases
nums1 = [1,1,1]
k1 = 2
print(subarraySum(nums1, k1)) # Output: 2

nums2 = [1,2,3]
k2 = 3
print(subarraySum(nums2, k2)) # Output: 2

nums3 = [1,-1,0]
k3 = 0
print(subarraySum(nums3, k3)) # Output: 3

nums4 = [3,4,7,2,-3,1,4,2]
k4 = 7
print(subarraySum(nums4, k4)) # Output: 4

nums5 = [0,0,0,0,0]
k5 = 0
print(subarraySum(nums5, k5)) # Output: 15

nums6 = [1]
k6 = 0
print(subarraySum(nums6, k6)) # Output: 0

nums7 = [1,2,1,2,1]
k7 = 3
print(subarraySum(nums7, k7)) # Output: 4

nums8 = [-1,-1,1]
k8 = 0
print(subarraySum(nums8, k8)) # Output: 1

nums9 = [1,-1,1,-1,1]
k9 = 0
print(subarraySum(nums9, k9)) # Output: 4

nums10 = [2,2,2,2]
k10 = 4
print(subarraySum(nums10, k10)) # Output: 3

nums11 = [5,1,2,3,-2,2]
k11 = 5
print(subarraySum(nums11, k11)) # Output: 3