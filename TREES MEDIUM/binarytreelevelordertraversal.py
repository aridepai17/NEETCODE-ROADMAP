# BINARY TREE LEVEL ORDER TRAVERSAL

'''
Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).
'''

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

'''
ALGORITHM:

1. Initialize an empty list `result` to store the level order traversal.
2. Initialize a deque `q` (queue) and add the `root` node to it. If the `root` is `None`, the queue will be empty.
3. While the `q` is not empty:
   a. Get the current `lenQ` (length of the queue), which represents the number of nodes at the current level.
   b. Initialize an empty list `level` to store the values of nodes at the current level.
   c. Iterate `lenQ` times:
      i. Dequeue a `node` from the left of the `q`.
      ii. If `node` is not `None`:
         - Append `node.val` to the `level` list.
         - Enqueue `node.left` to the right of the `q`.
         - Enqueue `node.right` to the right of the `q`.
   d. After processing all nodes at the current level, if the `level` list is not empty (meaning there were actual nodes at this level):
      - Append `level` to the `result` list.
4. Return the `result` list.
'''

from collections import deque

def BFS(root):
    result = []
    q = deque([root])
    
    while q:
        lenQ = len(q)
        level = []
        for i in range(lenQ):
            node = q.popleft()
            if node:
                level.append(node.val)
                q.append(node.left)
                q.append(ndoe.right)
        if level:
            result.append(level)
            
    return result

'''
Time Complexity: O(N), where N is the number of nodes in the binary tree.
Each node is visited and processed exactly once.

Space Complexity: O(W), where W is the maximum width of the tree.
In the worst case (a complete binary tree), the queue can hold up to N/2 nodes, so O(N).
The `level` list also contributes to space, storing nodes for the current level, which can be O(W).
'''

# Test Cases
root1 = [3,9,20,null,null,15,7]
print(BFS(root1)) # Output: [[3], [9, 20], [15, 7]]

root2 = [1]
print(BFS(root2)) # Output: [[1]]

root3 = []
print(BFS(root3)) # Output: []

root4 = [1,2,3,4,5,6,7]
print(BFS(root4)) # Output: [[1], [2, 3], [4, 5, 6, 7]]

root5 = [1,null,2,3]
print(BFS(root5)) # Output: [[1], [2], [3]]

root6 = [1,2,null,3,null,4,null,5]
print(BFS(root6)) # Output: [[1], [2], [3], [4], [5]]

root7 = [1,2,3,4,null,null,5]
print(BFS(root7)) # Output: [[1], [2, 3], [4, 5]]

root8 = [1,2,3,null,4,5,null]
print(BFS(root8)) # Output: [[1], [2, 3], [4, 5]]

root9 = [1,null,2,null,null,3,null,null,null,4]
print(BFS(root9)) # Output: [[1], [2], [3], [4]]

root10 = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
print(BFS(root10)) # Output: [[1], [2, 3], [4, 5, 6, 7], [8, 9, 10, 11, 12, 13, 14, 15]]