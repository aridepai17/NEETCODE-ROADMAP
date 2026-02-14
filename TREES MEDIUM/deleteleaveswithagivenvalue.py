# DELETE LEAVES WITH A GIVEN VALUE

'''
Given a binary tree root and an integer target, delete all the leaf nodes with value target.
Note that once you delete a leaf node with value target, if its parent node becomes a leaf node and has the value target, it should also be deleted (you need to continue doing that until you cannot).
'''

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

'''
ALGORITHM:

1. Define a recursive function `removeLeafNodes(root, target)` that returns the modified subtree.
2. Base case: If `root` is `None`, return `None`.
3. Recursively process the left subtree:
    - `root.left = removeLeafNodes(root.left, target)`
4. Recursively process the right subtree:
    - `root.right = removeLeafNodes(root.right, target)`
5. After processing children, check if current node is a leaf node with value equal to target:
    - A leaf node has both left and right children as `None`
    - If `root.left is None and root.right is None and root.val == target`:
        - Return `None` to delete this node
6. Otherwise, return the current `root` node (which may have been modified by the recursive calls).
7. The recursion naturally handles the cascading deletion because after removing a child, 
   the parent might become a leaf node with the target value, and it will be handled in the next recursive call.
'''

def removeLeafNodes(root, target):
    if not root:
        return None
    
    root.left = removeLeafNodes(root.left, target)
    root.right = removeLeafNodes(root.right, target)
    
    if root.left is None and root.right is None and root.val == target:
        return None
    
    return root

'''
Time Complexity: O(N), where N is the number of nodes in the binary tree.
In the worst case, we visit each node exactly once. Even if we delete nodes, 
the recursion still processes each node once.

Space Complexity: O(H), where H is the height of the tree.
The recursion stack depth equals the height of the tree:
- Worst case (skewed tree): O(N)
- Best case (balanced tree): O(log N)
'''

# Test Cases

# Test Case 1: Standard case - delete leaf nodes with value 2
# Input: root = [1,2,3,2,null,2,4], target = 2
root1 = TreeNode(1, TreeNode(2, TreeNode(2), TreeNode(3)), TreeNode(2, TreeNode(2), TreeNode(4)))
result1 = removeLeafNodes(root1, 2)
# Expected: [1, null, 3, null, null, null, 4]

# Test Case 2: Single node with target value
root2 = TreeNode(2)
result2 = removeLeafNodes(root2, 2)
print(result2) # Expected: None

# Test Case 3: Single node with non-target value
root3 = TreeNode(1)
result3 = removeLeafNodes(root3, 2)
print(result3) # Expected: [1]

# Test Case 4: Empty tree
root4 = None
result4 = removeLeafNodes(root4, 2)
print(result4) # Expected: None

# Test Case 5: Delete all leaf nodes
# Input: [1,2,3], target = 2
root5 = TreeNode(1, TreeNode(2), TreeNode(3))
result5 = removeLeafNodes(root5, 2)
# Expected: [1, null, 3]

# Test Case 6: No nodes with target value
root6 = TreeNode(1, TreeNode(2), TreeNode(3))
result6 = removeLeafNodes(root6, 5)
# Expected: [1, 2, 3]

# Test Case 7: Cascading deletion
# Input: [1,2,3,2,null,2], target = 2
root7 = TreeNode(1, TreeNode(2, TreeNode(2), TreeNode(3)), TreeNode(2, TreeNode(2)))
result7 = removeLeafNodes(root7, 2)
# Expected: [1]

# Test Case 8: Left-skewed tree with target at leaves
root8 = TreeNode(1, TreeNode(2, TreeNode(3)))
result8 = removeLeafNodes(root8, 3)
# Expected: [1, 2]

# Test Case 9: Right-skewed tree with target at leaves
root9 = TreeNode(1, None, TreeNode(2, None, TreeNode(3)))
result9 = removeLeafNodes(root9, 3)
# Expected: [1, None, 2]

# Test Case 10: Multiple deletions at different levels
# Input: [1,2,3,4,5], target = 4
root10 = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3))
result10 = removeLeafNodes(root10, 4)
# Expected: [1, 2, 3, null, 5]