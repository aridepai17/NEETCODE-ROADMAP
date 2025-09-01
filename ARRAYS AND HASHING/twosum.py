# TWO SUM

'''
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.
'''

def twoSum(nums, target):
    hashMap = {}
    
    for i in range(len(nums)):
        diff = target - nums[i]
        
        if diff in hashMap:
            return [hashMap[diff], i]
        
        hashMap[nums[i]] = i
        
    return []

# Test Cases
nums1 = [2, 7, 11, 15]
target1 = 9
print(twoSum(nums1, target1)) # Output: [0, 1]

nums2 = [3, 2, 4]
target2 = 6
print(twoSum(nums2, target2)) # Output: [1, 2]

nums3 = [3, 3]
target3 = 6
print(twoSum(nums3, target3)) # Output: [0, 1]

nums4 = [1, 5, 8, 10, 13]
target4 = 18
print(twoSum(nums4, target4)) # Output: [2, 4]

nums5 = [0, 4, 3, 0]
target5 = 0
print(twoSum(nums5, target5)) # Output: [0, 3]

nums6 = [-1, -2, -3, -4, -5]
target6 = -8
print(twoSum(nums6, target6)) # Output: [2, 4]

nums7 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
target7 = 19
print(twoSum(nums7, target7)) # Output: [8, 9]

nums8 = [100, 200, 300, 400]
target8 = 500
print(twoSum(nums8, target8)) # Output: [1, 3]

nums9 = [1, 1, 1, 1, 1]
target9 = 2
print(twoSum(nums9, target9)) # Output: [0, 1]

nums10 = [5, 10, 15, 20, 25]
target10 = 30
print(twoSum(nums10, target10)) # Output: [1, 3]
