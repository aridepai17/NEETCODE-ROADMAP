# SUM OF LEFT LEAVES

'''
Given the root of a binary tree, return the sum of all left leaves.
A leaf is a node with no children. A left leaf is a leaf that is the left child of another node.
'''

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

'''
ALGORITHM:

1. Define a function `sumOfLeftLeaves` that takes the `root` of the binary tree as input.
2. Base Case: If `root` is `None`, return `0` (no leaves, so no sum).
3. Initialize a variable `total` to `0`. This will store the sum of left leaves.
4. Check if the `root` has a left child (`root.left` is not `None`).
   a. If it does, check if this left child is a leaf node (i.e., `root.left.left` is `None` AND `root.left.right` is `None`).
   b. If `root.left` is a leaf node, add its value (`root.left.val`) to `total`.
5. Recursively call `sumOfLeftLeaves` on the `left` child of the current `root`: `sumOfLeftLeaves(root.left)`. Add the result to `total`.
6. Recursively call `sumOfLeftLeaves` on the `right` child of the current `root`: `sumOfLeftLeaves(root.right)`. Add the result to `total`.
7. Return the final `total`.
'''

def sumOfLeftLeaves(root):
    if not root:
        return 0
    total = 0
    
    if root.left and not root.left.left and not root.left.right:
        total += root.left.value
        
    total += sumOfLeftLeaves(root.left)
    total += sumOfLeftLeaves(root.right)
    
    return total

'''
Time Complexity: O(N), where N is the number of nodes in the binary tree.
This is because we visit each node exactly once.

Space Complexity: O(H), where H is the height of the binary tree.
This is due to the recursion stack. In the worst case (a skewed tree), H can be N.
In the best case (a balanced tree), H is log N.
'''

# Test Cases
root1 = [3,9,20,null,null,15,7]
print(sumOfLeftLeaves(root1)) # Output: 24

root2 = [1]
print(sumOfLeftLeaves(root2)) # Output: 0

root3 = [1,2]
print(sumOfLeftLeaves(root3)) # Output: 2

root4 = [1,2,3]
print(sumOfLeftLeaves(root4)) # Output: 2

root5 = [1,2,3,4,5]
print(sumOfLeftLeaves(root5)) # Output: 4

root6 = [1,null,2,3]
print(sumOfLeftLeaves(root6)) # Output: 0

root7 = [1,2,null,3,null,4]
print(sumOfLeftLeaves(root7)) # Output: 3

root8 = [1,2,3,4,null,5,6]
print(sumOfLeftLeaves(root8)) # Output: 4

root9 = [1,2,3,4,5,6,7]
print(sumOfLeftLeaves(root9)) # Output: 4

root10 = [1,2,3,4,5,6,7,8,9,10]
print(sumOfLeftLeaves(root10)) # Output: 12