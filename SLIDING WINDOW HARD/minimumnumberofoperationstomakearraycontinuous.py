# MINIMUM NUMBER OF OPERATIONS TO MAKE ARRAY CONTINUOUS

'''
You are given an integer array nums. In one operation, you can replace any element in nums with any integer.
nums is considered continuous if both of the following conditions are fulfilled:
All elements in nums are unique.
The difference between the maximum element and the minimum element in nums equals nums.length - 1.
For example, nums = [4, 2, 5, 3] is continuous, but nums = [1, 2, 3, 5, 6] is not continuous.
Return the minimum number of operations to make nums continuous.
'''

def minOperations(nums):
    n = len(nums)
    nums = sorted(set(nums))
    m = len(nums)
    minimum = n
    right = 0
    
    for left in range(m):
        while right < m and nums[right] < nums[left] + n:
            right += 1
        window = right - left
        operations = window - n
        minimum = min(minimum, operations)
        
    return minimum

'''
Time Complexity: O(n log n)
The algorithm can be broken down into two main parts: preprocessing and the sliding window.
1. Preprocessing:
   - `set(nums)`: Creating a set from the input list `nums` to get unique elements takes O(n) time, where n is the number of elements in the original `nums`.
   - `sorted(...)`: Sorting the unique elements takes O(m log m) time, where m is the number of unique elements. In the worst case, all elements are unique (m = n), so this step is O(n log n).
   This preprocessing part has a total time complexity of O(n + m log m), which is dominated by O(n log n).

2. Sliding Window:
   - The code then uses a two-pointer (sliding window) approach on the sorted unique array of size m.
   - The `left` pointer iterates from the beginning to the end of the array (m iterations).
   - The `right` pointer also moves from left to right and never resets.
   - In total, both `left` and `right` pointers traverse the array of size m at most once. Therefore, the time complexity of the sliding window part is O(m).

Combining both parts, the total time complexity is O(n log n) + O(m). Since m <= n, the overall time complexity is dominated by the sorting step, resulting in O(n log n).

Space Complexity: O(n)
- `set(nums)`: A new set is created to store the unique elements. In the worst case, if all elements in `nums` are unique, this set will have a size of n, requiring O(n) space.
- `sorted(...)`: The `sorted` function creates a new list from the set to store the sorted elements, which also requires O(m) space, or O(n) in the worst case.
- The other variables (`n`, `m`, `minimum`, `right`, `left`, `window`, `operations`) use a constant amount of extra space, O(1).
- Therefore, the dominant factor for space is the storage of the unique sorted array, making the space complexity O(n).
'''

# Test Cases
nums1 = [4,2,5,3]
print(minOperations(nums1)) # Output: 0

nums2 = [1, 2, 3, 5, 6]
print(minOperations(nums2)) # Output: 1

nums3 = [1, 10, 100, 1000]
print(minOperations(nums3)) # Output: 3

nums4 = [8, 5, 9, 9, 8, 4]
print(minOperations(nums4)) # Output: 2

nums5 = [1, 1, 1, 1, 1]
print(minOperations(nums5)) # Output: 4

nums6 = [100, 101, 102]
print(minOperations(nums6)) # Output: 0

nums7 = [42, 44, 45, 46, 47]
print(minOperations(nums7)) # Output: 1

nums8 = []
print(minOperations(nums8)) # Output: 0

nums9 = [10]
print(minOperations(nums9)) # Output: 0

nums10 = [1, 100, 200, 201, 202, 203]
print(minOperations(nums10)) # Output: 2