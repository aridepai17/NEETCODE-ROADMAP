# COUNT GOOD NODES IN BINARY TREE

'''
Given a binary tree root, a node X in the tree is named good if in the path from root to X there are no nodes with a value greater than X.
Return the number of good nodes in the binary tree.
'''

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

'''
ALGORITHM:

1. Define a function `goodNodes` that takes the `root` of the binary tree as input.
2. Define a helper function `dfs(node, maxValue)`:
   a. Base Case: If `node` is `None`, return `0` (no good nodes in an empty subtree).
   b. Initialize `result` to `0`.
   c. If `node.val` is greater than or equal to `maxValue` (the maximum value encountered so far on the path from the root to the parent of the current node):
      - Increment `result` by `1` (the current node is a good node).
   d. Update `maxValue` to be the maximum of its current value and `node.val`. This ensures `maxValue` always holds the maximum value encountered on the path to the current node.
   e. Recursively call `dfs` on the `left` child with the updated `maxValue` and add its return value to `result`.
   f. Recursively call `dfs` on the `right` child with the updated `maxValue` and add its return value to `result`.
   g. Return `result`.
3. Call the `dfs` function with the `root` of the binary tree and an initial `maxValue` equal to `root.val`.
4. Return the final count of good nodes.
'''

def goodNodes(root):
    def dfs(node, maxValue):
        if not node:
            return 0
        
        if node.val >= maxValue:
            result = 1
        else:
            result = 0
        
        maxValue = max(maxValue, node.val)
        result += dfs(node.left, maxValue)
        result += dfs(node.right, maxValue)
        
    return dfs(root, root.val)

'''
Time Complexity: O(N), where N is the number of nodes in the binary tree.
Each node is visited exactly once during the DFS traversal.

Space Complexity: O(H), where H is the height of the binary tree.
This is due to the recursion stack. In the worst case (a skewed tree), H can be N.
In the best case (a balanced tree), H is log N.
'''

# Test Cases
root1 = [3,1,4,3,null,1,5]
print(goodNodes(root1)) # Output: 4

root2 = [3,3,null,4,2]
print(goodNodes(root2)) # Output: 3

root3 = [1]
print(goodNodes(root3)) # Output: 1

root4 = [1,2,3]
print(goodNodes(root4)) # Output: 3

root5 = [5,4,3,null,null,null,6]
print(goodNodes(root5)) # Output: 3

root6 = [9,null,3,6]
print(goodNodes(root6)) # Output: 1

root7 = [-1, -2, -3, -4, -5, -6, -7]
print(goodNodes(root7)) # Output: 1

root8 = [10, 5, 15, 2, 7, 12, 17]
print(goodNodes(root8)) # Output: 7

root9 = [2, 3, 1]
print(goodNodes(root9)) # Output: 2

root10 = [3, 6, 1, 9, 2, 8, 4]
print(goodNodes(root10)) # Output: 3