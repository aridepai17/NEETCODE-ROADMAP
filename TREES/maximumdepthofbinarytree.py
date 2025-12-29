# MAXIMUM DEPTH OF BINARY TREE

'''
Given the root of a binary tree, return its maximum depth.
A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.
'''

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

'''
ALGORITHM (Recursive Depth First Search):

1. Define a function `maxDepth` that takes the `root` of the binary tree as input.
2. Base Case: If the `root` is `None`, return `0` (an empty tree has a depth of 0).
3. Recursive Step:
   a. Recursively call `maxDepth` on the `left` child to get the depth of the left subtree.
   b. Recursively call `maxDepth` on the `right` child to get the depth of the right subtree.
   c. The maximum depth of the current tree is `1` (for the current node) plus the maximum of the depths of its left and right subtrees.
   d. Return `1 + max(maxDepth(root.left), maxDepth(root.right))`.

ALGORITHM (Breadth First Search - Level Order Traversal):

1. Define a function `maxDepthBFS` that takes the `root` of the binary tree as input.
2. If the `root` is `None`, return `0`.
3. Initialize `level` to `0` to count the depth.
4. Initialize a queue `q` using `collections.deque` and add the `root` to it.
5. While the `q` is not empty:
   a. Get the current `level_size` (number of nodes at the current level).
   b. Loop `level_size` times:
      i. Dequeue a `node` from the front of the `q`.
      ii. If `node.left` exists, enqueue it.
      iii. If `node.right` exists, enqueue it.
   c. Increment `level` by `1` (we have processed one full level).
6. Return `level`.

ALGORITHM (Iterative Depth First Search):

1. Define a function `maxDepthIBFS` that takes the `root` of the binary tree as input.
2. Initialize an empty stack `stack`.
3. If the `root` is not `None`, push a tuple `(root, 1)` ontothe stack `stack`.
4. Initialize `result` to `0`.
5. While the `stack` is not empty:
   a. Pop a `node` and its `depth` from the `stack`.
   b. If `node` is not `None`:
      i. Update `result = max(result, depth)`.
      ii. Push `(node.left, depth + 1)` onto the `stack`.
      iii. Push `(node.right, depth + 1)` onto the `stack`.
6. Return `result`.
'''

# Recursive Depth First Search
from collections import deque


def maxDepth(root):
    if not root:
        return 0
    
    return 1 + max(maxDepth(root.left), maxDepth(root.right))

'''
Time Complexity: O(N), where N is the number of nodes in the tree.
Space Complexity: O(H), where H is the height of the tree due to recursion stack.
'''

# Breadth First Search
def maxDepthBFS(root):
    if not root:
        return 0
    
    level = 0
    q = deque([root])
    
    while q:
        for i in range(len(q)):
            node = q.popleft()
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        level += 1
        
    return level

'''
Time Complexity: O(N), where N is the number of nodes in the tree.
Each node is visited and processed exactly once.

Space Complexity: O(W), where W is the maximum width of the tree.
In the worst case (a complete binary tree), the queue can hold up to N/2 nodes, so O(N).
In the best case (a skewed tree), the queue holds only one node at each level, so O(H) where H is the height.
'''

# Iterative Depth First Search
def maxDepthIDFS(root):
    stack = [(root, 1)]
    result = 0
    
    while stack:
        node, depth = stack.pop()
        if node:
            result = max(result, depth)
            stack.append([node.left, depth + 1])
            stack.append([node.right, depth + 1])
    
    return result

'''
Time Complexity: O(N), where N is the number of nodes in the tree.
Each node is pushed onto the stack and popped exactly once.

Space Complexity: O(H), where H is the height of the tree.
In the worst case (skewed tree), H can be N, so O(N).
In the best case (balanced tree), H is log N, so O(log N).
This space is used by the stack to store tree nodes and their depths.
'''

# Test Cases
root1 = [3,9,20,null,null,15,7]
print(maxDepth(root1)) # Output: 3


root2 = [1,2,2,3,3,null,null,4,4]
print(maxDepth(root2)) # Output: 3

root3 = [1]
print(maxDepth(root3)) # Output: 1

root4 = [1,2,2,3,null,null,3]
print(maxDepth(root4)) # Output: 3

root5 = [1,2,3,4,5,6,7,8,9]
print(maxDepth(root5)) # Output: 9

root6 = [1,2,2,3,3,4,4,5,5,6]
print(maxDepth(root6)) # Output: 6

root7 = [1,2,3,4,null,null,5,6,7,8]
print(maxDepth(root7)) # Output: 5

root8 = [1,2,3,4,5,6,7,8,9,10]
print(maxDepth(root8)) # Output: 10

root9 = [1,2,3,4,5,6,7,8,9,10,11]
print(maxDepth(root9)) # Output: 11

root10 = [1,2,3,4,5,6,7,8,9,10,11,12]
print(maxDepth(root10)) # Output: 12