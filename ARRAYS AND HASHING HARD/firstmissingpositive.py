# FIRST MISSING POSITIVE

'''
Given an unsorted integer array nums. Return the smallest positive integer that is not present in nums.
You must implement an algorithm that runs in O(n) time and uses O(1) auxiliary space.
'''

def firstmissingPositive(nums):
    for i in range(len(nums)):
        if nums[i] < 0:
            nums[i] = 0
            
    for i in range(len(nums)):
        value = abs(nums[i])
        if 1 <= value <= len(nums):
            if nums[value - 1] > 0:
                nums[value - 1] *= -1
            elif nums[value - 1] == 0:
                nums[value - 1] = -1 * (len(nums) + 1)
                
    for i in range(1, len(nums) + 1):
        if num[i - 1] >= 0:
            return i
        
    return len(nums) + 1

'''
Time Complexity: O(n)
Let n be the number of elements in the input array `nums`.
- The first loop iterates through the array once to replace negative numbers with 0. This takes O(n) time.
- The second loop iterates through the array once to mark the presence of positive integers by negating values at corresponding indices. This takes O(n) time.
- The third loop iterates through the array once to find the first index with a non-negative value. This takes O(n) time.
- The overall time complexity is O(n) + O(n) + O(n), which simplifies to O(n).

Space Complexity: O(1)
- The algorithm modifies the input array `nums` in-place without using any additional data structures.
- Only a constant amount of extra space is used for variables like `i` and `value`.
- Therefore, the space complexity is O(1), which satisfies the problem's auxiliary space constraint.
'''

# Test Cases
nums1 = [3, 4, -1, 1]
print(firstmissingPositive(nums1)) # Output: 2

nums2 = [1, 2, 0]
print(firstmissingPositive(nums2)) # Output: 3

nums3 = [7, 8, 9, 11, 12]
print(firstmissingPositive(nums3)) # Output: 1

nums4 = [1]
print(firstmissingPositive(nums4)) # Output: 2

nums5 = [2]
print(firstmissingPositive(nums5)) # Output: 1

nums6 = [1, 2, 3, 4, 5]
print(firstmissingPositive(nums6)) # Output: 6

nums7 = [2, 3, 4]
print(firstmissingPositive(nums7)) # Output: 1

nums8 = [1, 1000]
print(firstmissingPositive(nums8)) # Output: 2

nums9 = [-5, -4, -3, -2, -1]
print(firstmissingPositive(nums9)) # Output: 1

nums10 = [1, 2, 6, 3, 5, 4]
print(firstmissingPositive(nums10)) # Output: 7