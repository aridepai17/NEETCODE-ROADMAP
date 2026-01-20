# VALIDATE BINARY SEARCH TREE

'''
Given the root of a binary tree, determine if it is a valid binary search tree (BST).
A valid BST is defined as follows:
The left subtree of a node contains only nodes with keys strictly less than the node's key.
The right subtree of a node contains only nodes with keys strictly greater than the node's key.
Both the left and right subtrees must also be binary search trees.
'''
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

'''
ALGORITHM:

This problem can be solved using either a Depth-First Search (DFS) or Breadth-First Search (BFS) approach,
maintaining a valid range (lower and upper bounds) for each node.

DFS Approach (Recursive):

1. Define a helper function `dfs(node, lower, upper)`:
   a. Base Case: If `node` is `None`, return `True` (an empty tree is a valid BST).
   b. Check if the current `node.val` violates the BST property:
      - If `node.val <= lower` or `node.val >= upper`, return `False`.
   c. Recursively check the left and right subtrees:
      - For the left child: `dfs(node.left, lower, node.val)` (the upper bound becomes `node.val`).
      - For the right child: `dfs(node.right, node.val, upper)` (the lower bound becomes `node.val`).
   d. Return `True` only if both recursive calls return `True`.
2. Call `dfs(root, float('-inf'), float('inf'))` to start the validation with initial infinite bounds.

BFS Approach (Iterative - as implemented below):

1. Initialize a `queue` using `collections.deque`.
2. Add the `root` node along with its initial `lower` bound (`float('-inf')`) and `upper` bound (`float('inf')`) to the `queue`.
   - `queue.append((root, float('-inf'), float('inf')))`
3. While the `queue` is not empty:
   a. Dequeue a `node`, `lower` bound, and `upper` bound from the left of the `queue`.
   b. If `node` is `None`, continue to the next iteration (nothing to validate).
   c. Check if the current `node.val` violates the BST property:
      - If `node.val <= lower` or `node.val >= upper`, return `False`.
   d. If `node.left` exists:
      - Enqueue (node.left, lower, node.val))
   e. If `node.right` exists:
      - Enqueue `(node.right, node.val, upper)` to the `queue`.
4. If the loop completes without returning `False`, it means all nodes satisfy the BST property, so return `True`.
'''

# DFS Approach (Recursive)
def isValidBST_DFS(root):
    def dfs(node, lower, upper):
        if not node:
            return True
        if not (lower < node.val < upper):
            return False
        
        return (dfs(node.left, lower, node.val) and
                dfs(node.right, node.val, upper))
    
    return dfs(root, float('-inf'), float('inf'))


# BFS Approach (Iterative)
import collections

def isValidBST(root):
    queue = collections.deque([(root, float('-inf'), float('inf'))])
    
    while queue:
        node, low, high = queue.popleft()
        
        if not (low < node.val < high):
            return False
        
        if node.left:
            queue.append((node.left, low, node.val))
        if node.right:
            queue.append((node.right, node.val, high))
            
    return True

'''
Time Complexity: O(N), where N is the number of nodes in the binary tree.
Each node is visited and processed exactly once.

Space Complexity: O(W), where W is the maximum width of the binary tree.
In the worst case (a complete binary tree), the queue can hold up to N/2 nodes, so O(N).
'''

# Test Cases
root1 = [2,1,3]
print(isValidBST(root1)) # Output: True

root2 = [5,1,4,null,null,3,6]
print(isValidBST(root2)) # Output: False

root3 = [5,4,6,null,null,3,7]
print(isValidBST(root3)) # Output: False

root4 = [1]
print(isValidBST(root4)) # Output: True

root5 = [1,1]
print(isValidBST(root5)) # Output: False

root6 = [10,5,15,null,null,6,20]
print(isValidBST(root6)) # Output: False

root7 = [3,1,5,0,2,4,6]
print(isValidBST(root7)) # Output: True

root8 = [3,1,5,0,4,2,6]
print(isValidBST(root8)) # Output: False

root9 = [0,null,-1]
print(isValidBST(root9)) # Output: False

root10 = [32,26,47,19,null,null,56,null,27]
print(isValidBST(root10)) # Output: False