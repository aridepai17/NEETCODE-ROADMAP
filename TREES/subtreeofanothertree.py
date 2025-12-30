# SUBTREE OF ANOTHER TREE

'''
Given the roots of two binary trees root and subRoot, return true if there is a subtree of root with the same structure and node values of subRoot and false otherwise.
A subtree of a binary tree tree is a tree that consists of a node in tree and all of this node's descendants. The tree tree could also be considered as a subtree of itself.
'''

'''
ALGORITHM:

1. Define a function `isSubtree` that takes two `TreeNode` objects, `s` (root of the main tree) and `t` (root of the potential subtree), as input.
2. Define a nested helper function `isSameTree(s, t)`:
   a. Base Case 1: If both `s` and `t` are `None`, return `True` (both are empty, hence identical).
   b. Base Case 2: If one of `s` or `t` is `None` but the other is not, return `False` (one is empty, the other is not, so they are not identical).
   c. Recursive Step: If both `s` and `t` are not `None`:
      - Check if their values are equal (`s.val == t.val`).
      - Recursively check if their left subtrees are identical (`isSameTree(s.left, t.left)`).
      - Recursively check if their right subtrees are identical (`isSameTree(s.right, t.right)`).
      - Return `True` only if all three conditions are met; otherwise, return `False`.
3. Back to `isSubtree` function:
   a. Base Case 1: If `t` is `None`, return `True` (an empty tree is always a subtree of any tree).
   b. Base Case 2: If `s` is `None` but `t` is not `None`, return `False` (a non-empty tree cannot be a subtree of an empty tree).
   c. Check if the tree rooted at `s` is identical to `t` using `isSameTree(s, t)`. If they are identical, return `True`.
   d. If not identical, recursively check if `t` is a subtree of the left child of `s`: `isSubtree(s.left, t)`.
   e. Recursively check if `t` is a subtree of the right child of `s`: `isSubtree(s.right, t)`.
   f. Return `True` if either of the recursive calls (left or right subtree) finds `t` as a subtree; otherwise, return `False`.
'''

def isSubtree(s, t):
    def isSameTree(s, t):
        if not s and not t:
            return True
        if s and t and s.val == t.val:
            return (
                isSameTree(s.left, t.left) and 
                isSameTree(s.right, t.right)
            )
        return False
    
    if not t:
        return True
    if not s:
        return False
    if isSameTree(s, t):
        return True
    return (
        isSubtree(s.left, t) or
        isSubtree(s.right, t)
    )
    
'''
Time Complexity: O(S * T), where S and T are the number of nodes in the `root` and `subRoot` trees respectively.
In the worst case, for each node in the `root` tree, we might call `isSameTree`, which itself takes O(T) time.

Space Complexity: O(max(H_s, H_t)), where H_s and H_t are the heights of the `root` and `subRoot` trees respectively.
This is due to the recursion stack. In the worst case (skewed trees), this can be O(S) or O(T).
'''

# Test Cases
s1 = [3,4,5,1,2], t1 = [4,1,2]
print(isSubtree(s1, t1)) # Output: True

s2 = [3,4,5,1,2,null,null,null], t2 = [4,1,2]
print(isSubtree(s2, t2)) # Output: True

s3 = [3,4,5,1,2,null,null,null], t3 = [4,1,2,3]
print(isSubtree(s3, t3)) # Output: False

s4 = [3,4,5,1,2,null,null,null], t4 = [3,4,5]
print(isSubtree(s4, t4)) # Output: True

s5 = [3,4,5,1,2,null,null,null], t5 = [3,4]
print(isSubtree(s5, t5)) # Output: True

s6 = [3,4,5,1,2,null,null,null], t6 = [2]
print(isSubtree(s6, t6)) # Output: True

s7 = [3,4,5,1,2,null,null,null], t7 = [1,2]
print(isSubtree(s7, t7)) # Output: True

s8 = [3,4,5,1,2,null,null,null], t8 = [1]
print(isSubtree(s8, t8)) # Output: True

s9 = [3,4,5,1,2,null,null,null], t9 = [5,1,2]
print(isSubtree(s9, t9)) # Output: True

s10 = [3,4,5,1,2,null,null,null], t10 = [5,1,2,3]
print(isSubtree(s10, t10)) # Output: False