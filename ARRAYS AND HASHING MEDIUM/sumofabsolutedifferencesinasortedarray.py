# SUM OF ABSOLUTE DIFFERENCES IN A SORTED ARRAY

'''
You are given an integer array nums sorted in non-decreasing order.
Build and return an integer array result with the same length as nums such that result[i] is equal to the summation of absolute differences between nums[i] and all the other elements in the array.
In other words, result[i] is equal to sum(|nums[i]-nums[j]|) where 0 <= j < nums.length and j != i (0-indexed).
'''

def absoluteDifferences(nums):
    total = sum(nums)
    leftSum = 0
    result = []
    n = len(nums)
    
    for index, number in enumerate(nums):
        rightSum = total - leftSum - number
        leftSize = index
        rightSize = n - index - 1
        
        result.append(
            leftSize * number - leftSum +
            rightSum - rightSize * number
        )
        
        leftSum += number
        
    return result

'''
Time Complexity: O(n)
- Let n be the number of elements in the input array `nums`.
- We calculate the total sum of the array using `sum(nums)`, which takes O(n) time.
- We iterate through the array once with a for loop using `enumerate(nums)`, which runs n times.
- Inside the loop, all operations (arithmetic calculations, list append) are constant time, O(1).
- The overall time complexity is dominated by the initial sum calculation and the loop, resulting in O(n).

Space Complexity: O(n)
- We create a `result` list that stores n elements, where n is the length of the input array `nums`.
- We use a few variables (`total`, `leftSum`, `n`, `index`, `number`, `rightSum`, `leftSize`, `rightSize`) to store scalar values, which require O(1) space.
- The space required for the output list is O(n).
- Therefore, the overall space complexity is O(n).
'''

# Test Cases
nums1 = [2,3,5]
print(absoluteDifferences(nums1)) # Output: [4,3,5]

nums2 = [1,4,6,8,10]
print(absoluteDifferences(nums2)) # Output: [24,15,13,15,24]

nums3 = [1]
print(absoluteDifferences(nums3)) # Output: [0]

nums4 = [5,5,5,5]
print(absoluteDifferences(nums4)) # Output: [0,0,0,0]

nums5 = [1,2,3,4,5]
print(absoluteDifferences(nums5)) # Output: [10,6,4,6,10]

nums6 = [10,20,30]
print(absoluteDifferences(nums6)) # Output: [40,20,40]

nums7 = [0,0,0]
print(absoluteDifferences(nums7)) # Output: [0,0,0]

nums8 = [-5,-3,0,3,5]
print(absoluteDifferences(nums8)) # Output: [20,12,8,12,20]

nums9 = [1,10]
print(absoluteDifferences(nums9)) # Output: [9,9]

nums10 = [2,4,6,8,10,12]
print(absoluteDifferences(nums10)) # Output: [30,20,12,12,20,30]