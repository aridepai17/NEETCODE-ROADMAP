# BRICK WALL

'''
There is a rectangular brick wall in front of you with n rows of bricks.
The ith row has some number of bricks each of the same height (i.e., one unit) but they can be of different widths. 
The total width of each row is the same.
Draw a vertical line from the top to the bottom and cross the least bricks. 
If your line goes through the edge of a brick, then the brick is not considered as crossed. 
You cannot draw a line just along one of the two vertical edges of the wall, in which case the line will obviously cross no bricks.
Given the 2D array wall that contains the information about the wall, return the minimum number of crossed bricks after drawing such a vertical line.
'''

def leastBricks(wall):
    countGaps = {0 : 0}
    
    for row in wall:
        total = 0
        for brick in row[:-1]:
            total += brick
            countGaps[total] = countGaps.get(total, 0) + 1
            
    return len(wall) - max(countGaps.values())
'''
Time Complexity: O(N * W)
- Let N be the number of rows in the `wall`.
- Let W be the average number of bricks in a row (or maximum number of bricks in a row).
- The outer loop iterates N times, once for each row in the `wall`.
- The inner loop iterates through the bricks in a row, specifically `W-1` times (excluding the last brick as its edge is the wall's edge).
- Inside the inner loop, dictionary operations (get and set) take O(1) on average.
- After processing all rows, finding the maximum value in `countGaps.values()` takes O(G) time, where G is the number of unique gap positions. In the worst case, G can be up to N * W.
- Therefore, the overall time complexity is O(N * W).

Space Complexity: O(W_total)
- The `countGaps` dictionary stores the frequencies of gap positions.
- In the worst case, each unique gap position across all rows could be stored.
- The maximum possible width of the wall is `W_total` (sum of all bricks in a row).
- The number of unique gap positions can be at most `W_total - 1` (excluding the final edge).
- Therefore, the space complexity is O(W_total), where W_total is the total width of the wall.
'''

# Test Cases
wall1 = [[1,2,2,1],[3,1,2],[1,3,2],[2,4],[3,1,2],[1,3,1,1]]
print(leastBricks(wall1)) # Output: 2

wall2 = [[1,1,1,1], [1,1,1,1], [1,1,1,1]]
print(leastBricks(wall2)) # Output: 0

wall3 = [[1,2,3], [2,3,1], [3,1,2]]
print(leastBricks(wall3)) # Output: 1

wall4 = [[1,2,3,4,5]]
print(leastBricks(wall4)) # Output: 0

wall5 = [[10], [10], [10]]
print(leastBricks(wall5)) # Output: 3

wall6 = []
print(leastBricks(wall6)) # Output: 0

wall7 = [[1,1,1], [2,1], [1,2]]
print(leastBricks(wall7)) # Output: 1

wall8 = [[1],[1],[1]]
print(leastBricks(wall8)) # Output: 3

wall9 = [[1,2,2,1], [3,1,2], [1,3,2], [2,4], [3,1,2], [1,3,1,1], [6]]
print(leastBricks(wall9)) # Output: 3

wall10 = [[1,1,1,1,1,1,1,1,1,1], [1,1,1,1,1,1,1,1,1,1], [1,1,1,1,1,1,1,1,1,1]]
print(leastBricks(wall10)) # Output: 0