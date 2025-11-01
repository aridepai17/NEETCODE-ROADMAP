# NUMBER OF ZERO-FILLED SUBARRAYS

'''
Given an integer array nums, return the number of subarrays filled with 0.
A subarray is a contiguous non-empty sequence of elements within an array.
'''

def zerofilledSubarrays(nums):
    result = 0
    count = 0
    
    for i in range(len(nums)):
        if nums[i] == 0:
            count += 1
        else:
            count = 0
        result += count
        
    return result

'''
Time Complexity: O(N)
- Let N be the number of elements in the input array `nums`.
- The algorithm iterates through the `nums` array exactly once.
- Inside the loop, all operations (accessing an element, comparison, addition, assignment) are performed in constant time, O(1).
- Since the loop runs N times with constant time work per iteration, the total time complexity is O(N).

Space Complexity: O(1)
- The algorithm uses a fixed number of variables (`result`, `count`, and the loop index `i`) to store state.
- The space required for these variables does not grow with the size of the input array.
- Therefore, the space complexity is constant, O(1).
'''

# Test Cases
nums1 = [1, 3, 0, 0, 2, 0, 0, 4]
print(zerofilledSubarrays(nums1)) # Output: 6

nums2 = [0,0,0,0,0]
print(zerofilledSubarrays(nums2)) # Output: 15

nums3 = [1,2,3,4,5]
print(zerofilledSubarrays(nums3)) # Output: 0

nums4 = [0,1,0,1,0]
print(zerofilledSubarrays(nums4)) # Output: 3

nums5 = [2,0,0,0,1,0,0,3]
print(zerofilledSubarrays(nums5)) # Output: 9

nums6 = [0]
print(zerofilledSubarrays(nums6)) # Output: 1

nums7 = [10]
print(zerofilledSubarrays(nums7)) # Output: 0

nums8 = []
print(zerofilledSubarrays(nums8)) # Output: 0

nums9 = [0,0,1,0,0,0,1,0]
print(zerofilledSubarrays(nums9)) # Output: 10

nums10 = [1,0,0,0,0,0,1]
print(zerofilledSubarrays(nums10)) # Output: 15