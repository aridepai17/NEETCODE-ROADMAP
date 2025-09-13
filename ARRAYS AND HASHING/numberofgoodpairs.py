# NUMBER OF GOOD PAIRS

'''
Given an array of integers nums, return the number of good pairs.
A pair (i, j) is called good if nums[i] == nums[j] and i < j.
'''

def numIdenticalPairs(nums):
    freq = {}
    result = 0
    
    for num in nums:
        if num in freq:
            result += freq[num]
            freq[num] += 1
        else:
            freq[num] = 1
            
    return result

'''
Time Complexity: O(N)
Let N be the number of elements in the `nums` array.
- The algorithm iterates through the `nums` array exactly once with a single `for` loop.
- Inside the loop, all operations on the hash map (`freq`)—checking for key existence, accessing a value, and updating a value—take, on average, constant time, O(1).
- Since the loop runs N times and each iteration performs O(1) work, the total time complexity is O(N).

Space Complexity: O(N)
- The algorithm uses a hash map (`freq`) to store the frequency of each number encountered.
- In the worst-case scenario, if all elements in the `nums` array are unique, the hash map will store N key-value pairs.
- The space required by the hash map is proportional to the number of unique elements in the input array.
- Therefore, the space complexity is O(N).
'''

# Test Cases
nums1 = [1, 2, 3, 1, 1, 3]
print(numIdenticalPairs(nums1)) # Output: 4

nums2 = [1, 1, 1, 1]
print(numIdenticalPairs(nums2)) # Output: 6

nums3 = [1, 2, 3]
print(numIdenticalPairs(nums3)) # Output: 0

nums4 = []
print(numIdenticalPairs(nums4)) # Output: 0

nums5 = [1]
print(numIdenticalPairs(nums5)) # Output: 0

nums6 = [1, 1]
print(numIdenticalPairs(nums6)) # Output: 1

nums7 = [1, 1, 2, 2, 3, 3]
print(numIdenticalPairs(nums7)) # Output: 3

nums8 = [1, 2, 1, 2, 1, 2]
print(numIdenticalPairs(nums8)) # Output: 6

nums9 = [5, 5, 5, 5, 5, 5]
print(numIdenticalPairs(nums9)) # Output: 15

nums10 = [10, 20, 10, 30, 10, 40, 10]
print(numIdenticalPairs(nums10)) # Output: 6