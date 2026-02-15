# BINARY TREE MAXIMUM PATH SUM

'''
A path in a binary tree is a sequence of nodes where each pair of adjacent nodes in the sequence has an edge connecting them. 
A node can only appear in the sequence at most once. Note that the path does not need to pass through the root.
The path sum of a path is the sum of the node's values in the path.
Given the root of a binary tree, return the maximum path sum of any non-empty path.
'''

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

'''
ALGORITHM:

1. Initialize `maxSum` to negative infinity to handle negative values in the tree.
2. Define a recursive helper function `getGain(node)` that returns the maximum gain from this node to any of its descendants:
    a. Base case: If node is None, return 0 (no contribution).
    b. Recursively get the gain from left subtree: `leftGain = max(getGain(node.left), 0)`
        - We use max() with 0 because we can choose to not include the subtree if it has negative values.
    c. Recursively get the gain from right subtree: `rightGain = max(getGain(node.right), 0)`
    d. Calculate the path sum passing through the current node:
        `currentPathSum = node.val + leftGain + rightGain`
    e. Update the global maximum: `maxSum = max(maxSum, currentPathSum)`
    f. Return the gain that can be passed to parent: `node.val + max(leftGain, rightGain)`
        (We can only use one child branch when extending the path upward)
3. Call `getGain(root)` to start the computation.
4. Return `maxSum`, which contains the maximum path sum.
'''

def maximumPathSum(root):
    maxSum = float('-inf')
    
    def getGain(node):
        nonlocal maxSum
        if not node:
            return 0
        
        leftGain = max(getGain(node.left), 0)
        rightGain = max(getGain(node.right), 0)
        
        currentPathSum = node.val + leftGain + rightGain
        maxSum = max(maxSum, currentPathSum)
        
        return node.val + max(leftGain, rightGain)
    
    getGain(root)
    return maxSum

'''
Time Complexity: O(N), where N is the number of nodes in the binary tree.
We visit each node exactly once, performing constant-time operations at each node.

Space Complexity: O(H), where H is the height of the tree.
The recursion stack depth equals the height of the tree:
- Worst case (skewed tree): O(N)
- Best case (balanced tree): O(log N)
We also use O(1) extra space for the maxSum variable.
'''

# Test Cases

# Test Case 1: Standard tree with positive and negative values
# Tree:      1
#           / \
#          2   3
root1 = TreeNode(1, TreeNode(2), TreeNode(3))
result1 = maximumPathSum(root1)
print(result1) # Expected: 6 (path: 2 -> 1 -> 3)

# Test Case 2: Single node
root2 = TreeNode(1)
result2 = maximumPathSum(root2)
print(result2) # Expected: 1

# Test Case 3: Tree with negative values
# Tree:      -1
#           / \
#          -2  -3
root3 = TreeNode(-1, TreeNode(-2), TreeNode(-3))
result3 = maximumPathSum(root3)
print(result3) # Expected: -1 (just the root)

# Test Case 4: Mix of positive and negative
# Tree:      2
#           /
#          1
#         /
#        -1
root4 = TreeNode(2, TreeNode(1, TreeNode(-1)))
result4 = maximumPathSum(root4)
print(result4) # Expected: 3 (path: -1 -> 1 -> 2)

# Test Case 5: Path goes through root with negative children
# Tree:      10
#           /  \
#         -2    -3
root5 = TreeNode(10, TreeNode(-2), TreeNode(-3))
result5 = maximumPathSum(root5)
print(result5) # Expected: 10 (just the root, since children are negative)

# Test Case 6: Complex tree
# Tree:       1
#            / \
#           2   3
#          / \
#         4   5
root6 = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3))
result6 = maximumPathSum(root6)
print(result6) # Expected: 11 (path: 4 -> 2 -> 1 -> 3)

# Test Case 7: All negative except one positive
# Tree:      -5
#           / \
#         -1   -2
root7 = TreeNode(-5, TreeNode(-1), TreeNode(-2))
result7 = maximumPathSum(root7)
print(result7) # Expected: -1

# Test Case 8: Path ending at leaf
# Tree:       4
#            / \
#           1   2
root8 = TreeNode(4, TreeNode(1), TreeNode(2))
result8 = maximumPathSum(root8)
print(result8) # Expected: 7 (path: 1 -> 4 -> 2)

# Test Case 9: Deep tree
# Tree:       1
#            /
#           2
#          /
#         3
#        /
#       4
root9 = TreeNode(1, TreeNode(2, TreeNode(3, TreeNode(4))))
result9 = maximumPathSum(root9)
print(result9) # Expected: 10 (path: 4 -> 3 -> 2 -> 1)

# Test Case 10: Tree with zeros
# Tree:       0
#            / \
#           0   0
root10 = TreeNode(0, TreeNode(0), TreeNode(0))
result10 = maximumPathSum(root10)
print(result10) # Expected: 0
