# CONVERT BST TO GREATER TREE

'''
Given the root of a Binary Search Tree (BST), convert it to a Greater Tree such that every key of the original BST is changed to the original key plus the sum of all keys greater than the original key in BST.
As a reminder, a binary search tree is a tree that satisfies these constraints:
The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.
'''

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

'''
ALGORITHM:

1. Initialize a variable `totalSum` to 0. This will keep track of the running sum of all node values visited so far (from right to left).
2. Define a helper function `traverseTree(node)` that performs a reverse inorder traversal (right, root, left):
    a. If the `node` is `None`, return immediately (base case).
    b. Recursively call `traverseTree(node.right)` to process the right subtree first.
    c. Update `totalSum` by adding the current node's value: `totalSum += node.val`.
    d. Update the current node's value to `totalSum`: `node.val = totalSum`.
    e. Rec`ursively call `traverseTree(node.left)` to process the left subtree.
3. Call `traverseTree(root)` to start the conversion from the root.
4. Return the modified `root`.
'''

def convertBST(root):
    totalSum = 0
    
    def traverseTree(node):
        nonlocal totalSum
        if not node:
            return 
        
        traverseTree(node.right)
        totalSum += node.val
        node.val = totalSum
        traverseTree(node.left)
        
    traverseTree(root)
    return root

'''
Time Complexity: O(N), where N is the number of nodes in the binary tree.
We visit each node exactly once. The reverse inorder traversal processes all nodes in a single pass.

Space Complexity: O(H), where H is the height of the tree.
The recursion stack depth equals the height of the tree:
- Worst case (skewed tree): O(N)
- Best case (balanced tree): O(log N)
We also use O(1) extra space for the totalSum variable.
'''

# Test Cases

# Test Case 1: Standard BST
# Input: [4,1,6,0,2,5,7,null,null,null,3,null,null,null,8]
root1 = TreeNode(4, TreeNode(1, TreeNode(0), TreeNode(2, TreeNode(3))), TreeNode(6, TreeNode(5), TreeNode(7, None, TreeNode(8))))
result1 = convertBST(root1)
# Expected: [30, 36, 21, 36, 35, 26, 15, null, null, null, 33, null, null, null, 8]

# Test Case 2: Single node
root2 = TreeNode(0)
result2 = convertBST(root2)
# Expected: [0]

# Test Case 3: Empty tree
root3 = None
result3 = convertBST(root3)
# Expected: None

# Test Case 4: BST with only right children (right-skewed)
root4 = TreeNode(1, None, TreeNode(2, None, TreeNode(3)))
result4 = convertBST(root4)
# Expected: [6, 5, 3]

# Test Case 5: BST with only left children (left-skewed)
root5 = TreeNode(3, TreeNode(2, TreeNode(1)))
result5 = convertBST(root5)
# Expected: [3, 5, 6]

# Test Case 6: Balanced BST
root6 = TreeNode(5, TreeNode(3, TreeNode(1), TreeNode(4)), TreeNode(8, TreeNode(6), TreeNode(9)))
result6 = convertBST(root6)
# Expected: [32, 30, 26, 26, 25, 21, 9]

# Test Case 7: Two nodes
root7 = TreeNode(1, TreeNode(0), TreeNode(2))
result7 = convertBST(root7)
# Expected: [3, 3, 2]

# Test Case 8: BST with negative values
root8 = TreeNode(-2, TreeNode(-5), TreeNode(5, TreeNode(2), TreeNode(8)))
result8 = convertBST(root8)
# Expected: [13, 8, 8, 8, 5, 0]

# Test Case 9: BST with duplicate values (only if valid BST)
root9 = TreeNode(2, TreeNode(1), TreeNode(3))
result9 = convertBST(root9)
# Expected: [6, 6, 3]

# Test Case 10: Large value at root
root10 = TreeNode(100, TreeNode(50), TreeNode(150))
result10 = convertBST(root10)
# Expected: [250, 250, 150]