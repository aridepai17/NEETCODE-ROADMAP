# MERGE SUM OF BST

'''
You are given two binary trees root1 and root2.
Imagine that when you put one of them to cover the other, some nodes of the two trees are overlapped while the others are not. 
You need to merge the two trees into a new binary tree. The merge rule is that if two nodes overlap, then sum node values up as the new value of the merged node.
Otherwise, the NOT null node will be used as the node of the new tree.
Return the merged tree.
Note: The merging process must start from the root nodes of both trees
'''

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
'''
ALGORITHM:
The algorithm for merging two binary trees can be described recursively:

1. **Base Case:** If both `root1` and `root2` are `None`, it means we've reached the end of both branches, so return `None`.

2. **Node Value Calculation:**
   - Get the value of `root1`. If `root1` is `None`, consider its value as 0.
   - Get the value of `root2`. If `root2` is `None`, consider its value as 0.
   - The value of the new merged node will be the sum of these two values.

3. **Create New Node:** Create a new `TreeNode` with the calculated sum as its value. This will be the current node of our merged tree.

4. **Recursive Calls for Children:**
   - **Left Child:** Recursively call `mergeTrees` for the left children of `root1` and `root2`.
     - If `root1` is `None`, pass `None` as its left child.
     - If `root2` is `None`, pass `None` as its left child.
     - Assign the result of this recursive call to the `left` child of the new merged node.
   - **Right Child:** Recursively call `mergeTrees` for the right children of `root1` and `root2`.
     - If `root1` is `None`, pass `None` as its right child.
     - If `root2` is `None`, pass `None` as its right child.
     - Assign the result of this recursive call to the `right` child of the new merged node.

5. **Return New Node:** Return the newly created merged node.
'''

def mergeTrees(root1, root2):
    if not root1 and not root2:
        return None
    
    v1 = root1.val if root1 else 0
    v2 = root2.val if root2 else 0
    root = TreeNode(v1 + v2)
    root.left = mergeTrees(root1.left if root1 else None, root2.left if root2 else None)
    root.right = mergeTrees(root1.right if root1 else None, root2.right if root2 else None)
    return root

'''
Time Complexity: O(min(N, M)), where N and M are the number of nodes in root1 and root2 respectively.
This is because the recursion stops when both nodes are None, effectively traversing only the overlapping parts of the trees.
In the worst case, if one tree is much smaller than the other, we only visit nodes present in both trees.

Space Complexity: O(min(H1, H2)), where H1 and H2 are the heights of root1 and root2 respectively.
This is due to the recursion stack. In the worst case (skewed trees), the space complexity could be O(min(N, M)).
In the best case (balanced trees), it would be O(log(min(N, M))).
'''

# Test Cases
root1 = [1,3,2,5], root2 = [2,1,3,null,4,null,7]
print(mergeTrees(root1, root2)) # Output: [3,4,5,5,4,null,7]


root3 = [1], root4 = [2,1]
print(mergeTrees(root3, root4)) # Output: [3,1]

root5 = [1,2,3], root6 = [4,1,6]
print(mergeTrees(root5, root6)) # Output: [5,3,9]

root7 = [1,3,2,5], root8 = [2,7,4]
print(mergeTrees(root7, root8)) # Output: [3,10,9,5]

root9 = [1,3,2,5,4], root10 = [2,1,3]
print(mergeTrees(root9, root10)) # Output: [3,4,5,5,4]

root11 = [1,3,2,5,4], root12 = []
print(mergeTrees(root11, root12)) # Output: [1,3,2,5,4]

root13 = [], root14 = [2,1,3]
print(mergeTrees(root13, root14)) # Output: [2,1,3]

root15 = [1], root16 = [2,1]
print(mergeTrees(root15, root16)) # Output: [3,1]

root17 = [1,2,3], root18 = [4,1,6,5]
print(mergeTrees(root17, root18)) # Output: [5,3,9,5]

root19 = [1,3,2,5,4], root20 = [2,7,4,null,null,5]
print(mergeTrees(root19, root20)) # Output: [3,10,9,5,5]