# PATH SUM

'''
Given the root of a binary tree and an integer targetSum, return true if the tree has a root-to-leaf path such that adding up all the values along the path equals targetSum.
A leaf is a node with no children.
'''

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

'''
ALGORITHM:

1. Define a function `pathSum` that takes the `root` of the binary tree and an integer `targetSum` as input.
2. Define a helper function `dfs(node, currentSum)`:
   a. Base Case 1: If `node` is `None`, return `False` (no path through an empty node).
   b. Update `currentSum` by adding the `node.val` to it.
   c. Base Case 2: If `node` is a leaf node (i.e., `node.left` is `None` AND `node.right` is `None`):
      - Check if `currentSum` is equal to `targetSum`. If it is, return `True`; otherwise, return `False`.
   d. Recursive Step: If `node` is not a leaf node:
      - Recursively call `dfs` on the `left` child: `dfs(node.left, currentSum)`.
      - Recursively call `dfs` on the `right` child: `dfs(node.right, currentSum)`.
      - Return `True` if either the left subtree path or the right subtree path leads to the `targetSum`. This is done using a logical OR: `dfs(node.left, currentSum) or dfs(node.right, currentSum)`.
3. Call the `dfs` function with the `root` of the binary tree and an initial `currentSum` of `0`.
4. Return the result of the `dfs` call.
'''

def pathSum(root, targetSum):
    def dfs(node, currentSum):
        if not node:
            return False
        
        currentSum += node.val
        if not node.left and not node.right:
            return currentSum == targetSum
        
        return dfs(node.left, currentSum) or dfs(node.right, currentSum)
    
    return dfs(root, 0)

'''
Time Complexity: O(N), where N is the number of nodes in the tree.
In the worst case, we might visit every node once to find a path or to confirm no such path exists.

Space Complexity: O(H), where H is the height of the tree.
This is due to the recursion stack. In the worst case (a skewed tree), H can be N.
In the best case (a balanced tree), H is log N.
'''

# Test Cases
root1 = [5,4,8,11,null,13,4,7,2,null,null,null,1], targetSum1 = 22
print(pathSum(root1, targetSum1)) # Output: True


root2 = [1,2,3], targetSum2 = 5
print(pathSum(root2, targetSum2)) # Output: False

root3 = [1,2], targetSum3 = 1
print(pathSum(root3, targetSum3)) # Output: False

root4 = [1,0,0,0,0,0,0,0,0,0,0,0], targetSum4 = 0
print(pathSum(root4, targetSum4)) # Output: True

root5 = [1,2,3,4,5], targetSum5 = 15
print(pathSum(root5, targetSum5)) # Output: True

root6 = [1,2,3,4], targetSum6 = 10
print(pathSum(root6, targetSum6)) # Output: False

root7 = [1], targetSum7 = 1
print(pathSum(root7, targetSum7)) # Output: True

root8 = [1,2,3,4,5,6,7,8,9,10], targetSum8 = 15
print(pathSum(root8, targetSum8)) # Output: False

root9 = [1,-2,-3,1,3,-2,null,-1], targetSum9 = -1
print(pathSum(root9, targetSum9)) # Output: True

root10 = [1,2,3,4,5,6,7,8,9,10,11], targetSum10 = 55
print(pathSum(root10, targetSum10)) # Output: False