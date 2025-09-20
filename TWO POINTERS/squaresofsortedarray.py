# SQUARES OF SORTED ARRAY

'''
Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.
'''

def sortedSquares(nums):
    result = []
    left = 0
    right = len(nums) - 1
    
    while left <= right:
        if nums[left] * nums[left] > nums[right] * nums[right]:
            result.append(nums[left] * nums[left])
            left += 1
        else:
            result.append(nums[right] * nums[right])
            right -= 1
            
    return result[::-1]

'''
Time Complexity: O(n)
Let n be the number of elements in the input array `nums`.
The algorithm uses a two-pointer approach, with `left` at the start and `right` at the end of the array.
The `while` loop iterates until the two pointers meet, which means it runs n times.
Inside the loop, we perform constant time operations: squaring two numbers, comparing them, and appending to a result list.
Finally, `result[::-1]` creates a reversed copy of the result list, which also takes O(n) time.
Thus, the total time complexity is linear with respect to the size of the input array, O(n).

Space Complexity: O(n)
The space complexity is determined by the `result` list, which is used to store the squared numbers.
This list will grow to have the same number of elements as the input array, n.
The space used by the pointers (`left`, `right`) is constant, O(1).
Therefore, the space required is proportional to the size of the input array, making the space complexity O(n).
'''

# Test Cases
nums1 = [-4,-1,0,3,10]
print(sortedSquares(nums1)) # Output: [0, 1, 9, 16, 100]

nums2 = [-7,-3,-2,-1]
print(sortedSquares(nums2)) # Output: [1, 4, 9, 49]

nums3 = [1,2,3,4,5]
print(sortedSquares(nums3)) # Output: [1, 4, 9, 16, 25]

nums4 = [-5]
print(sortedSquares(nums4)) # Output: [25]

nums5 = [5]
print(sortedSquares(nums5)) # Output: [25]

nums6 = [0]
print(sortedSquares(nums6)) # Output: [0]

nums7 = []
print(sortedSquares(nums7)) # Output: []

nums8 = [-3,-3,0,1,1]
print(sortedSquares(nums8)) # Output: [0, 1, 1, 9, 9]

nums9 = [-10,-5,0,1,2]
print(sortedSquares(nums9)) # Output: [0, 1, 4, 25, 100]

nums10 = [-5,-4,-3,-2,-1,0,1,2,3,4]
print(sortedSquares(nums10)) # Output: [0, 1, 1, 4, 4, 9, 9, 16, 16, 25]