# BINARY TREE ZIGZAG LEVEL ORDER TRAVERSAL

'''
Given the root of a binary tree, return the zigzag level order traversal of its nodes' values. (i.e., from left to right, then right to left for the next level and alternate between).
'''

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

'''
ALGORITHM:

1. Initialize an empty list `result` to store the zigzag level order traversal.
2. Initialize a deque `q` with the `root` node if it exists, otherwise an empty deque.
3. Initialize a variable `level` to 0 to keep track of the current level number.
4. While the `q` is not empty:
   a. Initialize an empty list `level` to store the nodes' values at the current level.
   b. Get the `size` of the queue, which represents the number of nodes at the current level.
   c. Iterate `size` times:
      i. Dequeue a `node` from the left of the `q`.
      ii. Append `node.val` to `level`.
      iii. If `node.left` exists, enqueue it to the right of the `q`.
      iv. If `node.right` exists, enqueue it to the right of the `q`.
   d. After processing all nodes at the current level:
      i. If `level` is odd (meaning it's the second, fourth, etc. level), reverse `level`.
      ii. Append `level` to the `result` list.
5. Return the `result` list.
'''

from collections import deque

def zigzagLevelOrder(root):
    result = []
    q = deque([root] if root else [])
    
    while q:
        level = []
        for i in range(len(q)):
            node = q.popleft()
            level.append(node.val)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        level = level[::-1] if len(result) % 2 else level
        result.append(level)
        
    return result

'''
Time Complexity: O(N), where N is the number of nodes in the binary tree.
Each node is visited and processed exactly once.

Space Complexity: O(W), where W is the maximum width of the tree.
In the worst case (a complete binary tree), the queue can hold up to N/2 nodes, so O(N).
In the best case (a skewed tree), the queue holds only one node at each level, so O(H) where H is the height.
The `level` list also contributes to space, storing nodes for the current level, which can be O(W).
'''

# Test Cases
root1 = [3,9,20,null,null,15,7]
print(zigzagLevelOrder(root1)) # Output: [[3],[20,9],[15,7]]

root2 = [1]
print(zigzagLevelOrder(root2)) # Output: [[1]]

root3 = [1,2]
print(zigzagLevelOrder(root3)) # Output: [[1],[2]]

root4 = [1,2,3]
print(zigzagLevelOrder(root4)) # Output: [[1],[3,2]]

root5 = [1,2,3,null,4]
print(zigzagLevelOrder(root5)) # Output: [[1],[3,2],[4]]

root6 = [1,2,3,null,4,null,5]
print(zigzagLevelOrder(root6)) # Output: [[1],[3,2],[5,4]]

root7 = [1,2,3,null,4,null,5,null,6]
print(zigzagLevelOrder(root7)) # Output: [[1],[3,2],[6,5,4]]

root8 = [1,2,3,null,4,null,5,null,6,null,7]
print(zigzagLevelOrder(root8)) # Output: [[1],[3,2],[7,6,5,4]]

root9 = [1,2,3,null,4,null,5,null,6,null,7,null,8]
print(zigzagLevelOrder(root9)) # Output: [[1],[3,2],[8,7,6,5,4]]

root10 = [1,2,3,null,4,null,5,null,6,null,7,null,8,null,9]
print(zigzagLevelOrder(root10)) # Output: [[1],[3,2],[9,8,7,6,5,4]]