# DELETE NODE IN BST

'''
Given a root node reference of a BST and a key, delete the node with the given key in the BST. 
Return the root node reference (possibly updated) of the BST.
Basically, the deletion can be divided into two stages:
- Search for a node to remove.
- If the node is found, delete the node.
'''

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

'''
ALGORITHM:

1. Define a function `deleteNode` that takes the `root` of the BST and the `key` to delete as input.
2. Base Case: If the `root` is `None`, return `root` (nothing to delete).
3. Recursive Step:
   a. If `root.val` is greater than `key`:
      - The node to be deleted is in the left subtree.
      - Recursively call `deleteNode` on the `left` child: `root.left = deleteNode(root.left, key)`.
   b. Else if `root.val` is less than `key`:
      - The node to be deleted is in the right subtree.
      - Recursively call `deleteNode` on the `right` child: `root.right = deleteNode(root.right, key)`.
   c. Else (if `root.val` is equal to `key` - this is the node to be deleted):
      i. Case 1: The node has no left child (`not root.left`):
         - Return `root.right` (the right child replaces the current node).
      ii. Case 2: The node has no right child (`not root.right`):
         - Return `root.left` (the left child replaces the current node).
      iii. Case 3: Thenode has both left and right children:
         - Find the inorder successor (the smallest node in the right subtree).
         - Replace the `root.val` with the inorder successor's value.
         - Recursively delete the inorder successor from the `root.right` subtree: `root.right = deleteNode(root.right, root.val)`.
4. Return the `root`.
'''

def deleteNode(root, key):
    if not root:
        return root
    
    if root.val > key:
        root.left = deleteNode(root.left, key)
    elif root.val < key:
        root.right = deleteNode(root.right, key)
    else:
        if not root.left:
            return root.right
        elif not root.right:
            return root.left
        else:
            current = root.right
            while current.left:
                current = current.left
            root.val = current.val
            root.right = deleteNode(root.right, root.val)
            
    return root

'''
Time Complexity: O(H), where H is the height of the BST.
In the worst case (a skewed tree), H can be N, where N is the number of nodes.
In the best case (a balanced tree), H is log N.
This is because in the worst case, we might traverse down to a leaf node to find the node to delete, and then potentially traverse down again to find the inorder successor.

Space Complexity: O(H), where H is the height of the BST.
This is due to the recursion stack. In the worst case (a skewed tree), H can be N.
In the best case (a balanced tree), H is log N.
'''

# Test Cases
root1 = [5,3,6,2,4,null,7], key1 = 3
print(deleteNode(root1, key1)) # Output: [5,4,6,2,null,null,7]

root2 = [5,3,6,2,4,null,7], key2 = 0
print(deleteNode(root2, key2)) # Output: [5,3,6,2,4,null,7]

root3 = [5,3,6,2,4,null,7], key3 = 5
print(deleteNode(root3, key3)) # Output: [6,3,7,2,4]

root4 = [5,3,6,2,4,null,7], key4 = 7
print(deleteNode(root4, key4)) # Output: [5,3,6,2,4]

root5 = [5,3,6,2,4,null,7], key5 = 2
print(deleteNode(root5, key5)) # Output: [5,3,6,4,null,null,7]

root6 = [5,3,6,2,4,null,7], key6 = 4
print(deleteNode(root6, key6)) # Output: [5,3,6,2,null,null,7]

root7 = [], key7 = 0
print(deleteNode(root7, key7)) # Output: []

root8 = [1], key8 = 1
print(deleteNode(root8, key8)) # Output: []

root9 = [1,null,2], key9 = 1
print(deleteNode(root9, key9)) # Output: [2]

root10 = [1,null,2], key10 = 2
print(deleteNode(root10, key10)) # Output: [1]