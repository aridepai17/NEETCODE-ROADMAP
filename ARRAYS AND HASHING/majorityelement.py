# MAJORITY ELEMENT

'''
Given an array nums of size n, return the majority element.
The majority element is the element that appears more than ⌊n / 2⌋ times. 
You may assume that the majority element always exists in the array.
'''

# Boye Moore's Voting Algorithm
def majorityElement(nums):
    count = 0
    candidate = float('-inf')
    
    for num in nums:
        if count == 0:
            candidate = num
            count = 1
        elif num == candidate:
            count += 1
        else:
            count -= 1
            
    return candidate

# Test Cases
nums1 = [3,2,3]
print(majorityElement(nums1)) # Output: 3

nums2 = [2,2,1,1,1,2,2]
print(majorityElement(nums2)) # Output: 2

nums3 = [1]
print(majorityElement(nums3)) # Output: 1

nums4 = [10, 9, 9, 9, 10]
print(majorityElement(nums4)) # Output: 9

nums5 = [6,5,5]
print(majorityElement(nums5)) # Output: 5

nums6 = [-1, 1, 1, 1, 2, 1]
print(majorityElement(nums6)) # Output: 1

nums7 = [1, 1, 1, 2, 2, 2, 2]
print(majorityElement(nums7)) # Output: 2

nums8 = [0, 0, 0]
print(majorityElement(nums8)) # Output: 0

nums9 = [8, 8, 7, 7, 7]
print(majorityElement(nums9)) # Output: 7

nums10 = [4, 4, 2, 4, 2, 2, 4, 4]
print(majorityElement(nums10)) # Output: 4