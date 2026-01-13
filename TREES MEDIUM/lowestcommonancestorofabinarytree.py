# LOWEST COMMON ANCESTOR OF A BINARY TREE

'''
Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.
According to the definition of LCA on Wikipedia: 
“The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”
'''

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

'''
ALGORITHM (Recursive Solution):

1. Define a function `lowestCommonAncestor` that takes the `root` of the binary tree, and the two nodes `p` and `q` as input.
2. Base Cases:
   a. If `root` is `None`, return `None`. This means we've reached the end of a path without finding `p` or `q`.
   b. If `root` is `p` or `root` is `q`, return `root`. This means we've found one of the target nodes. If the other node is in the subtree of this `root`, then `root` is the LCA. If not, then this `root` is one of the nodes itself, and it's the LCA.
3. Recursive Step:
   a. Recursively call `lowestCommonAncestor` on the `left` child: `left = lowestCommonAncestor(root.left, p, q)`.
   b. Recursively call `lowestCommonAncestor` on the `right` child: `right = lowestCommonAncestor(root.right, p, q)`.
4. After the recursive calls return:
   a. If both `left` and `right` are not `None`:
      - This means `p` and `q` were found in different subtrees of the current `root`.
      - Therefore, the current `root` is the LCA. Return `root`.
   b. If only `left` is not `None`:
      - This means both `p` and `q` (or just one of them, and the other is an ancestor of `left`) were found in the left subtree.
      - Return `left`.
   c. If only `right` is not `None`:
      - This means both `p` and `q` (or just one of them, and the other is an ancestor of `right`) were found in the right subtree.
      - Return `right`.
   d. If both `left` and `right` are `None`:
      - This means neither `p` nor `q` were found in the subtrees of the current `root`.
      - Return `None`.
'''

def lowestCommonAncestor(root, p, q):
    if not root or root is p or root is q:
        return root
    
    left = lowestCommonAncestor(root.left, p, q)
    right = lowestCommonAncestor(root.right, p, q)
    
    if left and right:
        return root
    
    return left if left else right

'''
Time Complexity: O(N), where N is the number of nodes in the binary tree.
In the worst case, we might visit every node in the tree once.

Space Complexity: O(H), where H is the height of the binary tree.
This is due to the recursion stack. In the worst case (a skewed tree), H can be N.
In the best case (a balanced tree), H is log N.
'''

# Test Cases
root1 = [3,5,1,6,2,0,8,null,null,7,4], p1 = 5, q1 = 1
print(lowestCommonAncestor(root1, p1, q1)) # Output: 3

root2 = [3,5,1,6,2,0,8,null,null,7,4], p2 = 5, q2 = 4
print(lowestCommonAncestor(root2, p2, q2)) # Output: 5

root3 = [1,2], p3 = 1, q3 = 2
print(lowestCommonAncestor(root3, p3, q3)) # Output: 1

root4 = [3,5,1,6,2,0,8,null,null,7,4], p4 = 6, q4 = 7
print(lowestCommonAncestor(root4, p4, q4)) # Output: 2

root5 = [3,5,1,6,2,0,8,null,null,7,4], p5 = 0, q5 = 8
print(lowestCommonAncestor(root5, p5, q5)) # Output: 1

root6 = [3,5,1,6,2,0,8,null,null,7,4], p6 = 3, q6 = 5
print(lowestCommonAncestor(root6, p6, q6)) # Output: 3

root7 = [3,5,1,6,2,0,8,null,null,7,4], p7 = 7, q7 = 4
print(lowestCommonAncestor(root7, p7, q7)) # Output: 2

root8 = [3,5,1,6,2,0,8,null,null,7,4], p8 = 6, q8 = 0
print(lowestCommonAncestor(root8, p8, q8)) # Output: 3

root9 = [3,5,1,6,2,0,8,null,null,7,4], p9 = 8, q9 = 4
print(lowestCommonAncestor(root9, p9, q9)) # Output: 3

root10 = [3,5,1,6,2,0,8,null,null,7,4], p10 = 6, q10 = 8
print(lowestCommonAncestor(root10, p10, q10)) # Output: 3