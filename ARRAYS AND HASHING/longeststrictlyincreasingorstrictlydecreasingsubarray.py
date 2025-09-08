# LONGEST STRICTLY INCREASING OR STRICTLY DECREASING SUBARRAY

'''
You are given an array of integers nums. 
Return the length of the longest subarray of nums which is either strictly increasing or strictly decreasing.
An array is said to be strictly increasing if each element is strictly greater than its previous one (if exists).
An array is said to be strictly decreasing if each element is strictly smaller than its previous one (if exists).
'''

def longestMonotonicSubarray(nums):
    increasingLen = 1
    decreasingLen = 1
    maxLen = 1
    
    for i in range(1, len(nums)):
        if nums[i] > nums[i - 1]:
            increasingLen += 1
            decreasingLen = 1
        elif nums[i] < nums[i - 1]:
            decreasingLen += 1
            increasingLen = 1
        else:
            increasingLen = 1
            decreasingLen = 1
            
    maxLen = max(maxLen, increasingLen, decreasingLen)
    
    return maxLen

'''
Time Complexity: O(n)
Let n be the number of elements in the input array `nums`.
We iterate through the array once from the second element to the end. This loop runs n-1 times.
Inside the loop, we perform a constant number of operations (comparisons, assignments, and increments).
Therefore, the time complexity is directly proportional to the size of the input array, making it O(n).

Space Complexity: O(1)
We use a few constant extra space variables (`increasingLen`, `decreasingLen`, `maxLen`, `i`) to store the lengths of the current subarrays and the loop index.
The amount of memory used does not grow with the size of the input array.
Thus, the space complexity is O(1).
'''

# Test Cases
nums1 = [1,4,3,3,2]
print(longestMonotonicSubarray(nums1)) # Output: 2

nums2 = [1,2,3,4,5]
print(longestMonotonicSubarray(nums2)) # Output: 5

nums3 = [5,4,3,2,1]
print(longestMonotonicSubarray(nums3)) # Output: 5

nums4 = [3,3,3,3]
print(longestMonotonicSubarray(nums4)) # Output: 1

nums5 = [10]
print(longestMonotonicSubarray(nums5)) # Output: 1

nums6 = []
print(longestMonotonicSubarray(nums6)) # Output: 0

nums7 = [1,2,3,1,1]
print(longestMonotonicSubarray(nums7)) # Output: 3

nums8 = [1,2,3,1,2]
print(longestMonotonicSubarray(nums8)) # Output: 3

nums9 = [9,8,7,6,5,1,2,3,4,0]
print(longestMonotonicSubarray(nums9)) # Output: 5

nums10 = [1,5,2,6,3,7,4]
print(longestMonotonicSubarray(nums10)) # Output: 2