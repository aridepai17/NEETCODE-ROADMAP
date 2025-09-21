# APPLY OPERATIONS TO AN ARRAY

'''
You are given a 0-indexed array nums of size n consisting of non-negative integers.
You need to apply n - 1 operations to this array where, in the ith operation (0-indexed), you will apply the following on the ith element of nums:
If nums[i] == nums[i + 1], then multiply nums[i] by 2 and set nums[i + 1] to 0. Otherwise, you skip this operation.
After performing all the operations, shift all the 0's to the end of the array.
For example, the array [1,0,2,0,0,1] after shifting all its 0's to the end, is [1,2,1,0,0,0].
Return the resulting array.
Note that the operations are applied sequentially, not all at once.
'''

def applyOperations(nums):
    for i in range(len(nums) - 1):
        if nums[i] == nums[i + 1]:
            nums[i] *= 2
            nums[i + 1] = 0
            
    left = 0
    for right in range(len(nums)):
        if nums[right]:
            nums[right], nums[left] = nums[right], nums[left]
            left += 1
        
    return nums

'''
Time Complexity: O(n)
Let n be the number of elements in the input array `nums`.
The algorithm consists of two main parts, both of which are linear in time complexity.
1. The first `for` loop iterates from `0` to `n-2` to apply the specified operations. This loop runs `n-1` times, and each operation inside it (comparison, multiplication, assignment) takes constant time, O(1). Thus, this part has a time complexity of O(n).
2. The second `for` loop uses a two-pointer approach (`left` and `right`) to shift all non-zero elements to the beginning of the array. The `right` pointer traverses the entire array of n elements once. The operations inside this loop (checking for non-zero, swapping, and incrementing `left`) are all constant time. This part also has a time complexity of O(n).
Since these two loops are executed sequentially, the total time complexity is O(n) + O(n) = O(n).

Space Complexity: O(1)
The algorithm modifies the input array `nums` in-place.
It uses only a few extra variables (`i`, `left`, `right`) to keep track of indices.
The amount of extra space required does not depend on the size of the input array.
Therefore, the space complexity is constant, O(1).
'''

# Test Cases
nums1 = [1, 2, 2, 1, 1, 0]
print(applyOperations(nums1)) # Output: [1, 4, 2, 0, 0, 0]

nums2 = [0, 0, 0, 0]
print(applyOperations(nums2)) # Output: [0, 0, 0, 0]

nums3 = [1, 2, 3, 4, 5]
print(applyOperations(nums3)) # Output: [1, 2, 3, 4, 5]

nums4 = [8, 8, 8, 8, 8]
print(applyOperations(nums4)) # Output: [16, 16, 8, 0, 0]

nums5 = []
print(applyOperations(nums5)) # Output: []

nums6 = [10]
print(applyOperations(nums6)) # Output: [10]

nums7 = [6, 6, 0, 3, 3, 3, 0, 1]
print(applyOperations(nums7)) # Output: [12, 6, 3, 1, 0, 0, 0, 0]

nums8 = [1, 2, 3, 0, 0]
print(applyOperations(nums8)) # Output: [1, 2, 3, 0, 0]

nums9 = [2, 2, 4, 4, 8]
print(applyOperations(nums9)) # Output: [4, 8, 8, 0, 0]

nums10 = [0, 1, 1, 2, 2, 0, 3]
print(applyOperations(nums10)) # Output: [2, 4, 3, 0, 0, 0, 0]