# CONVERT AN ARRAY INTO 2D ARRAY WITH CONDITIONS

'''
You are given an integer array nums. You need to create a 2D array from nums satisfying the following conditions:
The 2D array should contain only the elements of the array nums.
Each row in the 2D array contains distinct integers.
The number of rows in the 2D array should be minimal.
Return the resulting array. If there are multiple answers, return any of them.
Note that the 2D array can have a different number of elements on each row.
'''

def convertArray(nums):
    hashMap = {}
    result = []
    
    for num in nums:
        hashMap[num] = hashMap.get(num, 0) + 1
        row = hashMap[num] - 1
        if len(row) == count:
            result.append([])
        result[row].append(num)
        
    return result

'''
Time Complexity: O(n)
- Let n be the number of elements in the input array `nums`.
- We iterate through the array once with a for loop that runs n times.
- Inside the loop, all operations (hash map lookups, dictionary updates, list appends) are constant time, O(1).
- The overall time complexity is dominated by the loop, resulting in O(n).

Space Complexity: O(n)
- We use a dictionary `hashMap` to store the count of each number in the array.
- In the worst case, the dictionary can have at most n unique keys (one for each distinct number in the array).
- We also use a list `result` to store the 2D array, which can have at most n rows.
- Therefore, the space complexity is O(n).
'''

# Test Cases
nums1 = [1, 3, 4, 1, 2, 3, 1]
print(convertArray(nums1)) # Output: [[1, 2], [3, 4], [1, 3], [1]]

nums2 = [1, 2, 3, 4]
print(convertArray(nums2)) # Output: [[1, 2, 3, 4]]

nums3 = [1, 1, 1, 1]
print(convertArray(nums3)) # Output: [[1], [1], [1], [1]]

nums4 = [5, 5, 5, 2, 2, 1]
print(convertArray(nums4)) # Output: [[5, 2, 1], [5, 2], [5]]

nums5 = [1]
print(convertArray(nums5)) # Output: [[1]]

nums6 = [2, 1, 2, 1, 2, 1]
print(convertArray(nums6)) # Output: [[2, 1], [2, 1], [2, 1]]

nums7 = [10, 20, 30, 10, 20, 10]
print(convertArray(nums7)) # Output: [[10, 20, 30], [10, 20], [10]]

nums8 = [7, 7, 8, 8, 9, 9]
print(convertArray(nums8)) # Output: [[7, 8, 9], [7, 8, 9]]

nums9 = [1, 2, 3, 1, 2, 1]
print(convertArray(nums9)) # Output: [[1, 2, 3], [1, 2], [1]]

nums10 = [5, 4, 3, 2, 1, 5, 4, 3, 2, 5]
print(convertArray(nums10)) # Output: [[5, 4, 3, 2, 1], [5, 4, 3, 2], [5]]