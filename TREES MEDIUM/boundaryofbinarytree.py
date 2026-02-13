# BOUNDARY OF BINARY TREE

'''
Given a binary tree, return the values of its boundary in anti-clockwise direction starting from root. Boundary includes left boundary, leaves, and right boundary in order without duplicate nodes.
Left boundary is defined as the path from root to the left-most node. Right boundary is defined as the path from root to the right-most node. 
If the root doesn't have left subtree or right subtree, then the root itself is left boundary or right boundary. 
Note this definition only applies to the input binary tree, and not applies to any subtrees.
The left-most node is defined as a leaf node you could reach when you always firstly travel to the left subtree if exists.
If not, travel to the right subtree. Repeat until you reach a leaf node.
The right-most node is also defined by the same way with left and right exchanged.
'''

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

'''
ALGORITHM:

1. Define a function `boundaryOfBinaryTree` that takes the `root` of the binary tree as input.
2. If the `root` is `None`, return an empty list.
3. Define a helper function `isLeaf(node)` that returns `True` if the node has no left and right children.
4. Initialize an empty list `result` to store the boundary nodes.
5. Add the root value to `result` if the root is not a leaf node (to avoid duplicates).
6. Process the LEFT BOUNDARY:
        a. Start from `root.left` and traverse down to the left.
        b. For each node that is not a leaf, add its value to `result`.
        c. Always prefer going left if available, otherwise go right.
7. Define a helper function `addLeaves(node)` that performs an in-order traversal:
        a. If the node is `None`, return.
        b. If the node is a leaf, add its value to `result`.
        c. Recursively call `addLeaves` on the left child, then the right child.
8. Call `addLeaves(root)` to add all leaf nodes.
9. Process the RIGHT BOUNDARY:
        a. Start from `root.right` and traverse down to the right.
        b. For each node that is not a leaf, add its value to a temporary list `rightBoundary`.
        c. Always prefer going right if available, otherwise go left.
10. Reverse the `rightBoundary` list and extend `result` with it (to maintain anti-clockwise order).
11. Return the `result` list containing all boundary nodes in the correct order.
'''

def boundaryOfBinaryTree(root):
    if not root:
        return []
    
    def isLeaf(node):
        return not node.left and not node.right
    
    result = []
    
    if not isLeaf(root):
        result.append(root.val)
        
    current = root.left
    while current:
        if not isLeaf(current):
            result.append(current.val)
        if current.left:
            current = current.left
        else:
            current = current.right
            
    def addLeaves(node):
        if not node:
            return 
        if isLeaf(node):
            result.append(node.val)
        addLeaves(node.left)
        addLeaves(node.right)
        
        
    addLeaves(root)
    
    rightBoundary = []
    current = root.right
    while current:
        if not isLeaf(current):
            rightBoundary.append(current.val)
        if current.right:
            current = current.right
        else:
            current = current.left
            
    result.extend(reversed(rightBoundary))
    
    return result

'''
Time Complexity: O(N), where N is the number of nodes in the binary tree.
We visit each node exactly once:
- Left boundary traversal visits nodes along the left path: O(H) where H is the height
- Right boundary traversal visits nodes along the right path: O(H) where H is the height
- Leaf traversal (DFS) visits all nodes: O(N)
In the worst case (skewed tree), this becomes O(N).
In the best case (balanced tree), this is still O(N) because we need to visit all nodes anyway.

Space Complexity: O(H), where H is the height of the binary tree.
This is due to the recursion stack in the `addLeaves` function.
In the worst case (skewed tree), H can be N, resulting in O(N) space.
In the best case (balanced tree), H is log N, resulting in O(log N) space.
The `result` list and `rightBoundary` list store up to N nodes, but this is output space.
'''

# Test Cases
root1 = [1,2,3,4,5,6]
print(boundaryOfBinaryTree(root1)) # Output: [1,2,4,6,3]

root2 = [1,2,3,4,5,null,6,null,null,7]
print(boundaryOfBinaryTree(root2)) # Output: [1,2,7,6,3]

root3 = [1,null,2,3]
print(boundaryOfBinaryTree(root3)) # Output: [1,2,3]

root4 = [1,2,3,null,4]
print(boundaryOfBinaryTree(root4)) # Output: [1,2,4,3]

root5 = [1,2,3,4,null,5,6,null,7,null,null,8]
print(boundaryOfBinaryTree(root5)) # Output: [1,2,7,8,6,3]

root6 = [1]
print(boundaryOfBinaryTree(root6)) # Output: [1]

root7 = [1,2]
print(boundaryOfBinaryTree(root7)) # Output: [1,2]

root8 = [1,null,2]
print(boundaryOfBinaryTree(root8)) # Output: [1,2]

root9 = [1,2,3,4,5,6,null,7,8]
print(boundaryOfBinaryTree(root9)) # Output: [1,2,7,8,6,3]

root10 = [1,2,3,4,5,null,6,null,7,null,null,8,9]
print(boundaryOfBinaryTree(root10)) # Output: [1,2,7,8,9,6,3]