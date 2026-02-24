# TRIANGLE

'''
Given a triangle array, return the minimum path sum from top to bottom.
For each step, you may move to an adjacent number of the row below. More formally, if you are on index i on the current row, you may move to either index i or index i + 1 on the next row.
'''

'''
ALGORITHM:

This problem uses dynamic programming with space optimization. We can solve it in-place by modifying the triangle array from bottom to top.

The key insight is that for each element, the minimum path sum to reach it from the bottom is:
triangle[r][c] + min(triangle[r+1][c], triangle[r+1][c+1])

We iterate from the second-to-last row up to the first row, updating each element with the minimum sum to reach it from the bottom.

Algorithm:
1. Start from the second-to-last row (index len(triangle) - 2) and go up to row 0
2. For each element at position (r, c):
    - Add the minimum of the two elements directly below it
    - triangle[r][c] += min(triangle[r+1][c], triangle[r+1][c+1])
3. After processing all rows, triangle[0][0] contains the minimum path sum
4. Return triangle[0][0]
'''

def minimumTotal(triangle):
    for r in range(len(triangle) - 2, -1, -1):
        for c in range(len(triangle[r])):
            triangle[r][c] += min(triangle[r + 1][c], triangle[r + 1][c + 1])
            
    return triangle[0][0]

'''
Time Complexity: O(N^2), where N is the number of rows in the triangle. We visit each element once.
Space Complexity: O(1) - we modify the triangle in-place without using extra space.
'''

# Test Cases

# Test Case 1: Simple triangle
triangle1 = [[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]]
result1 = minimumTotal(triangle1)
print(result1) # Expected: 11 (path: 2 -> 3 -> 5 -> 1)

# Test Case 2: Single element
triangle2 = [[1]]
result2 = minimumTotal(triangle2)
print(result2) # Expected: 1

# Test Case 3: Two rows
triangle3 = [[2], [3, 4]]
result3 = minimumTotal(triangle3)
print(result3) # Expected: 4 (path: 2 -> 3)

# Test Case 4: All same values
triangle4 = [[1], [1, 1], [1, 1, 1], [1, 1, 1, 1]]
result4 = minimumTotal(triangle4)
print(result4) # Expected: 4

# Test Case 5: Increasing values
triangle5 = [[1], [2, 3], [4, 5, 6], [7, 8, 9, 10]]
result5 = minimumTotal(triangle5)
print(result5) # Expected: 10

# Test Case 6: Decreasing values
triangle6 = [[10], [9, 8], [7, 6, 5], [4, 3, 2, 1]]
result6 = minimumTotal(triangle6)
print(result6) # Expected: 16

# Test Case 7: Minimum at edge
triangle7 = [[5], [10, 1], [1, 1, 1]]
result7 = minimumTotal(triangle7)
print(result7) # Expected: 7 (path: 5 -> 1 -> 1)

# Test Case 8: Large triangle
triangle8 = [[1], [2, 3], [4, 5, 6], [7, 8, 9, 10], [11, 12, 13, 14, 15]]
result8 = minimumTotal(triangle8)
print(result8) # Expected: 20

# Test Case 9: Complex path
triangle9 = [[-1], [-2, -3], [-4, -5, -6], [-10, -8, -3, -2]]
result9 = minimumTotal(triangle9)
print(result9) # Expected: -20

# Test Case 10: Single row with multiple elements
triangle10 = [[1, 2, 3, 4]]
result10 = minimumTotal(triangle10)
print(result10) # Expected: 1 (returns first element after processing)
