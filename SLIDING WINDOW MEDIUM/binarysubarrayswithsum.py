# BINARY SUBARRAYS WITH SUM

'''
Given a binary array nums and an integer goal, return the number of non-empty subarrays with a sum goal.
A subarray is a contiguous part of the array.
'''

def numSubarraysWithSum(nums, goal):
    def atMost(target):
        if target < 0:
            return 0
        
        left = 0
        count = 0
        currentSum = 0
        
        for right in range(len(nums)):
            currentSum += nums[right]
            while currentSum > target:
                currentSum -= nums[left]
                left += 1
            count += (right - left + 1)
            
        return count
    
    return atMost(goal) - atMost(goal - 1)

'''
Time Complexity: O(n)
The solution uses a helper function `atMost(target)` which is called twice.
The `atMost` function employs a sliding window approach. Both the `right` and `left` pointers traverse the array at most once.
Each element of the `nums` array is added to `currentSum` once (by the `right` pointer) and subtracted from `currentSum` at most once (by the `left` pointer).
This results in a linear time complexity of O(n) for the `atMost` function, where 'n' is the length of the `nums` array.
Since `numSubarraysWithSum` calls `atMost` a constant number of times (twice), the overall time complexity remains O(n).

Space Complexity: O(1)
The algorithm uses a constant amount of extra space for variables like `left`, `count`, `currentSum`, and `right`.
The space required does not grow with the size of the input array, making the space complexity O(1).
'''

# Test Cases
nums1 = [1, 0, 1, 0, 1], goal1 = 2
print(numSubarraysWithSum(nums1, goal1)) # Output: 4

nums2 = [0, 0, 0, 0, 0], goal2 = 0
print(numSubarraysWithSum(nums2, goal2)) # Output: 15

nums3 = [1, 1, 1, 1, 1], goal3 = 2
print(numSubarraysWithSum(nums3, goal3)) # Output: 4

nums4 = [0, 1, 1, 0, 1], goal4 = 2
print(numSubarraysWithSum(nums4, goal4)) # Output: 5

nums5 = [1, 0, 0, 1, 0, 1], goal5 = 2
print(numSubarraysWithSum(nums5, goal5)) # Output: 4

nums6 = [], goal6 = 0
print(numSubarraysWithSum(nums6, goal6)) # Output: 0

nums7 = [1, 1, 1], goal7 = 3
print(numSubarraysWithSum(nums7, goal7)) # Output: 1

nums8 = [1, 0, 1, 0, 1], goal8 = 3
print(numSubarraysWithSum(nums8, goal8)) # Output: 1

nums9 = [0, 0, 0, 0, 1], goal9 = 1
print(numSubarraysWithSum(nums9, goal9)) # Output: 5

nums10 = [1, 0, 1, 0, 1], goal10 = 0
print(numSubarraysWithSum(nums10, goal10)) # Output: 2