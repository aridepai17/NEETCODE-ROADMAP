# CHECK IF ARRAY IS SORTED AND ROTATED

'''
Given an array nums, return true if the array was originally sorted in non-decreasing order, then rotated some number of positions (including zero). 
Otherwise, return false.
There may be duplicates in the original array.
Note: An array A rotated by x positions results in an array B of the same length such that B[i] == A[(i+x) % A.length] for every valid index i.
'''

def check(nums):
    n = len(nums)
    count = 1
    
    if n == 1:
        return True
    
    for i in range(1, n + n):
        if nums[(i - 1) % n] <= nums[i % n]:
            count += 1
        else:
            count = 1
        if count == n:
            return True
        
    return False

'''
Time Complexity: O(N)
Let N be the length of the `nums` array.
- The algorithm iterates through the array conceptually twice. The `for` loop runs from `1` up to `2*N - 1`.
- In the worst-case scenario, the loop will run `2*N - 1` times before returning.
- Inside the loop, all operations are constant time, O(1):
  - Accessing array elements using the modulo operator (`nums[(i - 1) % n]`).
  - Performing a comparison (`<=`).
  - Incrementing or resetting the `count` variable.
- Since the loop runs a maximum of `2*N - 1` times with constant time operations in each iteration, the overall time complexity is O(N).

Space Complexity: O(1)
- The algorithm uses a fixed amount of extra space for variables like `n`, `count`, and the loop index `i`.
- The amount of memory used does not depend on the size of the input array.
- No new data structures that scale with the input size are created.
- Therefore, the space complexity is constant, O(1).
'''

# Test Cases
nums1 = [3, 4, 5, 1, 2]
print(check(nums1)) # Output: True

nums2 = [2, 1, 3, 4]
print(check(nums2)) # Output: False

nums3 = [1, 2, 3]
print(check(nums3)) # Output: True

nums4 = [1, 1, 1]
print(check(nums4)) # Output: True

nums5 = [2, 1]
print(check(nums5)) # Output: True

nums6 = [7, 9, 1, 2, 3]
print(check(nums6)) # Output: True

nums7 = [1]
print(check(nums7)) # Output: True

nums8 = [6, 5, 4, 3, 2, 1]
print(check(nums8)) # Output: False

nums9 = [3, 1, 2, 4]
print(check(nums9)) # Output: False

nums10 = [2, 2, 3, 1]
print(check(nums10)) # Output: True