# SPECIAL ARRAY 1

'''
An array is considered special if the parity of every pair of adjacent elements is different. 
In other words, one element in each pair must be even, and the other must be odd.
You are given an array of integers nums. Return true if nums is a special array, otherwise, return false.
'''

def specialArray(nums):
    for i in range(1, len(nums)):
        if nums[i] & 1 == nums[i - 1] & 1:
            return False
    return True

'''
Time Complexity: O(N)
Let N be the length of the `nums` array.
- The algorithm iterates through the array with a single `for` loop, from the second element (index 1) to the end.
- In the worst-case scenario (if the array is special), the loop will run N - 1 times.
- Inside the loop, all operations are constant time, O(1):
  - Accessing array elements (`nums[i]`, `nums[i-1]`).
  - Performing a bitwise AND operation (`& 1`) to check the parity (even or odd).
  - Comparing the two parity results.
- Since the loop runs a maximum of N - 1 times with constant time operations in each iteration, the overall time complexity is O(N).

Space Complexity: O(1)
- The algorithm uses a fixed amount of extra space.
- The loop variable `i` is the only additional space used.
- No new data structures that scale with the input size are created.
- Therefore, the space complexity is constant, O(1).
'''

# Test Cases
nums1 = [1]
print(specialArray(nums1))  # Output: True

nums2 = [2, 1, 4]
print(specialArray(nums2))  # Output: True

nums3 = [4, 3, 2, 1]
print(specialArray(nums3))  # Output: True

nums4 = [2, 1, 3, 4]
print(specialArray(nums4))  # Output: False (1 and 3 have the same odd parity)

nums5 = [1, 2, 4, 5]
print(specialArray(nums5))  # Output: False (2 and 4 have the same even parity)

nums6 = [1, 0, 1, 0]
print(specialArray(nums6))  # Output: True (0 is even)

nums7 = [1, 1, 1, 1]
print(specialArray(nums7))  # Output: False

nums8 = [2, 4, 6, 8]
print(specialArray(nums8))  # Output: False

nums9 = []
print(specialArray(nums9))  # Output: True

nums10 = [2, 7]
print(specialArray(nums10)) # Output: True