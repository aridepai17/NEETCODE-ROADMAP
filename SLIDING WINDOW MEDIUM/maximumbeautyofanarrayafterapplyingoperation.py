# MAXIMUM BEAUTY OF AN ARRAY AFTER APPLYING OPERATION

'''
You are given a 0-indexed array nums and a non-negative integer k.
In one operation, you can do the following:
Choose an index i that hasn't been chosen before from the range [0, nums.length - 1].
Replace nums[i] with any integer from the range [nums[i] - k, nums[i] + k].
The beauty of the array is the length of the longest subsequence consisting of equal elements.
Return the maximum possible beauty of the array nums after applying the operation any number of times.
Note that you can apply the operation to each index only once.
A subsequence of an array is a new array generated from the original array by deleting some elements (possibly none) without changing the order of the remaining elements.
'''

def maximumBeauty(nums, k):
    nums.sort()
    result = 0
    left = 0
    
    for right in range(len(nums)):
        while nums[right] - nums[left] > 2 * k:
            left += 1
        result = max(result, right - left + 1)
        
    return result

'''
Time Complexity: O(N log N)
The time complexity is dominated by the initial sorting step.
1. **Sorting**: The input array `nums` is sorted, which takes O(N log N) time, where N is the length of `nums`.
2. **Sliding Window**: A single pass is made through the sorted array using two pointers, `left` and `right`. The `right` pointer moves N times, and the `left` pointer also moves at most N times in total. This makes the sliding window traversal O(N).
The overall time complexity is O(N log N) + O(N), which simplifies to O(N log N).

Space Complexity: O(1)
The space complexity is constant, as we are not using any extra data structures that scale with the input size.
1. The sorting is done in-place on the input array `nums`. While the sorting algorithm itself (Timsort in Python) might use some auxiliary space (up to O(N) in the worst case), the auxiliary space complexity of our function is typically considered O(1) as we don't create new data structures.
2. The variables `result`, `left`, and `right` occupy a constant amount of space.
Therefore, the auxiliary space complexity is O(1).
'''

# Test Cases
nums1 = [4, 6, 1, 2], k1 = 2
print(maximumBeauty(nums1, k1))  # Expected: 3

nums2 = [1, 1, 1, 1], k2 = 10
print(maximumBeauty(nums2, k2))  # Expected: 4

nums3 = [10, 2, 6, 8, 4], k3 = 3
print(maximumBeauty(nums3, k3))  # Expected: 4 ([2,4,6,8] can all become 5)

nums4 = [1, 10, 100, 1000], k4 = 1
print(maximumBeauty(nums4, k4))  # Expected: 1

nums5 = [5, 5, 5, 5, 5], k5 = 0
print(maximumBeauty(nums5, k5))  # Expected: 5

nums6 = [100, 200, 300], k6 = 50
print(maximumBeauty(nums6, k6))  # Expected: 2 ([100, 200] can become 150)

nums7 = [7, 8, 9, 10, 11], k7 = 1
print(maximumBeauty(nums7, k7))  # Expected: 3 ([7,8,9] can become 8)

nums8 = [1, 5, 10, 15], k8 = 10
print(maximumBeauty(nums8, k8))  # Expected: 4

nums9 = [4, 4, 4, 8, 8, 8], k9 = 2
print(maximumBeauty(nums9, k9))  # Expected: 6

nums10 = [0, 1, 5, 6, 10, 11], k10 = 1
print(maximumBeauty(nums10, k10))  # Expected: 2