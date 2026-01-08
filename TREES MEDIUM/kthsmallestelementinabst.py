# KTH SMALLEST ELEMENT IN A BST

'''
Given the root of a binary search tree, and an integer k, return the kth smallest value (1-indexed) of all the values of the nodes in the tree.
'''

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

'''
ALGORITHM (Iterative In-order Traversal):

1. Define a function `kthSmallest` that takes the `root` of the BST and an integer `k` as input.
2. Initialize `visited` to `0` to count the number of nodes visited so far.
3. Initialize an empty list `stack` to simulate the recursion stack for in-order traversal.
4. Initialize `current` pointer to the `root` of the BST.
5. Enter a `while` loop that continues as long as `current` is not `None` OR `stack` is not empty.
   a. Inner `while` loop (traverse left subtree): While `current` is not `None`:
      i. Push `current` onto the `stack`.
      ii. Move `current` to its `left` child: `current = current.left`.
   b. Pop a node from the `stack` and assign it to `current`.
   c. Increment `visited` by `1`.
   d. If `visited` is equal to `k`:
      i. Return `current.val` (this is the k-th smallest element).
   e. Move `current` to its `right` child: `current = current.right`.
'''

def kthSmallest(root, k):
    visited = 0
    stack = []
    current = root
    
    while current or stack:
        while current:
            stack.append(current.val)
            current = current.left
        current = stack.pop()
        visited += 1
        if visited == k:
            return current.val
        current = current.right

'''
Time Complexity: O(H + k), where H is the height of the BST and k is the target rank.
In the worst case (a skewed tree), H can be N, where N is the number of nodes.
The algorithm performs an in-order traversal. It traverses down to the leftmost node (O(H)) and then visits k nodes.

Space Complexity: O(H) in the worst case, where H is the height of the BST.
This is due to the recursion stack (if implemented recursively) or the explicit stack used for iterative in-order traversal.
In a skewed tree, H can be N, so O(N). In a balanced tree, H is log N, so O(log N).
'''

# Test Cases
root1 = [3, 1, 4, null, 2], k = 1
print(kthSmallest(root1, k1)) # Output: 1

root2 = [5, 3, 6, 2, 4, null, null, 1], k2 = 3
print(kthSmallest(root2, k2)) # Output: 3

root3 = [1], k3 = 1
print(kthSmallest(root3, k3)) # Output: 1

root4 = [2, 1], k4 = 2
print(kthSmallest(root4, k4)) # Output: 2

root5 = [3, 1, 4, null, 2], k5 = 4
print(kthSmallest(root5, k5)) # Output: 4

root6 = [5, 3, 6, 2, 4, null, null, 1], k6 = 1
print(kthSmallest(root6, k6)) # Output: 1

root7 = [5, 3, 6, 2, 4, null, null, 1], k7 = 6
print(kthSmallest(root7, k7)) # Output: 6

root8 = [10, 5, 15, 2, 7, 12, 17], k8 = 4
print(kthSmallest(root8, k8)) # Output: 7

root9 = [10, 5, 15, 2, 7, 12, 17], k9 = 7
print(kthSmallest(root9, k9)) # Output: 17

root10 = [10, 5, 15, 2, 7, 12, 17], k10 = 1
print(kthSmallest(root10, k10)) # Output: 2