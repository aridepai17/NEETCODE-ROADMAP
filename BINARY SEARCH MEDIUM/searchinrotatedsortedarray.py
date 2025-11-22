# SEARCH IN ROTATED SORTED ARRAY

'''
There is an integer array nums sorted in ascending order (with distinct values).
Prior to being passed to your function, nums is possibly left rotated at an unknown index k (1 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). 
For example, [0,1,2,4,5,6,7] might be left rotated by 3 indices and become [4,5,6,7,0,1,2].
Given the array nums after the possible rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums.
You must write an algorithm with O(log n) runtime complexity.
'''

'''
Algorithm and Intuition (Binary Search):
Intuition:
The array is sorted but rotated. This means it's divided into two sorted halves.
We can use binary search to find the target. The key is to determine which half is sorted and whether the target lies within that sorted half.

Algorithm Steps:
1. Initialize `left = 0` and `right = len(nums) - 1`.
2. While `left <= right`:
   a. Calculate `mid = (left + right) // 2`.
   b. If `nums[mid] == target`, return `mid`.
   c. Check if the left half (`nums[left]` to `nums[mid]`) is sorted:
      - If `nums[left] <= nums[mid]`:
         - If `target` is within this sorted left half (`nums[left] <= target <= nums[mid]`):
            - Set `right = mid - 1` to search in the left half.
         - Else (target is not in the left half):
            - Set `left = mid + 1` to search in the right half.
   d. Else (the right half (`nums[mid]` to `nums[right]`) must be sorted):
      - If `target` is within this sorted right half (`nums[mid] <= target <= nums[right]`):
         - Set `left = mid + 1` to search in the right half.
      - Else (target is not in the right half):
         - Set `right = mid - 1` to search in the left half.
3. If the loop finishes and the target is not found, return -1.
'''

def search(nums, target):
    left = 0
    right = len(nums) - 1
    
    while left <= right:
        mid = (left + right) // 2
        
        if nums[mid] == target:
            return mid
        
        if nums[left] <= nums[mid]:
            if nums[left] <= target <= nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        else:
            if nums[right] >= target >= nums[mid]:
                left = mid + 1
            else:
                right = mid - 1
                
    return -1

'''
Time Complexity: O(log n)
- The algorithm uses a modified binary search approach.
- In each iteration of the `while` loop, the search space (defined by `left` and `right`) is roughly halved.
- This halving of the search space is characteristic of binary search, leading to a logarithmic time complexity.
- The number of iterations is proportional to log n, where n is the number of elements in `nums`.
- Inside the loop, all operations (comparisons, arithmetic, pointer assignments) take constant time, O(1).
- Therefore, the overall time complexity is O(log n).

Space Complexity: O(1)
- The algorithm uses a constant amount of extra space.
- Variables `left`, `right`, `mid`, and `target` consume a fixed amount of memory regardless of the input array size `n`.
- No additional data structures (like lists, dictionaries, or recursive call stacks that grow with input size) are created.
- Therefore, the space complexity is O(1).
'''

# Test Cases
nums1 = [4,5,6,7,0,1,2]
target1 = 0
print(search(nums1, target1)) # Output: 4

nums2 = [4,5,6,7,0,1,2]
target2 = 3
print(search(nums2, target2)) # Output: -1

nums3 = [1]
target3 = 1
print(search(nums3, target3)) # Output: 0

nums4 = [1,3]
target4 = 3
print(search(nums4, target4)) # Output: 1

nums5 = [3,1]
target5 = 1
print(search(nums5, target5)) # Output: 1

nums6 = [5,1,3]
target6 = 3
print(search(nums6, target6)) # Output: 2

nums7 = [1,2,3,4,5,6,7]
target7 = 5
print(search(nums7, target7)) # Output: 4

nums8 = [6,7,0,1,2,3,4,5]
target8 = 6
print(search(nums8, target8)) # Output: 0

nums9 = [6,7,0,1,2,3,4,5]
target9 = 5
print(search(nums9, target9)) # Output: 7

nums10 = [6,7,0,1,2,3,4,5]
target10 = 8
print(search(nums10, target10)) # Output: -1