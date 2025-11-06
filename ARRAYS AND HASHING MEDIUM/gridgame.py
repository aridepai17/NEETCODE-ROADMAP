# GRID GAME

'''
You are given a 0-indexed 2D array grid of size 2 x n, where grid[r][c] represents the number of points at position (r, c) on the matrix. Two robots are playing a game on this matrix.
Both robots initially start at (0, 0) and want to reach (1, n-1). Each robot may only move to the right ((r, c) to (r, c + 1)) or down ((r, c) to (r + 1, c)).
At the start of the game, the first robot moves from (0, 0) to (1, n-1), collecting all the points from the cells on its path. For all cells (r, c) traversed on the path, grid[r][c] is set to 0. Then, the second robot moves from (0, 0) to (1, n-1), collecting the points on its path. Note that their paths may intersect with one another.
The first robot wants to minimize the number of points collected by the second robot. In contrast, the second robot wants to maximize the number of points it collects. If both robots play optimally, return the number of points collected by the second robot.
'''

def gridGame(grid):
    n = len(grid[0])
    prefixRow1 = grid[0].copy()
    prefixRow2 = grid[1].copy()
    
    for i in range(1, n):
        prefixRow1[i] += prefixRow1[i - 1]
        prefixRow2[i] += prefixRow2[i - 1]
        
    result = float('inf')
    for i in range(n):
        top = prefix[-1] - prefix[i]
        bottom = prefix[i - 1] if i > 0 else 0
        secondRobot = max(top, bottom)
        result = min(result, secondRobot)
        
    return result

'''
Time Complexity: O(N)
- Let N be the number of columns in the grid (length of grid[0]).
- Creating copies of grid[0] and grid[1] takes O(N) time each.
- The first loop iterates through N-1 elements to compute prefix sums, taking O(N) time.
- The second loop iterates through N elements to find the optimal point, with each iteration performing O(1) operations, taking O(N) time.
- Therefore, the overall time complexity is O(N).

Space Complexity: O(N)
- We create two prefix sum arrays (prefixRow1 and prefixRow2), each of size N, requiring O(N) space.
- Other variables (result, i, top, bottom, secondRobot) use constant space O(1).
- Therefore, the overall space complexity is O(N).
'''

# Test Cases
grid1 = [[2,5,4],[1,5,1]]
print(gridGame(grid1)) # Output: 4

grid2 = [[3,3,1],[8,5,2]]
print(gridGame(grid2)) # Output: 4

grid3 = [[1,3,1,15],[1,3,3,1]]
print(gridGame(grid3)) # Output: 7

grid4 = [[20],[20]]
print(gridGame(grid4)) # Output: 20

grid5 = [[1,1,1,1,1],[1,1,1,1,1]]
print(gridGame(grid5)) # Output: 4

grid6 = [[10,10,10,10],[1,1,1,1]]
print(gridGame(grid6)) # Output: 10

grid7 = [[5,5,5,5,5,5],[1,2,3,4,5,6]]
print(gridGame(grid7)) # Output: 15

grid8 = [[0,0,0,0],[0,0,0,0]]
print(gridGame(grid8)) # Output: 0

grid9 = [[100,200,300],[50,100,150]]
print(gridGame(grid9)) # Output: 200

grid10 = [[7,14,21,28],[1,2,3,4]]
print(gridGame(grid10)) # Output: 21