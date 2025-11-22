# SEARCH IN ROTATED SORTED ARRAY 2

'''
There is an integer array nums sorted in non-decreasing order (not necessarily with distinct values).
Before being passed to your function, nums is rotated at an unknown pivot index k (0 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed).
For example, [0,1,2,4,4,4,5,6,6,7] might be rotated at pivot index 5 and become [4,5,6,6,7,0,1,2,4,4].
Given the array nums after the rotation and an integer target, return true if target is in nums, or false if it is not in nums.
You must decrease the overall operation steps as much as possible.
'''

'''
Algorithm and Intuition (Binary Search with Duplicates):
Intuition:
This problem is a variation of "Search in Rotated Sorted Array" but with the added complexity of duplicate values.
The presence of duplicates can make it impossible to determine which half is sorted when `nums[left] == nums[mid]`.
For example, `[1,0,1,1,1]` and `target = 0`. If `left=0`, `mid=2`, `right=4`, then `nums[left]=1`, `nums[mid]=1`, `nums[right]=1`.
In such cases, we cannot definitively say if the left half or the right half is sorted or contains the target.
The strategy for handling duplicates is to shrink the search space by moving `left` and `right` inwards when `nums[left] == nums[mid] == nums[right]`. 
This eliminates the ambiguity and allows the binary search to continue.

Algorithm Steps:
1. Initialize `left = 0` and `right = len(nums) - 1`.
2. While `left <= right`:
   a. Calculate `mid = (left + right) // 2`.
   b. If `nums[mid] == target`, return `True`.
   c. Handle duplicates: If `nums[left] == nums[mid] == nums[right]`:
      - Increment `left` by 1 and decrement `right` by 1.
      - Continue to the next iteration (this step is crucial to avoid infinite loops and correctly handle duplicates).
   d. Check if the left half (`nums[left]` to `nums[mid]`) is sorted:
      - If `nums[left] <= nums[mid]`:
         - If `target` is within this sorted left half (`nums[left] <= target < nums[mid]`):
            - Set `right = mid - 1` to search in the left half.
         - Else (target is not in the left half):
            - Set `left = mid + 1` to search in the right half.
   e. Else (the right half (`nums[mid]` to `nums[right]`) must be sorted):
      - If `target` is within this sorted right half (`nums[mid] < target <= nums[right]`):
         - Set `left = mid + 1` to search in the right half.
      - Else (target is not in the right half):
         - Set `right = mid - 1` to search in the left half.
3. If the loop finishes and the target is not found, return `False`.
'''

def search(nums, target):
    left = 0
    right = len(nums) - 1
    
    while left <= right:
        mid = (left + right) // 2
        
        if nums[mid] == target:
            return True
        
        if nums[left] == nums[mid] == nums[right]:
            left += 1
            right -= 1
            continue
        
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
                
    return False

'''
Time Complexity: O(log n) in the best/average case, O(n) in the worst case.
- The algorithm is a modified binary search.
- In the ideal scenario (no duplicates or few duplicates), the search space is halved in each step, leading to O(log n) complexity.
- The worst-case scenario occurs when there are many duplicate elements, specifically when `nums[left] == nums[mid] == nums[right]`.
  In this case, both `left` and `right` pointers are moved inwards by one (`left += 1`, `right -= 1`).
  This operation reduces the search space by only 2 elements, not necessarily by half.
  If the array consists entirely of duplicates (e.g., `[1,1,1,1,1]` and `target = 1`), or a large segment of duplicates
  where `nums[left] == nums[mid] == nums[right]`, the `while` loop might iterate `n/2` times, making it O(n).
- For example, `nums = [1,1,1,1,1,1,1,1,1,1,1,1,1,2,1,1,1,1,1]` and `target = 2`.
  When `left` is 0, `right` is `n-1`, and `mid` is in the middle of the `1`s, `nums[left] == nums[mid] == nums[right]` will be true.
  The pointers will move `left += 1` and `right -= 1`. This continues until the duplicates are passed,
  effectively degenerating to a linear scan in that segment.
- Therefore, the worst-case time complexity is O(n).

Space Complexity: O(1)
- The algorithm uses a constant amount of extra space.
- Variables `left`, `right`, and `mid` consume a fixed amount of memory regardless of the input array size `n`.
- No additional data structures (like lists, dictionaries, or recursive call stacks that grow with input size) are created.
- Therefore, the overall space complexity is O(1).
'''

# Test Cases
nums1 = [2,5,6,0,0,1,2], target1 = 0
print(search(nums1, target1)) # Expected Output: True

nums2 = [2,5,6,0,0,1,2], target2 = 3
print(search(nums2, target2)) # Expected Output: False

nums3 = [1,0,1,1,1], target3 = 0
print(search(nums3, target3)) # Expected Output: True

nums4 = [1,1,1,1,1,1,1,1,1,1,1,1,1,2,1,1,1,1,1], target4 = 2
print(search(nums4, target4)) # Expected Output: True

nums5 = [1,1,1,1,1,1,1,1,1,1,1,1,1,2,1,1,1,1,1], target5 = 3
print(search(nums5, target5)) # Expected Output: False

nums6 = [1,3,1,1,1], target6 = 3
print(search(nums6, target6)) # Expected Output: True

nums7 = [3,1,2,2,2], target7 = 1
print(search(nums7, target7)) # Expected Output: True

nums8 = [1,1], target8 = 1
print(search(nums8, target8)) # Expected Output: True

nums9 = [1], target9 = 0
print(search(nums9, target9)) # Expected Output: False

nums10 = [1,2,3,4,5,1,1,1], target10 = 5
print(search(nums10, target10)) # Expected Output: True