# MAXIMUM WIDTH OF BINARY TREE

'''
Given the root of a binary tree, return the maximum width of the given tree.
The maximum width of a tree is the maximum width among all levels.
The width of one level is defined as the length between the end-nodes (the leftmost and rightmost non-null nodes), where the null nodes between the end-nodes that would be present in a complete binary tree extending down to that level are also counted into the length calculation.
It is guaranteed that the answer will in the range of a 32-bit signed integer.
'''

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

'''
ALGORITHM:

1. If the `root` is `None`, return `0` as there is no tree.
2. Initialize a `queue` with a tuple containing the `root` node and its position `0`.
   The position is used to track the relative index of nodes in a complete binary tree.
3. Initialize `answer` to `0`. This variable will store the maximum width found.
4. While the `queue` is not empty:
   a. Get the `firstPosition` (index) of the leftmost node in the current level from `queue[0][1]`.
   b. Get the `lastPosition` (index) of the rightmost node in the current level from `queue[-1][1]`.
   c. Update `answer` with the maximum of its current value and `lastPosition - firstPosition + 1`.
      This calculates the width of the current level.
   d. Initialize an empty list `nextLevel` to store nodes for the next level.
   e. Iterate through each `node` and `position` in the current `queue`:
      i. If `node.left` exists:
         - Append a tuple `(node.left, 2 * position)` to `nextLevel`.
         - The left child of a node at position `p` in a complete binary tree is at `2 * p`.
      ii. If `node.right` exists:
         - Append a tuple `(node.right, 2 * position + 1)` to `nextLevel`.
         - The right child of a node at position `p` in a complete binary tree is at `2 * p + 1`.
   f. Set `queue` to `nextLevel` to process the next level.
5. Return the final `answer`.
'''

def widthOfBinaryTree(root):
    if not root:
        return 0
    
    queue = [(root, 0)]
    answer = 0
    
    while queue:
        firstPosition = queue[0][1]
        lastPosition = queue[-1][1]
        answer = max(answer, lastPosition - firstPosition + 1)
        
        nextLevel = []
        for node, position in queue:
            if node.left:
                nextLevel.append((node.left, 2 * position))
            if node.right:
                nextLevel.append((node.right, 2 * position + 1))
                
        queue = nextLevel
        
    return answer

'''
Time Complexity: O(N), where N is the number of nodes in the binary tree.
Each node is visited and processed exactly once.

Space Complexity: O(W), where W is the maximum width of the tree.
In the worst case (a complete binary tree), the queue can hold up to N/2 nodes, so O(N).
'''

# Test Cases
root1 = [1,3,2,5,3,null,9]
print(widthOfBinaryTree(root1)) # Output: 4

root2 = [1,3,null,5,3]
print(widthOfBinaryTree(root2)) # Output: 2

root3 = [1,3,2,5]
print(widthOfBinaryTree(root3)) # Output: 2

root4 = [1,3,2,5,null,null,9,6,null,null,7]
print(widthOfBinaryTree(root4)) # Output: 8

root5 = [1,1,1,1,null,null,1,1,null,null,1]
print(widthOfBinaryTree(root5)) # Output: 8

root6 = [1]
print(widthOfBinaryTree(root6)) # Output: 1

root7 = [1,2]
print(widthOfBinaryTree(root7)) # Output: 2

root8 = [1,null,2]
print(widthOfBinaryTree(root8)) # Output: 1

root9 = [1,2,3,4,5,6,7]
print(widthOfBinaryTree(root9)) # Output: 4

root10 = [1,2,3,4,null,null,5,6,null,null,7,8,null,null,9]
print(widthOfBinaryTree(root10)) # Output: 8