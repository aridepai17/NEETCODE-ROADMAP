# CONTAINS DUPICATE

'''
Given an integer array nums, return true if any value appears at least twice in the array, 
and return false if every element is distinct.
'''

def containsDuplicate(nums):
    visited = set()
    
    for num in nums:
        if num in visited:
            return True
        visited.add(num)
        
    return False

# Test Cases
nums1 = [1, 2, 3, 1]
print(containsDuplicate(nums1)) # Output: True

nums2 = [1, 2, 3, 4]
print(containsDuplicate(nums2)) # Output: False

nums3 = [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]
print(containsDuplicate(nums3)) # Output: True

nums4 = [1]
print(containsDuplicate(nums4)) # Output: False

nums5 = [1, 1]
print(containsDuplicate(nums5)) # Output: True

nums6 = [0, 0, 0, 0]
print(containsDuplicate(nums6)) # Output: True

nums7 = [-1, -2, -3, -1]
print(containsDuplicate(nums7)) # Output: True

nums8 = [5, 4, 3, 2, 1]
print(containsDuplicate(nums8)) # Output: False

nums9 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(containsDuplicate(nums9)) # Output: False

nums10 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 1]
print(containsDuplicate(nums10)) # Output: True