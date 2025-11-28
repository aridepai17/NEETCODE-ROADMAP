# MEDIAN OF TWO SORTED ARRAYS

'''
Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.
The overall run time complexity should be O(log (m+n)).
'''

'''
Algorithm and Intuition (Binary Search on Partitions):
The core idea is to find a partition in both arrays such that all elements in the "left partition" 
of the combined (conceptual) array are less than or equal to all elements in the "right partition". 
If we can find this correct partition, the median can be found in O(1) time from the boundary 
elements of these partitions.

Let's say we partition `nums1` at index `i` and `nums2` at index `j`.
- The left partition will contain `nums1[0...i-1]` and `nums2[0...j-1]`.
- The right partition will contain `nums1[i...m-1]` and `nums2[j...n-1]`.

For the median to be correctly calculated, two conditions must be met:
1.  The total number of elements in the combined left partition must be equal to half the total elements.
    - `i + j = (m + n + 1) / 2`. We use `(m+n+1)/2` to handle both even and odd total lengths correctly.
2.  Every element in the left partition must be less than or equal to every element in the right partition.
    Since the arrays are sorted, we only need to check the boundary elements:
    - `max(left_partition) <= min(right_partition)`
    - This simplifies to `nums1[i-1] <= nums2[j]` and `nums2[j-1] <= nums1[i]`.

Instead of searching for both `i` and `j`, we can use the relationship `j = (m + n + 1) / 2 - i`. 
This means if we find the correct `i`, `j` is automatically determined.

This allows us to perform a binary search for the optimal partition index `i` in one of the arrays. 
To make it more efficient, we should perform the binary search on the *smaller* of the two arrays.

Algorithm Steps:
1.  Ensure `nums1` is the shorter array: If `len(nums1) > len(nums2)`, swap them. This ensures our binary search is on the smaller range, giving a time complexity of `O(log(min(m, n)))`.
2.  Initialize variables:
    - `n1`, `n2`: lengths of the arrays.
    - `total`: `n1 + n2`.
    - `half`: The desired size of the combined left partition, calculated as `(total + 1) // 2`.
3.  Binary Search on `nums1`:
    - Set up a binary search with `left = 0` and `right = n1`. The loop will search for the correct partition index `mid1` in `nums1`.
4.  Partition and Check:
    - In each iteration, calculate `mid1` (partition for `nums1`) and `mid2` (partition for `nums2`).
    - Identify the four boundary elements: `L1`, `R1` (from `nums1`) and `L2`, `R2` (from `nums2`). Handle edge cases where a partition is empty by using `float('-inf')` or `float('inf')`.
    - Check if the partition is correct: `L1 <= R2` and `L2 <= R1`.
5.  Calculate Median or Adjust Search:
    - If the partition is correct, calculate the median based on whether `total` is even or odd.
    - If `L1 > R2`, our partition `mid1` is too large, so we search in the left half (`right = mid1 - 1`).
    - Otherwise (`L2 > R1`), `mid1` is too small, so we search in the right half (`left = mid1 + 1`).
'''

