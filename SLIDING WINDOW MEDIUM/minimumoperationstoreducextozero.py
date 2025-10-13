# MINIMUM OPERATIONS TO REDUCE X TO ZERO

'''
You are given an integer array nums and an integer x. In one operation, you can either remove the leftmost or the rightmost element from the array nums and subtract its value from x. 
Note that this modifies the array for future operations.
Return the minimum number of operations to reduce x to exactly 0 if it is possible, otherwise, return -1.
'''

def minOperations(nums, x):
    target = sum(nums) - x
    currentSum = 0
    maxWindow = -1
    left = 0
    
    for right in range(len(nums)):
        currentSum += nums[right]
        while left <= right and currentSum > target:
            currentSum -= nums[left]
            left += 1
        if currentSum == target:
            maxWindow = max(maxWindow, right - left + 1)
            
    return -1 if maxWindow == -1 else len(nums) - maxWindow

'''

Time Complexity: O(n)
The initial calculation of `sum(nums)` takes O(n) time, where n is the number of elements in the `nums` array.
The main part of the algorithm uses a sliding window approach with two pointers, `left` and `right`.
The `right` pointer iterates through the array from beginning to end once.
The `left` pointer also moves from left to right and will not traverse the array more than once over the entire execution.
Since each element is visited at most twice (once by `right` and once by `left`), the time complexity of the loop is O(n).
Therefore, the total time complexity is O(n) + O(n) = O(n).

Space Complexity: O(1)
The algorithm uses a few variables (`target`, `currentSum`, `maxWindow`, `left`, `right`) to store intermediate values.
The amount of memory used does not depend on the size of the input array `nums`.
Thus, the space complexity is constant, O(1).
'''

# Test Cases
nums1 = [1, 1, 4, 2, 3], x1 = 5
print(minOperations(nums1, x1)) # Output: 2

nums2 = [5, 6, 7, 8, 9], x2 = 4
print(minOperations(nums2, x2)) # Output: -1

nums3 = [3, 2, 20, 1, 1, 3], x3 = 10
print(minOperations(nums3, x3)) # Output: 5

nums4 = [1, 2, 3, 4, 5], x4 = 15
print(minOperations(nums4, x4)) # Output: 5

nums5 = [10], x5 = 10
print(minOperations(nums5, x5)) # Output: 1

nums6 = [10], x6 = 5
print(minOperations(nums6, x6)) # Output: -1

nums7 = [8, 1, 2, 3, 4, 1, 1, 1, 5], x7 = 13
print(minOperations(nums7, x7)) # Output: 2

nums8 = [1, 1, 1, 10, 1, 1, 1], x8 = 3
print(minOperations(nums8, x8)) # Output: 3

nums9 = [5, 2, 3, 1, 4], x9 = 4
print(minOperations(nums9, x9)) # Output: 1

nums10 = [3, 2, 20, 1, 1, 3], x10 = 35
print(minOperations(nums10, x10)) # Output: -1