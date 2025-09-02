# REMOVE ELEMENT

'''
Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. 
The order of the elements may be changed. 
Then return the number of elements in nums which are not equal to val.
'''

def removeElement(nums, val):
    n = len(nums)
    left = 0
    
    for right in range(n):
        if nums[right] != val:
            nums[left] = nums[right]
            left += 1
    
    return left

# Time Complexity: O(n) because we iterate through the array once
# Space Complexity: O(1) because we are not using any extra space

# Test Cases
nums1 = [3,2,2,3], val1 = 3
print(removeElement(nums1, val1)) # Output: 2

nums2 = [0,1,2,2,3,0,4,2], val2 = 2
print(removeElement(nums2, val2)) # Output: 5

nums3 = [], val3 = 1
print(removeElement(nums3, val3)) # Output: 0

nums4 = [1,1,1], val4 = 1
print(removeElement(nums4, val4)) # Output: 0

nums5 = [1,2,3], val5 = 4
print(removeElement(nums5, val5)) # Output: 3

nums6 = [2,2,3], val6 = 2
print(removeElement(nums6, val6)) # Output: 1

nums7 = [3,3,3,3], val7 = 3
print(removeElement(nums7, val7)) # Output: 0

nums8 = [4,5,6,4,4], val8 = 4
print(removeElement(nums8, val8)) # Output: 2

nums9 = [0], val9 = 0
print(removeElement(nums9, val9)) # Output: 0

nums10 = [-1,0,1,-1], val10 = -1
print(removeElement(nums10, val10)) # Output: 2