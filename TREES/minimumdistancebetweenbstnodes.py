# MINIMUM DISTANCE BETWEEN BST NODES

'''
Given the root of a Binary Search Tree (BST), return the minimum difference between the values of any two different nodes in the tree.
'''

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

'''
ALGORITHM:

1. Initialize a variable `prev` to `None`. This will keep track of the previously visited node during the inorder traversal.
2. Initialize a variable `result` to `float('inf')`. This will store the minimum difference found so far.
3. Define a helper function `dfs(node)` for an inorder traversal:
   a. Base Case: If `node` is `None`, return.
   b. Recursively call `dfs` on the `left` child: `dfs(node.left)`.
   c. After visiting the left subtree, process the current `node`:
      i. Declare `prev` and `result` as `nonlocal` to modify the variables in the outer scope.
      ii. If `prev` is not `None` (meaning this is not the very first node visited):
          - Calculate the difference between the current `node.val` and `prev.val`.
          - Update `result` with the minimum of the current `result` and this new difference: `result = min(result, node.val - prev.val)`.
      iii. Set `prev` to the current `node`: `prev = node`.
   d. Recursively call `dfs` on the `right` child: `dfs(node.right)`.
4. Call the `dfs` function with the `root` of the BST.
5. Return the final `result`.
'''

def minDiffBST(root):
    prev = None
    result = float('inf')
    
    def dfs(node):
        if not node:
            return
        dfs(node.left)
        nonlocal prev, result
        if prev:
            result = min(result, node.val - prev.val)
        prev = node
        dfs(node.right)

    dfs(root)
    return result

'''
Time Complexity: O(N), where N is the number of nodes in the BST.
This is because we perform an inorder traversal, visiting each node exactly once.

Space Complexity: O(H), where H is the height of the BST.
This is due to the recursion stack for the DFS traversal. In the worst case (a skewed tree), H can be N.
In the best case (a balanced tree), H is log N.
'''

# Test Cases
root1 = [4,2,6,1,3]
print(minDiffBST(root1)) # Output: 1

root2 = [1,0,48,null,null,12,49]
print(minDiffBST(root2)) # Output: 1

root3 = [90,69,null,49,89,null,52]
print(minDiffBST(root3)) # Output: 1

root4 = [10,4,15,1,8,null,null]
print(minDiffBST(root4)) # Output: 2

root5 = [1,null,2]
print(minDiffBST(root5)) # Output: 1

root6 = [2,1,3]
print(minDiffBST(root6)) # Output: 1

root7 = [5,3,7,2,4,6,8]
print(minDiffBST(root7)) # Output: 1

root8 = [50,30,70,20,40,60,80]
print(minDiffBST(root8)) # Output: 10

root9 = [100,50,200,25,75,150,250]
print(minDiffBST(root9)) # Output: 25

root10 = [100,50,200,25,75,150,250,10,30,60,80,125,175,225,275]
print(minDiffBST(root10)) # Output: 5