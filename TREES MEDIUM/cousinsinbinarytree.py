# COUSINS IN BINARY TREE

'''
Given the root of a binary tree with unique values and the values of two different nodes of the tree x and y, return true if the nodes corresponding to the values x and y in the tree are cousins, or false otherwise.
Two nodes of a binary tree are cousins if they have the same depth with different parents.
Note that in a binary tree, the root node is at the depth 0, and children of each depth k node are at the depth k + 1.
'''

'''
ALGORITHM:
1. Use BFS (Level Order Traversal) to traverse the tree level by level
2. For each node, track both the node and its parent as a tuple (node, parent)
3. At each level, check if x or y is found and record their parents
4. After processing a level:
   - If both x and y are found at this level with different parents -> return True (cousins)
   - If only one is found at this level -> return False (different depths)
   - If neither found, continue to next level
5. If traversal completes without finding both -> return False
'''

import collections

def isCousins(root, x, y):
    queue = collections.deque([(root, None)])
    
    while queue:
        qLength = len(queue)
        xParent = yParent = None
        
        for i in range(qLength):
            node, parent = queue.popleft()
            if node.val == x:
                xParent = parent
            if node.val == y:
                yParent = parent
            if node.left:
                queue.append((node.left, node))
            if node.right:
                queue.append((node.right, node))
                
        if xParent or yParent:
            return (
                xParent is not None and 
                yParent is not None and 
                xParent != yParent
            )
            
    return False

'''
TIME COMPLEXITY: O(n)
- BFS visits each node exactly once
- All operations per node are O(1)

SPACE COMPLEXITY: O(n)
- Queue can hold at most O(n/2) nodes (last level of complete binary tree)
- Each queue entry stores (node, parent) tuple
'''

# Test Cases

# Test 1: x and y are cousins - Output: True
root1 = [1,2,3,4]
x1, y1 = 4, 3

# Test 2: x and y are siblings (same parent) - Output: False
root2 = [1,2,3,null,4,null,5]
x2, y2 = 5, 4

# Test 3: x and y at different depths - Output: False
root3 = [1,2,3,null,4]
x3, y3 = 2, 3

# Test 4: Larger tree, cousins at depth 2 - Output: True
root4 = [1,2,3,4,5,6,7]
x4, y4 = 4, 6

# Test 5: Root and child cannot be cousins - Output: False
root5 = [1,2,3]
x5, y5 = 1, 2

# Test 6: Siblings at depth 1 - Output: False
root6 = [1,2,3]
x6, y6 = 2, 3

# Test 7: Cousins in unbalanced tree - Output: True
root7 = [1,2,3,null,4,5,null]
x7, y7 = 4, 5

# Test 8: Nodes at depth 3 are cousins - Output: True
root8 = [1,2,3,4,5,6,7,8,null,null,null,null,null,null,9]
x8, y8 = 8, 9

# Test 9: Same subtree, different depths - Output: False
root9 = [1,2,null,3,null,4]
x9, y9 = 3, 4

# Test 10: Two nodes in left skewed tree - Output: False
root10 = [1,2,null,3,null,4,null,5]
x10, y10 = 4, 5