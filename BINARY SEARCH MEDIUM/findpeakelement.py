# FIND PEAK ELEMENT

'''
A peak element is an element that is strictly greater than its neighbors.
Given a 0-indexed integer array nums, find a peak element, and return its index. 
If the array contains multiple peaks, return the index to any of the peaks.
You may imagine that nums[-1] = nums[n] = -∞. 
In other words, an element is always considered to be strictly greater than a neighbor that is outside the array.
You must write an algorithm that runs in O(log n) time.
'''

"""
Algorithm:
1. Initialize two pointers: left = 0 and right = len(nums) - 1
2. While left < right:
   a. Calculate mid = (left + right) // 2
   b. If mid is at the beginning of the array or nums[mid] > nums[mid - 1]:
      - The peak element is either at mid or in the right half
      - Move left to mid + 1
   c. Else if mid is at the end of the array or nums[mid] > nums[mid + 1]:
      - The peak element is in the left half
      - Move right to mid - 1
   d. Else:
      - The peak element is at mid
      - Return mid
"""

def findPeakElement(nums):
    left = 0 
    right = len(nums) - 1

    while left <= right:
        mid = (left + right) // 2
        if mid > 0 and nums[mid] < nums[mid - 1]:
            right = mid - 1
        elif mid < len(nums) - 1 and nums[mid] < nums[mid + 1]:
            left = mid + 1
        else:
            return mid   
        
"""
Time Complexity: O(log n)
The algorithm uses binary search which reduces the search space by half at each iteration.
It takes at most log₂(n) iterations to find the peak element.

Space Complexity: O(1)
The algorithm uses only constant space O(1) for the variables left, right, and mid.
The space used by these variables is constant and does not depend on the size of the input array nums.
Therefore, the space complexity is constant, O(1).
"""

# Test Cases
nums1 = [1, 2, 3, 1]
print(findPeakElement(nums1)) # Output: 2

nums2 = [1, 2, 1, 3, 5, 6, 4]
print(findPeakElement(nums2)) # Output: 5


nums3 = [1, 2, 1, 3, 4, 0]
print(findPeakElement(nums3)) # Output: 4

nums4 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(findPeakElement(nums4)) # Output: 9

nums5 = [1, 2, 3, 4, 5, 4, 3, 2, 1]
print(findPeakElement(nums5)) # Output: 4

nums6 = [1, 2, 3, 4, 5, 6, 7, 8, 7, 6, 5, 4, 3, 2, 1]
print(findPeakElement(nums6)) # Output: 8

nums7 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
print(findPeakElement(nums7)) # Output: 18

nums8 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, -1]
print(findPeakElement(nums8)) # Output: 18

nums9 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
print(findPeakElement(nums9)) # Output: 18

nums10 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 0]
print(findPeakElement(nums10)) # Output: 18