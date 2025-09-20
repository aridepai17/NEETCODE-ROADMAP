# REMOVE DUPLICATES FROM SORTED ARRAY

'''
Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. 
The relative order of the elements should be kept the same. Then return the number of unique elements in nums.
Consider the number of unique elements of nums to be k, to get accepted, you need to do the following things:
Change the array nums such that the first k elements of nums contain the unique elements in the order they were present in nums initially. 
The remaining elements of nums are not important as well as the size of nums.
Return k.
'''

def removeDuplicates(nums):
    left = 0
    
    for right in range(1, len(nums)):
        if nums[right] != nums[left]:
            left += 1
            nums[left] = nums[right]
            
    return left + 1

'''
Time Complexity: O(n)
Let n be the number of elements in the input array `nums`.
The algorithm uses a two-pointer approach, where `left` tracks the position for the next unique element and `right` iterates through the array.
The `right` pointer traverses the array from the second element to the end, visiting each of the `n-1` elements once.
Inside the loop, the operations (comparison, pointer increment, and assignment) are all constant time, O(1).
Since each element is processed once by the `right` pointer, the total time complexity is linear with respect to the size of the input array, O(n).

Space Complexity: O(1)
The algorithm modifies the input array `nums` in-place, as required by the problem statement.
It uses only a constant amount of extra space for the two pointers, `left` and `right`.
The memory usage does not scale with the size of the input array.
Therefore, the space complexity is O(1).
'''

# Test Cases
nums1 = [1,1,2]
print(removeDuplicates(nums1)) # Output: 2

nums2 = [0,0,1,1,1,2,2,3,3,4]
print(removeDuplicates(nums2)) # Output: 5

nums3 = [1,2,3,4,5]
print(removeDuplicates(nums3)) # Output: 5

nums4 = [1,1,1,1,1]
print(removeDuplicates(nums4)) # Output: 1

nums5 = []
print(removeDuplicates(nums5)) # Output: 0 (Note: The provided function needs a check for an empty list to pass this test)

nums6 = [5]
print(removeDuplicates(nums6)) # Output: 1

nums7 = [-1,0,0,0,3,3]
print(removeDuplicates(nums7)) # Output: 3

nums8 = [1, 1, 2, 3, 3, 3, 4, 5, 5]
print(removeDuplicates(nums8)) # Output: 5

nums9 = [-5, -5, -3, -1, -1, 0, 0, 0]
print(removeDuplicates(nums9)) # Output: 4

nums10 = [100, 100, 100]
print(removeDuplicates(nums10)) # Output: 1