# COUNT NUMBER OF BAD PAIRS

'''
You are given a 0-indexed integer array nums. 
A pair of indices (i, j) is a bad pair if i < j and j - i != nums[j] - nums[i].
Return the total number of bad pairs in nums.
'''

def countBadPairs(nums):
    goodPairs = 0
    hashMap = {}
    n = len(nums)
    
    for i in range(n):
        currentValue = nums[i] - i
        if currentValue in hashMap:
            goodPairs += hashMap[currentValue]
        hashMap[currentValue] = hashMap.get(currentValue, 0) + 1
        
    totalPairs = (n * (n - 1)) // 2
    
    return totalPairs - goodPairs

'''
Time Complexity: O(N)
- Let N be the number of elements in the input array `nums`.
- The algorithm iterates through the array once in a single for loop, which takes O(N) time.
- Within the loop, dictionary operations (checking if a key exists and updating the value) are O(1) on average due to hash table implementation.
- Therefore, the overall time complexity is O(N).

Space Complexity: O(N)
- The space complexity is determined by the additional space used by the hashMap dictionary.
- In the worst-case scenario, all elements in the array have different values of `nums[i] - i`, meaning the dictionary will store N unique keys.
- Therefore, the space required for the dictionary is O(N).
- The other variables (`goodPairs`, `n`, `currentValue`, `i`) use constant space O(1).
- The dominant factor is the hashMap, so the overall space complexity is O(N).
'''

# Test Cases
nums1 = [4, 1, 3, 3]
print(countBadPairs(nums1)) # Output: 5

nums2 = [1, 2, 3, 4, 5]
print(countBadPairs(nums2)) # Output: 0

nums3 = [1, 1, 1, 1]
print(countBadPairs(nums3)) # Output: 6

nums4 = [10, 10, 10]
print(countBadPairs(nums4)) # Output: 2

nums5 = [0, 0, 0, 0, 0]
print(countBadPairs(nums5)) # Output: 6

nums6 = [1, 3, 2, 4, 5]
print(countBadPairs(nums6)) # Output: 3

nums7 = [5, 4, 3, 2, 1]
print(countBadPairs(nums7)) # Output: 10

nums8 = [2]
print(countBadPairs(nums8)) # Output: 0

nums9 = [1, 0, 1, 0]
print(countBadPairs(nums9)) # Output: 5

nums10 = [3, 6, 9, 12]
print(countBadPairs(nums10)) # Output: 0