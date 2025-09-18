# FIND THE DIFFERENCE OF TWO ARRAYS

'''
Given two 0-indexed integer arrays nums1 and nums2, return a list answer of size 2 where:
answer[0] is a list of all distinct integers in nums1 which are not present in nums2.
answer[1] is a list of all distinct integers in nums2 which are not present in nums1.
Note that the integers in the lists may be returned in any order.
'''

def findDifference(nums1, nums2):
    set1 = set(nums1)
    set2 = set(nums2)
    
    onlynums1 = list(set1 - set2)
    onlynums2 = list(set2 - set1)
    
    return [onlynums1, onlynums2]

'''
Time Complexity: O(N + M)
Let N be the number of elements in `nums1` and M be the number of elements in `nums2`.
- Converting `nums1` to a set, `set(nums1)`, takes O(N) time on average, as it iterates through each element of `nums1`.
- Similarly, converting `nums2` to a set, `set(nums2)`, takes O(M) time on average.
- The set difference operation, `set1 - set2`, takes time proportional to the size of `set1`, which is at most O(N).
- The set difference operation, `set2 - set1`, takes time proportional to the size of `set2`, which is at most O(M).
- Converting the resulting sets back to lists takes time proportional to the number of elements in those sets, which is at most O(N) and O(M) respectively.
- The total time complexity is the sum of these operations: O(N) + O(M) + O(N) + O(M), which simplifies to O(N + M).

Space Complexity: O(N + M)
- We create two sets, `set1` and `set2`, to store the unique elements of `nums1` and `nums2`. In the worst case, where all elements are unique, `set1` will require O(N) space and `set2` will require O(M) space.
- The output lists, `onlynums1` and `onlynums2`, also require space. In the worst case, `onlynums1` could contain all N elements from `nums1` (if there's no overlap with `nums2`), and `onlynums2` could contain all M elements from `nums2`.
- Therefore, the total space complexity is O(N) + O(M), which simplifies to O(N + M).
'''

# Test Cases
nums1 = [1,2,3], nums2 = [2,4,6]
print(findDifference(nums1, nums2)) # Output: [[1, 3], [4, 6]]

nums1, nums2 = [1,2,3,3], [1,1,2,2]
print(findDifference(nums1, nums2)) # Output: [[3], []]

nums1, nums2 = [], [1,2,3]
print(findDifference(nums1, nums2)) # Output: [[], [1, 2, 3]]

nums1, nums2 = [4,5,6], []
print(findDifference(nums1, nums2)) # Output: [[4, 5, 6], []]

nums1, nums2 = [], []
print(findDifference(nums1, nums2)) # Output: [[], []]

nums1, nums2 = [1,2,3], [1,2,3]
print(findDifference(nums1, nums2)) # Output: [[], []]

nums1, nums2 = [1,2,3], [4,5,6]
print(findDifference(nums1, nums2)) # Output: [[1, 2, 3], [4, 5, 6]]

nums1, nums2 = [-1, -2, 0], [0, 1, 2]
print(findDifference(nums1, nums2)) # Output: [[-1, -2], [1, 2]]

nums1, nums2 = [8,0,6,5], [0,1,5,8,7]
print(findDifference(nums1, nums2)) # Output: [[6], [1, 7]]

nums1, nums2 = [1000, -1000], [-1000, 1000]
print(findDifference(nums1, nums2)) # Output: [[], []]