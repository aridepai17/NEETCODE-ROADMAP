# MOVE ZEROES

'''
Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.
Note that you must do this in-place without making a copy of the array.
'''

def moveZeroes(nums):
    left = 0
    
    for right in range(len(nums)):
        if nums[right] != 0:
            if nums[left] == 0:
                nums[left], nums[right] = nums[right], nums[left]
            left += 1

'''
Time Complexity: O(n)
The algorithm uses a two-pointer approach. The `right` pointer iterates through the entire array from the beginning to the end, which takes `n` steps, where `n` is the number of elements in `nums`. The `left` pointer keeps track of the position for the next non-zero element.
Inside the loop, we perform a constant number of operations: a check, a potential swap, and an increment. Since each element of the array is visited by the `right` pointer exactly once, the total time complexity is linear, O(n).

Space Complexity: O(1)
The algorithm modifies the input array `nums` in-place, as required by the problem. It uses only two variables, `left` and `right`, to store pointers. The amount of extra memory used does not scale with the size of the input array. Therefore, the space complexity is constant, O(1).
'''

# Test Cases
nums1 = [0,1,0,3,12]
print(moveZeroes(nums1)) # Output: [1, 3, 12, 0, 0]

nums2 = [0]
print(moveZeroes(nums2)) # Output: [0]

nums3 = [1]
print(moveZeroes(nums3)) # Output: [1]

nums4 = []
print(moveZeroes(nums4)) # Output: []

nums5 = [1, 2, 3, 4, 5]
print(moveZeroes(nums5)) # Output: [1, 2, 3, 4, 5]

nums6 = [0, 0, 0, 0]
print(moveZeroes(nums6)) # Output: [0, 0, 0, 0]

nums7 = [1, 2, 0, 0, 3]
print(moveZeroes(nums7)) # Output: [1, 2, 3, 0, 0]

nums8 = [0, 0, 1, 2, 3]
print(moveZeroes(nums8)) # Output: [1, 2, 3, 0, 0]

nums9 = [1, 2, 3, 0, 0]
print(moveZeroes(nums9)) # Output: [1, 2, 3, 0, 0]

nums10 = [-1, 0, 5, -99, 0, 0, 4]
print(moveZeroes(nums10)) # Output: [-1, 5, -99, 4, 0, 0, 0]