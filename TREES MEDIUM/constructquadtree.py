# CONSTRUCT QUAD TREE

'''
Given a n * n matrix grid of 0's and 1's only. We want to represent grid with a Quad-Tree.
Return the root of the Quad-Tree representing grid.

A Quad-Tree is a tree data structure in which each internal node has exactly four children. Besides, each node has two attributes:
val: True if the node represents a grid of 1's or False if the node represents a grid of 0's. Notice that you can assign the val to True or False when isLeaf is False, and both are accepted in the answer.
isLeaf: True if the node is a leaf node on the tree or False if the node has four children.

class Node {
    public boolean val;
    public boolean isLeaf;
    public Node topLeft;
    public Node topRight;
    public Node bottomLeft;
    public Node bottomRight;
}

We can construct a Quad-Tree from a two-dimensional area using the following steps:
- If the current grid has the same value (i.e all 1's or all 0's) set isLeaf True and set val to the value of the grid and set the four children to Null and stop.
- If the current grid has different values, set isLeaf to False and set val to any value and divide the current grid into four sub-grids as shown in the photo.
- Recurse for each of the children with the proper sub-grid.
'''

class Node:
    def __init__(self, val, isLeaf, topLeft=None, topRight=None, bottomLeft=None, bottomRight=None):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight

'''
ALGORITHM:

1. Define a recursive function `dfs(n, r, c)` that takes:
    - n: the size of the current square grid
    - r: the starting row index
    - c: the starting column index
2. Base case: If n == 1 (grid size is 1x1), create and return a leaf node with:
    - val = grid[r][c]
    - isLeaf = True
    - No children (all four children are None)
3. Divide the grid into four equal quadrants:
    - half = n // 2
    - Recursively call dfs for each quadrant:
        a. topLeft: dfs(half, r, c)
        b. topRight: dfs(half, r, c + half)
        c. bottomLeft: dfs(half, r + half, c)
        d. bottomRight: dfs(half, r + half, c + half)
4. After getting all four children, check if they can be merged:
    - If all four children are leaves AND all have the same val, return a single leaf node
    - Otherwise, return an internal node with all four children

5. Start the recursion by calling dfs(len(grid), 0, 0)
'''

def construct(grid):
    def dfs(n, r, c):
        if n == 1:
            return Node(grid[r][c], True, None, None, None, None)
            
        half = n // 2
        topleft = dfs(half, r, c)
        topright = dfs(half, r, c + half)
        bottomleft = dfs(half, r + half, c)
        bottomright = dfs(half, r + half, c + half)
        
        if (topleft.isLeaf and topright.isLeaf and bottomleft.isLeaf and bottomright.isLeaf and topleft.val == topright.val == bottomleft.val == bottomright.val):
            return Node(topleft.val, True, None, None, None)
        
        return Node(1, False, topleft, topright, bottomleft, bottomright)
    
    return dfs(len(grid), 0, 0)

'''
Time Complexity: O(N^2), where N is the dimension of the grid (n x n).
We visit each cell in the grid at least once during the recursion.
In the worst case, we make 4 recursive calls for each subdivision, but each cell
is processed only when it becomes a leaf node or when we check all four quadrants.
The total complexity is O(n^2) because we process each element of the grid.

Space Complexity: O(log n) for the recursion stack.
The depth of the recursion is O(log n) because we divide the grid by 2 each time.
Additionally, we use O(1) extra space besides the recursion stack.
'''

# Test Cases

# Test Case 1: All zeros
grid1 = [
    [0, 0],
    [0, 0]
]
result1 = construct(grid1)
# Expected: isLeaf=True, val=0

# Test Case 2: All ones
grid2 = [
    [1, 1],
    [1, 1]
]
result2 = construct(grid2)
# Expected: isLeaf=True, val=1

# Test Case 3: Mixed values requiring splitting
grid3 = [
    [1, 1, 0, 0],
    [1, 1, 0, 0],
    [0, 0, 1, 1],
    [0, 0, 1, 1]
]
result3 = construct(grid3)
# Expected: isLeaf=False, with four quadrants as leaf nodes

# Test Case 4: Single element grid
grid4 = [[1]]
result4 = construct(grid4)
# Expected: isLeaf=True, val=1

# Test Case 5: Single element grid (0)
grid5 = [[0]]
result5 = construct(grid5)
# Expected: isLeaf=True, val=0

# Test Case 6: 4x4 grid with pattern
grid6 = [
    [1, 1, 1, 1],
    [1, 1, 1, 1],
    [1, 1, 1, 1],
    [1, 1, 1, 1]
]
result6 = construct(grid6)
# Expected: isLeaf=True, val=1

# Test Case 7: 4x4 grid with alternating values
grid7 = [
    [1, 0, 1, 0],
    [0, 1, 0, 1],
    [1, 0, 1, 0],
    [0, 1, 0, 1]
]
result7 = construct(grid7)
# Expected: isLeaf=False with multiple internal nodes

# Test Case 8: Uniform in 2x2 quadrants but different between quadrants
grid8 = [
    [1, 1, 0, 0],
    [1, 1, 0, 0],
    [0, 0, 1, 1],
    [0, 0, 1, 1]
]
result8 = construct(grid8)
# Expected: isLeaf=False with four leaf children

# Test Case 9: Complex 8x8 grid
grid9 = [
    [1, 1, 1, 1, 0, 0, 0, 0],
    [1, 1, 1, 1, 0, 0, 0, 0],
    [1, 1, 1, 1, 0, 0, 0, 0],
    [1, 1, 1, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 1, 1, 1, 1],
    [0, 0, 0, 0, 1, 1, 1, 1],
    [0, 0, 0, 0, 1, 1, 1, 1],
    [0, 0, 0, 0, 1, 1, 1, 1]
]
result9 = construct(grid9)
# Expected: isLeaf=False with four quadrants as leaves

# Test Case 10: 8x8 grid with some uniform regions
grid10 = [
    [1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 0, 0, 0, 0],
    [1, 1, 1, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0]
]
result10 = construct(grid10)
# Expected: isLeaf=False with internal structure