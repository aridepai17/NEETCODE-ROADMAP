# MINIMUM LIMIT OF BALLS IN A BAG

'''
You are given an integer array nums where the ith bag contains nums[i] balls. You are also given an integer maxOperations.
You can perform the following operation at most maxOperations times:
- Take any bag of balls and divide it into two new bags with a positive number of balls.
- For example, a bag of 5 balls can become two new bags of 1 and 4 balls, or two new bags of 2 and 3 balls.
Your penalty is the maximum number of balls in a bag. You want to minimize your penalty after the operations.
Return the minimum possible penalty after performing the operations.
'''

'''
Algorithm (Binary Search):
1.  Define the search space for the minimum possible penalty (the answer).
    -   `left = 1`: The smallest possible penalty is 1.
    -   `right = max(nums)`: The largest possible penalty is the size of the biggest bag if we do no operations.
2.  Perform a binary search on this range `[left, right]`.
    -   While `left <= right`:
        a.  Calculate `mid = (left + right) // 2`. This `mid` is our candidate for the minimum penalty.
        b.  Check if it's possible to achieve this penalty `mid` using at most `maxOperations`. This is done with a helper function `canDivide(mid)`.
3.  Helper function `canDivide(penalty)`:
    a.  Initialize `operations_needed = 0`.
    b.  For each `num` in `nums`:
        - Calculate the operations required to break the bag of `num` balls into smaller bags, each with at most `penalty` balls. This is `(num - 1) // penalty`, which is equivalent to `ceil(num / penalty) - 1`.
        - Add this to `operations_needed`.
    c.  Return `True` if `operations_needed <= maxOperations`, otherwise `False`.
4.  Based on the result of `canDivide(mid)`:
    -   If `True` (it's possible), it means `mid` is a valid penalty. We try for an even smaller one, so we search the lower half: `right = mid - 1`.
    -   If `False` (not possible), we need to allow a larger penalty, so we search the upper half: `left = mid + 1`.
5.  The loop terminates when `left > right`. The value of `left` is the smallest penalty for which `canDivide` was true. Return `left`.
'''

# Brute Force Solution ( Time Limit Exceeded )
def minimumSize(nums, maxOperations):
    def canDivide(maxBalls):
        operations = 0
        for num in nums:
            operations += ((num + maxBalls - 1) // maxBalls) - 1 # Ceil - 1 operations
            if operations > maxOperations:
                return False
        return True
    
    result = 0
    for i in range(1, max(nums) + 1):
        if canDivide(i):
            return i
        
'''
Time Complexity: O(M)
- The outer loop runs from 1 to max(nums), so O(M), where M = max(nums).
- For each i, canDivide performs a loop over nums, so O(N) per check, N = len(nums).
- Therefore, total time complexity is O(N * M).

Space Complexity: O(1)
- Only constant extra space is used aside from input, so O(1) auxiliary space.
'''

# Binary Search Solution
def minimumSize(nums, maxOperations):
    def canDivide(maxBalls):
        operations = 0
        for num in nums:
            operations += ((num + maxBalls - 1) // maxBalls) - 1
            if operations > maxOperations:
                return False
        return True
    
    left = 1
    right = max(nums)
    
    while left <= right:
        mid = (left + right) // 2
        if canDivide(mid):
            right = mid - 1
        else:
            left = mid + 1
            
    return left

'''
Time Complexity: O(N log M)
- The binary search operates on the range [1, max(nums)], where M = max(nums). This takes O(log M) iterations.
- In each iteration, the `canDivide` function is called, which iterates through the `nums` array once. This takes O(N) time, where N = len(nums).
- Therefore, the total time complexity is O(N log M).

Space Complexity: O(1)
- The algorithm uses a constant amount of extra space for variables like `left`, `right`, `mid`, `operations`, and `num`.
- No additional data structures are created that scale with the input size.
- Therefore, the space complexity is O(1).
'''

# Test Cases
nums1 = [9], maxOperations1 = 2
print(minimumSize(nums1, maxOperations1)) # Output: 3

# Test Case 2
nums2 = [2, 4, 8, 2], maxOperations2 = 4
print(minimumSize(nums2, maxOperations2)) # Output: 2

# Test Case 3
nums3 = [7, 17], maxOperations3 = 2
print(minimumSize(nums3, maxOperations3)) # Output: 7

# Test Case 4
nums4 = [1, 1, 1, 1, 1], maxOperations4 = 0
print(minimumSize(nums4, maxOperations4)) # Output: 1

# Test Case 5
nums5 = [10**9], maxOperations5 = 1
print(minimumSize(nums5, maxOperations5)) # Output: 500000000

# Test Case 6
nums6 = [1, 2, 3, 4, 5], maxOperations6 = 10
print(minimumSize(nums6, maxOperations6)) # Output: 1

# Test Case 7
nums7 = [1_000_000, 1_000_000], maxOperations7 = 1
print(minimumSize(nums7, maxOperations7)) # Output: 500000

# Test Case 8
nums8 = [5, 19, 8, 1], maxOperations8 = 5
print(minimumSize(nums8, maxOperations8)) # Output: 3

# Test Case 9
nums9 = [100], maxOperations9 = 0
print(minimumSize(nums9, maxOperations9)) # Output: 100

# Test Case 10
nums10 = [2, 2, 2, 2], maxOperations10 = 2
print(minimumSize(nums10, maxOperations10)) # Output: 1