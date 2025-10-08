# MINIMUM DIFFERENCE BETWEEN HIGHEST AND LOWEST K SCORES

'''
You are given a 0-indexed integer array nums, where nums[i] represents the score of the ith student. 
You are also given an integer k.
Pick the scores of any k students from the array so that the difference between the highest and the lowest of the k scores is minimized.
Return the minimum possible difference.
'''

def minimumDifference(nums, k):
    nums.sort()
    left = 0
    right = k - 1
    minimum = float('inf')
    
    while right < len(nums):
        minimum = min(minimum, nums[right] - nums[left])
        left += 1
        right += 1
        
    return minimum

'''
Time Complexity: O(n log n)
The dominant operation is sorting the input array `nums`, which takes O(n log n) time, where n is the number of elements in the array.
The sliding window part of the algorithm iterates through the sorted array once, which takes O(n) time.
Therefore, the total time complexity is O(n log n).

Space Complexity: O(1) or O(n)
The space complexity depends on the implementation of the sorting algorithm used.
If the sorting is done in-place, the space complexity is O(1) because we only use a few variables to keep track of the window and the minimum difference.
However, Python's built-in sort (Timsort) can use up to O(n) space in the worst case for temporary storage.
If we consider the space used by the sorting algorithm, the space complexity is O(n).

'''

# Test Cases
nums1 = [90], k1 = 1
print(minimumDifference(nums1, k1)) # Output: 0

nums2 = [9, 4, 1, 7], k2 = 2
print(minimumDifference(nums2, k2)) # Output: 2

nums3 = [87063, 61094, 44530, 21297, 95857, 93551, 9918], k3 = 6
print(minimumDifference(nums3, k3)) # Output: 74560

nums4 = [10, 20, 30, 40, 50], k4 = 5
print(minimumDifference(nums4, k4)) # Output: 40

nums5 = [-5, 0, 5, 10], k5 = 3
print(minimumDifference(nums5, k5)) # Output: 10

nums6 = [7, 7, 7, 7], k6 = 3
print(minimumDifference(nums6, k6)) # Output: 0

nums7 = [1, 5, 9, 12, 15, 18, 20, 22], k7 = 4
print(minimumDifference(nums7, k7)) # Output: 7

nums8 = [100, 20, 30, 10, 50, 40, 41], k8 = 3
print(minimumDifference(nums8, k8)) # Output: 10

nums9 = [10, 20, 5], k9 = 1
print(minimumDifference(nums9, k9)) # Output: 0

nums10 = [3, 8, 1, 9, 4], k10 = 4
print(minimumDifference(nums10, k10)) # Output: 6