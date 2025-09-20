# MERGE TWO 2D ARRAYS BY SUMMING VALUES

'''
You are given two 2D integer arrays nums1 and nums2.
nums1[i] = [idi, vali] indicate that the number with the id idi has a value equal to vali.
nums2[i] = [idi, vali] indicate that the number with the id idi has a value equal to vali.
Each array contains unique ids and is sorted in ascending order by id.
Merge the two arrays into one array that is sorted in ascending order by id, respecting the following conditions:
Only ids that appear in at least one of the two arrays should be included in the resulting array.
Each id should be included only once and its value should be the sum of the values of this id in the two arrays. 
If the id does not exist in one of the two arrays, then assume its value in that array to be 0.
Return the resulting array. The returned array must be sorted in ascending order by id.
'''

def mergeArrays(nums1, nums2):
    left = 0
    right = 0
    result = []
    
    while left < len(nums1) and right < len(nums2):
        if nums1[left][0] < nums2[right][0]:
            result.append(nums1[left])
            left += 1
        elif nums1[left][0] > nums2[right][0]:
            result.append(nums2[right])
            right += 1
        else:
            result.append([nums1[left][0], nums1[left][1] + nums2[right][1]])
            left += 1
            right += 1

    while left < len(nums1):
        result.append(nums1[left])
        left += 1
        
    while right < len(nums2):
        result.append(nums2[right])
        right += 1
        
    return result

'''
Time Complexity: O(N + M)
Let N be the length of `nums1` and M be the length of `nums2`.
The algorithm uses a two-pointer approach, with one pointer for each array (`left` and `right`).
The main `while` loop iterates as long as both pointers are within the bounds of their respective arrays. In each iteration, at least one of the pointers is incremented.
The two subsequent `while` loops handle any remaining elements in either `nums1` or `nums2`.
Effectively, each element from both input arrays is visited exactly once. The operations inside the loops (comparison, addition, and appending to the result list) are all constant time operations.
Therefore, the total time complexity is linear with respect to the sum of the lengths of the input arrays, O(N + M).

Space Complexity: O(N + M)
The space complexity is determined by the `result` list, which stores the merged output.
In the worst-case scenario, all IDs in `nums1` and `nums2` are unique. In this case, the `result` list will contain `N + M` elements.
The space required for the pointers (`left`, `right`) is constant, O(1).
Thus, the space complexity is proportional to the total number of elements in the input arrays, making it O(N + M).
'''

# Test Cases
nums1 = [[1, 2], [2, 3], [4, 5]], nums2 = [[1, 4], [3, 2], [4, 1]]
print(mergeArrays(nums1, nums2)) # Output: [[1, 6], [2, 3], [3, 2], [4, 6]]

nums1 = [[1, 1], [2, 2]], nums2 = []
print(mergeArrays(nums1, nums2)) # Output: [[1, 1], [2, 2]]

nums1 = [], nums2 = [[1, 1], [2, 2]]
print(mergeArrays(nums1, nums2)) # Output: [[1, 1], [2, 2]]

nums1 = [], nums2 = []
print(mergeArrays(nums1, nums2)) # Output: []

nums1 = [[1, 5], [3, 6]], nums2 = [[2, 7], [4, 8]]
print(mergeArrays(nums1, nums2)) # Output: [[1, 5], [2, 7], [3, 6], [4, 8]]

nums1 = [[1, 1], [2, 2], [3, 3]], nums2 = [[1, 1], [2, 2], [3, 3]]
print(mergeArrays(nums1, nums2)) # Output: [[1, 2], [2, 4], [3, 6]]

nums1 = [[1, 10], [3, 20]], nums2 = [[1, 5], [2, 15], [3, 25], [4, 30]]
print(mergeArrays(nums1, nums2)) # Output: [[1, 15], [2, 15], [3, 45], [4, 30]]

nums1 = [[5, 10]], nums2 = [[5, 20]]
print(mergeArrays(nums1, nums2)) # Output: [[5, 30]]

nums1 = [[5, 10]], nums2 = [[6, 20]]
print(mergeArrays(nums1, nums2)) # Output: [[5, 10], [6, 20]]

nums1 = [[1, 1]], nums2 = [[2, 2], [3, 3], [4, 4], [5, 5]]
print(mergeArrays(nums1, nums2)) # Output: [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5]]