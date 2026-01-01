# BINARY TREE PATH

# Given the root of a binary tree, return all root-to-leaf paths in any order. A leaf is a node with no children.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

'''
ALGORITHM:

1. Define a function `binaryTreePath` that takes the `root` of the binary tree as input.
2. If the `root` is `None`, return an empty list `[]` (no paths in an empty tree).
3. Initialize an empty list `result` to store all the root-to-leaf paths.
4. Define a helper function `dfs(node, path)`:
   a. Base Case: If `node` is a leaf node (i.e., `node.left` is `None` AND `node.right` is `None`):
      - Append the current `path` string to the `result` list.
      - Return.
   b. Recursive Step:
      - If `node.left` exists:
         - Recursively call `dfs` on `node.left`, extending the `path` with "->" and `node.left.val`.
      - If `node.right` exists:
         - Recursively call `dfs` on `node.right`, extending the `path` with "->" and `node.right.val`.
5. Call the `dfs` function with the `root` of the binary tree and an initial `path` string containing only `root.val`.
6. Return the `result` list.
'''

def binaryTreePath(root):
    if not root:
        return []
    result = []
    
    def dfs(node, path):
        if not node.left and not node.right:
            result.append(path)
            return 
        if node.left:
            dfs(node.left, path + "->" + str(node.left.val))
        if node.right:
            dfs(node.right, path + "->" + str(node.right.val))
            
    dfs(root, str(root.val))
    return result

'''
Time Complexity: O(N), where N is the number of nodes in the binary tree.
Each node is visited exactly once. In the worst case (a skewed tree), the path string construction
and appending to the result list can take O(H) time for each leaf node, where H is the height of the tree.
Since there can be up to N/2 leaf nodes, the total time could be closer to O(N*H) in the worst case
if string concatenation is inefficient. However, in Python, string concatenation for paths is often
optimized or the average case is considered O(N) because the total length of all paths is bounded.

Space Complexity: O(H), where H is the height of the binary tree.
This is due to the recursion stack. In the worst case (a skewed tree), H can be N.
In the best case (a balanced tree), H is log N.
Additionally, the `result` list stores all paths. In the worst case, if all nodes are leaves (e.g., a linked list),
the total length of all path strings could be O(N*H).
'''

# Test Cases
root1 = [1,2,3,None,5]
print(binaryTreePath(root1)) # Output: ["1->2->5", "1->3"]

root2 = [1,2,3,4]
print(binaryTreePath(root2)) # Output: ["1->2", "1->3", "1->4"]

root3 = [1,2,3,None,4]
print(binaryTreePath(root3)) # Output: ["1->2", "1->3->4"]

root4 = [1,2,3,None,4,5]
print(binaryTreePath(root4)) # Output: ["1->2", "1->3->5", "1->4"]

root5 = [1,2,3,None,4,None,5]
print(binaryTreePath(root5)) # Output: ["1->2", "1->3->5", "1->4"]

root6 = [1,2,None,3,None,4,5]
print(binaryTreePath(root6)) # Output: ["1->2->5", "1->3->4"]

root7 = [1,2,3,None,None,4,5]
print(binaryTreePath(root7)) # Output: ["1->2->5", "1->3->4"]

root8 = [1,2,3,None,None,None,4,5]
print(binaryTreePath(root8)) # Output: ["1->2->4", "1->2->5", "1->3"]

root9 = [1,2,3,None,4,None,5,None,6]
print(binaryTreePath(root9)) # Output: ["1->2->5->6", "1->2->4", "1->3"]

root10 = [1,2,3,None,4,5,6]
print(binaryTreePath(root10)) # Output: ["1->2->5->6", "1->2->4", "1->3"]