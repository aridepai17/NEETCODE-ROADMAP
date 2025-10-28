# LARGEST NUMBER

'''
Given a list of non-negative integers nums, arrange them such that they form the largest number and return it.
Since the result may be very large, so you need to return a string instead of an integer.
'''

import functools

def largestNumber(nums):
    for i in range(len(nums)):
        nums[i] = str(nums[i])
        
    def compare(a, b):
        if a + b > b + a:
            return -1
        else:
            return 1
        
    nums = sorted(nums, key = cmp_to_key(compare))
    
    result = "".join(nums)
    if result[0] == "0":
        return "0"
    return result

'''
Time Complexity: O(N * logN * K)
- Let N be the number of elements in the input array `nums`.
- Let K be the maximum number of digits for a number in the array.
- **String Conversion**: Converting N numbers to strings takes O(N * K) time, as converting a number to a string is proportional to its number of digits.
- **Custom Sort**: Python's `sorted()` function performs O(N * logN) comparisons. Each comparison, using our custom `compare` function, involves string concatenation and comparison, which takes O(K) time. Therefore, the sorting step has a complexity of O(N * logN * K).
- **String Joining**: The final `"".join(nums)` operation takes time proportional to the total length of the strings, which is at most O(N * K).
- The sorting step is the dominant factor, so the overall time complexity is O(N * logN * K).

Space Complexity: O(N * K)
- A new list of strings is created from the input numbers. The total space required to store these N strings, each with a maximum length of K, is O(N * K).
- The `sorted()` function creates a new list, but the space is dominated by the strings themselves.
- The final result string also requires up to O(N * K) space.
- Thus, the overall space complexity is O(N * K).
'''

# Test Cases
nums1 = [10, 2]
# sorted: ["2", "10"] -> "210"
print(largestNumber(nums1)) # Output: "210"

nums2 = [3, 30, 34, 5, 9]
# sorted: ["9", "5", "34", "3", "30"] -> "9534330"
print(largestNumber(nums2)) # Output: "9534330"

nums3 = [1]
print(largestNumber(nums3)) # Output: "1"

nums4 = [0, 0]
print(largestNumber(nums4)) # Output: "0"

nums5 = [111311, 1113]
# 1113111113 vs 1113111311 -> 1113111311 is larger, so "1113" comes first
# sorted: ["1113", "111311"] -> "1113111311"
print(largestNumber(nums5)) # Output: "1113111311"

nums6 = [0, 0, 0]
print(largestNumber(nums6)) # Output: "0"

nums7 = [1, 20, 23, 4, 8]
# sorted: ["8", "4", "23", "20", "1"] -> "8423201"
print(largestNumber(nums7)) # Output: "8423201"

nums8 = [4, 40, 45]
# sorted: ["45", "4", "40"] -> "45440"
print(largestNumber(nums8)) # Output: "45440"

nums9 = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
# sorted: ["9", "8", "7", "6", "5", "4", "3", "2", "1", "0"] -> "9876543210"
print(largestNumber(nums9)) # Output: "9876543210"

nums10 = [34323, 3432]
# 343234323 vs 343233432 -> 343234323 is larger, so "3432" comes first
# sorted: ["3432", "34323"] -> "343234323"
print(largestNumber(nums10)) # Output: "343234323"