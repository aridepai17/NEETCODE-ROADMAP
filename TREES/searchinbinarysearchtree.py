# SEARCH IN BINARY SEARCH TREE

'''
You are given the root of a binary search tree (BST) and an integer val.
Find the node in the BST that the node's value equals val and return the subtree rooted with that node. 
If such a node does not exist, return null.
'''

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

'''
ALGORITHM:

1. Define a function `searchTree` that takes the `root` of the BST and an integer `val` as input.
2. Initialize a `while` loop that continues as long as `root` is not `None`.
   a. Inside the loop, compare `root.val` with `val`.
   b. If `root.val` is equal to `val`:
      - The node with the target value is found.
      - Return `root` (the subtree rooted at this node).
   c. Else if `val` is less than `root.val`:
      - The target value, if it exists, must be in the left subtree.
      - Move `root` to its `left` child: `root = root.left`.
   d. Else (if `val` is greater than `root.val`):
      - The target value, if it exists, must be in the right subtree.
      - Move `root` to its `right` child: `root = root.right`.
3. If the loop finishes (meaning `root` becomes `None`) and the value was not found, return `None`.
'''

def searchTree(root, val):
    while root:
        if root.val == val:
            return root
        elif val < root.val:
            root = root.left
        else:
            root = root.right
    return None

'''
Time Complexity: O(H), where H is the height of the BST.
In the worst case (a skewed tree), H can be N, where N is the number of nodes.
In the best case (a balanced tree), H is log N.
This is because in each step, we move down one level in the tree.

Space Complexity: O(1).
We are only using a few pointers (root) and not allocating any additional data structures that grow with the input size.
'''

# Test Cases
root1 = [4,2,7,1,3], val1 = 2
print(searchTree(root1, val1)) # Output: [2,1,3]

root2 = [4,2,7,1,3], val2 = 5
print(searchTree(root2, val2)) # Output: None

root3 = [1,None,2], val3 = 2
print(searchTree(root3, val3)) # Output: [2]

root4 = [10,5,15,3,7,None,18], val4 = 7
print(searchTree(root4, val4)) # Output: [7]

root5 = [10,5,15,3,7,None,18], val5 = 10
print(searchTree(root5, val5)) # Output: [10,5,15,3,7,None,18]

root6 = [10,5,15,3,7,None,18], val6 = 18
print(searchTree(root6, val6)) # Output: [18]

root7 = [10,5,15,3,7,None,18], val7 = 3
print(searchTree(root7, val7)) # Output: [3]

root8 = [10,5,15,3,7,None,18], val8 = 1
print(searchTree(root8, val8)) # Output: None

root9 = [1], val9 = 1
print(searchTree(root9, val9)) # Output: [1]

root10 = [], val10 = 1
print(searchTree(root10, val10)) # Output: None