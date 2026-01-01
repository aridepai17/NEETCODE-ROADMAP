# COUNT COMPLETE TREE NODES

'''
Given the root of a complete binary tree, return the number of the nodes in the tree.
According to Wikipedia, every level, except possibly the last, is completely filled in a complete binary tree, and all nodes in the last level are as far left as possible. 
It can have between 1 and 2h nodes inclusive at the last level h.
Design an algorithm that runs in less than O(n) time complexity.
'''

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

'''
ALGORITHM (O(N) Solution - Simple DFS):

1. Define a function `countNodes` that takes the `root` of the binary tree as input.
2. Base Case: If the `root` is `None`, return `0` (an empty tree has 0 nodes).
3. Recursive Step:
   a. Recursively call `countNodes` on the `left` child: `countNodes(root.left)`.
   b. Recursively call `countNodes` on the `right` child: `countNodes(root.right)`.
   c. Return `1` (for the current node) plus the count of nodes in the left subtree and the count of nodes in the right subtree.
'''

def countNodes(root):
    if not root:
        return 0
    return 1 + countNodes(root.left) + countNodes(root.right)

'''
Time Complexity: O(N), where N is the number of nodes in the tree.
This is because in the worst case (a skewed tree or a complete tree where we traverse all nodes), we visit each node exactly once.

Space Complexity: O(H), where H is the height of the tree.
This is due to the recursion stack. In the worst case (a skewed tree), H can be N.
In the best case (a balanced tree), H is log N.
'''

# Test Cases
root1 = [1,2,3,4,5,6]
print(countNodes(root1)) # Output: 6

root2 = []
print(countNodes(root2)) # Output: 0

root3 = [1]
print(countNodes(root3)) # Output: 1

root4 = [1,2,3,4,5,6,7]
print(countNodes(root4)) # Output: 7

root5 = [1,2,3,4]
print(countNodes(root5)) # Output: 4

root6 = [1,2]
print(countNodes(root6)) # Output: 2

root7 = [1,2,3]
print(countNodes(root7)) # Output: 3

root8 = [1,2,3,4,5]
print(countNodes(root8)) # Output: 5

root9 = [1,2,3,4,5,6,7,8,9,10]
print(countNodes(root9)) # Output: 10

root10 = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
print(countNodes(root10)) # Output: 15
