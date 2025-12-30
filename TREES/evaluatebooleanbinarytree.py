# EVALUATE BOOLEAN BINARY TREE

'''
You are given the root of a full binary tree with the following properties:
- Leaf nodes have either the value 0 or 1, where 0 represents False and 1 represents True.
- Non-leaf nodes have either the value 2 or 3, where 2 represents the boolean OR and 3 represents the boolean AND.

The evaluation of a node is as follows:
- If the node is a leaf node, the evaluation is the value of the node, i.e. True or False.
- Otherwise, evaluate the node's two children and apply the boolean operation of its value with the children's evaluations.
- Return the boolean result of evaluating the root node.

A full binary tree is a binary tree where each node has either 0 or 2 children.
A leaf node is a node that has zero children.
'''

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
'''
ALGORITHM (Recursive Solution):

1. Define a function `evaluateTree` that takes the `root` of the binary tree as input.
2. Base Case: If the `root` is a leaf node (i.e., `root.left` is `None` AND `root.right` is `None`):
   - Return `True` if `root.val` is `1`, otherwise return `False`.
3. Recursive Step:
   a. Recursively call `evaluateTree` on the `left` child: `left = evaluateTree(root.left)`.
   b. Recursively call `evaluateTree` on the `right` child: `right = evaluateTree(root.right)`.
   c. If `root.val` is `2` (OR operation):
      - Return `left or right`.
   d. If `root.val` is `3` (AND operation):
      - Return `left and right`.

ALGORITHM (Iterative Solution):

1. Define a function `evaluateTrees` that takes the `root` of the binary tree as input.
2. Initialize an empty list `stack` and push the `root` onto it.
3. Initialize an empty dictionary `value` to store the evaluated boolean value for each node.
4. Loop while the `stack` is not empty:
   a. Pop a `node` from the `stack`.
   b. If the `node` is a leaf node (i.e., `node.left` is `None` AND `node.right` is `None`):
      - Store its boolean value in the `value` dictionary: `value[node] = (node.val == 1)`.
   c. Else (if the `node` is a non-leaf node):
      - Check if both children's values are already in the `value` dictionary: `if node.left in value and node.right in value`:
         i. If `node.val` is `2` (OR operation):
            - Store the result of `value[node.left] or value[node.right]` in `value[node]`.
         ii. If `node.val` is `3` (AND operation):
            - Store the result of `value[node.left] and value[node.right]` in `value[node]`.
    - Else (if the `node` is a non-leaf node and children's values are not yet computed):
         - Push the `node` back onto the `stack`.
         - Push `node.right` onto the `stack`.
         - Push `node.left` onto the `stack`.
5. Return `value[root]`.
'''

# Recursive Solution
def evaluateTree(root):
    if not root.left and not root.right:
        return root.val == 1
    
    left = evaluateTree(root.left)
    right = evaluateTree(root.right)
    
    if root.val == 2:
        return left or right
    if root.val == 3:
        return left and right

'''
Time Complexity: O(N), where N is the number of nodes in the binary tree.
This is because we visit each node exactly once to evaluate its value or perform its boolean operation.

Space Complexity: O(H), where H is the height of the binary tree.
This is due to the recursion stack. In the worst case (a skewed tree), H can be N.
In the best case (a balanced tree), H is log N.
'''

# Iterative Solution
def evaluateTrees(root):
    stack = [root]
    value = {}
    
    while stack:
        node = stack.pop()
        if not node.left and not node.right:
            value[node] = node.val == 1
        else:
            if node.left in value and node.right in value:
                if node.val == 2:
                    value[node] = value[node.left] or value[node.right]
                if node.val == 3:
                    vallue[node] = value[node.left] and value[node.right]
            else:
                stack.extend([node, node.left, node.right])
                
    return value[root]

'''
Time Complexity: O(N), where N is the number of nodes in the binary tree.
Each node is pushed onto the stack and processed a constant number of times.

Space Complexity: O(N), where N is the number of nodes in the binary tree.
In the worst case, the stack can hold all nodes, and the `value` dictionary can store results for all nodes.
'''

# Test Cases
root1 = [2,1,3,null,null,0,1]
print(evaluateTree(root1)) # Output: True

root2 = [0]
print(evaluateTree(root2)) # Output: False

root3 = [1]
print(evaluateTree(root3)) # Output: True

root4 = [3,0,1]
print(evaluateTree(root4)) # Output: False

root5 = [2,0,0]
print(evaluateTree(root5)) # Output: False

root6 = [2,1,1]
print(evaluateTree(root6)) # Output: True

root7 = [3,1,1]
print(evaluateTree(root7)) # Output: True

root8 = [2,0,3,null,null,1,1]
print(evaluateTree(root8)) # Output: True

root9 = [3,2,3,0,1,1,0]
print(evaluateTree(root9)) # Output: False

root10 = [2,3,2,0,1,1,0,null,null,null,null,1,1]
print(evaluateTree(root10)) # Output: True