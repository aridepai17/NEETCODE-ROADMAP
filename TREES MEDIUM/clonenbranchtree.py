# CLONE N-BRANCH TREE

'''
Given a root of an N-branch tree, return a deep copy (clone) of the tree.
'''

class TreeNode:
    def __init__(self, val=0, children=None):
        self.val = val
        self.children = children if children is not None else []
        
'''
Algorithm:
1. Base Case: If the root is None, return None (empty tree has no clone).
2. Create New Node: Create a new TreeNode with the same value as the current root.
3. Clone Children: Iterate through each child of the current root:
   - Recursively call cloneTree on each child.
   - Append the cloned child to the new node's children list.
4. Return: Return the newly created node (which now has all its children cloned).
This is a DFS (Depth-First Search) approach that:
- Visits the root first
- Then recursively clones all subtrees
- Builds the cloned tree from bottom-up as recursion unwinds
'''

def cloneTree(root):
    if not root:
        return None

    newRoot = TreeNode(root.val)

    for child in root.children:
        newRoot.children.append(cloneTree(child))

    return newRoot

'''
Time Complexity: O(N), where N is the number of nodes in the N-branch tree.
Each node is visited exactly once during the recursive traversal.
For each node, we create a new TreeNode and iterate through its children, performing constant time operations.

Space Complexity: O(H), where H is the maximum depth of the N-branch tree.
This is due to the recursion stack. In the worst case (a skewed tree, e.g., a linked list), H can be N.
In the best case (a very bushy tree with small depth), H can be much smaller than N.
'''

# Test Cases

# Test Case 1: Simple tree [1,2,3]
root1 = TreeNode(1, [TreeNode(2), TreeNode(3)])
print(cloneTree(root1).val)  # Output: 1

# Test Case 2: Empty tree
root2 = None
print(cloneTree(root2))  # Output: None

# Test Case 3: Single node
root3 = TreeNode(5)
print(cloneTree(root3).val)  # Output: 5

# Test Case 4: Tree with 3 levels [1,2,3,4,5,6]
root4 = TreeNode(1, [TreeNode(2, [TreeNode(5), TreeNode(6)]), TreeNode(3), TreeNode(4)])
print(cloneTree(root4).val)  # Output: 1

# Test Case 5: Linear chain [1,2,3,4]
root5 = TreeNode(1, [TreeNode(2, [TreeNode(3, [TreeNode(4)])])])
print(cloneTree(root5).val)  # Output: 1

# Test Case 6: Wide tree [1,2,3,4,5,6,7]
root6 = TreeNode(1, [TreeNode(2), TreeNode(3), TreeNode(4), TreeNode(5), TreeNode(6), TreeNode(7)])
print(cloneTree(root6).val)  # Output: 1

# Test Case 7: Tree with negative values [-1,-2,-3,-4]
root7 = TreeNode(-1, [TreeNode(-2, [TreeNode(-4)]), TreeNode(-3)])
print(cloneTree(root7).val)  # Output: -1

# Test Case 8: Tree with duplicate values [1,1,1,1,1]
root8 = TreeNode(1, [TreeNode(1, [TreeNode(1)]), TreeNode(1), TreeNode(1)])
print(cloneTree(root8).val)  # Output: 1

# Test Case 9: Balanced tree [1,2,3,4,5,6,7,8,9]
root9 = TreeNode(1, [TreeNode(2, [TreeNode(5), TreeNode(6)]), TreeNode(3, [TreeNode(7)]), TreeNode(4, [TreeNode(8), TreeNode(9)])])
print(cloneTree(root9).val)  # Output: 1

# Test Case 10: Large values [1000,999,998]
root10 = TreeNode(1000, [TreeNode(999), TreeNode(998)])
print(cloneTree(root10).val)  # Output: 1000