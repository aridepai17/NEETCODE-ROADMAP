# SERIALIZE AND DESERIALIZE BINARY TREE

'''
Design an algorithm and write code to serialize and deserialize a binary tree. Writing the tree to a file is called 'serialization' and reading back from the file to reconstruct the exact same binary tree is 'deserialization'.
There is no limit on how to serialize or deserialize a binary tree，you just need to ensure the binary tree can be serialized to a string，and the string can be deserialized to original binary tree.
'''

import collections

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

'''
ALGORITHM:

SERIALIZATION (Preorder Traversal):
1. Initialize an empty list `values` to store the serialized values.
2. Define a helper function `preorder(node)`:
    a. If node is None, append "#" to indicate a null node, return.
    b. Append the node's value (as string) to `values`.
    c. Recursively call preorder on node.left.
    d. Recursively call preorder on node.right.
3. Call preorder on the root.
4. Return the comma-separated join of `values`.

DESERIALIZATION:
1. Create a deque from the comma-separated data string.
2. Define a helper function `buildTree()`:
    a. If the deque is empty, return None.
    b. Pop the leftmost value from the deque.
    c. If value is "#", return None.
    d. Create a new TreeNode with the integer value.
    e. Recursively build the left subtree: node.left = buildTree()
    f. Recursively build the right subtree: node.right = buildTree()
    g. Return the node.
3. Call buildTree() and return the reconstructed root.
'''

def serialize(root):
    values = []
    
    def preorder(node):
        if not node:
            values.append("#")
            return
        values.append(str(node.val))
        preorder(node.left)
        preorder(node.right)
        
    preorder(root)
    return ",".join(values)

def deserialize(data):
    queue = collections.deque(data.split(","))
    
    def buildTree():
        if not queue:
            return None
        value = queue.popleft()
        if value == "#":
            return None
        node = TreeNode(int(value))
        node.left = buildTree()
        node.right = buildTree()
        return node
    
    return buildTree()

'''
Time Complexity:
- Serialization: O(N) - We visit each node exactly once.
- Deserialization: O(N) - We process each value in the serialized string exactly once.

Space Complexity:
- Serialization: O(N) - We store N values in the list.
- Deserialization: O(N) - The recursion stack can hold up to N nodes in the worst case.
'''

# Test Cases

# Test Case 1: Simple tree
# Tree:    1
#          / \
#         2   3
root1 = TreeNode(1, TreeNode(2), TreeNode(3))
data1 = serialize(root1)
print("Serialized:", data1)
reconstructed1 = deserialize(data1)
print("Deserialized root:", reconstructed1.val if reconstructed1 else None)
# Expected Serialized: "1,2,#,#,3,#,#"

# Test Case 2: Single node
root2 = TreeNode(1)
data2 = serialize(root2)
print("Serialized:", data2)
reconstructed2 = deserialize(data2)
print("Deserialized root:", reconstructed2.val if reconstructed2 else None)
# Expected Serialized: "1,#,#"

# Test Case 3: Empty tree
root3 = None
data3 = serialize(root3)
print("Serialized:", data3)
reconstructed3 = deserialize(data3)
print("Deserialized root:", reconstructed3)
# Expected Serialized: ""

# Test Case 4: Tree with null children
# Tree:    1
#          /
#         2
root4 = TreeNode(1, TreeNode(2))
data4 = serialize(root4)
print("Serialized:", data4)
reconstructed4 = deserialize(data4)
print("Deserialized root:", reconstructed4.val if reconstructed4 else None)
# Expected Serialized: "1,2,#,#,#,#"

# Test Case 5: Complete binary tree
# Tree:    1
#          / \
#         2   3
#        / \ / \
#       4  5 6  7
root5 = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3, TreeNode(6), TreeNode(7)))
data5 = serialize(root5)
print("Serialized:", data5)
reconstructed5 = deserialize(data5)
print("Deserialized root:", reconstructed5.val if reconstructed5 else None)
# Expected Serialized: "1,2,4,#,#,5,#,#,3,6,#,#,7,#,#"

# Test Case 6: Left-skewed tree
# Tree:    1
#          /
#         2
#        /
#       3
root6 = TreeNode(1, TreeNode(2, TreeNode(3)))
data6 = serialize(root6)
print("Serialized:", data6)
reconstructed6 = deserialize(data6)
print("Deserialized root:", reconstructed6.val if reconstructed6 else None)
# Expected Serialized: "1,2,3,#,#,#,#"

# Test Case 7: Right-skewed tree
# Tree:    1
#           \
#            2
#             \
#              3
root7 = TreeNode(1, None, TreeNode(2, None, TreeNode(3)))
data7 = serialize(root7)
print("Serialized:", data7)
reconstructed7 = deserialize(data7)
print("Deserialized root:", reconstructed7.val if reconstructed7 else None)
# Expected Serialized: "1,#,2,#,3,#,#"

# Test Case 8: Tree with negative values
# Tree:    -1
#          / \
#        -2   -3
root8 = TreeNode(-1, TreeNode(-2), TreeNode(-3))
data8 = serialize(root8)
print("Serialized:", data8)
reconstructed8 = deserialize(data8)
print("Deserialized root:", reconstructed8.val if reconstructed8 else None)
# Expected Serialized: "-1,-2,#,#,-3,#,#"

# Test Case 9: Larger tree
# Tree:      1
#           / \
#          2   3
#         /   / \
#        4   5   6
root9 = TreeNode(1, TreeNode(2, TreeNode(4)), TreeNode(3, TreeNode(5), TreeNode(6)))
data9 = serialize(root9)
print("Serialized:", data9)
reconstructed9 = deserialize(data9)
print("Deserialized root:", reconstructed9.val if reconstructed9 else None)
# Expected Serialized: "1,2,4,#,#,#,3,5,#,#,6,#,#"

# Test Case 10: Tree with zeros
# Tree:    0
#          / \
#         0   0
root10 = TreeNode(0, TreeNode(0), TreeNode(0))
data10 = serialize(root10)
print("Serialized:", data10)
reconstructed10 = deserialize(data10)
print("Deserialized root:", reconstructed10.val if reconstructed10 else None)
# Expected Serialized: "0,0,#,#,0,#,#"
