# FREQUENCY OF MOST FREQUENT ELEMENT

'''
The frequency of an element is the number of times it occurs in an array.
You are given an integer array nums and an integer k. 
In one operation, you can choose an index of nums and increment the element at that index by 1.
Return the maximum possible frequency of an element after performing at most k operations.
'''

def maxFrequency(nums, k):
    left = 0
    total = 0
    result = 0
    
    for right in range(len(nums)):
        total += nums[right]
        while nums[right] * (right - left + 1) > total * k:
            total -= nums[left]
            left += 1
        result = max(result, right - left + 1)
        
    return result

'''
Time Complexity: O(n log n)
The algorithm's time complexity is dominated by an implicit requirement to sort the input array `nums`.
1. Sorting: For the sliding window logic to be correct (i.e., making all elements in the window equal to the largest element, `nums[right]`), the array must be sorted first. Sorting the array takes O(n log n) time.
2. Sliding Window: After sorting, the algorithm iterates through the array with a `right` pointer, which takes O(n) time. The `left` pointer is advanced within a `while` loop, but since it only moves forward, it will also traverse the array at most once across all iterations. Therefore, the sliding window portion of the algorithm runs in linear time, O(n).
The total time complexity is the sum of these two parts, O(n log n) + O(n), which simplifies to O(n log n).

Space Complexity: O(1) or O(log n)
The space complexity depends on the implementation of the sorting algorithm used.
- The sliding window itself only uses a few variables (`left`, `total`, `result`, `right`), which take up constant, O(1), extra space.
- The sorting process might require additional space. An in-place sorting algorithm like Heapsort would use O(1) or O(log n) auxiliary space. Python's standard `sort()` (Timsort) can use up to O(n) space in the worst case.
- Assuming an efficient in-place sort, the overall space complexity is O(1) or O(log n).
'''

# Test Cases
nums1 = [1, 2, 4], k1 = 5
print(maxFrequency(nums1, k1)) # Output: 3

nums2 = [1, 4, 8, 13], k2 = 5
print(maxFrequency(nums2, k2)) # Output: 2

nums3 = [3, 9, 6], k3 = 0
print(maxFrequency(nums3, k3)) # Output: 1

nums4 = [4, 4, 4, 4], k4 = 10
print(maxFrequency(nums4, k4)) # Output: 4

nums5 = [8, 1, 3, 5], k5 = 7
print(maxFrequency(nums5, k5)) # Output: 3

nums6 = [10, 20, 30, 40, 50], k6 = 3
print(maxFrequency(nums6, k6)) # Output: 1

nums7 = [1, 2, 3, 4, 5], k7 = 10
print(maxFrequency(nums7, k7)) # Output: 5

nums8 = [1, 1, 5, 5, 9, 9], k8 = 6
print(maxFrequency(nums8, k8)) # Output: 3

nums9 = [], k9 = 100
print(maxFrequency(nums9, k9)) # Output: 0

nums10 = [100], k10 = 100
print(maxFrequency(nums10, k10)) # Output: 1