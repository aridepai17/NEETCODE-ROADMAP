# SLIDING WINDOW MAXIMUM

'''
You are given an array of integers nums, there is a sliding window of size k which is moving from the very left of the array to the very right. 
You can only see the k numbers in the window.
Each time the sliding window moves right by one position.
Return the max sliding window.
'''

def maxSlidingWindow(nums, k):
    output = []
    left = 0
    right = 0
    queue = collections.deque()
    
    while right < len(nums):
        while queue and nums[queue[-1]] < nums[right]:
            queue.pop()
        queue.append(right)
        
        if left > queue[0]:
            queue.popleft()
        
        if right - left + 1 == k:
            output.append(nums[queue[0]])
            left += 1
        right += 1
    
    return output

'''
Time Complexity: O(n)
The algorithm iterates through the input array `nums` once with the `right` pointer. Each element is processed a constant number of times.
- Each element's index is added to the deque exactly once.
- Each element's index is removed from the deque at most once (either from the right by `pop()` or from the left by `popleft()`).
Because every element is pushed and popped at most once from the deque, the total time spent on deque operations across all iterations is O(n). The main loop runs `n` times, and the amortized time for the operations inside is O(1). Thus, the overall time complexity is linear, O(n), where n is the number of elements in `nums`.

Space Complexity: O(k)
The space complexity is determined by the extra space used by the data structures.
- The `output` list stores `n - k + 1` results. If we consider the space for the output, it would be O(n - k + 1).
- The primary auxiliary data structure is the `queue` (a deque). This deque stores indices of elements within the current window.
- In the worst-case scenario (e.g., a subarray of `k` elements in decreasing order), the deque can hold up to `k` indices.
- Therefore, the auxiliary space required by the algorithm is O(k), where k is the size of the sliding window.
'''

# Test Cases
nums1 = [1,3,-1,-3,5,3,6,7], k1 = 3
print(maxSlidingWindow(nums1, k1)) # Output: [3,3,5,5,6,7]

nums2 = [1], k2 = 1
print(maxSlidingWindow(nums2, k2)) # Output: [1]

nums3 = [1, -1], k3 = 1
print(maxSlidingWindow(nums3, k3)) # Output: [1, -1]

nums4 = [9, 11], k4 = 2
print(maxSlidingWindow(nums4, k4)) # Output: [11]

nums5 = [4, -2], k5 = 2
print(maxSlidingWindow(nums5, k5)) # Output: [4]

# Test case with decreasing numbers
nums6 = [9, 8, 7, 6, 5, 4, 3, 2, 1], k6 = 3
print(maxSlidingWindow(nums6, k6)) # Output: [9, 8, 7, 6, 5, 4, 3]

# Test case with increasing numbers
nums7 = [1, 2, 3, 4, 5, 6, 7, 8, 9], k7 = 4
print(maxSlidingWindow(nums7, k7)) # Output: [4, 5, 6, 7, 8, 9]

# Test case with all same numbers
nums8 = [5, 5, 5, 5, 5, 5], k8 = 2
print(maxSlidingWindow(nums8, k8)) # Output: [5, 5, 5, 5, 5]

# Test case where k is the length of the array
nums9 = [1, 3, 5, 2, 4], k9 = 5
print(maxSlidingWindow(nums9, k9)) # Output: [5]

# Test case with an empty array
nums10 = [], k10 = 2
print(maxSlidingWindow(nums10, k10)) # Output: []