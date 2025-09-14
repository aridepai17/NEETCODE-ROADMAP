# MAXIMUM PRODUCT DIFFERENCE BETWEEN TWO PAIRS

'''
The product difference between two pairs (a, b) and (c, d) is defined as (a * b) - (c * d).
For example, the product difference between (5, 6) and (2, 7) is (5 * 6) - (2 * 7) = 16.
Given an integer array nums, choose four distinct indices w, x, y, and z such that the product difference between pairs (nums[w], nums[x]) and (nums[y], nums[z]) is maximized.
Return the maximum such product difference.
'''

# Solution 1: Using Built-In Sort
def maxProductDifference1(nums):
    nums.sort()
    return (nums[-1] * nums[-2]) - (nums[0] * nums[1])

'''
Time Complexity: O(N log N)
- Let N be the number of elements in the `nums` array.
- The dominant operation is `nums.sort()`, which has an average and worst-case time complexity of O(N log N) for Timsort (Python's default sorting algorithm).
- The final calculation involves accessing elements by index, which is an O(1) operation.
- Therefore, the overall time complexity is O(N log N).

Space Complexity: O(N) or O(log N)
- The space complexity depends on the implementation of the sorting algorithm.
- Python's `sort()` method (Timsort) is not strictly in-place. It can require up to O(N) auxiliary space in the worst case for temporary storage during merges. 
- In many practical cases, it uses less, and for some inputs, it can be O(log N).
'''

# Solution 2: Using 4 Flags
def maxProductDifference2(nums):
    max1, max2 = 0, 0
    min1, min2 = float('inf'), float('inf')
    
    for num in nums:
        if num > max2:
            if num > max1:
                max1, max2 = num, max1
            else:
                max2 = num
        if num < min2:
            if num < min1:
                min1, min2 = num, min1
            else:
                min2 = num
                
    return max1 * max2 - min1 * min2

'''
Time Complexity: O(N)
- Let N be the number of elements in the `nums` array.
- The algorithm iterates through the array a single time to find the two largest and two smallest numbers.
- Inside the loop, all operations (comparisons and assignments) take constant time, O(1).
- Since the loop runs N times, the total time complexity is proportional to the size of the input array, resulting in O(N).

Space Complexity: O(1)
- The algorithm uses a constant amount of extra space to store four variables (`max1`, `max2`, `min1`, `min2`).
- The space required does not grow with the size of the input array `nums`.
- Therefore, the space complexity is O(1).
'''

# Test Cases
nums1 = [5,6,2,7,4]
print(maxProductDifference2(nums1)) # Output: 34

nums2 = [4,2,5,9,7,4,8]
print(maxProductDifference2(nums2)) # Output: 64

nums3 = [1,1,1,1,1]
print(maxProductDifference2(nums3)) # Output: 0

nums4 = [10,9,8,7,6,5,4,3,2,1]
print(maxProductDifference2(nums4)) # Output: 88

nums5 = [1,2,3,4,5,6,7,8,9,10]
print(maxProductDifference2(nums5)) # Output: 88

nums6 = [1, 6, 10, 4, 7, 9, 5]
print(maxProductDifference2(nums6)) # Output: 86

nums7 = [10000, 1, 10000, 1]
print(maxProductDifference2(nums7)) # Output: 99999999

nums8 = [1, 2, 10, 20]
print(maxProductDifference2(nums8)) # Output: 198

nums9 = [5, 5, 5, 5]
print(maxProductDifference2(nums9)) # Output: 0

nums10 = [2, 8, 1, 9, 4, 6]
print(maxProductDifference2(nums10)) # Output: 70