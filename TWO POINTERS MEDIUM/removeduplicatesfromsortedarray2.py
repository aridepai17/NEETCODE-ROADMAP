# REMOVE DUPLICATES FROM SORTED ARRAY

'''
Given an integer array nums sorted in non-decreasing order, remove some duplicates in-place such that each unique element appears at most twice. 
The relative order of the elements should be kept the same.
Since it is impossible to change the length of the array in some languages, you must instead have the result be placed in the first part of the array nums. 
More formally, if there are k elements after removing the duplicates, then the first k elements of nums should hold the final result. 
It does not matter what you leave beyond the first k elements.
Return k after placing the final result in the first k slots of nums.
Do not allocate extra space for another array. You must do this by modifying the input array in-place with O(1) extra memory.
'''

def removeDuplicates(nums):
    if len(nums) <= 2:
        return len(nums)
    
    left = 2
    
    for right in range(2, len(nums)):
        if nums[right] != nums[left - 2]:
            nums[left] = nums[right]
            left += 1
            
    return left

'''
Time Complexity: O(n)
The algorithm iterates through the array with a single pass using the 'right' pointer. 
For an array of size n, the loop runs approximately n times. Thus, the time complexity is linear.

Space Complexity: O(1)
The algorithm modifies the input array in-place. It uses only a constant amount of extra space for variables like 'left' and 'right', regardless of the input size.
'''

# Test Cases
nums1 = [1, 1, 1, 2, 2, 3]
print(removeDuplicates(nums1)) # Output: 5

nums2 = [1, 2, 3, 4, 5]
print(removeDuplicates(nums2)) # Output: 5

nums3 = [1, 1, 1, 1, 1]
print(removeDuplicates(nums3)) # Output: 2

nums4 = [0, 0, 0, 0, 1, 2, 3]
print(removeDuplicates(nums4)) # Output: 5

nums5 = [1, 2, 3, 4, 4, 4, 4]
print(removeDuplicates(nums5)) # Output: 5

nums6 = [1, 1, 2, 2, 2, 3, 3]
print(removeDuplicates(nums6)) # Output: 6

nums7 = []
print(removeDuplicates(nums7)) # Output: 0

nums8 = [5]
print(removeDuplicates(nums8)) # Output: 1

nums9 = [5, 5]
print(removeDuplicates(nums9)) # Output: 2

nums10 = [0, 0, 1, 1, 1, 1, 2, 3, 3, 3]
print(removeDuplicates(nums10)) # Output: 7