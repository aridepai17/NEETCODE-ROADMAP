# SEARCH IN 2D MATRIX

'''
You are given an m x n integer matrix matrix with the following two properties:
- Each row is sorted in non-decreasing order.
- The first integer of each row is greater than the last integer of the previous row.
Given an integer target, return true if target is in matrix or false otherwise.
You must write a solution in O(log(m * n)) time complexity.
'''

"""
Algorithm:
1. Initialize two pointers: left = 0 and right = m * n - 1
2. While left <= right:
   a. Calculate mid = (left + right) // 2
   b. Calculate row = mid // n and col = mid % n to get the index of the element in the matrix
   c. If matrix[row][col] == target:
      - The target is found
      - Return True
   d. If matrix[row][col] < target:
      - The target is in the right half of the matrix
      - Move left to mid + 1
   e. Else:
      - The target is in the left half of the matrix
      - Move right to mid - 1
3. The target is not found in the matrix
- Return False
"""

def searchMatrix(matrix, target):
    n = len(matrix)
    m = len(matrix[0])
    
    left = 0
    right = n * m - 1
    
    while left <= right:
        mid = (left + right) // 2
        
        row = mid // m
        col = mid % m
        
        if matrix[row][col] < target:
            left = mid + 1
        elif matrix[row][col] > target:
            right = mid - 1
        else:
            return True
        
    return False

"""
Time Complexity: O(log(m * n))
The time complexity of the above algorithm is O(log(m * n)), where m and n are the dimensions of the matrix.
This is because the binary search algorithm reduces the search space by half at each step.

Space Complexity: O(1)
The space complexity of the above algorithm is O(1), since no additional data structures are used.
The only space used is for the variables left, right, mid, row, and col, which are fixed size and do not scale with the input size.
"""

# Test Cases
matrix1 = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
target1 = 3
print(searchMatrix(matrix1, target1)) # Output: True

matrix2 = [[1, 3, 5], [10, 11, 16]]
target2 = 10
print(searchMatrix(matrix2, target2)) # Output: False

matrix3 = [[1, 2], [3, 4]]
target3 = 3
print(searchMatrix(matrix3, target3)) # Output: True

matrix4 = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
target4 = 11
print(searchMatrix(matrix4, target4)) # Output: True

matrix5 = [[1, 3, 5], [10, 11, 16]]
target5 = 1
print(searchMatrix(matrix5, target5)) # Output: True

matrix6 = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
target6 = 60
print(searchMatrix(matrix6, target6)) # Output: True

matrix7 = [[1, 3, 5], [10, 11, 16]]
target7 = 16
print(searchMatrix(matrix7, target7)) # Output: True

matrix8 = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
target8 = 21
print(searchMatrix(matrix8, target8)) # Output: False

matrix9 = [[1, 3, 5], [10, 11, 16]]
target9 = 17
print(searchMatrix(matrix9, target9)) # Output: False

matrix10 = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
target10 = 34
print(searchMatrix(matrix10, target10)) # Output: True