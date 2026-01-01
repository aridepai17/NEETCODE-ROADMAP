# LOWEST COMMON ANCESTOR OF BINARY SEARCH TREE

'''
Given a binary search tree (BST), find the lowest common ancestor (LCA) node of two given nodes in the BST.
According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”
'''

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

'''
ALGORITHM (Iterative Solution):

1. Define a function `lowestCommonAncestor` that takes the `root` of the BST, and the two nodes `p` and `q` as input.
2. Initialize a `current` pointer to the `root` of the BST.
3. Enter a `while` loop that continues as long as `current` is not `None`.
   a. Inside the loop, compare the value of the `current` node with the values of `p` and `q`.
   b. If `current.val` is greater than both `p.val` and `q.val`:
      - This means both `p` and `q` must be in the left subtree of `current`.
      - Move `current` to its `left` child: `current = current.left`.
   c. Else if `current.val` is less than both `p.val` and `q.val`:
      - This means both `p` and `q` must be in the right subtree of `current`.
      - Move `current` to its `right` child: `current = current.right`.
   d. Else (if `current.val` is between `p.val` and `q.val`, or equal to one of them):
      - This means `current` is the split point where `p` and `q` diverge into different subtrees, or `current` itself is `p` or `q`.
      - In a BST, this `current` node is the Lowest Common Ancestor.
      - Return `current`.
'''

def lowestCommonAncestor(root, p, q):
    current = root
    
    while current:
        if current.val > p.val and current.val > q.val:
            current = current.right
        elif current.val < p.val and current.val < q.val:
            current = current.left
        else:
            return current

'''
Time Complexity: O(H), where H is the height of the BST.
In the worst case (a skewed tree), H can be N, where N is the number of nodes.
In the best case (a balanced tree), H is log N.
This is because in each step, we move down one level in the tree.

Space Complexity: O(1).
We are only using a few pointers (current) and not allocating any additional data structures that grow with the input size.
'''

# Test Cases
root1 = [6,2,8,0,4,7,9,null,null,3,5], p1 = 2, q1 = 8
print(lowestCommonAncestor(root1, p1, q1)) # Output: 6

root2 = [6,2,8,0,4,7,9,null,null,3,5], p2 = 2, q2 = 4
print(lowestCommonAncestor(root2, p2, q2)) # Output: 2

root3 = [2,1], p3 = 2, q3 = 1
print(lowestCommonAncestor(root3, p3, q3)) # Output: 2

root4 = [6,2,8,0,4,7,9,null,null,3,5], p4 = 0, q4 = 5
print(lowestCommonAncestor(root4, p4, q4)) # Output: 2

root5 = [6,2,8,0,4,7,9,null,null,3,5], p5 = 7, q5 = 9
print(lowestCommonAncestor(root5, p5, q5)) # Output: 8

root6 = [6,2,8,0,4,7,9,null,null,3,5], p6 = 3, q6 = 5
print(lowestCommonAncestor(root6, p6, q6)) # Output: 4

root7 = [6,2,8,0,4,7,9,null,null,3,5], p7 = 6, q7 = 8
print(lowestCommonAncestor(root7, p7, q7)) # Output: 6

root8 = [6,2,8,0,4,7,9,null,null,3,5], p8 = 6, q8 = 4
print(lowestCommonAncestor(root8, p8, q8)) # Output: 6

root9 = [6,2,8,0,4,7,9,null,null,3,5], p9 = 0, q9 = 9
print(lowestCommonAncestor(root9, p9, q9)) # Output: 6

root10 = [6,2,8,0,4,7,9,null,null,3,5], p10 = 3, q10 = 7
print(lowestCommonAncestor(root10, p10, q10)) # Output: 6