# SINGLE ELEMENT IN A SORTED ARRAY

'''
You are given a sorted array consisting of only integers where every element appears exactly twice, except for one element which appears exactly once.
Return the single element that appears only once.
Your solution must run in O(log n) time and O(1) space.
'''

'''
Algorithm:
1. Initialize two pointers: left = 0 and right = len(nums) - 1
2. While left < right:
   a. Calculate mid = (left + right) // 2
   b. If mid is odd, decrement mid by 1 to make it even
   c. If nums[mid] == nums[mid + 1]:
      - The single element is in the right half
      - Move left pointer to mid + 2
   d. Else:
      - The single element is in the left half (including mid)
      - Move right pointer to mid
3. Return nums[left] as the single element
'''

def singleNonDuplicate(nums):
    left = 0
    right = len(nums) - 1
    
    while left < right:
        mid = (left + right) // 2
        
        if mid % 2 == 1:
            mid -= 1
        if nums[mid] == nums[mid + 1]:
            left = mid + 2
        else:
            right = mid 
    
    return nums[left]

'''
Time Complexity: O(log n)
Let n be the number of elements in the input array `nums`.
- The algorithm uses binary search on the array.
- In each iteration, we calculate the midpoint and adjust it to be even if necessary (O(1) operation).
- We then compare nums[mid] with nums[mid + 1] to determine which half contains the single element.
- The search space is halved in each iteration by adjusting either `left` or `right`.
- The loop continues until `left >= right`, which takes at most log₂(n) iterations.
- All operations inside the loop (calculating mid, comparisons, pointer updates) are O(1).
- Therefore, the overall time complexity is O(log n).

Space Complexity: O(1)
- The algorithm uses a constant amount of extra space for variables: `left`, `right`, and `mid`.
- No additional data structures are created that scale with the input size.
- Therefore, the space complexity is O(1).
'''

# Test Cases
nums1 = [1, 1, 2, 3, 3, 4, 4, 8, 8]
print(singleNonDuplicate(nums1)) # Output: 2

nums2 = [3, 3, 7, 7, 10, 11, 11]
print(singleNonDuplicate(nums2)) # Output: 10

nums3 = [1, 1, 2, 2, 3]
print(singleNonDuplicate(nums3)) # Output: 3

nums4 = [1]
print(singleNonDuplicate(nums4)) # Output: 1

nums5 = [1, 1, 2, 2, 3, 3, 4, 4, 5]
print(singleNonDuplicate(nums5)) # Output: 5

nums6 = [0, 1, 1, 2, 2, 5, 5]
print(singleNonDuplicate(nums6)) # Output: 0

nums7 = [1, 1, 3, 3, 4, 4, 5, 5, 6, 6, 7]
print(singleNonDuplicate(nums7)) # Output: 7

nums8 = [2, 2, 3, 3, 4, 5, 5, 6, 6]
print(singleNonDuplicate(nums8)) # Output: 4

nums9 = [1, 1, 2, 2, 3, 3, 4]
print(singleNonDuplicate(nums9)) # Output: 4

nums10 = [1, 2, 2, 3, 3, 4, 4, 5, 5]
print(singleNonDuplicate(nums10)) # Output: 1