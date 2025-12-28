# BINARY TREE PREORDER TRAVERSAL

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

1. Initialize an empty list `result` to store the preorder traversal.
2. Define a helper function `traverseTree(node)`:
   a. Base Case: If `node` is `None`, return.
   b. Append the `node.val` to the `result` list: `result.append(node.val)`.
   c. Recursively call `traverseTree` on the `left` child: `traverseTree(node.left)`.
   d. Recursively call `traverseTree` on the `right` child: `traverseTree(node.right)`.
3. Call the helper function `traverseTree` with the `root` of the binary tree.
4. Return the `result` list.

ALGORITHM (Iterative Approach):

1. Initialize an empty list `result` to store the preorder traversal.
2. Initialize an empty stack `stack`.
3. If the `root` is `None`, return `result`.
4. Push the `root` onto the `stack`.
5. Loop while the `stack` is not empty:
   a. Pop a node from the `stack` and assign it to `current`.
   b. Append `current.val` to the `result` list.
   c. If `current.right` is not `None`, push `current.right` onto the `stack`.
   d. If `current.left` is not `None`, push `current.left` onto the `stack`.
      (Note: Push right child first, then left child, so left child is processed first due to LIFO stack behavior).
6. Return the `result` list.
'''

# Recursive Approach
def preorderTraversal(root):
    result = []
    
    def traverseTree(root):
        if not root:
            return 
        
        result.append(root.val)
        traverseTree(root.left)
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
def preorderTraversal2(root):
    stack = []
    result = []
    current = root
    
    while current or stack:
        if current:
            result.append(current.val)
            stack.append(current.right)
            current = current.left
        else:
            current = stack.pop()
            
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
print(preorderTraversal2(root1)) # Output: [1,2,3]


root2 = [1,2,3,null,null,4,5]
print(preorderTraversal2(root2)) # Output: [1,2,3,4,5]

root3 = [1,2,null,null,3]
print(preorderTraversal2(root3)) # Output: [1,2,3]

root4 = [1,null,2,3,null,null,4]
print(preorderTraversal2(root4)) # Output: [1,2,3,4]

root5 = [1,null,3,2,4,null,null,5]
print(preorderTraversal2(root5)) # Output: [1,3,2,4,5]

root6 = [1,null,3,null,2,null,4,null,null,5]
print(preorderTraversal2(root6)) # Output: [1,3,2,4,5]

root7 = [1,null,3,null,2,null,4,5,null,null,null,6]
print(preorderTraversal2(root7)) # Output: [1,3,2,4,5,6]

root8 = [1,2,3,null,null,null,4,null,5,null,null,6]
print(preorderTraversal2(root8)) # Output: [1,2,3,4,5,6]

root9 = [1,null,3,2,null,null,4,null,null,5,null,null,6]
print(preorderTraversal2(root9)) # Output: [1,3,2,4,5,6]

root10 = [1,null,3,2,4,null,5,null,null,6]
print(preorderTraversal2(root10)) # Output: [1,3,2,4,5,6]