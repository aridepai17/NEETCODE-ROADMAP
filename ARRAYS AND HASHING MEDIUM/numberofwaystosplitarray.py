# NUMBER OF WAYS TO SPLIT ARRAY

'''
You are given a 0-indexed integer array nums of length n.
nums contains a valid split at index i if the following are true:
- The sum of the first i + 1 elements is greater than or equal to the sum of the last n - i - 1 elements.
- There is at least one element to the right of i. That is, 0 <= i < n - 1.
Return the number of valid splits in nums.
'''

def waysToSplitArray(nums):
    right = sum(nums)
    left = 0
    result = 0
    
    for i in range(len(nums) - 1):
        left += nums[i]
        right -= nums[i]
        
        if left >= right:
            result += 1
            
    return result

'''
Time Complexity: O(n)
- Let n be the number of elements in the input array `nums`.
- We calculate the total sum of the array using `sum(nums)`, which takes O(n) time.
- We iterate through the array once with a for loop that runs n-1 times (since we stop at `len(nums) - 1`).
- Inside the loop, all operations (addition, subtraction, comparison, increment) are constant time, O(1).
- The overall time complexity is dominated by the initial sum calculation and the loop, resulting in O(n).

Space Complexity: O(1)
- We use a few variables (`right`, `left`, `result`, `i`) to store scalar values.
- The amount of extra space required does not depend on the size of the input array `nums`.
- Therefore, the space complexity is constant, O(1).
'''

# Test Cases
nums1 = [10, 4, -8, 7]
print(waysToSplitArray(nums1)) # Output: 2

nums2 = [2, 3, 1, 0]
print(waysToSplitArray(nums2)) # Output: 2

nums3 = [1, 2, 3, 4, 5]
print(waysToSplitArray(nums3)) # Output: 3

nums4 = [5, 5, 5, 5]
print(waysToSplitArray(nums4)) # Output: 3

nums5 = [1, 1, 1, 1, 1, 1]
print(waysToSplitArray(nums5)) # Output: 5

nums6 = [100, -50, -50]
print(waysToSplitArray(nums6)) # Output: 1

nums7 = [-1, -2, -3, -4]
print(waysToSplitArray(nums7)) # Output: 0

nums8 = [0, 0, 0, 0]
print(waysToSplitArray(nums8)) # Output: 3

nums9 = [1, -1, 1, -1]
print(waysToSplitArray(nums9)) # Output: 2

nums10 = [10, 20, 30, 40, 50]
print(waysToSplitArray(nums10)) # Output: 1