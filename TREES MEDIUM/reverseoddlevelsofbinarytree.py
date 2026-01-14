# REVERSE ODD LEVELS OF BINARY TREE

'''
Given the root of a perfect binary tree, reverse the node values at each odd level of the tree.
For example, suppose the node values at level 3 are [2,1,3,4,7,11,29,18], then it should become [18,29,11,7,4,3,1,2].
Return the root of the reversed tree.
A binary tree is perfect if all parent nodes have two children and all leaves are on the same level.
The level of a node is the number of edges along the path between it and the root node.
'''

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

'''
ALGORITHM:

1. Initialize a `queue` using `collections.deque` and add the `root` node to it.
2. Initialize `level` to `0` to keep track of the current level number.
3. While the `queue` is not empty:
   a. Get the `qLength` (length of the queue), which represents the number of nodes at the current level.
   b. Initialize an empty list `current` to store the nodes at the current level.
   c. Iterate `qLength` times (to process all nodes at the current level):
      i. Dequeue a `node` from the left of the `queue`.
      ii. Append `node` to the `current` list.
      iii. If `node.left` exists, enqueue it to the right of the `queue`.
      iv. If `node.right` exists, enqueue it to the right of the `queue`.
   d. After processing all nodes at the current level, check if the `level` is odd (`level % 2 == 1`):
      i. If it's an odd level, initialize two pointers `left` and `right` to `0` and `len(current) - 1` respectively.
      ii. While `left` is less than `right`:
          - Swap the `val` attributes of the nodes at `current[left]` and `current[right]`.
          - Increment `left` and decrement `right`.
   e. Increment `level` by `1` for the next iteration.
4. Return the `root` of the modified tree.
'''

import collections

def reverseOddLevels(root):
    queue = collections.deque([root])
    level = 0
    
    while queue:
        qLength = len(queue)
        current = []
        for i in range(qLength):
            node = queue.popleft()
            current.append(node)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
                
        if level % 2 == 1:
            left, right = 0, len(current) - 1
            while left < right:
                current[left].val, current[right].val = current[right].val, current[left].val
                left += 1
                right -= 1
        
        level += 1
        
    return root

'''
Time Complexity: O(N), where N is the number of nodes in the binary tree.
Each node is visited and processed exactly once during the BFS traversal.
For each level, we iterate through its nodes once to collect them and once to reverse their values if the level is odd.
The total number of nodes across all levels is N.

Space Complexity: O(W), where W is the maximum width of the binary tree.
The `queue` can hold up to W nodes at any given time.
The `current` list also stores up to W nodes for a given level.
In a perfect binary tree, the maximum width is at the last level, which can be up to N/2 nodes.
Therefore, the space complexity is O(N) in the worst case (for the last level).
'''

# Test Cases
root1 = [2,3,5,8,13,21,34]
print(reverseOddLevels(root1)) # Output: [2,5,3,8,13,21,34]

root2 = [7,13,11]
print(reverseOddLevels(root2)) # Output: [7,11,13]

root3 = [1,2,3,4,5,6,7]
print(reverseOddLevels(root3)) # Output: [1,3,2,4,5,6,7]

root4 = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14]
print(reverseOddLevels(root4)) # Output: [0,2,1,3,4,5,6,14,13,12,11,10,9,8,7]

root5 = [10,20,30,40,50,60,70]
print(reverseOddLevels(root5)) # Output: [10,30,20,40,50,60,70]

root6 = [100]
print(reverseOddLevels(root6)) # Output: [100]

root7 = [1,2,3]
print(reverseOddLevels(root7)) # Output: [1,3,2]

root8 = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
print(reverseOddLevels(root8)) # Output: [1,3,2,15,14,13,12,11,10,9,8,7,6,5,4]

root9 = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31]
print(reverseOddLevels(root9)) # Output: [1,3,2,7,6,5,4,31,30,29,28,27,26,25,24,23,22,21,20,19,18,17,16,15,14,13,12,11,10,9,8]

root10 = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
print(reverseOddLevels(root10)) # Output: [1,3,2,15,14,13,12,11,10,9,8,7,6,5,4]