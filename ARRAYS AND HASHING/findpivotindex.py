# FIND PIVOT INDEX

'''
Given an array of integers nums, calculate the pivot index of this array.
The pivot index is the index where the sum of all the numbers strictly to the left of the index is equal to the sum of all the numbers strictly to the index's right.
If the index is on the left edge of the array, then the left sum is 0 because there are no elements to the left. 
This also applies to the right edge of the array.
Return the leftmost pivot index. If no such index exists, return -1.
'''

def pivotIndex(nums):
    total = sum(nums)
    leftSum = 0
    
    for i in range(len(nums)):
        rightSum = total - nums[i] - leftSum
        if leftSum == rightSum:
            return i
        leftSum += nums[i]
        
    return -1

'''
Time Complexity: O(n)
Let n be the number of elements in the input array `nums`.
First, we calculate the total sum of the array using `sum(nums)`, which takes O(n) time.
Then, we iterate through the array once with a for loop that runs n times.
Inside the loop, all operations (subtraction, comparison, addition) are constant time, O(1).
The overall time complexity is dominated by the initial sum calculation and the loop, resulting in O(n).

Space Complexity: O(1)
We use a few variables (`total`, `leftSum`, `rightSum`, `i`) to store scalar values.
The amount of extra space required does not depend on the size of the input array `nums`.
Therefore, the space complexity is constant, O(1).
'''

# Test Cases
nums1 = [1,7,3,6,5,6]
print(pivotIndex(nums1)) # Output: 3

nums2 = [1, 2, 3]
print(pivotIndex(nums2)) # Output: -1

nums3 = [2, 1, -1]
print(pivotIndex(nums3)) # Output: 0

nums4 = [1, -1, 0, 5]
print(pivotIndex(nums4)) # Output: 3

nums5 = [1, -1, 4]
print(pivotIndex(nums5)) # Output: 2

nums6 = [0, 0, 0, 0]
print(pivotIndex(nums6)) # Output: 0

nums7 = [10]
print(pivotIndex(nums7)) # Output: 0

nums8 = [1, -1]
print(pivotIndex(nums8)) # Output: -1

nums9 = [0, -1, 1, 1, -1, 0]
print(pivotIndex(nums9)) # Output: 3

nums10 = [1, 1, 1, 1, 1]
print(pivotIndex(nums10)) # Output: 2