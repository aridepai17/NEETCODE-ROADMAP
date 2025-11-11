# SHORTEST SUBARRAY WITH SUM AT LEAST K

'''
Given an integer array nums and an integer k, return the length of the shortest non-empty subarray of nums with a sum of at least k. 
If there is no such subarray, return -1.
A subarray is a contiguous part of an array.
'''

def shortestSubarray(nums, k):
    result = float("inf")
    currentSum = 0
    q = deque() # (PrefixSum, EndIndex)
    
    for r in range(len(nums)):
        currentSum += nums[r]
        if currentSum >= k:
            result = min(result, r + 1)
            
        # Find the minimum valid subarray ending at r
        while q and currentSum - q[0][0] >= k:
            prefixSum, endIndex = q.popleft()
            result = min(result, r - endIndex)
            
        # Validate the monotonic deque
        while q and q[-1][0] >= currentSum:
            q.pop()
        
        q.append((currentSum, r))
        
    return -1 if result == float("inf") else result

'''
Time Complexity: O(n)
Let n be the number of elements in the input array `nums`.
- We iterate through the array once with the for loop, which runs n times.
- Inside the loop, we perform operations on the deque:
  - The first while loop (finding minimum valid subarray) pops elements from the front of the deque. Each element can be added to the deque at most once and removed at most once across all iterations, so the total time for all popleft operations is O(n).
  - The second while loop (maintaining monotonic property) pops elements from the back of the deque. Similarly, each element can be popped at most once across all iterations, so the total time for all pop operations is O(n).
  - Appending to the deque is O(1).
- Therefore, the overall time complexity is O(n) + O(n) + O(n) = O(n).

Space Complexity: O(n)
- We use a deque `q` to store tuples of (prefixSum, endIndex).
- In the worst case, all elements could be added to the deque without any being removed (e.g., when the array is strictly increasing and no subarray sum reaches k).
- Therefore, the deque can store up to n elements.
- The space complexity is O(n).
'''

# Test Cases
nums1 = [1], k1 = 1
print(shortestSubarray(nums1, k1)) # Output: 1

nums2 = [2, -1, 2], k2 = 3
print(shortestSubarray(nums2, k2)) # Output: 3

nums3 = [1, 2], k3 = 4
print(shortestSubarray(nums3, k3)) # Output: -1

nums4 = [2, -1, 2, 1], k4 = 3
print(shortestSubarray(nums4, k4)) # Output: 2

nums5 = [84, -37, 32, 40, 95], k5 = 167
print(shortestSubarray(nums5, k5)) # Output: 3

nums6 = [1, 2, 3, 4, 5], k6 = 11
print(shortestSubarray(nums6, k6)) # Output: 3

nums7 = [-1, -2, -3], k7 = 5
print(shortestSubarray(nums7, k7)) # Output: -1

nums8 = [10, -5, 8, -3, 7], k8 = 15
print(shortestSubarray(nums8, k8)) # Output: 2

nums9 = [5, -2, 3, -1, 4], k9 = 7
print(shortestSubarray(nums9, k9)) # Output: 2

nums10 = [1, 1, 1, 1, 1], k10 = 3
print(shortestSubarray(nums10, k10)) # Output: 3