# MAX CONSECUTIVE ONES 3

'''
Given a binary array nums and an integer k, return the maximum number of consecutive 1's in the array if you can flip at most k 0's.
'''

def longestOnes(nums, k):
    left = 0
    maxOnes = 0
    zeroCount = 0
    
    for right in range(len(nums)):
        if nums[right] == 0:
            zeroCount += 1
        while zeroCount > k:
            if nums[left] == 0:
                zeroCount -= 1
            left += 1
        maxOnes = max(maxOnes, right - left + 1)
        
    return maxOnes

'''
Time Complexity: O(n)
The algorithm uses a sliding window approach.
- The `right` pointer iterates through the array from beginning to end, which takes O(n) steps, where n is the length of the `nums` array.
- The `left` pointer also moves from left to right. Although it's inside a `while` loop, it never moves backward.
- Each element in the array is visited by the `right` pointer once and by the `left` pointer at most once.
- The operations inside the loop (checking values, incrementing/decrementing counters) are all constant time.
- Therefore, the total time complexity is O(n).

Space Complexity: O(1)
The algorithm uses a few variables (`left`, `maxOnes`, `zeroCount`, `right`) to keep track of the window boundaries and the count of zeros.
- The space required for these variables is constant and does not depend on the size of the input array.
- No additional data structures are created that scale with the input size.
- Therefore, the space complexity is O(1).
'''

# Test Cases
nums1 = [1,1,1,0,0,0,1,1,1,1,0], k1 = 2
print(longestOnes(nums1, k1)) # Output: 6

nums2 = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], k2 = 3
print(longestOnes(nums2, k2)) # Output: 10

nums3 = [0,0,0,1], k3 = 4
print(longestOnes(nums3, k3)) # Output: 4

nums4 = [1,1,1,1,1], k4 = 0
print(longestOnes(nums4, k4)) # Output: 5

nums5 = [0,0,0,0,0], k5 = 2
print(longestOnes(nums5, k5)) # Output: 2

nums6 = [], k6 = 5
print(longestOnes(nums6, k6)) # Output: 0

nums7 = [1,0,1,0,1], k7 = 0
print(longestOnes(nums7, k7)) # Output: 1

nums8 = [0,0,1,1,1,1,0,1], k8 = 2
print(longestOnes(nums8, k8)) # Output: 6

nums9 = [0,1,0,1,0,1], k9 = 3
print(longestOnes(nums9, k9)) # Output: 6

nums10 = [1,0,0,1,1,0,1,0,1,1,1], k10 = 2
print(longestOnes(nums10, k10)) # Output: 8