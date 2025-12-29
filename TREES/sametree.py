# SAME TREE

'''
Given the roots of two binary trees p and q, write a function to check if they are the same or not.
Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.
'''

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

'''
ALGORITHM:

1. Define a function `isSameTree` that takes two `TreeNode` objects, `p` and `q`, as input.
2. Base Cases:
   a. If both `p` and `q` are `None`, return `True` (both are empty, hence identical).
   b. If one of `p` or `q` is `None` but the other is not, return `False` (one is empty, the other is not, so they are not identical).
3. Recursive Step:
   a. If neither `p` nor `q` is `None`, check two conditions:
      i. Their values must be equal: `p.val == q.val`.
      ii. Their left subtrees must be identical: `isSameTree(p.left, q.left)`.
      iii. Their right subtrees must be identical: `isSameTree(p.right, q.right)`.
   b. Return `True` only if all three conditions (value equality, left subtree identity, and right subtree identity) are met. Otherwise, return `False`.
'''

def isSameTree(p, q):
    if not p or not q:
        return p == q
    
    return (p.val == q.val) and isSameTree(p.left, q.left) and isSameTree(p.right, q.right)

'''
Time Complexity: O(min(N, M)), where N is the number of nodes in tree p and M is the number of nodes in tree q.
In the worst case, we might visit all nodes of the smaller tree. If both trees are identical, we visit all nodes in both trees.

Space Complexity: O(min(H_p, H_q)), where H_p and H_q are the heights of tree p and tree q respectively.
This is due to the recursion stack. In the worst case (skewed tree), this can be O(min(N, M)).
In the best case (balanced tree), this can be O(log(min(N, M))).
'''

# Test Cases
p1 = [1,2,3], q1 = [1,2,3]
print(isSameTree(p1, q1)) # Output: True

# Test Case 2: Different values
p2 = [1,2], q2 = [1,None,2]
print(isSameTree(p2, q2)) # Output: False

# Test Case 3: Different structure
p3 = [1,2,1], q3 = [1,1,2]
print(isSameTree(p3, q3)) # Output: False

# Test Case 4: One tree is empty
p4 = [], q4 = [1]
print(isSameTree(p4, q4)) # Output: False

# Test Case 5: Both trees are empty
p5 = [], q5 = []
print(isSameTree(p5, q5)) # Output: True

# Test Case 6: Complex identical trees
p6 = [1,2,3,4,5,6,7], q6 = [1,2,3,4,5,6,7]
print(isSameTree(p6, q6)) # Output: True

# Test Case 7: Complex different values
p7 = [1,2,3,4,5,6,7], q7 = [1,2,3,4,5,6,8]
print(isSameTree(p7, q7)) # Output: False

# Test Case 8: Complex different structure
p8 = [1,2,3,4,5,6,7], q8 = [1,2,3,4,5,7,6]
print(isSameTree(p8, q8)) # Output: False

# Test Case 9: Left child missing in one, right in another
p9 = [1,2,None], q9 = [1,None,2]
print(isSameTree(p9, q9)) # Output: False

# Test Case 10: Single node trees, different values
p10 = [1], q10 = [2]
print(isSameTree(p10, q10)) # Output: False