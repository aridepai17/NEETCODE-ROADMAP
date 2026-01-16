# CONSTRUCT BINARY TREE FROM PREORDER AND INORDER TRAVERSAL

'''
Given two integer arrays preorder and inorder where preorder is the preorder traversal of a binary tree and inorder is the inorder traversal of the same tree, construct and return the binary tree.
'''

'''
ALGORITHM:
1. Base Case: If preorder or inorder is empty, return None
2. The first element of preorder is always the root of the current subtree
3. Find the index of the root in inorder array (this divides left and right subtrees)
4. Elements to the left of root in inorder belong to left subtree
5. Elements to the right of root in inorder belong to right subtree
6. Recursively build left subtree using:
   - preorder[1:mid+1] (elements after root, count = left subtree size)
   - inorder[:mid] (elements before root)
7. Recursively build right subtree using:
   - preorder[mid+1:] (remaining elements)
   - inorder[mid+1:] (elements after root)
8. Return the constructed root node
'''

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def buildTree(preorder, inorder):
    if not preorder or not inorder:
        return None
    
    root = TreeNode(preorder[0])
    mid = inorder.index(preorder[0])
    root.left = buildTree(preorder[1: mid + 1], inorder[:mid])
    root.right = buildTree(preorder[mid + 1:], inorder[mid + 1:])
    
    return root

'''
TIME COMPLEXITY: O(n^2)
- We process each node once: O(n)
- For each node, we call inorder.index() which takes O(n) in worst case
- Array slicing also takes O(n) for each recursive call
- Overall: O(n^2) in worst case (skewed tree)
- Note: Can be optimized to O(n) using a hashmap to store inorder indices

SPACE COMPLEXITY: O(n)
- Recursion stack: O(h) where h is height of tree
  - Best case (balanced): O(log n)
  - Worst case (skewed): O(n)
- Array slicing creates new arrays at each level: O(n) total
- Overall: O(n)
'''

# Test Cases
preorder1 = [3,9,20,15,7], inorder1 = [9,3,15,20,7]
print(buildTree(preorder1, inorder1)) # Output: [3,9,20,null,null,15,7]

preorder2 = [-1], inorder2 = [-1]
print(buildTree(preorder2, inorder2)) # Output: [-1]

preorder3 = [1,2,3], inorder3 = [3,2,1]
print(buildTree(preorder3, inorder3)) # Output: [1,2,null,3]

preorder4 = [1,2,3], inorder4 = [1,2,3]
print(buildTree(preorder4, inorder4)) # Output: [1,null,2,null,3]

preorder5 = [1,2,4,5,3,6,7], inorder5 = [4,2,5,1,6,3,7]
print(buildTree(preorder5, inorder5)) # Output: [1,2,3,4,5,6,7]

preorder6 = [-10,-20,-5], inorder6 = [-20,-10,-5]
print(buildTree(preorder6, inorder6)) # Output: [-10,-20,-5]

preorder7 = [1,2], inorder7 = [2,1]
print(buildTree(preorder7, inorder7)) # Output: [1,2]

preorder8 = [1,2], inorder8 = [1,2]
print(buildTree(preorder8, inorder8)) # Output: [1,null,2]

preorder9 = [5,4,11,7,2,8,13,4,1], inorder9 = [7,11,2,4,5,13,8,4,1]
print(buildTree(preorder9, inorder9)) # Output: [5,4,8,11,null,13,4,7,2,null,null,null,1]

preorder10 = [], inorder10 = []
print(buildTree(preorder10, inorder10)) # Output: None