# N-ARY TREE POSTORDER TRAVERSAL

'''
Given the root of an n-ary tree, return the postorder traversal of its nodes' values.
Nary-Tree input serialization is represented in their level order traversal. 
Each group of children is separated by the null value.
'''

class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []

'''
Step-by-step algorithm for Recursive Approach:

1. Define a function `postorder` that takes the `root` of the N-ary tree as input.
2. Initialize an empty list `result` to store the postorder traversal.
3. Define a helper function `traverseTree` that takes a `node` as input.
4. Inside `traverseTree`:
   a. If the `node` is `None` (base case), return.
   b. Iterate through each `child` in `node.children`:
      i. Recursively call `traverseTree` on the `child`.
   c. Append the `node.val` to the `result` list.
5. Call `traverseTree` with the `root` of the N-ary tree to start the traversal.
6. Return the `result` list.

Step-by-step algorithm for Iterative Approach:

1. Define a function `postorder2` that takes the `root` of the N-ary tree as input.
2. If the `root` is `None`, return an empty list.
3. Initialize an empty list `result` to store the postorder traversal.
4. Initialize a stack `stack` and push a tuple `(root, False)` onto it. The `False` flag indicates that the node's children have not yet been processed.
5. While the `stack` is not empty:
   a. Pop a `node` and its `visited` flag from the `stack`.
   b. If `visited` is `True`:
      i. Append `node.val` to the `result` list.
   c. Else (`visited` is `False`):
      i. Push the `node` back onto the `stack` with `True` as its `visited` flag (indicating that its children will be processed next, and then the node itself).
      ii. Iterate through the `node.children` in reverse order:
          1. For each `child`, push `(child, False)` onto the `stack`. (Pushing in reverse order ensures left children are processed before right children when popped).
6. Return the `result` list.
'''

# Recursive Approach
def postorder(root):
    result = []
    
    def traverseTree(root):
        if not root:
            return
        
        for child in root.children:
            traverseTree(child)
        result.append(root.val)
        
    traverseTree(root)
    return result

'''
Time Complexity: O(N), where N is the number of nodes in the N-ary tree.
Each node is visited exactly once.

Space Complexity: O(H), where H is the maximum depth of the N-ary tree.
This is due to the recursion stack. In the worst case (a skewed tree where each node has only one child), H can be N.
'''

# Iterative Approach
def postorder2(root):
    if not root:
        return []
    
    result = []
    stack = [(root, False)]
    
    while stack:
        node, visited = stack.pop()
        if visited:
            result.append(node.val)
        else:
            stack.append((node, True))
            for c in node.children[::-1]:
                stack.append((c, False))
                
    return result

'''
Time Complexity: O(N), where N is the number of nodes in the N-ary tree.
Each node is pushed onto the stack and popped exactly once.
The children are iterated over once for each node.

Space Complexity: O(H), where H is the maximum depth of the N-ary tree.
In the worst case (a skewed tree), the stack can hold all nodes, leading to O(N) space.
In the best case (a balanced tree), the stack space is proportional to the height of the tree.
'''

# Test Cases
root1 = [1,null,3,2,4,null,5,6]
print(postorder(root1)) # Output: [5,6,3,2,4,1]

root2 = [1,null,2,3,4,5,null,null,6,7,null,null,8,null,9,10,null,null,11,null,12,null,13,null,null,14]
print(postorder(root2)) # Output: [2,6,14,11,7,3,12,8,4,13,9,10,5,1]

root3 = []
print(postorder(root3)) # Output: []

root4 = [1]
print(postorder(root4)) # Output: [1]

root5 = [1,null,2,null,3,null,4,null,5]
print(postorder(root5)) # Output: [5,4,3,2,1]

root6 = [1,null,2,3,null,4,5,null,6,7,null,8,9,null,10,11,null,12,null,13,null,null,14]
print(postorder(root6)) # Output: [2,6,12,13,14,11,10,9,8,7,5,4,3,1]

root7 = [1,null,3,2,4]
print(postorder(root7)) # Output: [2,4,3,1]

root8 = [1,null,2,null,3,null,4,null,5,null,6,null,7]
print(postorder(root8)) # Output: [7,6,5,4,3,2,1]

root9 = [1,null,3,2,4,null,5,6,null,7,8,null,9,10,null,11,12,null,13,null,null,14]
print(postorder(root9)) # Output: [7,11,12,13,14,10,9,8,6,5,4,2,3,1]

root10 = [1,null,2,3,4,5,null,null,6,7,null,8,null,9,10,null,null,11,null,12,null,13,null,null,14]
print(postorder(root10)) # Output: [6,14,11,7,12,13,10,9,8,5,4,3,2,1]