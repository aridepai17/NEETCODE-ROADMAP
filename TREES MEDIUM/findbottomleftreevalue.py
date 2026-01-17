# FIND BOTTOM LEFT TREE VALUE

'''
Given the root of a binary tree, return the leftmost value in the last row of the tree.
'''

'''
ALGORITHM:
1. Use BFS (Breadth-First Search) with a twist - traverse right to left instead of left to right.
2. Start by adding the root node to a queue.
3. For each node, first add its right child to the queue, then add its left child.
4. By processing right before left, the last node processed will be the leftmost node at the deepest level.
5. When the queue is empty, the last node we processed is the bottom-left value.
6. Return the value of that last node.
'''

import collections


def findBottomLeftValue(root):
    queue = collections.deque([root])
    
    while queue:
        node = queue.popleft()
        if node.right:
            queue.append(node.right)
        if node.left:
            queue.append(node.left)
            
    return node.val

'''
Time Complexity: O(N), where N is the number of nodes in the binary tree.
Each node is visited and processed exactly once during the BFS traversal.

Space Complexity: O(W), where W is the maximum width of the binary tree.
The `queue` can hold up to W nodes at any given time.
In the worst case (a complete binary tree), the maximum width is at the last level, which can be up to N/2 nodes.
Therefore, the space complexity is O(N) in the worst case.
'''

# TreeNode class for creating test cases
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Test Cases

# Test 1: Simple tree with 3 nodes
root1 = TreeNode(2, TreeNode(1), TreeNode(3))
print(findBottomLeftValue(root1)) # Output: 1

# Test 2: Left-skewed tree
root2 = TreeNode(1, TreeNode(2, TreeNode(3, TreeNode(4))))
print(findBottomLeftValue(root2)) # Output: 4

# Test 3: Right-skewed tree
root3 = TreeNode(1, None, TreeNode(2, None, TreeNode(3, None, TreeNode(4))))
print(findBottomLeftValue(root3)) # Output: 4

# Test 4: Complete binary tree
root4 = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3, TreeNode(6), TreeNode(7)))
print(findBottomLeftValue(root4)) # Output: 4

# Test 5: Single node tree
root5 = TreeNode(42)
print(findBottomLeftValue(root5)) # Output: 42

# Test 6: Tree where bottom left is on the right subtree
root6 = TreeNode(1, TreeNode(2), TreeNode(3, TreeNode(4, TreeNode(6)), TreeNode(5)))
print(findBottomLeftValue(root6)) # Output: 6

# Test 7: Unbalanced tree with deeper right side
root7 = TreeNode(1, TreeNode(2, TreeNode(4)), TreeNode(3, None, TreeNode(5, TreeNode(6))))
print(findBottomLeftValue(root7)) # Output: 6

# Test 8: Tree with negative values
root8 = TreeNode(-1, TreeNode(-2, TreeNode(-4), TreeNode(-5)), TreeNode(-3))
print(findBottomLeftValue(root8)) # Output: -4

# Test 9: Larger tree
root9 = TreeNode(10, TreeNode(5, TreeNode(3, TreeNode(1)), TreeNode(7)), TreeNode(15, TreeNode(12), TreeNode(20)))
print(findBottomLeftValue(root9)) # Output: 1

# Test 10: Tree with same values
root10 = TreeNode(1, TreeNode(1, TreeNode(1), TreeNode(1)), TreeNode(1, TreeNode(1), TreeNode(1)))
print(findBottomLeftValue(root10)) # Output: 1