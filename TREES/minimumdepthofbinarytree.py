# MINIMUM DEPTH OF BINARY TREE

'''
Given a binary tree, find its minimum depth.
The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.
Note: A leaf is a node with no children.
'''

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

'''
ALGORITHM (Recursive Depth First Search Solution):

1. Define a function `minimumDepth` that takes the `root` of the binary tree as input.
2. Base Case: If the `root` is `None`, return `0` (an empty tree has a depth of 0).
3. Initialize `minimum` to `float('inf')` to store the shortest path found.
4. Define a helper function `dfs(node, depth)`:
   a. Declare `minimum` as `nonlocal` to modify the variable in the outer scope.
   b. Base Case: If `node` is a leaf node (i.e., `node.left` is `None` AND `node.right` is `None`):
      - Update `minimum = min(minimum, depth)`.
      - Return.
   c. Recursive Step:
      - If `node.left` exists, recursively call `dfs(node.left, depth + 1)`.
      - If `node.right` exists, recursively call `dfs(node.right, depth + 1)`.
5. Call the `dfs` function with the `root` and an initial `depth` of `1`.
6. Return the final `minimum`.

ALGORITHM (Breadth First Search Solution):

1. Define a function `minimumDepth2` that takes the `root` of the binary tree as input.
2. Base Case: If the `root` is `None`, return `0`.
3. Initialize a queue `q` using `collections.deque` and add a tuple `(root, 1)` to it (node and its depth).
4. While the `q` is not empty:
   a. Dequeue a `node` and its `depth` from the left of the `q`.
   b. If `node` is a leaf node (i.e., `node.left` is `None` AND `node.right` is `None`):
      - Return `depth` (this is the first leaf encountered, so it's the minimum depth).
   c. If `node.left` exists, add `(node.left, depth + 1)` to the queue.
   d. If `node.right` exists, add `(node.right, depth + 1)` to the queue.
'''

# Recursive Depth First Search Solution
def minimumDepth(root):
    if not root:
        return 0
    minimum = float('inf')
    
    def dfs(node, depth):
        nonlocal minimum
        if not node.left and not node.right:
            minimum = min(minimum, depth)
            return
        if node.left:
            dfs(node.left, depth + 1)
        if node.right:
            dfs(node.right, depth + 1)
        
    dfs(root, 1)
    return minimum

'''
Time Complexity: O(N), where N is the number of nodes in the tree.
In the worst case, we might visit every node to find the minimum depth.

Space Complexity: O(H), where H is the height of the tree.
This is due to the recursion stack. In the worst case (a skewed tree), H can be N.
In the best case (a balanced tree), H is log N.
'''

# Breadth First Search Solution
def minimumDepth2(root):
    if not root:
        return 0
    
    q = deque([(root, 1)])
    
    while q:
        node, depth = q.popleft()
        if not node.left and not node.right:
            return depth
        if node.left:
            q.append((node.left, depth + 1))
        if node.right:
            q.append((node.right, depth + 1))

'''
Time Complexity: O(N), where N is the number of nodes in the tree.
Each node is visited and processed exactly once.

Space Complexity: O(W), where W is the maximum width of the tree.
In the worst case (a complete binary tree), the queue can hold up to N/2 nodes, so O(N).
In the best case (a skewed tree), the queue holds only one node at each level, so O(H) where H is the height.
'''

# Test Cases
root1 = [3,9,20,null,null,15,7]
print(minimumDepth(root1)) # Output: 2

root2 = [2,null,3,null,4,null,5,null,6]
print(minimumDepth(root2)) # Output: 5

root3 = [1]
print(minimumDepth(root3)) # Output: 1

root4 = [1,2]
print(minimumDepth(root4)) # Output: 2

root5 = [1,2,3,4,5]
print(minimumDepth(root5)) # Output: 2

root6 = [1,2,null,3,null,4]
print(minimumDepth(root6)) # Output: 4

root7 = [1,null,2,3,null,4,null,5]
print(minimumDepth(root7)) # Output: 5

root8 = [1,2,3,null,null,4,5,6,7]
print(minimumDepth(root8)) # Output: 3

root9 = [1,2,3,4,null,null,5]
print(minimumDepth(root9)) # Output: 3

root10 = [1,2,null,3]
print(minimumDepth(root10)) # Output: 3