# BINARY TREE RIGHT SIDE VIEW

'''
Given the root of a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.
'''

import collections

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

'''
ALGORITHM:

1. Initialize an empty list `result` to store the values of the rightmost nodes.
2. Initialize a deque `queue` and add the `root` node to it.
3. While the `queue` is not empty:
   a. Initialize `rightSide` to `None`. This variable will store the rightmost node of the current level.
   b. Get the `qLength` (length of the queue), which represents the number of nodes at the current level.
   c. Iterate `qLength` times (to process all nodes at the current level):
      i. Dequeue a `node` from the left of the `queue`.
      ii. If `node` is not `None`:
          - Set `rightSide` to `node` (the last valid node encountered at this level will be the rightmost).
          - If `node.left` exists, enqueue it to the right of the `queue`.
          - If `node.right` exists, enqueue it to the right of the `queue`.
   d. After processing all nodes at the current level, if `rightSide` is not `None`:
      - Append `rightSide.val` to the `result` list.
4. Return the `result` list.
'''

def rightSideView(root):
    result = []
    queue = collections.deque([root])
    
    while queue:
        rightSide = None
        qLength = len(queue)
        for i in range(qLength):
            node = queue.popleft()
            if node:
                rightSide = node
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
        if rightSide:
            resulta.append(rightSide.val)
            
    return result

'''
Time Complexity: O(N), where N is the number of nodes in the binary tree.
Each node is visited and processed exactly once during the BFS traversal.

Space Complexity: O(W), where W is the maximum width of the binary tree.
In the worst case (a complete binary tree), the queue can hold up to N/2 nodes, so O(N).
'''

# Test Cases
root1 = [1,2,3,null,5,null,4]
print(rightSideView(root1)) # Output: [1,3,4]

root2 = [1,null,3]
print(rightSideView(root2)) # Output: [1,3]

root3 = []
print(rightSideView(root3)) # Output: []

root4 = [1,2,3,4,5,6,7]
print(rightSideView(root4)) # Output: [1,3,7]

root5 = [1,2]
print(rightSideView(root5)) # Output: [1,2]

root6 = [1,null,2,null,3,null,4]
print(rightSideView(root6)) # Output: [1,2,3,4]

root7 = [1,2,null,3,null,4]
print(rightSideView(root7)) # Output: [1,2,3,4]

root8 = [1,2,3,null,5,null,4,6,7,8,9]
print(rightSideView(root8)) # Output: [1,3,4,9]

root9 = [1,2,3,4,null,5,null,6,null,7,null,8]
print(rightSideView(root9)) # Output: [1,3,5,7,8]

root10 = [1,null,2,3,null,4,null,5,null,6]
print(rightSideView(root10)) # Output: [1,2,3,4,5,6]