def findMedianSortedArrays(nums1, nums2):
    # Ensure nums1 is the shorter array to optimize binary search range
    if len(nums1) > len(nums2):
        nums1, nums2 = nums2, nums1
        
    n1, n2 = len(nums1), len(nums2)
    total = n1 + n2
    
    # `half` represents the number of elements needed in the left partition
    # If total is odd, the median is the single element in the left partition.
    # If total is even, the median is the average of the two middle elements.
    # By using (total + 1) // 2, we ensure that `half` always points to the
    # correct number of elements for the left partition, regardless of parity.
    # For example:
    # total = 5, half = (5+1)//2 = 3. Left partition has 3 elements.
    # total = 4, half = (4+1)//2 = 2. Left partition has 2 elements.
    half = (total + 1) // 2 
    
    # Binary search range for `mid1` (number of elements taken from nums1 for the left partition)
    # `mid1` can range from 0 (take no elements from nums1) to n1 (take all elements from nums1)
    left = 0
    right = n1
    
    while left <= right:
        # `mid1` is the partition point for nums1. It means `mid1` elements are taken from nums1.
        mid1 = (left + right) // 2
        # `mid2` is the partition point for nums2. It means `mid2` elements are taken from nums2.
        # `mid2` is derived from `half` and `mid1` to ensure the total number of elements
        # in the left partition (`mid1 + mid2`) is `half`.
        mid2 = half - mid1
        
        # L1: Last element of the left partition from nums1. If mid1 is 0, no elements from nums1, so L1 is -infinity.
        L1 = nums1[mid1 - 1] if mid1 > 0 else float('-inf')
        # L2: Last element of the left partition from nums2. If mid2 is 0, no elements from nums2, so L2 is -infinity.
        L2 = nums2[mid2 - 1] if mid2 > 0 else float('-inf')
        # R1: First element of the right partition from nums1. If mid1 is n1, all elements from nums1 are in left, so R1 is +infinity.
        R1 = nums1[mid1] if mid1 < n1 else float('inf')
        # R2: First element of the right partition from nums2. If mid2 is n2, all elements from nums2 are in left, so R2 is +infinity.
        R2 = nums2[mid2] if mid2 < n2 else float('inf')
        
        # Check if the partition is valid:
        # L1 <= R2 ensures that the largest element in the left part of nums1 is not greater than
        # the smallest element in the right part of nums2.
        # L2 <= R1 ensures the same for nums2 and nums1.
        if L1 <= R2 and L2 <= R1:
            # Valid partition found! Calculate median.
            if total % 2 == 0:
                # Even total length: median is average of two middle elements
                return (max(L1, L2) + min(R1, R2)) / 2.0
            else:
                # Odd total length: median is the single middle element (largest in the left partition)
                return float(max(L1, L2))
        elif L1 > R2:
            # L1 is too large, meaning we took too many elements from nums1.
            # Move the partition point in nums1 to the left.
            right = mid1 - 1
        else:
            # L2 is too large (or R1 is too small), meaning we took too few elements from nums1.
            # Move the partition point in nums1 to the right.
            left = mid1 + 1
            
'''
Time Complexity: O(log(min(n1, n2)))
    - The binary search is performed on the shorter array (nums1), which has length n1.
    - In each step of the binary search, we perform constant time operations (array accesses, comparisons).
    - The search space for `mid1` is `[0, n1]`, so the number of iterations is `log(n1)`.
    - Therefore, the overall time complexity is O(log(min(n1, n2))).

Space Complexity: O(1)
    - The algorithm uses a constant amount of extra space for variables like `n1`, `n2`, `total`, `half`,
    `left`, `right`, `mid1`, `mid2`, `L1`, `L2`, `R1`, `R2`.
    - No additional data structures are used that scale with the input size.
'''

# Test Cases
nums1 = [1, 3], nums2 = [2]
print(findMedianSortedArrays(nums1, nums2)) # Output: 2.0

nums1 = [1, 2], nums2 = [3, 4]
print(findMedianSortedArrays(nums1, nums2)) # Output: 2.5

nums1 = [0, 0], nums2 = [0, 0]
print(findMedianSortedArrays(nums1, nums2)) # Output: 0.0

nums1 = [], nums2 = [1]
print(findMedianSortedArrays(nums1, nums2)) # Output: 1.0

nums1 = [2], nums2 = []
print(findMedianSortedArrays(nums1, nums2)) # Output: 2.0

nums1 = [1, 3, 8, 9, 15], nums2 = [7, 11, 18, 19, 21, 25]
print(findMedianSortedArrays(nums1, nums2)) # Output: 11.0

nums1 = [23, 26, 31, 35], nums2 = [3, 5, 7, 9, 11, 16]
print(findMedianSortedArrays(nums1, nums2)) # Output: 13.5

nums1 = [1], nums2 = [2, 3, 4, 5, 6]
print(findMedianSortedArrays(nums1, nums2)) # Output: 3.5

nums1 = [1, 2, 3, 4], nums2 = [5, 6, 7, 8, 9]
print(findMedianSortedArrays(nums1, nums2)) # Output: 5.0

nums1 = [100000], nums2 = [100001]
print(findMedianSortedArrays(nums1, nums2)) # Output: 100000.5