# NON DECREASING ARRAY

'''
Given an array nums with n integers, your task is to check if it could become non-decreasing by modifying at most one element.
We define an array is non-decreasing if nums[i] <= nums[i + 1] holds for every i (0-based) such that (0 <= i <= n - 2).
'''

def checkPossibility(nums):
    changes = False
    
    for i in range(len(nums) - 1):
        if nums[i] <= nums[i + 1]:
            continue
        if changes:
            return False
        if i == 0 or nums[i + 1] >= nums[i - 1]:
            nums[i] = nums[i + 1]
        else:
            nums[i + 1] = nums[i]
        changes = True
        
    return True


'''
Time Complexity: O(N)
- The algorithm traverses the list once, performing at most one element modification in a single pass.
- Each comparison, assignment, or return in the for loop takes constant time, so the total time is proportional to the input size N.

Space Complexity: O(1)
- The algorithm uses a constant number of variables (`changes`, `i`) and modifies the array in-place.
- No additional data structures whose size depends on the input are used.
'''

# Test Cases
nums1 = [4,2,3]
print(checkPossibility(nums1)) # Output: True



nums2 = [4,2,1]
print(checkPossibility(nums2)) # Output: False
# Explanation: Cannot be made non-decreasing with one change.

nums3 = [3,4,2,3]
print(checkPossibility(nums3)) # Output: False
# Explanation: At i=1 (4 > 2), if we change 4 to 2 -> [3,2,2,3] (still decreasing at start). If we change 2 to 4 -> [3,4,4,3] (still decreasing at end).

nums4 = [1,2,3]
print(checkPossibility(nums4)) # Output: True
# Explanation: Already non-decreasing.

nums5 = [5,7,1,8]
print(checkPossibility(nums5)) # Output: True
# Explanation: Change 1 to 7 -> [5,7,7,8].

nums6 = [1]
print(checkPossibility(nums6)) # Output: True
# Explanation: An array with one element is always non-decreasing.

nums7 = [2,1]
print(checkPossibility(nums7)) # Output: True
# Explanation: Change 2 to 1 -> [1,1].

nums8 = [1,1,1]
print(checkPossibility(nums8)) # Output: True
# Explanation: Already non-decreasing with duplicates.

nums9 = [-1,4,2,3]
print(checkPossibility(nums9)) # Output: True
# Explanation: Change 4 to 2 -> [-1,2,2,3].

nums10 = [1,5,2,6,3]
print(checkPossibility(nums10)) # Output: False
# Explanation: Needs more than one change.