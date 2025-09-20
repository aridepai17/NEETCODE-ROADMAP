# SORT ARRAY BY PARITY

'''
Given an integer array nums, move all the even integers at the beginning of the array followed by all the odd integers.
Return any array that satisfies this condition.
'''

def sortArrayByParity(nums):
    left = 0
    
    for right in range(len(nums)):
        if nums[right] % 2 == 0:
            nums[right], nums[left] = nums[left], nums[right]
            left += 1
            
    return nums

'''
Time Complexity: O(n)
Let n be the number of elements in the input array `nums`.
The algorithm uses a single `for` loop that iterates through the entire array once. The `right` pointer traverses each element from the beginning to the end.
Inside the loop, the operations performed—checking for parity (modulo), swapping elements, and incrementing the `left` pointer—all take constant time, O(1).
Since the loop runs n times, the total time complexity is linear with respect to the size of the input array, O(n).

Space Complexity: O(1)
The algorithm modifies the input array in-place.
It uses only a few extra variables (`left` and `right` pointers) to keep track of positions within the array.
The amount of extra space used does not scale with the size of the input array.
Therefore, the space complexity is constant, O(1).

'''

# Test Cases
nums1 = [3, 1, 2, 4]
print(sortArrayByParity(nums1)) # Output: [2, 4, 3, 1]
nums2 = [2, 4, 1, 3, 6]
print(sortArrayByParity(nums2)) # Output: [2, 4, 6, 3, 1]

nums3 = [0, 1, 2, 3, 4, 5]
print(sortArrayByParity(nums3)) # Output: [0, 2, 4, 3, 1, 5]

nums4 = []
print(sortArrayByParity(nums4)) # Output: []

nums5 = [1, 3, 5, 7]
print(sortArrayByParity(nums5)) # Output: [1, 3, 5, 7]

nums6 = [2, 4, 6, 8]
print(sortArrayByParity(nums6)) # Output: [2, 4, 6, 8]

nums7 = [1]
print(sortArrayByParity(nums7)) # Output: [1]

nums8 = [0]
print(sortArrayByParity(nums8)) # Output: [0]

nums9 = [1, 2]
print(sortArrayByParity(nums9)) # Output: [2, 1]

nums10 = [2, 1]
print(sortArrayByParity(nums10)) # Output: [2, 1]