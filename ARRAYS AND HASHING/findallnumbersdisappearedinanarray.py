# FIND ALL NUMBERS DISAPPEARED IN AN ARRAY 

'''
Given an array nums of n integers where nums[i] is in the range [1, n], 
return an array of all the integers in the range [1, n] that do not appear in nums.
'''

# Solution 1: Brute force using Set
def findDisappearedNumbers1(nums):
    visited = set(nums)
    disappeared = []
    
    for i in range(1, len(nums) + 1):
        if i not in visited:
            disappeared.append(i)
            
    return disappeared

'''
Time Complexity: O(n)
Let n be the number of elements in the input array `nums`.
- Converting the list `nums` to a set `visited` takes O(n) time.
- We then iterate from 1 to n (inclusive). This loop runs n times.
- Inside the loop, checking for an element's existence in a set (`i not in visited`) is an O(1) operation on average.
- The overall time complexity is O(n) for building the set and O(n) for the loop, which simplifies to O(n).

Space Complexity: O(n)
- We use a set `visited` to store the unique numbers from `nums`. In the worst case, if all numbers are unique, the set will store n elements, requiring O(n) space.
- The output list `disappeared` can also store up to n-1 elements in the worst case (e.g., if `nums` is `[1, 1, ..., 1]`).
- Therefore, the space complexity is O(n) due to the extra space used by the set and the result list.
'''

# Solution 2: Using No Extra Space
def findDisappearedNumbers2(nums):
    for num in nums:
        index = abs(num) - 1
        if num[index] > 0:
            nums[index] *= -1
            
    disappeared = []
    
    for i in range(len(nums)):
        if nums[i] > 0:
            disappeared.append(i + 1)
            
    return disappeared

'''
Time Complexity: O(n)
Let n be the number of elements in the input array `nums`.
- The first loop iterates through the `nums` array once to mark the presence of numbers by negating the value at the corresponding index. This loop runs n times, and each operation inside is O(1). Total time for this step is O(n).
- The second loop iterates through the modified `nums` array once to find the indices that still have positive values. This loop also runs n times, with O(1) operations inside. Total time for this step is O(n).
- The overall time complexity is O(n) + O(n), which simplifies to O(n).

Space Complexity: O(1) (excluding the output array)
- This solution modifies the input array `nums` in-place.
- The extra space used is for the variables `num`, `index`, and `i`, which is constant O(1).
- The space required for the output list `disappeared` is not typically counted as extra space in the context of this problem's constraints ("no extra space"). If it were counted, the space complexity would be O(k), where k is the number of disappeared numbers (k <= n).
'''

# Test Cases
nums1 = [4,3,2,7,8,2,3,1]
print(findDisappearedNumbers2(nums1)) # Output: [5, 6]

# Test Case 2: No numbers missing
nums2 = [1, 2, 3, 4, 5]
print(findDisappearedNumbers2(nums2)) # Output: []

# Test Case 3: All numbers missing except one
nums3 = [1, 1, 1, 1]
print(findDisappearedNumbers2(nums3)) # Output: [2, 3, 4]

# Test Case 4: All elements are the same
nums4 = [2, 2, 2, 2, 2]
print(findDisappearedNumbers2(nums4)) # Output: [1, 3, 4, 5]

# Test Case 5: Empty array
nums5 = []
print(findDisappearedNumbers2(nums5)) # Output: []

# Test Case 6: Array of size 1, number present
nums6 = [1]
print(findDisappearedNumbers2(nums6)) # Output: []

# Test Case 7: First and last numbers missing
nums7 = [2, 3, 4, 2, 3]
print(findDisappearedNumbers2(nums7)) # Output: [1, 5]

# Test Case 8: Sorted-like array with missing numbers
nums8 = [1, 1, 2, 2, 4, 4]
print(findDisappearedNumbers2(nums8)) # Output: [3, 5, 6]

# Test Case 9: A larger array with missing numbers in the middle
nums9 = [10, 2, 5, 10, 9, 1, 1, 4, 3, 7]
print(findDisappearedNumbers2(nums9)) # Output: [6, 8]

# Test Case 10: All numbers present up to a point, with duplicates
nums10 = [1, 2, 2, 3, 3, 4, 4, 5]
print(findDisappearedNumbers2(nums10)) # Output: [6, 7, 8]