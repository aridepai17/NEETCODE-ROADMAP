# REARRANGE ARRAY ELEMENTS BY SIGN

'''
You are given a 0-indexed integer array nums of even length consisting of an equal number of positive and negative integers.
You should return the array of nums such that the the array follows the given conditions:
Every consecutive pair of integers have opposite signs.
For all integers with the same sign, the order in which they were present in nums is preserved.
The rearranged array begins with a positive integer.
Return the modified array after rearranging the elements to satisfy the aforementioned conditions.
'''

def rearrangeArray(nums):
    pos = 0
    neg = 1
    
    result = [0] * len(nums)
    
    for num in nums:
        if num > 0:
            result[pos] = num
            pos += 2
        else:
            result[neg] = num
            neg += 2
            
    return result

'''
Time Complexity: O(N)
- The algorithm iterates through the input array `nums` exactly once using a single `for` loop.
- The loop runs N times, where N is the number of elements in `nums`.
- Inside the loop, all operations—checking the sign of the number, assigning it to the `result` array, and updating the `pos` or `neg` pointers—are performed in constant time, O(1).
- Creating the `result` array of size N also takes O(N) time.
- Since the algorithm makes a single pass through the array, the overall time complexity is linear.
- Therefore, the time complexity is O(N).

Space Complexity: O(N)
- The algorithm creates a new array `result` to store the rearranged elements.
- The size of this `result` array is the same as the input array `nums`, which is N.
- Apart from the `result` array, the algorithm uses only a few variables (`pos`, `neg`, `num`), which occupy a constant amount of space, O(1).
- The space required for the output array is the dominant factor.
- Therefore, the space complexity is O(N).
'''

# Test Cases
nums1 = [3,1,-2,-5,2,-4]
print(rearrangeArray(nums1)) # Output: [3, -2, 1, 5, 2, -4]

nums2 = [-1,-2,-3,1,2,3]
print(rearrangeArray(nums2)) # Output: [1, -1, 2, -2, 3, -3]

nums3 = [1,2,3,-1,-2,-3]
print(rearrangeArray(nums3)) # Output: [1, -1, 2, -2, 3, -3]

nums4 = [1,-1]
print(rearrangeArray(nums4)) # Output: [1, -1]

nums5 = [-1,1]
print(rearrangeArray(nums5)) # Output: [1, -1]

nums6 = [28,-41,22,-8,-37,46,35,-9,-32,40]
print(rearrangeArray(nums6)) # Output: [28, -41, 22, -8, 46, -37, 35, -9, 40, -32]

nums7 = [-1,-2,-3,-4,1,2,3,4]
print(rearrangeArray(nums7)) # Output: [1, -1, 2, -2, 3, -3, 4, -4]

nums8 = [10,20,30,40,-10,-20,-30,-40]
print(rearrangeArray(nums8)) # Output: [10, -10, 20, -20, 30, -30, 40, -40]

nums9 = [1,-1,2,-2,3,-3]
print(rearrangeArray(nums9)) # Output: [1, -1, 2, -2, 3, -3]

nums10 = [-2,3,-4,1]
print(rearrangeArray(nums10)) # Output: [3, -2, 1, -4]