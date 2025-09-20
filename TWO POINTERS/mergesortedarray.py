# MERGE SORTED ARRAY

'''
You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, representing the number of elements in nums1 and nums2 respectively.
Merge nums1 and nums2 into a single array sorted in non-decreasing order.
The final sorted array should not be returned by the function, 
but instead be stored inside the array nums1. To accommodate this, nums1 has a length of m + n, 
where the first m elements denote the elements that should be merged, and the last n elements are set to 0 and should be ignored. 
nums2 has a length of n.
'''

def merge(nums1, m, nums2, n):
    last = m + n - 1
    
    while m > 0 and n > 0:
        if nums1[m - 1] > nums2[n - 1]:
            nums1[last] = nums1[m - 1]
            m -= 1
        else:
            nums1[last] = nums2[n - 1]
            n -= 1
        last -= 1
        
    while n > 0:
        nums1[last] = nums2[n - 1]
        n -= 1
        last -= 1

'''
Time Complexity: O(m + n)
The algorithm uses a three-pointer approach. One pointer (`last`) is for the last index of the merged array `nums1`, and the other two pointers (`m-1` and `n-1`) are for the last elements of the initial parts of `nums1` and `nums2`, respectively.
In each iteration of the `while` loops, we perform a comparison and an assignment, and then decrement at least one of the pointers.
Every element from the initial `m` elements of `nums1` and `n` elements of `nums2` is visited and placed exactly once.
The total number of operations is therefore proportional to the total number of elements being merged, which is `m + n`.

Space Complexity: O(1)
The algorithm modifies the `nums1` array in-place.
It uses only a few variables to store pointers (`last`, `m`, `n`), which occupy a constant amount of extra space.
The space required does not scale with the size of the input arrays.
Thus, the space complexity is O(1).
'''

# Test Cases
nums1 = [1,2,3,0,0,0], m1 = 3, nums2 = [2,5,6], n1 = 3
print(merge(nums1, m1, nums2, n1)) # Output: [1, 2, 2, 3, 5, 6]

nums3 = [1], m2 = 1, nums4 = [], n2 = 0
print(merge(nums3, m2, nums4, n2)) # Output: [1]

nums5 = [0], m3 = 0, nums6 = [1], n3 = 1
print(merge(nums5, m3, nums6, n3)) # Output: [1]

nums7 = [1,2,3], m4 = 3, nums8 = [], n4 = 0
print(merge(nums7, m4, nums8, n4)) # Output: [1,2,3]

nums9 = [1,2,3,0,0,0], m5 = 3, nums10 = [4,5,6], n5 = 3
print(merge(nums9, m5, nums10, n5)) # Output: [1,2,3,4,5,6]

nums11 = [4,5,6,0,0,0], m6 = 3, nums12 = [1,2,3], n6 = 3
print(merge(nums11, m6, nums12, n6)) # Output: [1,2,3,4,5,6]

nums13 = [1,3,5,0,0,0], m7 = 3, nums14 = [2,4,6], n7 = 3
print(merge(nums13, m7, nums14, n7)) # Output: [1,2,3,4,5,6]

nums15 = [2,2,3,0,0,0], m8 = 3, nums16 = [1,5,6], n8 = 3
print(merge(nums15, m8, nums16, n8)) # Output: [1,2,2,3,5,6]

nums17 = [-1,0,0,3,3,0,0,0,0], m9 = 5, nums18 = [1,2,2,4], n9 = 4
print(merge(nums17, m9, nums18, n9)) # Output: [-1,0,0,1,2,2,3,3,4]

nums19 = [0,0,0], m10 = 0, nums20 = [2,5,6], n10 = 3
print(merge(nums19, m10, nums20, n10)) # Output: [2,5,6]

nums21 = [], m11 = 0, nums22 = [], n11 = 0
print(merge(nums21, m11, nums22, n11)) # Output: []