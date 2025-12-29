# BINARY TREE POSTORDER TRAVERSAL

'''
Given the root of a binary tree, return the postorder traversal of its nodes' values.
'''

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

'''
Step-by-step algorithm for Recursive Approach:

1. Define a function `postorderTraversal` that takes the `root` of the binary tree as input.
2. Initialize an empty list `result` to store the postorder traversal.
3. Define a helper function `traverseTree` that takes a `node` as input.
4. Inside `traverseTree`:
   a. If the `node` is `None` (base case), return.
   b. Recursively call `traverseTree` on the `node.left` child.
   c. Recursively call `traverseTree` on the `node.right` child.
   d. Append the `node.val` to the `result` list.
5. Call `traverseTree` with the `root` of the binary tree to start the traversal.
6. Return the `result` list.

Iterative Approach (using a visited flag or two stacks):

1. Define a function `postorderTraversal2` that takes the `root` of the binary tree as input.
2. If the `root` is `None`, return an empty list.
3. Initialize an empty list `result` to store the postorder traversal.
4. Initialize a stack `stack` and push the `root` onto it.
5. Initialize another stack `visited` (or use a set) to keep track of visited nodes for the purpose of processing them after their children.
6. While the `stack` is not empty:
   a. Pop a `node` from the `stack`.
   b. If the `node` is not `None`:
      i. If the `node` has been visited (i.e., it's in the `visited` stack/set), append its value to `result`.
      ii. Else (if the `node` has not been visited):
          1. Push the `node` back onto the `stack`.
          2. Mark the `node` as visited (e.g., push a flag onto `visited` or add to a set).
          3. Push the `node.right` child onto the `stack`.
          4. Push the `node.left` child onto the `stack`.
7. Return the `result` list.
'''

# Recursive Approach
def postorderTraversal(root):
    result = []
    
    def traverseTree(root):
        if not root:
            return 
        
        traverseTree(root.left)
        traverseTree(root.right)
        result.append(root.val)
        
    traverseTree(root)
    return result

'''
Time Complexity: O(N), where N is the number of nodes in the tree.
Each node is visited exactly once.

Space Complexity: O(H), where H is the height of the tree.
This is due to the recursion stack. In the worst case (skewed tree), H can be N.
In the best case (balanced tree), H is log N.
'''

# Iterative Approach
def postorderTraversal2(root):
    stack = [root]
    result = []
    visited = []
    
    while stack:
        current, v = stack.pop(), visited.pop()
        if current:
            if v:
                result.append(current.val)
            else:
                stack.append(current.val)
                visited.append(True)
                stack.append(current.right)
                visited.append(False)
                stack.append(current.left)
                visited.append(False)
                
    return result

'''
Time Complexity: O(N), where N is the number of nodes in the tree.
Each node is pushed onto the stack and popped exactly once.

Space Complexity: O(N), where N is the number of nodes in the tree.
In the worst case (a skewed tree), the stack can hold all nodes.
'''

# Test Cases
root1 = [1,null,2,3]
print(inorderTraversal(root1)) # Output: [3, 2, 1]

root2 = [1,2,3,null,null,4,5]
print(inorderTraversal(root2)) # Output: [5, 4, 3, 2, 1]

root3 = [1,null,2]
print(inorderTraversal(root3)) # Output: [2, 1]

root4 = [1,null,3,2]
print(inorderTraversal(root4)) # Output: [3, 2, 1]

root5 = [1,null,3,null,2]
print(inorderTraversal(root5)) # Output: [3, 2, 1]

root6 = [1,2,null,null,3]
print(inorderTraversal(root6)) # Output: [3, 2, 1]

root7 = [1,null,3,null,null,2]
print(inorderTraversal(root7)) # Output: [3, 2, 1]

root8 = [1,null,3,null,4,null,2]
print(inorderTraversal(root8)) # Output: [4, 3, 2, 1]

root9 = [1,null,3,null,null,2,null,null,5]
print(inorderTraversal(root9)) # Output: [5, 3, 2, 1]

root10 = [1,null,3,null,4,null,2,null,null,5]
print(inorderTraversal(root10)) # Output: [5, 4, 3, 2, 1]