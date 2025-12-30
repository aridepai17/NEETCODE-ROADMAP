# RANGE SUM OF BST

'''
Given the root node of a binary search tree and two integers low and high, return the sum of values of all nodes with a value in the inclusive range [low, high].
'''

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

'''
ALGORITHM:

1. Define a function `rangeSumBST` that takes the `root` of the BST, `low`, and `high` as input.
2. Base Case: If `root` is `None`, return `0` (no nodes to sum).
3. Pruning based on BST properties:
   a. If `root.val` is greater than `high`:
      - The current node and its right subtree are all greater than `high`.
      - Therefore, only the left subtree might contain nodes within the range.
      - Recursively call `rangeSumBST` on `root.left` with the same `low` and `high`.
   b. If `root.val` is less than `low`:
      - The current node and its left subtree are all less than `low`.
      - Therefore, only the right subtree might contain nodes within the range.
      - Recursively call `rangeSumBST` on `root.right` with the same `low` and `high`.
4. If `root.val` is within the range `[low, high]` (i.e., `low <= root.val <= high`):
   - Include `root.val` in the sum.
   - Recursively call `rangeSumBST` on both `root.left` and `root.right` to find sums from their respective subtrees.
   - Return `root.val + rangeSumBST(root.left, low, high) + rangeSumBST(root.right, low, high)`.
'''

def rangeSumBST(root, low, high):
    if not root:
        return 0
    
    if root.val > high:
        return rangeSumBST(root.left, low, high)
    if root.val < low:
        return rangeSumBST(root.right, low, high)
    return root.val + rangeSumBST(root.left, low, high) + rangeSumBST(root.right, low, high)

'''
Time Complexity: O(N), where N is the number of nodes in the BST.
In the worst case, we might visit every node if all nodes are within the [low, high] range or if the tree is skewed.
However, due to the pruning based on BST properties, we only visit nodes that could potentially be in the range.
In a balanced tree, if the range is small, it could be closer to O(log N + K) where K is the number of nodes in the range.
But in the worst case (e.g., a skewed tree where all nodes are in range), it's O(N).

Space Complexity: O(H), where H is the height of the BST.
This is due to the recursion stack. In the worst case (a skewed tree), H can be N.
In the best case (a balanced tree), H is log N.
'''

# Test Cases
root1 = [10,5,15,3,7,null,18], low1 = 7, high1 = 15
print(rangeSumBST(root1, low1, high1)) # Output: 32

root2 = [10,5,15,3,7,13,18,1,null,6], low2 = 6, high2 = 10
print(rangeSumBST(root2, low2, high2)) # Output: 23


root3 = [10,5,15,3,7,13,18,1,null,6], low3 = 1, high3 = 10
print(rangeSumBST(root3, low3, high3)) # Output: 55

root4 = [10,5,15,3,7,13,18,1,null,6], low4 = -1, high4 = 100
print(rangeSumBST(root4, low4, high4)) # Output: 108

root5 = [10,5,15,3,7,13,18,1,null,6], low5 = 7, high5 = 100
print(rangeSumBST(root5, low5, high5)) # Output: 70

root6 = [10,5,15,3,7,13,18,1,null,6], low6 = 7, high6 = 20
print(rangeSumBST(root6, low6, high6)) # Output: 42

root7 = [10,5,15,3,7,13,18,1,null,6], low7 = 0, high7 = 12
print(rangeSumBST(root7, low7, high7)) # Output: 35

root8 = [10,5,15,3,7,13,18,1,null,6], low8 = 0, high8 = 1
print(rangeSumBST(root8, low8, high8)) # Output: 1

root9 = [10,5,15,3,7,13,18,1,null,6], low9 = 15, high9 = 18
print(rangeSumBST(root9, low9, high9)) # Output: 36

root10 = [10,5,15,3,7,13,18,1,null,6], low10 = 16, high10 = 18
print(rangeSumBST(root10, low10, high10)) # Output: 18