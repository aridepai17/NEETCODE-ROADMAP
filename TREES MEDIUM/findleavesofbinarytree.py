# FIND LEAVES OF BINARY TREE

'''
Given a binary tree, collect a tree's nodes as if you were doing this: Collect and remove all leaves, repeat until the tree is empty.
'''

'''
ALGORITHM:
1. Use a recursive helper function `getHeight(node)` that returns the height of the node
2. The height is defined as the distance from the node to its deepest leaf (0 for null nodes)
3. For each node, compute the height as 1 + max(left_height, right_height)
4. The height determines which group the node belongs to:
        - Height 0 = first group of leaves
        - Height 1 = second group of leaves
        - Height 2 = third group of leaves, etc.
5. Use a `result` list where result[i] contains all nodes at height i
6. Dynamically append new lists to result when a new height is encountered
7. Return the result list containing all groups of leaves
'''

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def findLeaves(root):
    result = []
    
    def getHeight(node):
        if not node:
            return -1 
        
        left = getHeight(node.left)
        right = getHeight(node.right)
        
        currentHeight = 1 + max(left, right)
        
        if len(result) == currentHeight:
            result.append([])
            
        result[currentHeight].append(node.val)
        
        return currentHeight
    
    getHeight(root)
    return result

'''
Time Complexity: O(N), where N is the number of nodes in the binary tree.
Each node is visited exactly once during the post-order traversal.
All operations within the traversal (comparisons, appending to lists) are O(1) per node.

Space Complexity: O(H), where H is the height of the binary tree.
The recursion stack can have up to H frames at any time.
Additionally, the result list stores all N nodes across all height groups.
Therefore, total space is O(H + N), but since H ≤ N, it's O(N) in the worst case.
'''

# Test Cases
root1 = [1, 2, 3, 4, 5]
print(findLeaves(buildTree(root1)))  # Output: [[4, 5, 2], [3], [1]]

root2 = [1]
print(findLeaves(buildTree(root2)))  # Output: [[1]]

root3 = [1, 2, 3, None, 4]
print(findLeaves((root3)))  # Output: [[4, 2], [3], [1]]

root4 = [1, 2, 3, 4, 5, 6, 7]
print(findLeaves(buildTree(root4)))  # Output: [[4, 5, 6, 7], [2, 3], [1]]

root5 = [1, 2, None, 3, None, 4, None]
print(findLeaves(buildTree(root5)))  # Output: [[4], [3], [2], [1]]

root6 = [1, 2, 3, None, None, 4, 5]
print(findLeaves(buildTree(root6)))  # Output: [[4, 5], [3], [2], [1]]

root7 = [1, 2, 3, 4, None, None, 5]
print(findLeaves(buildTree(root7)))  # Output: [[4, 5], [2], [3], [1]]

root8 = [1, 2, 3, 4, 5, None, 6, 7]
print(findLeaves(buildTree(root8)))  # Output: [[7, 5, 6], [4], [2], [3], [1]]

root9 = [1, 2, 3, None, 4, 5, None]
print(findLeaves(buildTree(root9)))  # Output: [[4, 5], [2], [3], [1]]

root10 = [1, 2, None, 3, None, None, 4]
print(findLeaves(buildTree(root10)))  # Output: [[4], [3], [2], [1]]