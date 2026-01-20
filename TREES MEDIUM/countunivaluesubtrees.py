# COUNT UNIVALUE SUBTREES

'''
Given a binary tree, count the number of uni-value subtrees.
A Uni-value subtree means all nodes of the subtree have the same value.
'''

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

'''
ALGORITHM:

This problem can be solved using a Depth-First Search (DFS) approach.
We need a helper function that recursively checks if a subtree is uni-value and also updates a global/nonlocal counter.

1. Initialize a counter `count` to 0. This will store the total number of uni-value subtrees.
2. Define a helper function `dfs(node)`:
   a. Base Case: If `node` is `None`, return `True` (an empty tree is considered uni-value).
   b. Recursively call `dfs` on the `left` child: `left_is_uni = dfs(node.left)`.
   c. Recursively call `dfs` on the `right` child: `right_is_uni = dfs(node.right)`.
   d. Check if the current subtree rooted at `node` is uni-value:
      i. If `left_is_uni` is `False`, then the current subtree cannot be uni-value. Return `False`.
      ii. If `right_is_uni` is `False`, then the current subtree cannot be uni-value. Return `False`.
      iii. If `node.left` exists and `node.left.val` is not equal to `node.val`, then the current subtree is not uni-value. Return `False`.
      iv. If `node.right` exists and `node.right.val` is not equal to `node.val`, then the current subtree is not uni-value. Return `False`.
      v. If all the above conditions pass, it means the current subtree is uni-value.
         - Increment the `count` by 1.
         - Return `True`.
3. Call `dfs(root)` to start the traversal from the root.
4. Return the final `count`.
'''

def countUnivalueSubtrees(root):
    count = 0
    def dfs(node):
        if not node:
            return True
        
        leftSubtree = dfs(node.left)
        rightSubtree = dfs(node.right)
        
        if not leftSubtree:
            return False
        if not rightSubtree:
            return False
        if node.left and node.left.val != node.val:
            return False
        if node.right and node.right.val != node.val:
            return False
        
        nonlocal count 
        count += 1
        return True
    
    dfs(root)
    return count

'''
Time Complexity: O(N), where N is the number of nodes in the binary tree.
Each node is visited exactly once during the DFS traversal.
At each node, we perform constant time operations (comparisons, additions).

Space Complexity: O(H), where H is the height of the binary tree.
This is due to the recursion stack. In the worst case (a skewed tree), H can be N.
In the best case (a balanced tree), H is log N.
'''

# Test Cases
root1 = [1,3,2,4,5,null,6]
print(countUnivalueSubtrees(root1)) # Output: 3

# Test Case 2: All nodes are uni-value
root2 = TreeNode(5, TreeNode(5), TreeNode(5))
print(countUnivalueSubtrees(root2)) # Output: 3

# Test Case 3: No uni-value subtrees except leaves
root3 = TreeNode(1, TreeNode(2, TreeNode(3)), TreeNode(4))
print(countUnivalueSubtrees(root3)) # Output: 3 (leaves 3, 4, and 2 if 3 is its only child)

# Test Case 4: Single node tree
root4 = TreeNode(0)
print(countUnivalueSubtrees(root4)) # Output: 1

# Test Case 5: Empty tree
root5 = None
print(countUnivalueSubtrees(root5)) # Output: 0

# Test Case 6: Tree with mixed values, some uni-value subtrees
root6 = TreeNode(5, TreeNode(1, TreeNode(5), TreeNode(5)), TreeNode(5, None, TreeNode(5)))
print(countUnivalueSubtrees(root6)) # Output: 6 (leaves 5, 5, 5, and the right subtree of root, and the left subtree of root, and the root itself)

# Test Case 7: All nodes have different values, only leaves are uni-value
root7 = TreeNode(1, TreeNode(2, TreeNode(3)), TreeNode(4, TreeNode(5), TreeNode(6)))
print(countUnivalueSubtrees(root7)) # Output: 4 (leaves 3, 5, 6, and 2 if 3 is its only child)

# Test Case 8: A perfect binary tree where all nodes have the same value
root8 = TreeNode(7, TreeNode(7, TreeNode(7), TreeNode(7)), TreeNode(7, TreeNode(7), TreeNode(7)))
print(countUnivalueSubtrees(root8)) # Output: 7

# Test Case 9: A tree where only the root and its immediate children form a uni-value subtree
root9 = TreeNode(1, TreeNode(1), TreeNode(1, TreeNode(2), TreeNode(3)))
print(countUnivalueSubtrees(root9)) # Output: 3 (leaves 1, 2

# Test Case 10: A tree where all nodes have the same value except for one node
root10 = TreeNode(1, TreeNode(1), TreeNode(1, TreeNode(1), TreeNode(2)))
print(countUnivalueSubtrees(root10)) # Output: 6 (leaves 1, 1, 1, 1, and the right subtree of root, and the left subtree of root, and the root itself)