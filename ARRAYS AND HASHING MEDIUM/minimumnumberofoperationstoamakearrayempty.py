# MINIMUM NUMBER OF OPERATIONS TO MAKE ARRAY EMPTY

'''
You are given a 0-indexed array nums consisting of positive integers.
There are two types of operations that you can apply on the array any number of times:
- Choose two elements with equal values and delete them from the array.
- Choose three elements with equal values and delete them from the array.
Return the minimum number of operations required to make the array empty, or -1 if it is not possible
'''

def minOperations(nums):
    hashMap = {}
    result = 0
    
    for num in nums:
        hashMap[num] = hashMap.get(num, 0) + 1
        
    for value in hashMap.items():
        if value == 1:
            return -1
        result += (value + 2) // 3 # result += math.ceil(value / 3)
        
    return result

'''
Time Complexity: O(N)
- Let N be the number of elements in the input array `nums`.
- The first loop iterates through the `nums` array once to build the frequency map (`hashMap`). This takes O(N) time, as each hash map operation (get and assignment) is O(1) on average.
- The second loop iterates through the values in the `hashMap`. In the worst case, if all elements are unique, the hash map will have N entries. However, more typically, it will have fewer entries. Let's say there are K unique elements, where K ≤ N. This loop runs K times, and each operation inside (comparison and arithmetic) is O(1). This step takes O(K) time.
- Since K ≤ N, the overall time complexity is O(N) + O(K) = O(N).

Space Complexity: O(N)
- The `hashMap` stores the frequency of each unique element in `nums`. In the worst case, if all elements are unique, the hash map will contain N key-value pairs, requiring O(N) space.
- Other variables (`result`, `num`, `value`) use constant space O(1).
- Therefore, the overall space complexity is O(N).
'''

# Test Cases
nums1 = [2, 3, 3, 2, 2, 4, 2, 3, 4]
print(minOperations(nums1)) # Output: 4

nums2 = [1, 1, 1, 1]
print(minOperations(nums2)) # Output: 2

nums3 = [5, 5, 5, 5, 5]
print(minOperations(nums3)) # Output: 2

nums4 = [4]
print(minOperations(nums4)) # Output: -1

nums5 = [6, 6, 6, 6, 6, 6]
print(minOperations(nums5)) # Output: 2

nums6 = [7, 7, 8, 8, 8, 8, 8, 8]
print(minOperations(nums6)) # Output: 3

nums7 = [9, 9, 9, 10, 10, 10, 10]
print(minOperations(nums7)) # Output: 3

nums8 = [11, 11, 11, 11, 11, 11, 11]
print(minOperations(nums8)) # Output: 3

nums9 = [12, 13, 12, 13, 12, 13]
print(minOperations(nums9)) # Output: 2

nums10 = [14, 14, 15, 15, 15]
print(minOperations(nums10)) # Output: 2