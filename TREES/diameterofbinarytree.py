# DIAMETER OF BINARY TREE

'''
Given the root of a binary tree, return the length of the diameter of the tree.
The diameter of a binary tree is the length of the longest path between any two nodes in a tree. 
This path may or may not pass through the root.
The length of a path between two nodes is represented by the number of edges between them.
'''

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

'''
ALGORITHM:

1. Initialize a variable `result` to 0. This variable will store the maximum diameter found so far.
2. Define a helper function `dfs(current)` that takes a `TreeNode` as input:
   a. Base Case: If `current` is `None`, return 0 (the height of an empty subtree is 0).
   b. Recursively call `dfs` on the `left` child: `left = dfs(current.left)`. This gets the height of the left subtree.
   c. Recursively call `dfs` on the `right` child: `right = dfs(current.right)`. This gets the height of the right subtree.
   d. Update the `result`: `result = max(result, left + right)`. The diameter passing through the `current` node would be the sum of the heights of its left and right subtrees. We take the maximum of this value and the `result` found so far.
   e. Return `1 + max(left, right)`. This is the height of the subtree rooted at `current` (1 for the current node itself, plus the maximum height of its children).
3. Call the `dfs` function with the `root` of the binary tree: `dfs(root)`.
4. Return the final `result`.
'''

def diameterOfBinaryTree(root):
    result = 0
    
    def dfs(current):
        if not current:
            return 0
        
        left = dfs(current.left)
        right = dfs(current.right)
        
        nonlocal result
        result = max(result, left + right)
        
        return 1 + max(left, right)
    
    dfs(root)
    return result

'''
Time Complexity: O(N), where N is the number of nodes in the tree.
This is because we visit each node exactly once.

Space Complexity: O(H), where H is the height of the tree.
This is due to the recursion stack. In the worst case (skewed tree), H can be N.
In the best case (balanced tree), H is log N.
'''

# Test Cases
root1 = [1,2,3,4,5]
print(diameterOfBinaryTree(root1)) # Output: 3

root2 = [1,2]
print(diameterOfBinaryTree(root2)) # Output: 1

root3 = [1]
print(diameterOfBinaryTree(root3)) # Output: 0

root4 = [1,2,3]
print(diameterOfBinaryTree(root4)) # Output: 2

root5 = [4,-7,-3,null,null,-9,-3,9,-7,-4,null,6,null,-6,-6,null,null,0,6,5,null,9,null,null,-1,-4,null,null,null,-2]
print(diameterOfBinaryTree(root5)) # Output: 8

root6 = [1,null,2,null,3,null,4,null,5]
print(diameterOfBinaryTree(root6)) # Output: 4

root7 = [1,2,null,3,null,4,null,5]
print(diameterOfBinaryTree(root7)) # Output: 4

root8 = [1,2,3,4,5,6,7]
print(diameterOfBinaryTree(root8)) # Output: 4

root9 = [1,2,null,3,4,null,null,5,6]
print(diameterOfBinaryTree(root9)) # Output: 5

root10 = [1,null,2,3,4,5,6,7,8]
print(diameterOfBinaryTree(root10)) # Output: 6