# CHECK COMPLETENESS OF BINARY TREE

'''
Given the root of a binary tree, determine if it is a complete binary tree.
In a complete binary tree, every level, except possibly the last, is completely filled, and all nodes in the last level are as far left as possible. 
It can have between 1 and 2h nodes inclusive at the last level h.
'''

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

'''
ALGORITHM:

1. Initialize a `queue` using `collections.deque` and add the `root` node to it.
2. Enter a `while` loop that continues as long as the `queue` is not empty.
   a. Dequeue a `node` from the left of the `queue`.
   b. If `node` is `None`:
      i. Enter another `while` loop that continues as long as the `queue` is not empty.
         - Dequeue a `temp_node` from the left of the `queue`.
         - If `temp_node` is not `None`, it means we found a non-null node after encountering a null node, which violates the completeness property. Return `False`.
      ii. If the inner `while` loop completes, it means all remaining nodes in the queue were `None`, so the tree is complete. Break out of the outer `while` loop.
   c. If `node` is not `None`:
      i. Enqueue `node.left` to the right of the `queue`.
      ii. Enqueue `node.right` to the right of the `queue`.
3. If the outer `while` loop completes, it means all nodes were processed and no completeness violation was found. Return `True`.
'''

import collections

def isCompleteTree(root):
    queue = collections.deque[(root)]
    while queue:
        node = queue.popleft()
        if node:
            queue.append(node.left)
            queue.append(node.right)
        else:
            while queue:
                if queue.popleft():
                    return False
                
    return True

'''
Time Complexity: O(N), where N is the number of nodes in the binary tree.
Each node is visited and processed exactly once during the BFS traversal.

Space Complexity: O(W), where W is the maximum width of the binary tree.
The `queue` can hold up to W nodes at any given time.
In the worst case (a complete binary tree), the maximum width is at the last level, which can be up to N/2 nodes.
Therefore, the space complexity is O(N) in the worst case.
'''

# Test Cases
root1 = [1,2,3,4,5,6]
print(isCompleteTree(root1)) # Output: True

root2 = [1,2,3,4,5,6,7]
print(isCompleteTree(root2)) # Output: True

root3 = [1,2,3,4,5,null,7]
print(isCompleteTree(root3)) # Output: False

root4 = [1]
print(isCompleteTree(root4)) # Output: True

root5 = []
print(isCompleteTree(root5)) # Output: True (An empty tree is considered complete)

root6 = [1,2,null,4]
print(isCompleteTree(root6)) # Output: False

root7 = [1,2,3,4,null,6]
print(isCompleteTree(root7)) # Output: False

root8 = [1,2,3,null,5,6]
print(isCompleteTree(root8)) # Output: False

root9 = [1,2,3,4,5,6,null,8]
print(isCompleteTree(root9)) # Output: False

root10 = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
print(isCompleteTree(root10)) # Output: True