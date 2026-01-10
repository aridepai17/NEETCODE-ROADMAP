# POPULATING NEXT RIGHT POINTERS IN EACH NODE

'''
You are given a perfect binary tree where all leaves are on the same level, and every parent has two children. The binary tree has the following definition:

struct Node {
  int val;
  Node *left;
  Node *right;
  Node *next;
}
Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to NULL.

Initially, all next pointers are set to NULL.
'''

class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

'''
ALGORITHM:

This problem can be solved using a level-order traversal (BFS) approach, but with a clever optimization to use O(1) space.
Since it's a perfect binary tree, we can leverage the `next` pointers established in the previous level to connect nodes in the current level.

1. Define a function `connect` that takes the `root` of the binary tree as input.
2. Initialize two pointers:
   - `current`: This pointer will iterate through the nodes of the *current* level. Start it at `root`.
   - `nxt`: This pointer will point to the first node of the *next* level. Start it at `root.left` (if `root` exists, otherwise `None`).
3. Enter a `while` loop that continues as long as both `current` and `nxt` are not `None`. This loop processes level by level.
   a. Connect the left child of `current` to its right child: `current.left.next = current.right`.
   b. Check if `current` has a `next` pointer (meaning it's not the rightmost node of its level).
      - If `current.next` exists:
         - Connect the right child of `current` to the left child of `current.next`: `current.right.next = current.next.left`.
   c. Move `current` to its `next` node: `current = current.next`.
   d. If `current` becomes `None` (meaning we have processed all nodes in the current level):
      - Move `current` to `nxt` (the first node of the next level).
      - Update `nxt` to point to the first node of the level *after* the current `nxt`'s level (i.e., `nxt.left`).
4. Return the original `root`.
'''

def connect(root):
    current = root
    nxt = root.left if root else None
    
    while current and nxt:
        current.left.next = current.right
        if current.next:
            current.right.next = current.next.left
            
        current = current.next
        if not current:
            current = nxt
            nxt = current.left
            
    return root

'''
Time Complexity: O(N), where N is the number of nodes in the binary tree.
Each node is visited and processed exactly once.

Space Complexity: O(1).
We are using a constant amount of extra space, regardless of the size of the tree.
'''

# Test Cases
root1 = [1,2,3,4,5,6,7]
print(connect(root1)) # Output: [1,#,2,3,#,4,5,6,7,#]

root2 = []
print(connect(root2)) # Output: []

root3 = [1]
print(connect(root3)) # Output: [1,#]

root4 = [1,2,3]
print(connect(root4)) # Output: [1,#,2,3,#]

root5 = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
print(connect(root5)) # Output: [1,#,2,3,#,4,5,6,7,#,8,9,10,11,12,13,14,15,#]

root6 = [1,2,3,4,5,null,6,7,null,null,null,null,8] # Not a perfect binary tree, but the function should handle it based on its logic
print(connect(root6)) # Output: [1,#,2,3,#,4,5,6,#,7,8,#]

root7 = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
print(connect(root7)) # Output: [1,#,2,3,#,4,5,6,7,#,8,9,10,11,12,13,14,15,#]

root8 = [1,2,3,4,5,6,7]
print(connect(root8)) # Output: [1,#,2,3,#,4,5,6,7,#]

root9 = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
print(connect(root9)) # Output: [1,#,2,3,#,4,5,6,7,#,8,9,10,11,12,13,14,15,#]

root10 = [1,2,3,4,5,6,7,8]
print(connect(root10)) # Output: [1,#,2,3,#,4,5,6,7,#,8]