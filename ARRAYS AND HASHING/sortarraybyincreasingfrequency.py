# SORT ARRAY BY INCREASING FREQUENCY

'''
Given an array of integers nums, sort the array in increasing order based on the frequency of the values. 
If multiple values have the same frequency, sort them in decreasing order.
Return the sorted array.
'''

def frequencySort(nums):
    hashMap = {}
    
    for num in nums:
        hashMap[num] = hashMap.get(num, 0) + 1
        
    def customSort(n):
        return (hashMap[n], -n)
        
    nums.sort(key = customSort)
    
    return nums

'''
Time Complexity: O(N log N)
Let N be the number of elements in the input array `nums`.
- The first step is to build a frequency map (`hashMap`) of the elements in `nums`. This involves iterating through the array once, which takes O(N) time. Each dictionary insertion/update is an O(1) operation on average.
- The second step is to sort the `nums` array using Python's built-in `sort()` method. The time complexity of `sort()` (which uses Timsort) is O(N log N).
- For each element during the sort, a custom key function `customSort` is called. This function performs a dictionary lookup, which is an O(1) operation on average. Therefore, the key function does not change the overall sorting complexity.
- The total time complexity is the sum of these steps: O(N) + O(N log N), which is dominated by the sorting step. Thus, the overall time complexity is O(N log N).

Space Complexity: O(N)
- A hash map (`hashMap`) is used to store the frequency of each number. In the worst-case scenario, where all elements in `nums` are unique, the hash map will store N key-value pairs. This requires O(N) space.
- The space complexity of Python's `sort()` method (Timsort) can be up to O(N) in the worst case for temporary storage.
- Therefore, the total auxiliary space required is O(N) for the hash map plus the space for sorting, which results in an overall space complexity of O(N).
'''

# Test Cases
nums1 = [1, 1, 2, 2, 2, 3]
print(frequencySort(nums1)) # Output: [3, 1, 1, 2, 2, 2]

nums2 = [2, 3, 1, 3, 2]
print(frequencySort(nums2)) # Output: [1, 3, 3, 2, 2]

nums3 = [-1, 1, -6, 4, 5, -6, 1, 4, 1]
print(frequencySort(nums3)) # Output: [5, -1, 4, 4, -6, -6, 1, 1, 1]

nums4 = [5, 2, 8, 1, 9]
print(frequencySort(nums4)) # Output: [9, 8, 5, 2, 1]

nums5 = [7, 7, 7, 7, 7]
print(frequencySort(nums5)) # Output: [7, 7, 7, 7, 7]

nums6 = []
print(frequencySort(nums6)) # Output: []

nums7 = [0, 0, 5, 5, 0, -1]
print(frequencySort(nums7)) # Output: [-1, 5, 5, 0, 0, 0]

nums8 = [3, 3, 1, 1, 1, 8, 8, 8, 8, 0, 0]
print(frequencySort(nums8)) # Output: [3, 3, 0, 0, 1, 1, 1, 8, 8, 8, 8]

nums9 = [4, -2, 3, 1, 4, 3, -2, 1]
print(frequencySort(nums9)) # Output: [4, 4, 3, 3, 1, 1, -2, -2]

nums10 = [6, 6, 2, 2, 9]
print(frequencySort(nums10)) # Output: [9, 6, 6, 2, 2]