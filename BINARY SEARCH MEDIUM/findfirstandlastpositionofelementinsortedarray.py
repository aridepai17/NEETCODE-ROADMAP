# FIND FIRST AND LAST POSITION IN SORTED ARRAY

'''
Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.
If target is not found in the array, return [-1, -1].
You must write an algorithm with O(log n) runtime complexity.
'''

'''
Algorithm and Intuition (Binary Search):
Intuition:
Since the array is sorted, we can use binary search to find the target.
To find the first and last occurrences, we can modify the standard binary search.
The key idea is that once we find an instance of the target, we continue searching in one direction
to find the boundary (either the leftmost or rightmost occurrence).

Algorithm Steps:
1. Define a helper function `binarySearch(nums, target, findLeftIndex)`:
   - Initialize `left = 0`, `right = len(nums) - 1`, and `index = -1` (to store the potential result).
   - While `left <= right`:
     a. Calculate `mid = (left + right) // 2`.
     b. If `nums[mid] < target`, move to the right half: `left = mid + 1`.
     c. If `nums[mid] > target`, move to the left half: `right = mid - 1`.
     d. If `nums[mid] == target`:
        - Store `mid` as a potential `index`.
        - If `findLeftIndex` is `True` (searching for the first occurrence), try to find an even smaller index by searching in the left half: `right = mid - 1`.
        - If `findLeftIndex` is `False` (searching for the last occurrence), try to find an even larger index by searching in the right half: `left = mid + 1`.
   - Return `index`.
2. In the main `searchRange` function:
   - Call `binarySearch(nums, target, True)` to find the `left` (first) occurrence.
   - Call `binarySearch(nums, target, False)` to find the `right` (last) occurrence.
   - Return `[left, right]`.
'''

def searchRange(nums, target):
    def binarySearch(nums, target, leftIndex):
        left = 0
        right = len(nums) - 1
        index = -1
        
        while left <= right:
            mid = (left + right) // 2
            
            if nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
            else:
                index = mid
                if leftIndex:
                    right = mid - 1
                else:
                    left = mid + 1
                    
        return index
    
    left = binarySearch(nums, target, True)
    right = binarySearch(nums, target, False)
    
    return [left, right]

'''
Time Complexity: O(log n)
- The algorithm consists of two calls to the `binarySearch` helper function.
- Each `binarySearch` function performs a standard binary search on the input array `nums`.
- A binary search algorithm reduces the search space by half in each iteration, leading to a logarithmic time complexity.
- Therefore, each call to `binarySearch` takes O(log n) time, where n is the number of elements in `nums`.
- Since there are two such calls, the total time complexity remains O(log n).
- All operations inside the `binarySearch` loop (calculating mid, comparisons, pointer assignments) are O(1).

Space Complexity: O(1)
- The algorithm uses a constant amount of extra space.
- Variables `left`, `right`, `mid`, `index`, and `leftIndex` consume a fixed amount of memory regardless of the input array size `n`.
- No additional data structures (like lists, dictionaries, or recursive call stacks that grow with input size) are created.
- Therefore, the space complexity is O(1).
'''

# Test Cases
nums1 = [5,7,7,8,8,10], target1 = 8
print(searchRange(nums1, target1)) # Output: [3,4]

nums2 = [5,7,7,8,8,10], target2 = 6
print(searchRange(nums2, target2)) # Output: [-1,-1]

nums3 = [], target3 = 0
print(searchRange(nums3, target3)) # Output: [-1,-1]

nums4 = [1], target4 = 1
print(searchRange(nums4, target4)) # Output: [0,0]

nums5 = [1,2,3,3,3,3,4,5], target5 = 3
print(searchRange(nums5, target5)) # Output: [2,5]

nums6 = [1,1,1,1,1], target6 = 1
print(searchRange(nums6, target6)) # Output: [0,4]

nums7 = [1,2,3,4,5], target7 = 0
print(searchRange(nums7, target7)) # Output: [-1,-1]

nums8 = [1,2,3,4,5], target8 = 6
print(searchRange(nums8, target8)) # Output: [-1,-1]

nums9 = [2,2], target9 = 2
print(searchRange(nums9, target9)) # Output: [0,1]

nums10 = [1,3], target10 = 1
print(searchRange(nums10, target10)) # Output: [0,0]