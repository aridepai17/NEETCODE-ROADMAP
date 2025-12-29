# BALANCED BINARY TREE

'''
Given a binary tree, determine if it is height-balanced.
A height-balanced binary tree is a binary tree in which the depth of the two subtrees of every node never differs by more than one.
'''

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

'''
ALGORITHM:

1. Define a helper function `dfs(root)` that returns a list `[is_balanced, height]`.
   a. Base Case: If `root` is `None`, return `[True, 0]` (an empty tree is balanced and has a height of 0).
   b. Recursively call `dfs` on the `left` child: `left = dfs(root.left)`.
   c. Recursively call `dfs` on the `right` child: `right = dfs(root.right)`.
   d. Determine if the current subtree is balanced:
      - It is balanced if both its left and right subtrees are balanced (`left[0]` and `right[0]`).
      - AND the absolute difference between the heights of its left and right subtrees is less than or equal to 1 (`abs(left[1] - right[1]) <= 1`).
      - Store this boolean in a variable `balanced`.
   e. Calculate the height of the current subtree: `1 + max(left[1], right[1])` (1 for the current node plus the maximum height of its children).
   f. Return `[balanced, height]`.
2. Call the `dfs` function with the main `root` of the binary tree.
3.Return the first element of the list returned by `dfs(root)` (which is the boolean indicating if the tree is balanced).
'''

def isBalanced(root):
    def dfs(root):
        if not root:
            return [True, 0]
        
        left = dfs(root.left)
        right = dfs(root.right)
        balanced = (left[0] and right[0] and abs(left[1] - right[1]) <= 1)
        
        return [balanced, 1 + max(left[1], right[1])]
    
    return dfs(root)[0]

'''
Time Complexity: O(N), where N is the number of nodes in the tree.
Each node is visited exactly once during the DFS traversal.

Space Complexity: O(H), where H is the height of the tree.
This is due to the recursion stack. In the worst case (skewed tree), H can be N.
In the best case (balanced tree), H is log N.
'''

# Test Cases
root1 = [3,9,20,null,null,15,7]
print(isBalanced(root1)) # Output: True


root2 = [1,2,2,3,3,null,null,4,4]
print(isBalanced(root2)) # Output: False

root3 = [1]
print(isBalanced(root3)) # Output: True

root4 = [1,2,2,3,null,null,3]
print(isBalanced(root4)) # Output: False

root5 = [1,2,3,4,5,6,7,8,9]
print(isBalanced(root5)) # Output: True

root6 = [1,2,2,3,3,4,4,5,5,6]
print(isBalanced(root6)) # Output: False

root7 = [1,2,3,4,null,null,5,6,7,8]
print(isBalanced(root7)) # Output: False

root8 = [1,2,3,4,5,6,7,8,9,10]
print(isBalanced(root8)) # Output: True

root9 = [1,2,3,4,5,6,7,8,9,10,11]
print(isBalanced(root9)) # Output: True

root10 = [1,2,3,4,5,6,7,8,9,10,11,12]
print(isBalanced(root10)) # Output: True