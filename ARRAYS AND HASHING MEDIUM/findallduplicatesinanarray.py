# FIND ALL DUPLICATES IN AN ARRAY

'''
Given an integer array nums of length n where all the integers of nums are in the range [1, n] and each integer appears at most twice, 
return an array of all the integers that appears twice.
You must write an algorithm that runs in O(n) time and uses only constant auxiliary space, 
excluding the space needed to store the output
'''

def findDuplicates(nums):
    result = []
    
    for n in nums:
        n = abs(n)
        if nums[n - 1] < 0:
            result.append(n)
        nums[n - 1] = -nums[n - 1]
        
    return result

'''
Time Complexity: O(N)
- The algorithm iterates through the input array `nums` exactly once, where N is the length of `nums`.
- All operations inside the loop (absolute value, array access, comparison, negation) are O(1) operations.
- Therefore, the overall time complexity is O(N).

Space Complexity: O(1) auxiliary space
- The algorithm uses only constant extra space beyond the input and output arrays.
- The `result` list is the output and is not counted in auxiliary space complexity.
- Only a few variables (`n`, loop index) use constant space O(1).
- The algorithm modifies the input array in-place to mark visited elements using negative signs.
- Therefore, the auxiliary space complexity is O(1), satisfying the problem constraints.
'''

# Test Cases
nums1 = [4,3,2,7,8,2,3,1]
print(findDuplicates(nums1)) # Output: [2, 3]

nums2 = [1, 1, 2]
print(findDuplicates(nums2)) # Output: [1]

nums3 = [1]
print(findDuplicates(nums3)) # Output: []

nums4 = [1, 2, 3, 4, 5]
print(findDuplicates(nums4)) # Output: []

nums5 = [1, 1, 1, 1, 1]
print(findDuplicates(nums5)) # Output: [1, 1]

nums6 = [2, 1, 2, 1]
print(findDuplicates(nums6)) # Output: [2, 1]

nums7 = [3, 2, 1, 3, 2]
print(findDuplicates(nums7)) # Output: [3, 2]

nums8 = [5, 4, 3, 2, 1, 5, 4]
print(findDuplicates(nums8)) # Output: [5, 4]

nums9 = [1, 2, 3, 1, 2, 3]
print(findDuplicates(nums9)) # Output: [1, 2, 3]

nums10 = [6, 5, 4, 3, 2, 1, 6, 5]
print(findDuplicates(nums10)) # Output: [6, 5]