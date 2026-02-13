# BINARY TREE LONGEST CONSECUTIVE SEQUENCE

'''
Given a binary tree, find the length of the longest consecutive sequence path.
The path refers to any sequence of nodes from some starting node to any node in the tree along the parent-child connections. 
The longest consecutive path need to be from parent to child (cannot be the reverse).
'''

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

'''
ALGORITHM:

1. Initialize a variable `maxStreak` to 0. This will track the maximum length of consecutive sequence found so far.
2. Define a helper function `dfs(node, parentVal, currentStreak)` that performs a depth-first traversal:
        a. If `node` is `None`, return immediately (base case).
        b. Check if the current node's value is exactly one greater than its parent's value:
            - If yes, increment `currentStreak` by 1 (continuing the consecutive sequence).
            - If no, reset `currentStreak` to 1 (starting a new sequence from the current node).
        c. Update `maxStreak` to be the maximum of `maxStreak` and `currentStreak`.
        d. Recursively call `dfs` on the left child with current node's value and updated streak.
        e. Recursively call `dfs` on the right child with current node's value and updated streak.
3. If `root` is not `None`, call `dfs(root, root.val, 0)` to start the traversal.
4. Return `maxStreak`, which contains the length of the longest consecutive sequence.
'''

def longestConsecutive(root):
    maxStreak = 0
    
    def dfs(node, parentVal, currentStreak):
        nonlocal maxStreak
        if not node:
            return 
        
        if node.val == parentVal + 1:
            currentStreak += 1
        else:
            currentStreak = 1
            
        maxStreak = max(maxStreak, currentStreak)
        
        dfs(node.left, node.val, currentStreak)
        dfs(node.right, node.val, currentStreak)
        
    if root:
        dfs(root, root.val, 0)
        
    return maxStreak

'''
Time Complexity: O(N), where N is the number of nodes in the binary tree.
We visit each node exactly once, performing constant-time operations at each node.

Space Complexity: O(H), where H is the height of the tree.
The recursion stack depth equals the height of the tree:
- Worst case (skewed tree): O(N)
- Best case (balanced tree): O(log N)
We also use O(1) extra space for the maxStreak variable.
'''

# Test Cases

# Test Case 1: Standard case with consecutive path
# Input: [1,null,2,3,4,5,6]
root1 = TreeNode(1, None, TreeNode(2, TreeNode(3), TreeNode(4, TreeNode(5), TreeNode(6))))
result1 = longestConsecutive(root1)
print(result1) # Expected: 4 (path: 1 -> 2 -> 3 -> 4)

# Test Case 2: Single node
root2 = TreeNode(1)
result2 = longestConsecutive(root2)
print(result2) # Expected: 1

# Test Case 3: Empty tree
root3 = None
result3 = longestConsecutive(root3)
print(result3) # Expected: 0

# Test Case 4: No consecutive sequence
# Input: [1,2,3,5]
root4 = TreeNode(1, TreeNode(2), TreeNode(3, TreeNode(5)))
result4 = longestConsecutive(root4)
print(result4) # Expected: 2 (path: 1 -> 2 or 1 -> 3)

# Test Case 5: Left branch consecutive
# Input: [2,1,3]
root5 = TreeNode(2, TreeNode(1), TreeNode(3))
result5 = longestConsecutive(root5)
print(result5) # Expected: 3 (path: 1 -> 2 -> 3)

# Test Case 6: Right branch consecutive
# Input: [1,3,2]
root6 = TreeNode(1, None, TreeNode(3, TreeNode(2)))
result6 = longestConsecutive(root6)
print(result6) # Expected: 2 (path: 1 -> 3 is not consecutive, 3 -> 2 is not consecutive, so just 2 or 1 alone)

# Test Case 7: Multiple branches with different lengths
# Input: [4,null,2,1,3]
root7 = TreeNode(4, None, TreeNode(2, TreeNode(1), TreeNode(3)))
result7 = longestConsecutive(root7)
print(result7) # Expected: 3 (path: 1 -> 2 -> 3)

# Test Case 8: All nodes consecutive in a straight line
# Input: [1,2,3,4,5,6,7]
root8 = TreeNode(1, TreeNode(2, TreeNode(3, TreeNode(4, TreeNode(5, TreeNode(6, TreeNode(7)))))))
result8 = longestConsecutive(root8)
print(result8) # Expected: 7 (path: 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7)

# Test Case 9: Negative values
# Input: [-2, -3, -1]
root9 = TreeNode(-2, TreeNode(-3), TreeNode(-1))
result9 = longestConsecutive(root9)
print(result9) # Expected: 3 (path: -3 -> -2 -> -1)

# Test Case 10: Two separate consecutive paths
# Input: [1,null,3,2,null,4,5]
root10 = TreeNode(1, None, TreeNode(3, TreeNode(2, None, TreeNode(4, None, TreeNode(5)))))
result10 = longestConsecutive(root10)
print(result10) # Expected: 4 (path: 2 -> 3 -> 4 -> 5)