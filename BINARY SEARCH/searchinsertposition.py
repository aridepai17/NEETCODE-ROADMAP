# SEARCH INSERT POSITION

'''
Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.
You must write an algorithm with O(log n) runtime complexity.
'''

def searchInsert(nums, target):
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
    
    return left

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
nums1 = [1,3,5,6], target1 = 5
print(searchInsert(nums1, target1)) # Output: 2

nums2 = [1,3,5,6]
target2 = 2
print(searchInsert(nums2, target2)) # Output: 1

nums3 = [1,3,5,6]
target3 = 7
print(searchInsert(nums3, target3)) # Output: 4

nums4 = [1,3,5,6]
target4 = 0
print(searchInsert(nums4, target4)) # Output: 0

nums5 = [1]
target5 = 1
print(searchInsert(nums5, target5)) # Output: 0

nums6 = [1]
target6 = 2
print(searchInsert(nums6, target6)) # Output: 1

nums7 = [1,3,5,7,9,11]
target7 = 6
print(searchInsert(nums7, target7)) # Output: 3

nums8 = [2,4,6,8,10]
target8 = 1
print(searchInsert(nums8, target8)) # Output: 0

nums9 = [2,4,6,8,10]
target9 = 11
print(searchInsert(nums9, target9)) # Output: 5

nums10 = [1,2,3,4,5,6,7,8,9,10]
target10 = 5
print(searchInsert(nums10, target10)) # Output: 4