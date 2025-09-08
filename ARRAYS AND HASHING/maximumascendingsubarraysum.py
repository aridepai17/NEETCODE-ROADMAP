# MAXIMUM ASCENDING SUBARRAY SUM

'''
Given an array of positive integers nums, return the maximum possible sum of an strictly increasing subarray in nums.
An array is said to be strictly increasing if each element is strictly greater than its previous one (if exists).
A subarray is defined as a contiguous sequence of numbers in an array.
'''

def maxAscendingSum(nums):
    currentSum = nums[0]
    result = nums[0]
    
    for i in range(1, len(nums)):
        if nums[i] > nums[i - 1]:
            currentSum += nums[i]
        else:
            currentSum = nums[i]

        result = max(result, currentSum)
        
    return result

'''
Time Complexity: O(n)
Let n be the number of elements in the input array `nums`.
We iterate through the array once from the second element to the end. This loop runs n-1 times.
Inside the loop, we perform a constant number of operations (comparison, addition, assignment, and finding the maximum).
Therefore, the time complexity is directly proportional to the size of the input array, making it O(n).

Space Complexity: O(1)
We use a few constant extra space variables (`currentSum`, `result`, `i`) to keep track of the current ascending sum, the maximum sum found so far, and the loop index.
The amount of memory used does not grow with the size of the input array.
Thus, the space complexity is O(1).
'''

# Test Cases
nums1 = [10,20,30,5,10,50]
print(maxAscendingSum(nums1)) # Output: 65

nums2 = [100,10,1]
print(maxAscendingSum(nums2)) # Output: 100

nums3 = [12,17,15,13,10,11,12]
print(maxAscendingSum(nums3)) # Output: 33

nums4 = [1,1,1,1,1]
print(maxAscendingSum(nums4)) # Output: 1

nums5 = [1,2,3,4,5]
print(maxAscendingSum(nums5)) # Output: 15

nums6 = [5,4,3,2,1]
print(maxAscendingSum(nums6)) # Output: 5

nums7 = [10]
print(maxAscendingSum(nums7)) # Output: 10

nums8 = [3,6,10,1,2,7,9,100,2,5,7]
print(maxAscendingSum(nums8)) # Output: 119

nums9 = [10,20,30,40,50]
print(maxAscendingSum(nums9)) # Output: 150

nums10 = [50,40,30,20,10]
print(maxAscendingSum(nums10)) # Output: 50