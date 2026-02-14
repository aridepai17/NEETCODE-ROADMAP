# DIAMETER OF BINARY TREE

'''
Given a binary tree, you need to compute the length of the diameter of the tree. 
The diameter of a binary tree is the length of the longest path between any two nodes in a tree.
'''

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

'''
ALGORITHM:

1. Initialize a variable `diameter` to 0. This will track the maximum diameter found so far.
2. Define a helper function `getHeight(node)` that returns the height of the subtree rooted at `node`:
    a. If `node` is `None`, return 0 (height of empty tree).
    b. Recursively compute the height of the left subtree: `leftHeight = getHeight(node.left)`.
    c. Recursively compute the height of the right subtree: `rightHeight = getHeight(node.right)`.
    d. Update `diameter` to be the maximum of current `diameter` and the sum of `leftHeight + rightHeight`.
        This represents the diameter passing through the current node.
    e. Return the height of the current subtree: `1 + max(leftHeight, rightHeight)`.
3. Call `getHeight(root)` to start the computation from the root.
4. Return `diameter`, which contains the length of the longest path between any two nodes.
'''

def diameterOfBinaryTree(root):
    diameter = 0
    
    def getHeight(node):
        nonlocal diameter
        if not node:
            return 0
        
        leftHeight = getHeight(node.left)
        rightHeight = getHeight(node.right)
        
        diameter = max(diameter, leftHeight + rightHeight)
        
        return 1 + max(leftHeight, rightHeight)
    
    getHeight(root)
    return diameter

'''
Time Complexity: O(N), where N is the number of nodes in the binary tree.
We visit each node exactly once, performing constant-time operations at each node.

Space Complexity: O(H), where H is the height of the tree.
The recursion stack depth equals the height of the tree:
- Worst case (skewed tree): O(N)
- Best case (balanced tree): O(log N)
We also use O(1) extra space for the diameter variable.
'''

# Test Cases

# Test Case 1: Standard tree with diameter through root
# Input: [1,2,3,4,5]
root1 = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3))
result1 = diameterOfBinaryTree(root1)
print(result1) # Expected: 3 (path: 4 -> 2 -> 1 -> 3)

# Test Case 2: Single node
root2 = TreeNode(1)
result2 = diameterOfBinaryTree(root2)
print(result2) # Expected: 0

# Test Case 3: Empty tree
root3 = None
result3 = diameterOfBinaryTree(root3)
print(result3) # Expected: 0

# Test Case 4: Diameter on the left side
# Input: [1,2,3,4,5,6,7]
root4 = TreeNode(1, TreeNode(2, TreeNode(3, TreeNode(4, TreeNode(5)))))
result4 = diameterOfBinaryTree(root4)
print(result4) # Expected: 4 (path: 5 -> 4 -> 3 -> 2 -> 1)

# Test Case 5: Diameter on the right side
root5 = TreeNode(1, None, TreeNode(2, None, TreeNode(3, None, TreeNode(4, None, TreeNode(5)))))
result5 = diameterOfBinaryTree(root5)
print(result5) # Expected: 4 (path: 1 -> 2 -> 3 -> 4 -> 5)

# Test Case 6: Balanced tree
root6 = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3, TreeNode(6), TreeNode(7)))
result6 = diameterOfBinaryTree(root6)
print(result6) # Expected: 4 (path: 4 -> 2 -> 1 -> 3 -> 7)

# Test Case 7: Two nodes
root7 = TreeNode(1, TreeNode(2))
result7 = diameterOfBinaryTree(root7)
print(result7) # Expected: 1 (path: 1 -> 2)

# Test Case 8: Tree with only right children
root8 = TreeNode(1, None, TreeNode(2, None, TreeNode(3)))
result8 = diameterOfBinaryTree(root8)
print(result8) # Expected: 2 (path: 1 -> 2 -> 3)

# Test Case 9: Tree with only left children
root9 = TreeNode(1, TreeNode(2, TreeNode(3)))
result9 = diameterOfBinaryTree(root9)
print(result9) # Expected: 2 (path: 3 -> 2 -> 1)

# Test Case 10: Wide tree with diameter not passing through root
# Input: [1,2,3,4,5,6,7,8,9,10]
root10 = TreeNode(1, TreeNode(2, TreeNode(4, TreeNode(8), TreeNode(9)), TreeNode(5)), TreeNode(3, TreeNode(6), TreeNode(7, TreeNode(10))))
result10 = diameterOfBinaryTree(root10)
print(result10) # Expected: 6 (path: 8 -> 4 -> 2 -> 1 -> 3 -> 7 -> 10)