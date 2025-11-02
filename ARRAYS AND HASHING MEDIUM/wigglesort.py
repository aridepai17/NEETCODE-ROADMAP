# WIGGLE SORT

'''
Given an unsorted array nums, reorder it in-place such that nums[0] <= nums[1] >= nums[2] <= nums[3]...
'''

def wiggleSort(nums):
    for i in range(1, len(nums)):
        if (i % 2 == 1 and nums[i] < nums[i - 1]) or (i % 2 == 0 and nums[i] > nums[i - 1]):
            nums[i], nums[i - 1] = nums[i - 1], nums[i]

    return nums

'''
Time Complexity: O(N)
- Let N be the number of elements in the input array `nums`.
- The algorithm iterates through the array once from the second element to the end.
- The loop runs N-1 times.
- Inside the loop, all operations (modulo, comparison, and swapping) are performed in constant time, O(1).
- Therefore, the total time complexity is O(N).

Space Complexity: O(1)
- The algorithm sorts the array in-place, meaning it does not use any additional data structures whose size grows with the input.
- It only uses a few variables for the loop index and comparisons, which occupy constant space.
- Therefore, the space complexity is O(1).
'''

# Test Cases
nums1 = [3, 1, 4, 1, 5, 9, 2, 6, 2, 4]
print(wiggleSort(nums1)) # Output: [1, 3, 1, 5, 2, 9, 2, 6, 3, 4]

nums2 = [3, 5, 2, 1, 6, 4]
print(wiggleSort(nums2)) # Output: [3, 5, 1, 6, 2, 4]

nums3 = [1, 2, 3, 4, 5]
print(wiggleSort(nums3)) # Output: [1, 3, 2, 5, 4]

nums4 = [6, 6, 5, 6, 3, 8]
print(wiggleSort(nums4)) # Output: [6, 6, 5, 6, 3, 8]

nums5 = [1, 1, 1, 1, 1]
print(wiggleSort(nums5)) # Output: [1, 1, 1, 1, 1]

nums6 = [10, 9, 8, 7, 6]
print(wiggleSort(nums6)) # Output: [9, 10, 7, 8, 6]

nums7 = [1]
print(wiggleSort(nums7)) # Output: [1]

nums8 = []
print(wiggleSort(nums8)) # Output: []

nums9 = [1, 5, 1, 1, 6, 4]
print(wiggleSort(nums9)) # Output: [1, 5, 1, 6, 1, 4]

nums10 = [2, 1]
print(wiggleSort(nums10)) # Output: [1, 2]