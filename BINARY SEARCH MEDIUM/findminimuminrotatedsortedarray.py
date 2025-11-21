# FIND MINIMUM IN ROTATED SORTED ARRAY

'''
Suppose an array of length n sorted in ascending order is rotated between 1 and n times. For example, the array nums = [0,1,2,4,5,6,7] might become:
- [4,5,6,7,0,1,2] if it was rotated 4 times.
- [0,1,2,4,5,6,7] if it was rotated 7 times.
Notice that rotating an array [a[0], a[1], a[2], ..., a[n-1]] 1 time results in the array [a[n-1], a[0], a[1], a[2], ..., a[n-2]].
Given the sorted rotated array nums of unique elements, return the minimum element of this array.
You must write an algorithm that runs in O(log n) time.
'''

'''
Algorithm and Intuition (Binary Search):
Intuition:
The array is sorted but rotated. This means there's a "pivot" point where the rotation occurred.
The minimum element will always be immediately to the right of the largest element, or it will be the first element if the array is not rotated (rotated n times).
We can use binary search to efficiently find this minimum element.
The key observation is to compare the middle element `nums[mid]` with the rightmost element `nums[right]`.
- If `nums[mid] > nums[right]`, it means the minimum element must be in the right half (from `mid + 1` to `right`), because the left half (from `left` to `mid`) is still in ascending order but `nums[mid]` is greater than `nums[right]`, implying a rotation point exists after `mid`.
- If `nums[mid] <= nums[right]`, it means the minimum element is either `nums[mid]` itself or in the left half (from `left` to `mid`). 
- The right half (from `mid` to `right`) is sorted, and `nums[mid]` is less than or equal to `nums[right]`, so the minimum cannot be in `mid + 1` to `right`. 
- We set `right = mid` to include `mid` as a potential minimum.

Algorithm Steps:
1. Initialize `left = 0` and `right = len(nums) - 1`.
2. While `left < right`:
   a. Calculate `mid = (left + right) // 2`.
   b. If `nums[mid] > nums[right]`, set `left = mid + 1`. This means the minimum is in the right unsorted portion.
   c. Else (`nums[mid] <= nums[right]`), set `right = mid`. This means `nums[mid]` could be the minimum, or the minimum is in the left portion.
3. When the loop terminates, `left` will be equal to `right`, and this index will point to the minimum element. Return `nums[left]`.
'''

def findMin(nums):
    left = 0
    right = len(nums) - 1

    while left < right:
        mid = (left + right) // 2
        
        if nums[mid] > nums[right]:
            left = mid + 1
        else:
            right = mid
            
    return nums[left]

'''
Time Complexity: O(log n)
- The algorithm uses binary search, which repeatedly halves the search space.
- In each iteration, the `mid` element is calculated, and a comparison is made to decide whether to search the left or right half.
- This process continues until `left` is no longer less than `right`.
- The number of iterations is logarithmic with respect to the number of elements `n` in the `nums` array.
- All operations inside the loop (arithmetic, comparisons, pointer assignments) take constant time.
- Therefore, the overall time complexity is O(log n).

Space Complexity: O(1)
- The algorithm uses a constant amount of extra space.
- Variables `left`, `right`, and `mid` are used to keep track of the search boundaries and the current midpoint.
- These variables consume a fixed amount of memory regardless of the input array size `n`.
- No additional data structures are created that scale with the input size.
- Therefore, the space complexity is O(1).
'''

# Test Cases
nums1 = [3,4,5,1,2]
print(findMin(nums1)) # Output: 1

nums2 = [4,5,6,7,0,1,2]
print(findMin(nums2)) # Output: 0

nums3 = [11,13,15,17]
print(findMin(nums3)) # Output: 11

nums4 = [1]
print(findMin(nums4)) # Output: 1

nums5 = [2,1]
print(findMin(nums5)) # Output: 1

nums6 = [5,1,2,3,4]
print(findMin(nums6)) # Output: 1

nums7 = [3,1,2]
print(findMin(nums7)) # Output: 1

nums8 = [0,1,2,3,4,5,6,7]
print(findMin(nums8)) # Output: 0

nums9 = [7,0,1,2,3,4,5,6]
print(findMin(nums9)) # Output: 0

nums10 = [6,7,0,1,2,3,4,5]
print(findMin(nums10)) # Output: 0