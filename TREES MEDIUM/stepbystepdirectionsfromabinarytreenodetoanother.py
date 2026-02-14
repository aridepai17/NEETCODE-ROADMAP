# STEP BY STEP DIRECTIONS FROM A BINARY TREE NODE TO ANOTHER

'''
You are given the root of a binary tree with n nodes. Each node is uniquely assigned a value from 1 to n. 
You are also given an integer startValue representing the value of the start node s, and a different integer destValue representing the value of the destination node t.
Find the shortest path starting from node s and ending at node t. Generate step-by-step directions of such path as a string consisting of only the uppercase letters 'L', 'R', and 'U'. Each letter indicates a specific direction:
'L' means to go from a node to its left child node.
'R' means to go from a node to its right child node.
'U' means to go from a node to its parent node.
Return the step-by-step directions of the shortest path from node s to node t.
'''

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

'''
ALGORITHM:

1. Define a DFS helper function `dfs(node, target, path)` that finds the path from root to a specific target node:
    a. If node is None, return False (target not found).
    b. If node.val == target, return True (target found).
    c. Try to go left:
        - Append "L" to path
        - If dfs(node.left, target, path) returns True, we've found the path, return True
        - Otherwise, pop "L" from path (backtrack)
    d. Try to go right:
        - Append "R" to path
        - If dfs(node.right, target, path) returns True, return True
        - Otherwise, pop "R" from path (backtrack)
    e. Return False if target not found in this subtree.

2. Find paths from root to both startValue and destValue:
    - Call dfs(root, startValue, startPath)
    - Call dfs(root, destValue, destPath)

3. Find the common prefix of both paths:
    - Iterate through both paths simultaneously
    - Stop when paths differ or one ends
    - Let i be the index where paths diverge or end

4. Construct the result:
    - All remaining nodes in startPath after index i need to go up (U)
    - All remaining nodes in destPath from index i are the directions to destination
    - Result = "U" * len(startPath[i:]) + destPath[i:]

5. Return the joined result string.
'''

def getDirections(root, startValue, destValue):
    def dfs(node, target, path):
        if not node:
            return 
        
        if node.val == target:
            return True
        
        path.append("L")
        if dfs(node.left, target, path):
            return True
        path.pop()
        
        path.append("R")
        if dfs(node.right, target, path):
            return True
        path.pop()
        
        return False
    
    startPath = []
    destPath = []
    dfs(root, startValue, startPath)
    dfs(root, destValue, destPath)
    
    i = 0
    while i < len(startPath) and i < len(destPath) and startPath[i] == destPath[i]:
        i += 1
        
    result = ["U"] * len(startPath[i:]) + destPath[i:]
    return "".join(result)

'''
Time Complexity: O(N), where N is the number of nodes in the binary tree.
In the worst case, we traverse the entire tree twice (once for each target), plus O(H) for path comparison.
H is the height of the tree.

Space Complexity: O(H), where H is the height of the tree.
- We use O(H) space for storing each path (startPath and destPath)
- The recursion stack depth is O(H)
- We use O(H) for the result string
'''

# Test Cases

# Test Case 1: Simple case - start is parent of dest
# Tree:     5
#          / \
#         1   6
#        /
#       3
# Start: 5, Dest: 3
root1 = TreeNode(5, TreeNode(1, TreeNode(3)), TreeNode(6))
result1 = getDirections(root1, 5, 3)
print(result1) # Expected: "L"

# Test Case 2: Start is root, dest is right child
# Tree:     2
#          / \
#         1   3
# Start: 2, Dest: 3
root2 = TreeNode(2, TreeNode(1), TreeNode(3))
result2 = getDirections(root2, 2, 3)
print(result2) # Expected: "R"

# Test Case 3: Start and dest are siblings
# Tree:     1
#          / \
#         2   3
# Start: 2, Dest: 3
root3 = TreeNode(1, TreeNode(2), TreeNode(3))
result3 = getDirections(root3, 2, 3)
print(result3) # Expected: "UR"

# Test Case 4: Deep path
# Tree:     1
#          / \
#         2   3
#        / \
#       4   5
#      /
#     6
# Start: 6, Dest: 3
root4 = TreeNode(1, TreeNode(2, TreeNode(4, TreeNode(6)), TreeNode(5)), TreeNode(3))
result4 = getDirections(root4, 6, 3)
print(result4) # Expected: "UUUR"

# Test Case 5: Start is leaf, dest is root
# Tree:     5
#          / \
#         3   8
#        / \   \
#       1   4   9
# Start: 1, Dest: 5
root5 = TreeNode(5, TreeNode(3, TreeNode(1), TreeNode(4)), TreeNode(8, None, TreeNode(9)))
result5 = getDirections(root5, 1, 5)
print(result5) # Expected: "UU"

# Test Case 6: Long path going up and down
# Tree:     1
#          / \
#         2   3
#        /     \
#       4       5
#        \     /
#         6   7
# Start: 6, Dest: 7
root6 = TreeNode(1, TreeNode(2, TreeNode(4, None, TreeNode(6))), TreeNode(3, TreeNode(7), TreeNode(5)))
result6 = getDirections(root6, 6, 7)
print(result6) # Expected: "UURUUR"

# Test Case 7: Dest is left child of start's ancestor
# Tree:     5
#          / \
#         1   6
#        / \
#       2   3
# Start: 6, Dest: 2
root7 = TreeNode(5, TreeNode(1, TreeNode(2), TreeNode(3)), TreeNode(6))
result7 = getDirections(root7, 6, 2)
print(result7) # Expected: "UL"

# Test Case 8: Start is dest's ancestor going down
# Tree:     1
#          / \
#         2   3
#        / \
#       4   5
#        \
#         7
# Start: 2, Dest: 7
root8 = TreeNode(1, TreeNode(2, TreeNode(4, None, TreeNode(7)), TreeNode(5)), TreeNode(3))
result8 = getDirections(root8, 2, 7)
print(result8) # Expected: "LR"

# Test Case 9: Both are deep in different subtrees
# Tree:        1
#            /   \
#           2     3
#         /  \   /  \
#        4    5 6   7
#       /            \
#      8              9
# Start: 8, Dest: 9
root9 = TreeNode(1, TreeNode(2, TreeNode(4, TreeNode(8)), TreeNode(5)), TreeNode(3, TreeNode(6), TreeNode(7, None, TreeNode(9))))
result9 = getDirections(root9, 8, 9)
print(result9) # Expected: "UUURRRU"

# Test Case 10: Direct parent-child relationship
# Tree:     10
#          / \
#         5   15
# Start: 15, Dest: 10
root10 = TreeNode(10, TreeNode(5), TreeNode(15))
result10 = getDirections(root10, 15, 10)
print(result10) # Expected: "U"