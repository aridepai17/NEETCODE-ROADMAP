# INVERT BINARY TREE

'''
Given the root of a binary tree, invert the tree, and return its root.
'''

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

'''
ALGORITHM:

1. Base Case: If the `root` is `None`, return `None` (an empty tree remains empty).
2. Recursive Step:
   a. Recursively call `invertTree` on the `right` child of the current `root`.
   b. Recursively call `invertTree` on the `left` child of the current `root`.
   c. Swap the `left` and `right` children of the current `root`.
      This is done by simultaneously assigning the result of `invertTree(root.right)` to `root.left`
      and the result of `invertTree(root.left)` to `root.right`.
3. Return the `root` of the now inverted subtree.
'''

def invertTree(root):
    if not root:
        return None
    
    root.left, root.right = invertTree(root.right), invertTree(root.left)
    
    return root

'''
Time Complexity: O(N), where N is the number of nodes in the tree.
This is because we visit each node exactly once.

Space Complexity: O(H), where H is the height of the tree.
This is due to the recursion stack. In the worst case (skewed tree), H can be N.
In the best case (balanced tree), H is log N.
'''

# Test Cases
root1 = [4,2,7,1,3,6,9]
print(invertTree(root1)) # Output: [4,7,2,9,6,3,1]


root2 = [2,1,3]
print(invertTree(root2)) # Output: [2,3,1]

root3 = [1,2]
print(invertTree(root3)) # Output: [1,2]

root4 = [1,null,2]
print(invertTree(root4)) # Output: [1,null,2]

root5 = [1,null,2,3]
print(invertTree(root5)) # Output: [1,3,2]

root6 = [1,null,2,3,null,4]
print(invertTree(root6)) # Output: [1,4,3,2]

root7 = [1,2,3,4]
print(invertTree(root7)) # Output: [1,4,3,2]

root8 = [1,2,3,null,4]
print(invertTree(root8)) # Output: [1,4,3,2]

root9 = [1,2,3,null,4,5]
print(invertTree(root9)) # Output: [1,5,4,3,2]

root10 = [1,2,3,4,5,6]
print(invertTree(root10)) # Output: [1,6,5,4,3,2]