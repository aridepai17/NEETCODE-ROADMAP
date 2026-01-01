# COUNT COMPLETE TREE NODES

'''
Given the root of a complete binary tree, return the number of the nodes in the tree.
According to Wikipedia, every level, except possibly the last, is completely filled in a complete binary tree, and all nodes in the last level are as far left as possible. 
It can have between 1 and 2h nodes inclusive at the last level h.
Design an algorithm that runs in less than O(n) time complexity.
'''

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

'''
ALGORITHM (O(N) Solution - Simple DFS):

1. Define a function `countNodes` that takes the `root` of the binary tree as input.
2. Base Case: If the `root` is `None`, return `0` (an empty tree has 0 nodes).
3. Recursive Step:
   a. Recursively call `countNodes` on the `left` child: `countNodes(root.left)`.
   b. Recursively call `countNodes` on the `right` child: `countNodes(root.right)`.
   c. Return `1` (for the current node) plus the count of nodes in the left subtree and the count of nodes in the right subtree.
   
ALGORITHM (O(log^2 N) Solution - Optimized for Complete Binary Trees):

1. Define a function `countNodes2` that takes the `root` of the complete binary tree as input.
2. Define a helper function `leftHeight(node)`:
   a. Initialize `h = 0`.
   b. While `node` is not `None`:
      - Increment `h`.
      - Move `node` to its `left` child: `node = node.left`.
   c. Return `h`.
3. Define a helper function `rightHeight(node)`:
   a. Initialize `h = 0`.
   b. While `node` is not `None`:
      - Increment `h`.
      - Move `node` to its `right` child: `node = node.right`.
   c. Return `h`.
4. Base Case: If `root` is `None`, return `0`.
5. Calculate the height of the leftmost path (`lh`) and the rightmost path (`rh`) from the `root`.
   a. `lh = leftHeight(root)`
   b. `rh = rightHeight(root)`
6. If `lh` is equal to `rh`:
   - This means the subtree rooted at `root` is a perfect binary tree (all levels are completely filled).
   - The number of nodes in a perfect binary tree of height `h` is `2^h - 1`.
   - Return `(2 ** lh) - 1`.
7. Else (if `lh` is not equal to `rh`):
   - This means the last level is not completely filled, and the tree is not perfect.
   - The total number of nodes is `1` (for the current `root`) plus the count of nodes in its `left` subtree and the count of nodes in its `right` subtree.
   - Recursively call `countNodes2` on `root.left` and `root.right`.
   - Return `1 + countNodes2(root.left) + countNodes2(root.right)`.
'''

# O(n) Solution
def countNodes(root):
    if not root:
        return 0
    return 1 + countNodes(root.left) + countNodes(root.right)

'''
Time Complexity: O(N), where N is the number of nodes in the tree.
This is because in the worst case (a skewed tree or a complete tree where we traverse all nodes), we visit each node exactly once.

Space Complexity: O(H), where H is the height of the tree.
This is due to the recursion stack. In the worst case (a skewed tree), H can be N.
In the best case (a balanced tree), H is log N.
'''

# O(log^2 N) time Solution
def countNodes2(root):
    def leftHeight(node):
        h = 0
        while node:
            h += 1
            node = node.left
        return h
    
    def rightHeight(node):
        h = 0
        while node:
            h += 1
            node = node.right
        return h
    
    if not root:
        return 0
    
    lh = leftHeight(root)
    rh = rightHeight(root)
    
    if lh == rh:
        return (2 ** lh) - 1
    
    return 1 + countNodes2(root.left) + countNodes2(root.right)

'''
Time Complexity: O(log^2 N), where N is the number of nodes in the tree.
In the worst case, we traverse down the tree for `leftHeight` and `rightHeight` which takes O(H) = O(log N) time.
In the recursive step, we make at most two recursive calls. However, due to the property of complete binary trees,
at least one of the subtrees will have a full height, allowing us to calculate its node count in O(log N) time.
The recursion depth is O(log N). So, it's O(log N * log N) = O(log^2 N).

Space Complexity: O(H), where H is the height of the tree.
This is due to the recursion stack. For a complete binary tree, H is log N.
So, the space complexity is O(log N).
'''

# Test Cases
root1 = [1,2,3,4,5,6]
print(countNodes(root1)) # Output: 6

root2 = []
print(countNodes(root2)) # Output: 0

root3 = [1]
print(countNodes(root3)) # Output: 1

root4 = [1,2,3,4,5,6,7]
print(countNodes(root4)) # Output: 7

root5 = [1,2,3,4]
print(countNodes(root5)) # Output: 4

root6 = [1,2]
print(countNodes(root6)) # Output: 2

root7 = [1,2,3]
print(countNodes(root7)) # Output: 3

root8 = [1,2,3,4,5]
print(countNodes(root8)) # Output: 5

root9 = [1,2,3,4,5,6,7,8,9,10]
print(countNodes(root9)) # Output: 10

root10 = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
print(countNodes(root10)) # Output: 15
