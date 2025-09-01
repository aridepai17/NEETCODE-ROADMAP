# MAXIMUM CONSECUTIVE ONES

'''
Given a binary array nums, return the maximum number of consecutive 1's in the array.
'''

def findMaxConsecutiveOnes(nums):
    maxOne = 0
    count = 0
    
    for num in nums:
        if num == 1:
            count += 1
            maxOne = max(maxOne, count)
        else:
            count = 0
            
    return maxOne

# Test Cases
nums1 = [1, 1, 0, 1, 1, 1]
print(findMaxConsecutiveOnes(nums1)) # Output: 3

nums2 = [1, 0, 1, 1, 0, 1]
print(findMaxConsecutiveOnes(nums2)) # Output: 2

nums3 = [1, 1, 1, 1, 1]
print(findMaxConsecutiveOnes(nums3)) # Output: 5

nums4 = [0, 0, 0, 0, 0]
print(findMaxConsecutiveOnes(nums4)) # Output: 0

nums5 = [1]
print(findMaxConsecutiveOnes(nums5)) # Output: 1

nums6 = [0]
print(findMaxConsecutiveOnes(nums6)) # Output: 0

nums7 = [1, 0, 1, 0, 1, 0, 1]
print(findMaxConsecutiveOnes(nums7)) # Output: 1

nums8 = [1, 1, 1, 0, 0, 0, 1, 1, 1, 1]
print(findMaxConsecutiveOnes(nums8)) # Output: 4

nums9 = [0, 0, 1, 1, 1, 0, 0, 1, 1, 0]
print(findMaxConsecutiveOnes(nums9)) # Output: 3

nums10 = [1, 1, 1, 1, 0, 1, 1, 1, 1, 1]
print(findMaxConsecutiveOnes(nums10)) # Output: 5