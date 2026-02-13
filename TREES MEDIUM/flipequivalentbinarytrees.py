# FLIP EQUIVALENT BINARY TREES

'''
For a binary tree T, we can define a flip operation as follows: choose any node, and swap the left and right child subtrees.
A binary tree X is flip equivalent to a binary tree Y if and only if we can make X equal to Y after some number of flip operations.
Given the roots of two binary trees root1 and root2, return true if the two trees are flip equivalent or false otherwise.
'''

'''
ALGORITHM:
1. If both nodes are null, return True (empty trees are flip equivalent)
2. If only one node is null, return False (different structures)
3. If node values don't match, return False (cannot be flip equivalent)
4. Recursively check two possibilities:
        a. Without flip: left-left and right-right subtrees must be flip equivalent
        b. With flip: left-right and right-left subtrees must be flip equivalent
5. Return True if either possibility is valid
'''

def flipEquiv(r1, r2):
    if not r1 or not r2:
        return not r1 and not r2
    
    if r1.val != r2.val:
        return False
    
    a = flipEquiv(r1.left, r2.left) and flipEquiv(r1.right, r2.right)
    return a or flipEquiv(r1.left, r2.right) and flipEquiv(r1.right, r2.left)

'''
Time Complexity: O(N) - In the worst case, we visit every node exactly once. For each node, we perform constant-time operations
(comparisons and boolean operations) and make recursive calls to its children. Since each node has at most
two children, the total number of recursive calls is bounded by the total number of nodes in the tree.

Space Complexity: O(H) - The space complexity is determined by the maximum depth of the recursion stack. In the worst case (a skewed tree),
the recursion stack will have H = N frames, where N is the number of nodes. In the best case (a balanced tree),
the stack depth is O(log N). The auxiliary space does not include the space required to store the input trees.
'''

# Test Cases
root1 = [1,2,3,4,5,6,null,null,null,7,8], root2 = [1,3,2,null,6,4,5,null,null,null,null,8,7]
print(flipEquiv(root1, root2)) # Output: True

root1 = [], root2 = []
print(flipEquiv(root1, root2)) # Output: True

root1 = [1], root2 = []
print(flipEquiv(root1, root2)) # Output: False

root1 = [1], root2 = [1]
print(flipEquiv(root1, root2)) # Output: True

root1 = [1], root2 = [2]
print(flipEquiv(root1, root2)) # Output: False

root1 = [1,2,None,3], root2 = [1,None,2,3]
print(flipEquiv(root1, root2)) # Output: True

root1 = [1,None,2,None,3], root2 = [1,None,None,2,3]
print(flipEquiv(root1, root2)) # Output: True

root1 = [1,2,3], root2 = [1,3,2]
print(flipEquiv(root1, root2)) # Output: True

root1 = [1,2,3,4,5], root2 = [1,2,3,4,None,5]
print(flipEquiv(root1, root2)) # Output: False

root1 = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15], root2 = [1,3,2,6,5,4,7,15,14,13,12,11,10,9,8]
print(flipEquiv(root1, root2)) # Output: True

root1 = [1,2,3,4,None,None,5], root2 = [1,2,None,4,3,None,5]
print(flipEquiv(root1, root2)) # Output: True