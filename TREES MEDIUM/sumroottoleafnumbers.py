# SUM ROOT TO LEAF NUMBERS

'''
You are given the root of a binary tree containing digits from 0 to 9 only.
Each root-to-leaf path in the tree represents a number.
For example, the root-to-leaf path 1 -> 2 -> 3 represents the number 123.
Return the total sum of all root-to-leaf numbers. Test cases are generated so that the answer will fit in a 32-bit integer.
A leaf node is a node with no children.
'''

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

'''
ALGORITHM (Step by Step):
1. Start DFS from the root with an initial total of 0
2. For each node visited:
   a. If the node is null, return 0 (base case)
   b. Calculate the new total by: total = total * 10 + node.val
      - This builds the number digit by digit (e.g., 1 -> 12 -> 123)
   c. If the node is a leaf (no left and no right child):
      - Return the current total (this is one complete root-to-leaf number)
   d. If the node is not a leaf:
      - Recursively call DFS on left child with current total
      - Recursively call DFS on right child with current total
      - Return the sum of both recursive calls
3. The final result is the sum of all root-to-leaf numbers
'''

def sumNumbers(root):
    def dfs(node, total):
        if not node:
            return 0

        total = total * 10 + node.val
        if not node.left and not node.right:
            return total

        return dfs(node.left, total) + dfs(node.right, total)

    return dfs(root, 0)

'''
TIME COMPLEXITY: O(n)
- We visit each node exactly once during the DFS traversal
- Where n is the total number of nodes in the binary tree

SPACE COMPLEXITY: O(h)
- Where h is the height of the tree
- This is due to the recursive call stack
- Best case (balanced tree): O(log n)
- Worst case (skewed tree): O(n)
'''

# Test Cases
root1 = [1,2,3]
print(sumNumbers(root1)) # Output: 25

root2 = [4,9,0,5,1]
print(sumNumbers(root2)) # Output: 1026

root3 = [5]
print(sumNumbers(root3)) # Output: 5

root4 = [1,2,None,3]
print(sumNumbers(root4)) # Output: 123

root5 = [1,None,2,None,3]
print(sumNumbers(root5)) # Output: 123

root6 = [1,0,0]
print(sumNumbers(root6)) # Output: 20

root7 = [9,1,2,3,4,5,6]
print(sumNumbers(root7)) # Output: 3678

root8 = [7,7,7]
print(sumNumbers(root8)) # Output: 154

root9 = [0,1,2]
print(sumNumbers(root9)) # Output: 3

root10 = [6,2,8,0,4,7,9]
print(sumNumbers(root10)) # Output: 2620