# SPECIAL ARRAY WITH X ELEMENTS GREATER THAN OR EQUAL X

'''
You are given an array nums of non-negative integers. nums is considered special if there exists a number x such that there are exactly x numbers in nums that are greater than or equal to x.
Notice that x does not have to be an element in nums.
Return x if the array is special, otherwise, return -1. 
It can be proven that if nums is special, the value for x is unique.
'''
# Solution 1: Using Sorting 
def specialArray1(nums):
    nums.sort()
    
    for i in range(len(nums)):
        n = len(nums) - i
        if (nums[i] >= n and (i== 0 or n > nums[i - 1])):
            return n
        
    return -1

'''
Time Complexity: O(N log N)
Let N be the number of elements in the input array `nums`.
- The primary operation is sorting the array, `nums.sort()`, which takes O(N log N) time.
- After sorting, the code iterates through the array once with a `for` loop. This loop runs N times.
- The operations inside the loop (comparisons and arithmetic) are all constant time, O(1).
- Therefore, the total time complexity is dominated by the sorting step, resulting in O(N log N).

Space Complexity: O(N) or O(log N)
- The space complexity depends on the implementation of the sorting algorithm used.
- Python's Timsort, used in `sort()`, can use up to O(N) auxiliary space in the worst case for temporary storage. In many average cases, it's more efficient, using O(log N) space.
- Apart from the space used by sorting, the algorithm uses a constant amount of extra space for variables like `i` and `n`.
- Thus, the space complexity is determined by the sorting algorithm, which is typically O(N) in the worst case.
'''

# Solution 2: Using Counting Sort
def specialArray2(nums):
    n = len(nums)
    
    count = [0] * (n + 1)
    
    for num in nums:
        if num > n:
            count[n] += 1
        else:
            count[num] += 1
    
    totalSoFar = 0
    for i in range(n, 0, -1):
        totalSoFar += count[i]
        if totalSoFar == i:
            return i
        
    return -1

'''
Time Complexity: O(N)
Let N be the number of elements in the input array `nums`.
- We initialize a `count` array of size N + 1, which takes O(N) time.
- We iterate through the `nums` array once to populate the `count` array. This loop runs N times, with constant time operations inside. So, this step is O(N).
- We then iterate from N down to 1 to check for the special number `x`. This loop also runs at most N times, with constant time operations inside. This step is O(N).
- The overall time complexity is the sum of these steps, O(N) + O(N) + O(N), which simplifies to O(N).

Space Complexity: O(N)
- We create an auxiliary array `count` of size N + 1 to store the frequencies of the numbers.
- The space required for this array is directly proportional to N.
- Therefore, the space complexity of the algorithm is O(N).
'''

# Test Cases
nums1 = [3,5]
print(specialArray2(nums1)) # Output: 2

nums2 = [0,0]
print(specialArray2(nums2)) # Output: -1

nums3 = [0,4,3,0,4]
print(specialArray2(nums3)) # Output: 3

nums4 = [3,6,7,7,0]
print(specialArray2(nums4)) # Output: -1

nums5 = [100]
print(specialArray2(nums5)) # Output: 1

nums6 = [0]
print(specialArray2(nums6)) # Output: -1

nums7 = [5,5,5,5,5]
print(specialArray2(nums7)) # Output: 5

nums8 = [1,2,3,8,9]
print(specialArray2(nums8)) # Output: 3

nums9 = [1,1,1,1,1]
print(specialArray2(nums9)) # Output: -1

nums10 = [4,5,6,7,8]
print(specialArray2(nums10)) # Output: 5