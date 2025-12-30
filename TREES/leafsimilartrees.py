# LEAF SIMILAR TREES

'''
Consider all the leaves of a binary tree, from left to right order, the values of those leaves form a leaf value sequence.
Two binary trees are considered leaf-similar if their leaf value sequence is the same.
Return true if and only if the two given trees with head nodes root1 and root2 are leaf-similar.
'''

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

'''
ALGORITHM:

1. Define a function `leafSimilar` that takes two `TreeNode` objects, `root1` and `root2`, as input.
2. Define a helper function `dfs(root, leaf)`:
   a. Base Case 1: If `root` is `None`, return (no node to process).
   b. Base Case 2: If `root` is a leaf node (i.e., `root.left` is `None` AND `root.right` is `None`):
      - Append `root.val` to the `leaf` list.
      - Return.
   c. Recursive Step: If `root` is not a leaf node:
      - Recursively call `dfs` on the `left` child: `dfs(root.left, leaf)`.
      - Recursively call `dfs` on the `right` child: `dfs(root.right, leaf)`.
3. Initialize two empty lists, `leaf1` and `leaf2`, to store the leaf value sequences for `root1` and `root2` respectively.
4. Call `dfs(root1, leaf1)` to populate `leaf1`.
5. Call `dfs(root2, leaf2)` to populate `leaf2`.
6. Compare `leaf1` and `leaf2`. If they are equal, return `True`; otherwise, return `False`.
'''

def leafSimilar(root1, root2):
    def dfs(root, leaf):
        if not root:
            return 
        if not root.left and not root.right:
            leaf.append(root.val)
            return 
        dfs(root.left, leaf)
        dfs(root.right, leaf)
        
    leaf1, leaf2 = [], []
    dfs(root1, leaf1)
    dfs(root2, leaf2)
    
    return leaf1 == leaf2

'''
Time Complexity: O(N1 + N2), where N1 and N2 are the number of nodes in root1 and root2 respectively.
This is because we traverse each tree once to extract its leaf sequence.

Space Complexity: O(H1 + H2), where H1 and H2 are the heights of root1 and root2 respectively.
This is due to the recursion stack for the DFS calls. In the worst case (skewed trees), this can be O(N1 + N2).
Additionally, the `leaf1` and `leaf2` lists store the leaf values. In the worst case, all nodes could be leaves,
leading to O(N1 + N2) space for these lists.
'''

# Test Cases
root1 = [3,5,1,6,2,9,8,null,null,7,4], root2 = [3,5,1,6,7,4,2,null,null,null,null,null,null,9,8]
print(leafSimilar(root1, root2)) # Output: True

root1 = [1,2,3], root2 = [1,3,2]
print(leafSimilar(root1, root2)) # Output: False

root1 = [], root2 = []
print(leafSimilar(root1, root2)) # Output: True

root3 = [1], root4 = [1]
print(leafSimilar(root3, root4)) # Output: True

root5 = [1,2], root6 = [2,1]
print(leafSimilar(root5, root6)) # Output: False

root7 = [1,2,3], root8 = [1,2,3]
print(leafSimilar(root7, root8)) # Output: True

root9 = [1,2,null,3], root10 = [1,3,null,2]
print(leafSimilar(root9, root10)) # Output: False

root11 = [1,2,3,4,5], root12 = [1,2,3,4,5]
print(leafSimilar(root11, root12)) # Output: True

root13 = [1,2,3,4,null,5], root14 = [1,2,3,4,5]
print(leafSimilar(root13, root14)) # Output: False

root15 = [1,2,3,4,5,6,7], root16 = [1,2,3,4,5,6,7]
print(leafSimilar(root15, root16)) # Output: True