# UNIVALUED BINARY TREE

'''
A binary tree is uni-valued if every node in the tree has the same value.
Given the root of a binary tree, return true if the given tree is uni-valued, or false otherwise.
'''

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

'''
ALGORITHM:

1. Define a function `univaluedTree` that takes the `root` of the binary tree as input.
2. If the `root` is `None`, return `True` (an empty tree is considered uni-valued).
3. Store the value of the `root` node in a variable, say `value`. This will be the reference value for all other nodes.
4. Define a helper function `dfs(node)` for a depth-first traversal:
   a. Base Case: If `node` is `None`, return `True` (an empty subtree is uni-valued).
   b. Check if the current `node.val` is equal to the `value` stored from the root.
      - If `node.val` is NOT equal to `value`, return `False` immediately (the tree is not uni-valued).
   c. Recursively call `dfs` on the `left` child: `dfs(node.left)`.
   d. Recursively call `dfs` on the `right` child: `dfs(node.right)`.
   e. Return `True` only if both recursive calls return `True` (meaning both subtrees are uni-valued with respect to the `value`).
5. Call the `dfs` function with the `root` of the binary tree.
6. Return the result of the `dfs` call.
'''

def univaluedTree(root):
    value = root.val
    def dfs(node):
        if not node:
            return True
        if node.val != value:
            return False
        return dfs(node.left) and dfs(node.right)
    return dfs(root)

'''
Time Complexity: O(N), where N is the number of nodes in the tree.
This is because we visit each node exactly once. In the worst case, we might traverse the entire tree to confirm it's univalued or find a differing node.

Space Complexity: O(H), where H is the height of the tree.
This is due to the recursion stack. In the worst case (skewed tree), H can be N.
In the best case (balanced tree), H is log N.
'''

# Test Cases
root1 = [1,1,1,1,1,null,1]
print(univaluedTree(root1)) # Output: True

root2 = [2,2,2,5,2]
print(univaluedTree(root2)) # Output: False

root3 = [1]
print(univaluedTree(root3)) # Output: True

root4 = [1,1,1]
print(univaluedTree(root4)) # Output: True

root5 = [1,2,1]
print(univaluedTree(root5)) # Output: False

root6 = [1,null,1]
print(univaluedTree(root6)) # Output: True

root7 = [1,1,null,1]
print(univaluedTree(root7)) # Output: True

root8 = [1,1,1,null,2]
print(univaluedTree(root8)) # Output: False

root9 = [0,0,0,0,0,0,0]
print(univaluedTree(root9)) # Output: True

root10 = [0,0,0,0,0,0,1]
print(univaluedTree(root10)) # Output: False