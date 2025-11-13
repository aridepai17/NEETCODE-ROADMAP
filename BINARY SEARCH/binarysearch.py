# BINARY SEARCH 

'''
Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.
You must write an algorithm with O(log n) runtime complexity.
'''

def binarySearch(nums, target):
    left = 0
    right = len(nums) - 1
    
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] < target:
            left = mid + 1
        elif nums[mid] > target:
            right = mid - 1
        else:
            return mid
    
    return -1

'''
Time Complexity: O(log n)
Let n be the number of elements in the input array `nums`.
- The algorithm uses binary search, which repeatedly divides the search space in half.
- In each iteration of the while loop, we either move the `left` pointer up or the `right` pointer down, effectively halving the remaining elements to search.
- The maximum number of iterations needed is log₂(n), as we can divide n by 2 at most log₂(n) times before the search space becomes empty.
- All operations inside the loop (calculating `mid`, comparisons, pointer updates) take constant time, O(1).
- Therefore, the overall time complexity is O(log n).

Space Complexity: O(1)
- The algorithm uses a constant amount of extra space for the variables `left`, `right`, and `mid`.
- No additional data structures are created, and the space used does not depend on the size of the input array.
- Therefore, the space complexity is O(1).
'''

# Test Cases
nums1 = [-1,0,3,5,9,12]
target1 = 9
print(binarySearch(nums1, target1)) # Output: 4

nums2 = [-1,0,3,5,9,12]
target2 = 2
print(binarySearch(nums2, target2)) # Output: -1

nums3 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
target3 = 1
print(binarySearch(nums3, target3)) # Output: 0

nums4 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
target4 = 10
print(binarySearch(nums4, target4)) # Output: 9

nums5 = [5]
target5 = 5
print(binarySearch(nums5, target5)) # Output: 0

nums6 = [5]
target6 = 3
print(binarySearch(nums6, target6)) # Output: -1

nums7 = [1, 3, 5, 7, 9, 11, 13, 15]
target7 = 7
print(binarySearch(nums7, target7)) # Output: 3

nums8 = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
target8 = 15
print(binarySearch(nums8, target8)) # Output: -1

nums9 = [-10, -5, 0, 5, 10, 15, 20]
target9 = -5
print(binarySearch(nums9, target9)) # Output: 1

nums10 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
target10 = 11
print(binarySearch(nums10, target10)) # Output: -1