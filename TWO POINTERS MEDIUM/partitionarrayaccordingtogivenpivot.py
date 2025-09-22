# PARTITION ARRAY ACCORDING TO GIVEN PIVOT

'''
You are given a 0-indexed integer array nums and an integer pivot. Rearrange nums such that the following conditions are satisfied:
Every element less than pivot appears before every element greater than pivot.
Every element equal to pivot appears in between the elements less than and greater than pivot.
The relative order of the elements less than pivot and the elements greater than pivot is maintained.
More formally, consider every pi, pj where pi is the new position of the ith element and pj is the new position of the jth element. 
If i < j and both elements are smaller (or larger) than pivot, then pi < pj.
Return nums after the rearrangement.
'''

def pivotArray(nums, pivot):
    result = [0] * len(nums)
    left = 0
    
    for num in nums:
        if num < pivot:
            result[left] = num
            left += 1
            
    for num in nums:
        if num == pivot:
            result[left] = num
            left += 1
            
    for num in nums:
        if num > pivot:
            result[left] = num
            left += 1
            
    return result

'''
Time Complexity: O(N)
We iterate through the input array `nums` three times. Each pass takes O(N) time, where N is the number of elements in `nums`.
The total time complexity is O(N) + O(N) + O(N) = O(N).

Space Complexity: O(N)
We create a new array `result` of the same size as the input array `nums`.
This requires O(N) additional space to store the rearranged elements.
'''

# Test Cases
nums1 = [9,12,5,10,14,3,10], pivot1 = 10
print(pivotArray(nums1, pivot1)) # Output: [9, 5, 3, 10, 10, 12, 14]

nums2 = [-3, 4, 3, 2], pivot2 = 2
print(pivotArray(nums2, pivot2)) # Output: [-3, 2, 4, 3]

nums3 = [5, 2, 8, 1, 9], pivot3 = 1
print(pivotArray(nums3, pivot3)) # Output: [1, 5, 2, 8, 9]

nums4 = [5, 2, 8, 1, 9], pivot4 = 9
print(pivotArray(nums4, pivot4)) # Output: [5, 2, 8, 1, 9]

nums5 = [7, 7, 7, 7], pivot5 = 7
print(pivotArray(nums5, pivot5)) # Output: [7, 7, 7, 7]

nums6 = [1, 2, 4, 5], pivot6 = 3
print(pivotArray(nums6, pivot6)) # Output: [1, 2, 4, 5]

nums7 = [], pivot7 = 100
print(pivotArray(nums7, pivot7)) # Output: []

nums8 = [10], pivot8 = 10
print(pivotArray(nums8, pivot8)) # Output: [10]

nums9 = [1, 2, 5, 5, 8, 9], pivot9 = 5
print(pivotArray(nums9, pivot9)) # Output: [1, 2, 5, 5, 8, 9]

nums10 = [12, 11, 10, 10, 4, 2], pivot10 = 10
print(pivotArray(nums10, pivot10)) # Output: [4, 2, 10, 10, 12, 11]
