# MONOTONIC ARRAY

'''
An array is monotonic if it is either monotone increasing or monotone decreasing.
An array nums is monotone increasing if for all i <= j, nums[i] <= nums[j]. 
An array nums is monotone decreasing if for all i <= j, nums[i] >= nums[j].
Given an integer array nums, return true if the given array is monotonic, or false otherwise.
'''

# Solution 1: Using Simple Traversal
def isMonotonic1(nums):
    if nums[-1] - nums[0] < 0:
        nums.sort()
        
    for i in range(len(nums) - 1):
        if not (nums[i] <= nums[i + 1]):
            return False
        
    return True

'''
Time Complexity: O(N log N)
Let N be the length of the `nums` array.
- The function's runtime is dominated by the `nums.sort()` operation, which is executed if the last element is smaller than the first.
- Python's `sort()` method uses the Timsort algorithm, which has a time complexity of O(N log N) in the average and worst cases.
- The `for` loop iterates through the array once, which is an O(N) operation.
- Since sorting is the most time-consuming part of the algorithm, the total time complexity is O(N log N).

Space Complexity: O(log N) to O(N)
- The space complexity is determined by the auxiliary space used by the in-place `list.sort()` method.
- While the sort is in-place (it modifies the original list), the Timsort algorithm requires temporary storage for merging runs.
- The space required for this is O(log N) on average and can be up to O(N) in the worst case.
- Outside of the sort, the algorithm uses constant extra space, O(1).
- Thus, the overall space complexity is dictated by the sorting algorithm's needs.
'''

# Solution 2: Using Two Boolean Flags
def isMonotonic2(nums):
    increasing = True
    decreasing = True
    
    for i in range(len(nums) - 1):
        if not (nums[i] <= nums[i + 1]):
            increasing = False
        elif not (nums[i] >= nums[i + 1]):
            decreasing = False
            
    return increasing or decreasing

'''
Time Complexity: O(N)
Let N be the length of the `nums` array.
- The algorithm iterates through the array once with a single `for` loop, from the first element up to the second-to-last element.
- The loop runs N - 1 times.
- Inside the loop, all operations are constant time, O(1):
  - Accessing array elements (`nums[i]`, `nums[i+1]`).
  - Performing comparisons (`<=`, `>=`).
  - Updating the boolean flags (`increasing`, `decreasing`).
- Since the loop runs N - 1 times with constant time operations in each iteration, the overall time complexity is O(N).

Space Complexity: O(1)
- The algorithm uses a fixed amount of extra space for the boolean flags `increasing` and `decreasing`, and the loop index `i`.
- The amount of memory used does not depend on the size of the input array.
- No new data structures that scale with the input size are created.
- Therefore, the space complexity is constant, O(1).
'''

# Test Cases
nums1 = [1, 2, 2, 3]
print(isMonotonic2(nums1)) # Output: True

nums2 = [6, 5, 4, 4]
print(isMonotonic2(nums2)) # Output: True

nums3 = [1, 3, 2]
print(isMonotonic2(nums3)) # Output: False

nums4 = [1, 1, 1]
print(isMonotonic2(nums4)) # Output: True

nums5 = [1]
print(isMonotonic2(nums5)) # Output: True

nums6 = []
print(isMonotonic2(nums6)) # Output: True

nums7 = [1, 2, 3, 4, 5]
print(isMonotonic2(nums7)) # Output: True

nums8 = [5, 4, 3, 2, 1]
print(isMonotonic2(nums8)) # Output: True

nums9 = [1, 2, 0]
print(isMonotonic2(nums9)) # Output: False

nums10 = [11, 11, 9, 4, 1]
print(isMonotonic2(nums10)) # Output: True