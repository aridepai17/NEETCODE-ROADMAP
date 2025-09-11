# FIND MISSING AND REPEATED VALUES

'''
You are given a 0-indexed 2D integer matrix grid of size n * n with values in the range [1, n2]. 
Each integer appears exactly once except a which appears twice and b which is missing. 
The task is to find the repeating and missing numbers a and b.
Return a 0-indexed integer array ans of size 2 where ans[0] equals to a and ans[1] equals to b.
'''

def findMissingandRepeatedValues(grid):
    n = len(grid)
    hashMap = {}
    
    for i in range(n):
        for j in range(n):
            if grid[i][j] not in hashMap:
                hashMap[grid[i][j]] = 0
            hashMap[grid[i][j]] += 1
            
    double = 0
    missing = 0
    
    for num in range(1, n*n + 1):
        if num not in hashMap:
            missing = num
        elif hashMap[num] == 2:
            double = num
            
    return [double, missing]

'''
Time Complexity: O(n^2)
Let n be the size of one dimension of the n x n grid. The total number of elements in the grid is n^2.
- The first nested loop iterates through each of the n*n elements in the grid to populate the `hashMap`. This takes O(n^2) time, as hash map operations (insertion, access) are O(1) on average.
- The second loop iterates from 1 to n*n. This loop also runs n^2 times. Inside the loop, checking for a key in the hash map (`in`) and accessing a value are O(1) on average. This part also takes O(n^2) time.
- The overall time complexity is O(n^2) + O(n^2), which simplifies to O(n^2).

Space Complexity: O(n^2)
- We use a hash map, `hashMap`, to store the frequency of each number in the grid.
- The numbers in the grid are in the range [1, n^2]. The hash map will store up to n^2 - 1 unique keys (since one number is missing and one is repeated).
- Therefore, the space required for the hash map is proportional to the total number of elements in the grid, which is O(n^2).
- The other variables (`n`, `i`, `j`, `double`, `missing`, `num`) use constant O(1) space.
- The dominant factor is the hash map, making the overall space complexity O(n^2).
'''

# Test Cases
grid1 = [[1,3],[2,2]]
print(findMissingandRepeatedValues(grid1)) # Output: [2, 4]

# Test Case 2: 3x3 grid
grid2 = [[1, 2, 3], [4, 5, 6], [5, 8, 9]]
print(findMissingandRepeatedValues(grid2)) # Output: [5, 7]

# Test Case 3: Repeated and missing are boundaries (1 and n^2)
grid3 = [[1, 1], [2, 3]]
print(findMissingandRepeatedValues(grid3)) # Output: [1, 4]

# Test Case 4: Repeated and missing are boundaries (n^2 and 1)
grid4 = [[4, 2], [3, 4]]
print(findMissingandRepeatedValues(grid4)) # Output: [4, 1]

# Test Case 5: A larger 4x4 grid
grid5 = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 10, 16]]
print(findMissingandRepeatedValues(grid5)) # Output: [10, 15]

# Test Case 6: Adjacent repeated and missing numbers
grid6 = [[1, 2, 3], [5, 6, 7], [8, 9, 3]]
print(findMissingandRepeatedValues(grid6)) # Output: [3, 4]

# Test Case 7: Another adjacent case
grid7 = [[8, 1, 2], [3, 4, 5], [6, 9, 8]]
print(findMissingandRepeatedValues(grid7)) # Output: [8, 7]

# Test Case 8: Unordered grid
grid8 = [[4, 3], [1, 3]]
print(findMissingandRepeatedValues(grid8)) # Output: [3, 2]

# Test Case 9: Another 3x3 grid with boundary values
grid9 = [[9, 2, 3], [4, 5, 6], [7, 8, 9]]
print(findMissingandRepeatedValues(grid9)) # Output: [9, 1]

# Test Case 10: Simple 2x2 case
grid10 = [[1, 2], [2, 4]]
print(findMissingandRepeatedValues(grid10)) # Output: [2, 3]