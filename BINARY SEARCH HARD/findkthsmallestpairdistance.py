# FIND KTH SMALLEST PAIR DISTANCE

'''
The distance of a pair of integers a and b is defined as the absolute difference between a and b.
Given an integer array nums and an integer k, return the kth smallest distance among all the pairs nums[i] and nums[j] where 0 <= i < j < nums.length.
'''

'''
Algorithm and Intuition (Binary Search on the Answer):
Intuition:
The problem asks for the kth smallest distance. This is a classic "binary search on the answer" problem.
If we can count how many pairs have a distance less than or equal to some value `X`, we can use binary search.
Let `countPairs(distance)` be a function that returns the number of pairs `(nums[i], nums[j])` such that `abs(nums[i] - nums[j]) <= distance`.
This function is monotonic: if `countPairs(X)` is `C`, then `countPairs(Y)` for `Y > X` will be `>= C`.
This monotonicity allows us to binary search for the smallest `distance` `X` such that `countPairs(X) >= k`.

Algorithm Steps:
1. Sort the input array `nums`. This is crucial because it allows us to efficiently count pairs with a given maximum distance using a two-pointer approach.
2. Define the search space for the `distance`:
   - `left = 0`: The minimum possible distance between any two numbers.
   - `right = nums[-1] - nums[0]`: The maximum possible distance between any two numbers in the sorted array.
3. Implement the `helper(distance)` function (which is `countPairs(distance)`):
   - Initialize `count = 0` and `left_ptr = 0`.
   - Iterate `right_ptr` from `0` to `n-1`:
     - While `nums[right_ptr] - nums[left_ptr] > distance`, increment `left_ptr`.
     - The number of pairs `(nums[left_ptr], nums[right_ptr]), ..., (nums[right_ptr-1], nums[right_ptr])` all have a distance less than or equal to `distance`. This count is `right_ptr - left_ptr`. Add this to `count`.
   - Return `count`.
4. Perform binary search on the range `[left, right]` for the `distance`:
   - If `helper(mid)` (number of pairs with distance <= `mid`) is `>= k`, it means `mid` could be our answer, or we might find an even smaller distance. So, we try `right = mid`.
   - If `helper(mid)` is `< k`, it means `mid` is too small; we need a larger distance to get at least `k` pairs. So, we try `left = mid + 1`.
5. The loop terminates when `left == right`. This `left` (or `right`) value is the smallest distance `X` such that there are at least `k` pairs with distance `<= X`. Return `left`.
'''

def smallestDistancePair(nums, k):
    nums.sort()
    n = len(nums)
    
    def helper(distance):
        left = 0
        result = 0
        
        for right in range(n):
            while nums[right] - nums[left] > distance:
                left += 1
            result += right - left
            
        return result
    
    left = 0
    right = nums[-1] - nums[0]
    
    while left < right:
        mid = left + (right - left) // 2
        pairs = helper(mid)
        if pairs >= k:
            right = mid
        else:
            left = mid + 1
            
    return left

'''
Time Complexity: O(N log N + N log D)
    1. Sorting the array: O(N log N)
    2. Binary search for the distance: O(log D) iterations, where D is the maximum possible distance (nums[-1] - nums[0]).
    3. Inside each binary search iteration, the `helper` function is called:
        - The `helper` function uses a two-pointer approach. The `right` pointer iterates from 0 to N-1.
        - The `left` pointer also iterates, but it never goes backward. In total, `left` pointer makes at most N increments.
        - So, the `helper` function takes O(N) time.
    - Combining these: O(N log N) for sort + O(N * log D) for binary search.
    - Overall: O(N log N + N log D)

Space Complexity: O(1) or O(log N) or O(N)
    - O(1) if the sorting algorithm used is in-place (e.g., Heapsort).
    - O(log N) if the sorting algorithm uses recursion stack space (e.g., Quicksort).
    - O(N) if the sorting algorithm uses auxiliary space (e.g., Mergesort).
    - The rest of the algorithm uses a constant amount of extra space for variables.
    - Since Python's `list.sort()` is Timsort, which is O(N) in worst case for auxiliary space,
    the space complexity is effectively O(N) due to sorting.
'''

# Test Cases
nums1 = [1,3,1], k1 = 1
print(smallestDistancePair(nums1, k1)) # Output: 0

nums2 = [1, 6, 1], k2 = 3
print(smallestDistancePair(nums2, k2)) # Output: 5

nums3 = [1, 1, 1], k3 = 2
print(smallestDistancePair(nums3, k3)) # Output: 0

nums4 = [1, 3, 6, 7, 9], k4 = 5
print(smallestDistancePair(nums4, k4)) # Output: 3

nums5 = [62, 100, 4], k5 = 2
print(smallestDistancePair(nums5, k5)) # Output: 38

nums6 = [9, 10, 7, 10, 6, 1, 5, 4], k6 = 8
print(smallestDistancePair(nums6, k6)) # Output: 2

nums7 = [1, 1, 1, 3, 3], k7 = 4
print(smallestDistancePair(nums7, k7)) # Output: 0

nums8 = [1, 2], k8 = 1
print(smallestDistancePair(nums8, k8)) # Output: 1

nums9 = [1, 6, 1, 6], k9 = 6
print(smallestDistancePair(nums9, k9)) # Output: 5

nums10 = [1, 3, 7, 8, 10, 13], k10 = 10
print(smallestDistancePair(nums10, k10)) # Output: 6