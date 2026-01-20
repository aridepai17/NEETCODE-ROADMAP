# FIND THE SUM OF TWO NODES OF TWO BST

'''
Given two BSTs with root nodes root1 and root2, you are asked to find one node from each of the two trees such that the sum of the values of the two nodes equals the target value.
Returns true if it can be found, otherwise returns false.
'''

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

'''
ALGORITHM:

1. Initialize an empty set `values` to store node values from the first BST.
2. Define a helper function `dfs1(node)` for the first BST (root1):
   a. Base Case: If `node` is `None`, return.
   b. Add `node.val` to the `values` set.
   c. Recursively call `dfs1` on `node.left`.
   d. Recursively call `dfs1` on `node.right`.
3. Define a helper function `dfs2(node)` for the second BST (root2):
   a. Base Case: If `node` is `None`, return `False`.
   b. Check if `target - node.val` exists in the `values` set.
      - If it does, return `True` (a pair is found).
   c. Recursively call `dfs2` on `node.left`.
   d. Recursively call `dfs2` on `node.right`.
   e. Return `True` if either of the recursive calls returns `True`, otherwise return `False`.
4. Call `dfs1(root1)` to populate the `values` set with all nodes from the first BST.
5. Call `dfs2(root2)` to check for the target sum.
6. Return the result of `dfs2(root2)`.
'''

def twoNodesSum(root1, root2, target):
    values = set()
    
    def dfs1(node):
        if not node:
            return 
        values.add(node.val)
        dfs1(node.left)
        dfs1(node.right)
        
    def dfs2(node):
        if not node:
            return False
        if target - node.val in values:
            return True
        return dfs2(node.left) or dfs2(node.right)
    
    dfs1(root1)
    return dfs2(root2)

'''
Time Complexity: O(N1 + N2), where N1 is the number of nodes in root1 and N2 is the number of nodes in root2.
- The first DFS (dfs1) traverses all nodes in root1, adding their values to the set. This takes O(N1) time.
- The second DFS (dfs2) traverses all nodes in root2. For each node, it performs a set lookup, which takes O(1) on average. This takes O(N2) time.
- Therefore, the total time complexity is O(N1 + N2).

Space Complexity: O(N1 + H1 + H2), where N1 is the number of nodes in root1, H1 is the height of root1, and H2 is the height of root2.
- The `values` set stores all unique node values from root1. In the worst case, it can store N1 values, leading to O(N1) space.
- The recursion stack for `dfs1` can go up to O(H1) in the worst case (skewed tree).
- The recursion stack for `dfs2` can go up to O(H2) in the worst case (skewed tree).
- Therefore, the total space complexity is O(N1 + H1 + H2).
'''

# Test Cases
root1 = [2,1,4]
root2 = [1,0,3]
target1 = 5
print(twoNodesSum(root1, root2, target1)) # Output: True

# Test Case 2: Sum not found
root1_2 = build_bst([2,1,4])
root2_2 = build_bst([1,0,3])
target2 = 10
print(twoNodesSum(root1_2, root2_2, target2)) # Output: False

# Test Case 3: Empty trees
root1_3 = None
root2_3 = None
target3 = 5
print(twoNodesSum(root1_3, root2_3, target3)) # Output: False

# Test Case 4: One empty tree
root1_4 = build_bst([2,1,4])
root2_4 = None
target4 = 5
print(twoNodesSum(root1_4, root2_4, target4)) # Output: False

# Test Case 5: Target with negative numbers
root1_5 = build_bst([-2,-1,0])
root2_5 = build_bst([1,2,3])
target5 = 0
print(twoNodesSum(root1_5, root2_5, target5)) # Output: True (-2 + 2 = 0 or -1 + 1 = 0)

# Test Case 6: Larger trees, sum found
root1_6 = build_bst([10,5,15,3,7,12,18])
root2_6 = build_bst([20,13,25,11,17,22,28])
target6 = 30 # 5 + 25 = 30
print(twoNodesSum(root1_6, root2_6, target6)) # Output: True

# Test Case 7: Larger trees, sum not found
root1_7 = build_bst([10,5,15,3,7,12,18])
root2_7 = build_bst([20,13,25,11,17,22,28])
target7 = 100
print(twoNodesSum(root1_7, root2_7, target7)) # Output: False

# Test Case 8: Target with zero
root1_8 = build_bst([0])
root2_8 = build_bst([0])
target8 = 0
print(twoNodesSum(root1_8, root2_8, target8)) # Output: True

# Test Case 9: Target with large numbers
root1_9 = build_bst([1000, 500, 1500])
root2_9 = build_bst([2000, 1200, 2500])
target9 = 3500 # 1000 + 2500 = 3500
print(twoNodesSum(root1_9, root2_9, target9)) # Output: True

# Test Case 10: One tree has only one node, sum found
root1_10 = build_bst([5])
root2_10 = build_bst([1, 2, 3, 4, 5])
target10 = 10 # 5 + 5 = 10
print(twoNodesSum(root1_10, root2_10, target10)) # Output: True