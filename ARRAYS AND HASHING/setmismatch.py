# SET MISMATCH

'''
You have a set of integers s, which originally contains all the numbers from 1 to n. 
Unfortunately, due to some error, one of the numbers in s got duplicated to another number in the set, which results in repetition of one number and loss of another number.
You are given an integer array nums representing the data status of this set after the error.
Find the number that occurs twice and the number that is missing and return them in the form of an array.
'''

# Solution 1: Using a HashMap
def setMismatch1(nums):
    hashMap = {}
    
    for num in nums:
        hashMap[num] = hashMap.get(num, 0) + 1
        
    duplicate = -1
    missing = -1
    
    for i in range(1, len(nums) + 1):
        if i in hashMap:
            if hashMap[i] == 2:
                duplicate = i
        else:
            missing = i
            
    return [duplicate, missing]

'''
Time Complexity: O(N)
- Let N be the number of elements in the input array `nums`.
- The first loop iterates through the `nums` array once to populate the hash map. This takes O(N) time.
- The second loop iterates from 1 to N to check for the duplicate and missing numbers. This also takes O(N) time.
- The total time complexity is O(N) + O(N) = O(2N), which simplifies to O(N).

Space Complexity: O(N)
- A hash map is used to store the frequency of each number in `nums`.
- In the worst case, the hash map will store N-1 unique elements (one number is duplicated, one is missing).
- The space required by the hash map is proportional to the number of elements in the input array, so the space complexity is O(N).
'''

# Solution 2: Using HashSet
def setMismatch2(nums):
    hashSet = set()
    duplicate = -1
    
    for num in nums:
        if num in hashSet:
            duplicate = num
        else:
            hashSet.add(num)
            
    missing = -1
    for i in range(1, len(nums) + 1):
        if i not in hashSet:
            missing = i
            break
            
    return [duplicate, missing]

'''
Time Complexity: O(N)
- Let N be the number of elements in the input array `nums`.
- The first loop iterates through the `nums` array once to find the duplicate number and populate the hash set. This takes O(N) time, as set lookups and insertions are O(1) on average.
- The second loop iterates from 1 to N to find the missing number. This also takes O(N) time in the worst case.
- The total time complexity is O(N) + O(N) = O(2N), which simplifies to O(N).

Space Complexity: O(N)
- A hash set is used to store the unique numbers from `nums`.
- In the worst case, the hash set will store N-1 unique elements (one number is duplicated, one is missing).
- The space required by the hash set is proportional to the number of elements in the input array, so the space complexity is O(N).
'''

# Solution 3: Using no Extra Space
def setMismatch3(nums):
    n = len(nums)
    
    sumNums = sum(nums)
    sumExpected = n * (n + 1) // 2
    
    sumSquares = sum(num * num for num in nums)
    sumSquaresExpected = n * (n + 1) * (2 * n + 1) // 6
    
    sumDiff = sumExpected - sumNums
    sumSquaresDiff = sumSquaresExpected - sumSquares
    
    missing = (sumSquaresDiff + sumDiff) // (2 * sumDiff)
    duplicate = missing - sumDiff
    
    return [duplicate, missing]

'''
Time Complexity: O(N)
- Let N be the number of elements in the input array `nums`.
- The calculation of `sumNums` involves iterating through the `nums` array once, which takes O(N) time.
- The calculation of `sumSquares` also involves iterating through the `nums` array once, taking O(N) time.
- All other operations (calculating expected sums, differences, and the final missing/duplicate values) are constant time, O(1).
- The total time complexity is dominated by the linear scans, resulting in O(N) + O(N) = O(N).

Space Complexity: O(1)
- The algorithm uses a fixed number of variables to store sums, differences, and the final result.
- The amount of extra space used does not depend on the size of the input array `nums`.
- Therefore, the space complexity is O(1), as no additional data structures are created.
'''

# Test Cases
nums1 = [1, 2, 2, 4]
print(setMismatch1(nums1)) # Output: [2, 3]

nums2 = [1, 1]
print(setMismatch1(nums2)) # Output: [1, 2]

nums3 = [2, 2]
print(setMismatch1(nums3)) # Output: [2, 1]

nums4 = [3, 2, 2]
print(setMismatch1(nums4)) # Output: [2, 1]

nums5 = [1, 3, 3]
print(setMismatch1(nums5)) # Output: [3, 2]

nums6 = [4, 1, 2, 1]
print(setMismatch1(nums6)) # Output: [1, 3]

nums7 = [1, 5, 3, 2, 2]
print(setMismatch1(nums7)) # Output: [2, 4]

nums8 = [5, 3, 1, 5, 2]
print(setMismatch1(nums8)) # Output: [5, 4]

nums9 = [6, 2, 3, 4, 5, 3]
print(setMismatch1(nums9)) # Output: [3, 1]

nums10 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 9]
print(setMismatch1(nums10)) # Output: [9, 10]