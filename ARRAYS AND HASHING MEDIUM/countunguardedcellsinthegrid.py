# COUNT UNGUARDED CELLS IN THE GRID

'''
You are given two integers m and n representing a 0-indexed m x n grid. You are also given two 2D integer arrays guards and walls where guards[i] = [rowi, coli] and walls[j] = [rowj, colj] represent the positions of the ith guard and jth wall respectively.
A guard can see every cell in the four cardinal directions (north, east, south, or west) starting from their position unless obstructed by a wall or another guard. A cell is guarded if there is at least one guard that can see it.
Return the number of unoccupied cells that are not guarded.
'''

def countUnguarded(m, n, guards, walls):
    
    '''
    0 -> FREE
    1 -> GUARD
    2 -> WALL
    3 -> GUARDED
    '''
    
    grid = []
    for _ in range(m):
        row = []
        for _ in range(n):
            row.append(0)
        grid.append(row)
        
    for r, c in guards:
        grid[r][c] = 1
    
    for r, c in walls:
        grid[r][c] = 2
        
    def makeGuarded(r, c):
        for row in range(r + 1, m):
            if grid[row][c] in [1, 2]:
                break
            grid[row][c] = 3
            
        for row in reversed(range(0, r)):
            if grid[row][c] in [1, 2]:
                break
            grid[row][c] = 3
            
        for col in range(c + 1, n):
            if grid[r][col] in [1, 2]:
                break
            grid[r][col] = 3
            
        for col in reversed(range(0, c)):
            if grid[r][col] in [1, 2]:
                break
            grid[r][col] = 3

    for r, c in guards:
        makeGuarded(r, c)
        
    result = 0
    for row in grid:
        for cell in row:
            if cell == 0:
                result += 1
                
    return result

'''
Time Complexity: O(m * n + g * (m + n))
- Let m be the number of rows and n be the number of columns in the grid.
- Let g be the number of guards and w be the number of walls.
- Initializing the grid takes O(m * n) time.
- Marking guards and walls takes O(g + w) time.
- For each guard, the makeGuarded function traverses up to m cells vertically and n cells horizontally, which is O(m + n) per guard.
- Since we call makeGuarded for each of the g guards, this takes O(g * (m + n)) time.
- Counting unguarded cells requires iterating through the entire grid, which takes O(m * n) time.
- Therefore, the overall time complexity is O(m * n + g * (m + n)).

Space Complexity: O(m * n)
- The grid stores m * n cells, requiring O(m * n) space.
- Other variables like result, row, and col use constant space.
- Therefore, the overall space complexity is O(m * n).
'''

# Test Cases
m1, n1 = 4, 6
guards1 = [[0,0],[1,1],[2,3]]
walls1 = [[0,1],[2,2],[1,4]]
print(countUnguarded(m1, n1, guards1, walls1)) # Output: 7

m2, n2 = 3, 3
guards2 = [[1,1]]
walls2 = []
print(countUnguarded(m2, n2, guards2, walls2)) # Output: 0

m3, n3 = 5, 5
guards3 = [[0,0],[4,4]]
walls3 = [[2,2]]
print(countUnguarded(m3, n3, guards3, walls3)) # Output: 6

m4, n4 = 2, 7
guards4 = [[1,5],[1,1],[1,6],[0,2]]
walls4 = [[0,6],[0,3],[0,5]]
print(countUnguarded(m4, n4, guards4, walls4)) # Output: 1

m5, n5 = 1, 1
guards5 = []
walls5 = []
print(countUnguarded(m5, n5, guards5, walls5)) # Output: 1

m6, n6 = 3, 3
guards6 = []
walls6 = [[1,1]]
print(countUnguarded(m6, n6, guards6, walls6)) # Output: 8

m7, n7 = 4, 4
guards7 = [[0,0],[0,3],[3,0],[3,3]]
walls7 = []
print(countUnguarded(m7, n7, guards7, walls7)) # Output: 0

m8, n8 = 5, 5
guards8 = [[2,2]]
walls8 = [[0,2],[2,0],[2,4],[4,2]]
print(countUnguarded(m8, n8, guards8, walls8)) # Output: 16

m9, n9 = 6, 6
guards9 = [[0,0],[5,5]]
walls9 = [[2,2],[3,3]]
print(countUnguarded(m9, n9, guards9, walls9)) # Output: 18

m10, n10 = 10, 10
guards10 = [[5,5]]
walls10 = [[0,5],[5,0],[5,10-1],[10-1,5]]
print(countUnguarded(m10, n10, guards10, walls10)) # Output: 72