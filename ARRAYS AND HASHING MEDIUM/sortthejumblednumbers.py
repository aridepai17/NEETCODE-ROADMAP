# SORT THE JUMBLED NUMBERS

'''
You are given a 0-indexed integer array mapping which represents the mapping rule of a shuffled decimal system. 
mapping[i] = j means digit i should be mapped to digit j in this system.
The mapped value of an integer is the new integer obtained by replacing each occurrence of digit i in the integer with mapping[i] for all 0 <= i <= 9.
You are also given another integer array nums. Return the array nums sorted in non-decreasing order based on the mapped values of its elements.
Notes:
Elements with the same mapped values should appear in the same relative order as in the input.
The elements of nums should only be sorted based on their mapped values and not be replaced by them.
'''

def sortJumbled(nums, mapping):
    memo = {}
    def getMappedValue(n):
        if n in memo:
            return memo[n]
        
        numStr = str(n)
        mappedValue = ""
        for digit in numStr:
            mappedValue += str(mapping[int(digit)])
            
        memo[n] = int(mappedValue)
        return int(mappedValue)
    
    return sorted(nums, key=getMappedValue)

'''
Time Complexity: O(N * M + N log N)
- Let N be the number of elements in the `nums` array.
- Let M be the average number of digits in the numbers in `nums`.
- **getMappedValue function**: For each number, we convert it to a string (O(M)), iterate through each digit (O(M)), and perform constant-time operations (string concatenation and mapping lookup). So, computing the mapped value for one number takes O(M).
- **Memoization**: The memo dictionary stores already computed mapped values. In the worst case, if all numbers in `nums` are unique, we compute N mapped values, each taking O(M) time, resulting in O(N * M) for all memoization operations.
- **Sorting**: The `sorted()` function performs O(N log N) comparisons. Each comparison calls `getMappedValue`, which either retrieves from memo in O(1) or computes in O(M). Since we memoize, each unique number is computed once, and subsequent calls are O(1). The sorting step is O(N log N) comparisons.
- Overall time complexity: O(N * M) for computing mapped values + O(N log N) for sorting = O(N * M + N log N).

Space Complexity: O(N * M)
- **Memo dictionary**: Stores up to N key-value pairs (one for each unique number in `nums`). Each key is an integer, and each value is the mapped integer, which can have up to M digits. This requires O(N * M) space in the worst case.
- **Temporary strings**: During the computation of mapped values, we create strings of length M for each number, but these are temporary and don't accumulate.
- **Sorted output**: The `sorted()` function creates a new list of size N, which is O(N).
- Overall space complexity: O(N * M) dominated by the memo dictionary.
'''

# Test Cases
mapping1 = [8,9,4,0,2,1,3,5,7,6], nums1 = [991,338,38]
print(sortJumbled(nums1, mapping1)) # Output: [338, 38, 991]

mapping2 = [0,1,2,3,4,5,6,7,8,9], nums2 = [123,456,789]
print(sortJumbled(nums2, mapping2)) # Output: [123, 456, 789]

mapping3 = [9,8,7,6,5,4,3,2,1,0], nums3 = [0,1,2,3,4,5,6,7,8,9]
print(sortJumbled(nums3, mapping3)) # Output: [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]

mapping4 = [1,2,3,4,5,6,7,8,9,0], nums4 = [100,200,300]
print(sortJumbled(nums4, mapping4)) # Output: [300, 100, 200]

mapping5 = [5,4,3,2,1,0,9,8,7,6], nums5 = [12,34,56,78,90]
print(sortJumbled(nums5, mapping5)) # Output: [90, 78, 56, 34, 12]

mapping6 = [2,1,0,9,8,7,6,5,4,3], nums6 = [111,222,333]
print(sortJumbled(nums6, mapping6)) # Output: [333, 222, 111]

mapping7 = [0,1,2,3,4,5,6,7,8,9], nums7 = [1000,999,888,777]
print(sortJumbled(nums7, mapping7)) # Output: [777, 888, 999, 1000]

mapping8 = [3,2,1,0,9,8,7,6,5,4], nums8 = [10,20,30,40,50]
print(sortJumbled(nums8, mapping8)) # Output: [50, 40, 30, 20, 10]

mapping9 = [9,0,1,2,3,4,5,6,7,8], nums9 = [5,15,25,35,45]
print(sortJumbled(nums9, mapping9)) # Output: [5, 15, 25, 35, 45]

mapping10 = [1,0,3,2,5,4,7,6,9,8], nums10 = [987,654,321]
print(sortJumbled(nums10, mapping10)) # Output: [321, 654, 987]