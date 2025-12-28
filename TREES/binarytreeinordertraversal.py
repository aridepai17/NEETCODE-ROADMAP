# BINARY TREE INORDER TRAVERSAL

'''
Given the root of a binary tree, return the inorder traversal of its nodes' values.
'''

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

'''
ALGORITHM (Recursive Approach):

1. Initialize an empty list `result` to store the inorder traversal.
2. Define a helper function `traverseTree(node)`:
   a. Base Case: If `node` is `None`, return.
   b. Recursively call `traverseTree` on the `left` child: `traverseTree(node.left)`.
   c. Append the `node.val` to the `result` list: `result.append(node.val)`.
   d. Recursively call `traverseTree` on the `right` child: `traverseTree(node.right)`.
3. Call the helper function `traverseTree` with the `root` of the binary tree.
4. Return the `result` list.

ALGORITHM (Iterative Approach):

1. Initialize an empty list `result` to store the inorder traversal.
2. Initialize an empty stack `stack`.
3. Initialize a `current` pointer to the `root` of the binary tree.
4. Loop while the `stack` is not empty OR `current` is not `None`:
   a. Inner Loop (traverse left subtree): While `current` is not `None`:
      i. Push `current` onto the `stack`.
      ii. Move `current` to its `left` child: `current = current.left`.
   b. Pop a node from the `stack` and assign it to `current`.
   c. Append `current.val` to the `result` list.
   d. Move `current` to its `right` child: `current = current.right`.
5. Return the `result` list.
'''

# Recursive Approach
def inorderTraversal(root):
    result = []
    
    def traverseTree(root):
        if not root:
            return
        traverseTree(root.left)
        result.append(root.val)
        traverseTree(root.right)
        
    traverseTree(root)
    return result

'''
Time Complexity: O(N) where N is the number of nodes in the tree.
This is because we visit each node exactly once.

Space Complexity: O(H) where H is the height of the tree.
In the worst case (skewed tree), H can be N, so O(N).
In the best case (balanced tree), H is log N, so O(log N).
This space is used by the recursion stack.
'''

# Iterative Approach
def inorderTraversal2(root):
    result = []
    stack = []
    current = root
    
    while stack or current:
        while current:
            stack.append(current)
            current = current.left
        current = stack.pop()
        result.append(current.val)
        current = current.right
        
    return result

'''
Time Complexity: O(N) where N is the number of nodes in the tree.
Each node is pushed onto the stack and popped from the stack exactly once.

Space Complexity: O(H) where H is the height of the tree.
In the worst case (skewed tree), H can be N, so O(N).
In the best case (balanced tree), H is log N, so O(log N).
This space is used by the stack to store tree nodes.
'''

# Test Cases
root1 = [1,null,2,3]
print(inorderTraversal2(root1)) # Output: [1,3,2]


root2 = [1,2,3,null,null,4,5]
print(inorderTraversal2(root2)) # Output: [1,2,3,4,5]

root3 = [1,null,2]
print(inorderTraversal2(root3)) # Output: [1,2]

root4 = [1,null,3,2]
print(inorderTraversal2(root4)) # Output: [1,3,2]

root5 = [1,null,3,null,2]
print(inorderTraversal2(root5)) # Output: [1,3,2]

root6 = [1,null,3,null,null,2]
print(inorderTraversal2(root6)) # Output: [1,3,2]

root7 = [1,null,3,null,4,null,2]
print(inorderTraversal2(root7)) # Output: [1,3,4,2]

root8 = [1,null,3,null,null,null,2]
print(inorderTraversal2(root8)) # Output: [1,3,2]

root9 = [1,null,3,null,4,5,2]
print(inorderTraversal2(root9)) # Output: [1,3,4,5,2]

root10 = [1,null,3,null,null,null,2,null,null,5]
print(inorderTraversal2(root10)) # Output: [1,3,2,5]