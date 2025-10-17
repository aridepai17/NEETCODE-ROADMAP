# FIND THE POWER OF K SIZE SUBARRAYS 1

'''
You are given an array of integers nums of length n and a positive integer k.
The power of an array is defined as:
- Its maximum element if all of its elements are consecutive and sorted in ascending order.
- -1 otherwise.
You need to find the power of all subarrays of nums of size k.
Return an integer array results of size n - k + 1, where results[i] is the power of nums[i..(i + k - 1)].
'''

def resultsArray(nums, k):
    result = []
    left = 0
    consecutiveCount = 1
    
    for right in range(len(nums)):
        if right > 0 and nums[right - 1] + 1 == nums[right]:
            consecutiveCount += 1
        if right - left + 1 > k:
            if nums[left] + 1 == nums[left]:
                consecutiveCount -= 1
            left += 1
        if right - left + 1 == k:
            if consecutiveCount == k:
                result.append(nums[right])
            else:
                result.append(-1)
                
    return result

'''
Time Complexity: O(n)
The algorithm uses a sliding window approach over the input array `nums`.
- The `for` loop iterates through the array with the `right` pointer from `0` to `n-1`, where `n` is the length of `nums`.
- The `left` pointer also moves from left to right, ensuring that each element is processed a constant number of times.
- All operations inside the loop, such as comparisons and appending to the result list, take constant time, O(1).
- Therefore, the total time complexity is linear, O(n).

Space Complexity: O(n)
- The `result` array is used to store the output. In the end, it will contain `n - k + 1` elements.
- The space required for the output is therefore proportional to `n - k + 1`, which simplifies to O(n).
- The other variables (`left`, `right`, `consecutiveCount`) use only a constant amount of extra space, O(1).
- Thus, the overall space complexity is O(n).
'''

# Test Cases
nums1 = [1,2,3,4,3,2,5], k1 = 3
print(resultsArray(nums1, k1)) # Output: [3, 4, -1, -1, -1]

nums2 = [1, 3, 5, 2, 4, 6], k2 = 2
print(resultsArray(nums2, k2)) # Output: [-1, -1, -1, -1, -1]

nums3 = [10, 11, 12, 13, 14], k3 = 3
print(resultsArray(nums3, k3)) # Output: [12, 13, 14]

nums4 = [5, 6, 7], k4 = 1
print(resultsArray(nums4, k4)) # Output: [5, 6, 7]

nums5 = [1, 2, 3, 4, 5], k5 = 5
print(resultsArray(nums5, k5)) # Output: [5]

nums6 = [1, 2, 3], k6 = 4
print(resultsArray(nums6, k6)) # Output: []

nums7 = [1, 2, 3, 3, 4, 5], k7 = 3
print(resultsArray(nums7, k7)) # Output: [3, -1, -1, 5]

nums8 = [-2, -1, 0, 1, 0, 1, 2], k8 = 4
print(resultsArray(nums8, k8)) # Output: [1, -1, -1, -1]

nums9 = [8, 7, 6, 7, 8, 9, 10, 5, 6], k9 = 4
print(resultsArray(nums9, k9)) # Output: [-1, -1, 9, 10, -1, -1]

nums10 = [], k10 = 2
print(resultsArray(nums10, k10)) # Output: []