# COUNT THE NUMBER OF FAIR PAIRS

'''
Given a 0-indexed integer array nums of size n and two integers lower and upper, return the number of fair pairs.
A pair (i, j) is fair if:
- 0 <= i < j < n, and
- lower <= nums[i] + nums[j] <= upper
'''
'''
Algorithm and Intuition (Sorting + Binary Search):
Intuition:
A brute-force approach would be to check every possible pair (i, j), which would be O(N^2) and likely too slow.
We can optimize this by sorting the array first. Sorting allows us to use more efficient methods to find pairs.
For each element `nums[i]`, the condition `lower <= nums[i] + nums[j] <= upper` can be rearranged to find a target range for `nums[j]`:
`lower - nums[i] <= nums[j] <= upper - nums[i]`.
So, for each `nums[i]`, we need to count how many elements `nums[j]` (with `j > i`) fall into the range `[lower - nums[i], upper - nums[i]]`.
Since the array is sorted, we can use binary search to quickly count the number of elements within this range.

Algorithm Steps:
1. Sort the `nums` array. This is crucial for using binary search.
2. Initialize a `result` counter to 0.
3. Iterate through the array with index `i` from `0` to `n-1`.
4. For each `nums[i]`, calculate the required range for its partner `nums[j]`:
   - `low = lower - nums[i]`
   - `up = upper - nums[i]`
5. We need to count how many elements in the subarray `nums[i+1:]` are between `low` and `up` (inclusive). This can be calculated as:
   (count of elements <= `up`) - (count of elements < `low`).
6. Use two binary searches on the subarray `nums[i+1:]` to find these counts. The difference gives the number of valid partners for `nums[i]`.
7. Add this count to the `result`.
8. After iterating through all `i`, return the total `result`.
'''

def countFairPairs(nums, lower, upper):
    def binarySearch(left, right, target):
        # Return largest index, where nums[index] < target
        while left <= right:
            mid = (left + right) // 2 # left + (right - left) // 2
            if nums[mid] >= target:
                right = mid - 1
            else:
                left = mid + 1
                
        return right
    
    nums.sort()
    result = 0
    
    for i in range(len(nums)):
        low = lower - nums[i]
        up = upper - nums[i]
        result += (
            binarySearch(i + 1, len(nums) - 1, up + 1) -
            binarySearch(i + 1, len(nums) - 1, low)
        )
        
    return result

'''
Time Complexity: O(N log N)
- Sorting `nums`: O(N log N), where N is the length of the `nums` array.
- The main loop iterates `N` times (for each `i` from `0` to `N-1`).
- Inside the loop, two calls to `binarySearch` are made.
- Each `binarySearch` call operates on a subarray of `nums` of size at most `N`.
- A binary search on an array of size `N` takes O(log N) time.
- Therefore, the total time complexity for the loop is O(N log N).
- Combining the sorting and the loop, the overall time complexity is O(N log N + N log N) = O(N log N).

Space Complexity: O(log N) or O(N)
- Sorting `nums`: The space complexity of sorting depends on the specific algorithm used by Python's `sort()` method.
  - Timsort (Python's default sort) uses O(N) space in the worst case, but can be O(log N) in the best case.
- `binarySearch` function: Uses a constant amount of extra space for variables (`left`, `right`, `mid`, `target`). This is O(1).
- The `result` variable also uses O(1) space.
- Therefore, the dominant factor for space complexity comes from the sorting process, which is typically O(N) in the worst case for Timsort.
'''

# Test Cases
nums1 = [0,1,7,4,4,5], lower1 = 3, upper1 = 6
print(countFairPairs(nums1, lower1, upper1)) # Output: 6

nums2 = [1,7,9,2,5], lower2 = 11, upper2 = 11
print(countFairPairs(nums2, lower2, upper2)) # Output: 1

nums3 = [1,2,3,4,5,6], lower3 = 7, upper3 = 10
print(countFairPairs(nums3, lower3, upper3)) # Output: 6

nums4 = [0,0,0,0,0], lower4 = 0, upper4 = 0
print(countFairPairs(nums4, lower4, upper4)) # Output: 10

# Additional Test Cases
nums5 = [1, 2, 3], lower5 = 3, upper5 = 4
print(countFairPairs(nums5, lower5, upper5)) # Output: 2 (pairs: (1,2), (1,3))

nums6 = [1, 1, 1, 1], lower6 = 2, upper6 = 2
print(countFairPairs(nums6, lower6, upper6)) # Output: 6 (all pairs sum to 2)

nums7 = [10, 20, 30, 40], lower7 = 50, upper7 = 60
print(countFairPairs(nums7, lower7, upper7)) # Output: 2 (pairs: (20,30), (20,40))

nums8 = [0, 0, 0], lower8 = 1, upper8 = 1
print(countFairPairs(nums8, lower8, upper8)) # Output: 0

nums9 = [5, 5, 5, 5, 5], lower9 = 10, upper9 = 10
print(countFairPairs(nums9, lower9, upper9)) # Output: 10 (all pairs sum to 10)

nums10 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], lower10 = 1, upper10 = 20
print(countFairPairs(nums10, lower10, upper10)) # Output: 45 (all possible pairs)