# INTERSECTION OF TWO ARRAYS

'''
Given two integer arrays nums1 and nums2, return an array of their intersection. 
Each element in the result must be unique and you may return the result in any order.
The intersection of two arrays is defined as the set of elements that are present in both arrays.
'''
# Solution 1: Using HashSet
def intersection1(nums1, nums2):
    hashSet = set(nums1)
    intersectionSet = set()
    
    for num in nums2:
        if num in hashSet:
            intersectionSet.add(num)
            
    return list(intersectionSet)

'''
Time Complexity: O(m + n)
- Let m be the number of elements in `nums1` and n be the number of elements in `nums2`.
- Creating a hash set from `nums1` takes O(m) time on average, as each element is inserted into the set.
- The algorithm then iterates through each of the n elements in `nums2`.
- For each element in `nums2`, checking for its presence in the hash set (`num in hashSet`) is an average O(1) operation.
- Adding an element to the `intersectionSet` is also an average O(1) operation.
- The total time complexity is the sum of these operations: O(m) for set creation + O(n) for the loop, which results in O(m + n).

Space Complexity: O(m + n)
- The algorithm uses two sets to store elements.
- `hashSet` stores the unique elements of `nums1`, which can take up to O(m) space in the worst case (if all elements are unique).
- `intersectionSet` stores the common elements found. In the worst case, this set can contain up to `min(m, n)` elements.
- The total space required is the sum of the space for both sets, which is O(m + min(m, n)). This can be simplified to O(m + n) as an upper bound.
'''

# Solution 2: Using One-Liner
def intersection2(nums1, nums2):
    return list(set(nums1) & set(nums2))

'''
Time Complexity: O(m + n)
- Let m be the length of `nums1` and n be the length of `nums2`.
- `set(nums1)`: Creating a set from the list `nums1` takes O(m) time on average.
- `set(nums2)`: Creating a set from the list `nums2` takes O(n) time on average.
- `&`: The intersection operation on the two sets takes time proportional to the sum of their sizes, O(m + n) in the worst case, but often optimized to O(min(m, n)).
- `list()`: Converting the resulting set to a list takes time proportional to the size of the intersection, which is at most `min(m, n)`.
- The overall time complexity is dominated by the creation of the two sets, making it O(m + n).

Space Complexity: O(m + n)
- The algorithm creates two sets to store the unique elements of `nums1` and `nums2`.
- `set(nums1)` can take up to O(m) space.
- `set(nums2)` can take up to O(n) space.
- An intermediate set is also created for the result of the intersection.
- The total space complexity is determined by the space required for these sets, which is O(m + n).
'''

# Test Cases
nums1 = [1,2,2,1], nums2 = [2,2]
print(intersection2(nums1, nums2)) # Output: [2]

nums1 = [4,9,5], nums2 = [9,4,9,8,4]
print(intersection2(nums1, nums2)) # Output: [9, 4]

nums1 = [1,2,3], nums2 = [4,5,6]
print(intersection2(nums1, nums2)) # Output: []

nums1 = [], nums2 = [1,2]
print(intersection2(nums1, nums2)) # Output: []

nums1 = [1,2,3,4], nums2 = [2,4]
print(intersection2(nums1, nums2)) # Output: [2, 4]

nums1 = [1,1,1], nums2 = [1,1]
print(intersection2(nums1, nums2)) # Output: [1]

nums1 = [1,2,3], nums2 = [3,2,1]
print(intersection2(nums1, nums2)) # Output: [1, 2, 3]

nums1 = [0,0,0], nums2 = [1,1,1]
print(intersection2(nums1, nums2)) # Output: []

nums1 = [-1, -5, 2], nums2 = [0, 3, -5]
print(intersection2(nums1, nums2)) # Output: [-5]

nums1 = [1000, 2000], nums2 = [2000, 3000]
print(intersection2(nums1, nums2)) # Output: [2000]