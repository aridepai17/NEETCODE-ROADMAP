# COUSINS IN BINARY TREE 2

'''
Given the root of a binary tree, replace the value of each node in the tree with the sum of all its cousins' values.
Two nodes of a binary tree are cousins if they have the same depth with different parents.
Return the root of the modified tree.
Note that the depth of a node is the number of edges in the path from the root node to it.
'''

'''
ALGORITHM:

1. First Pass - Calculate level sums using BFS:
   - Initialize an empty levelSum array to store sum at each level
   - Initialize a queue with the root node
   - While queue is not empty:
     a. Initialize currentSum = 0 for this level
     b. Get the number of nodes at current level (qLength)
     c. For each node in the current level:
        - Pop node from queue
        - Add node.val to currentSum
        - If node has left child, add it to queue
        - If node has right child, add it to queue
     d. Append currentSum to levelSum array

2. Second Pass - Replace values with cousin sums using BFS:
   - Initialize queue with root node
   - Set root.val = 0 (root has no cousins at its level)
   - Initialize level = 0 to track current depth
   - While queue is not empty:
     a. Get the number of nodes at current level (qLength)
     b. For each node in the current level:
        - Pop node from queue
        - Calculate childSum = sum of node's children values (siblings to each other)
          * If node.left exists: childSum += node.left.val
          * If node.right exists: childSum += node.right.val
        - Update each child's value to: levelSum[level + 1] - childSum
          * This gives: (total sum at child's level) - (sibling sum) = cousin sum
        - Add children to queue for next level processing
     c. Increment level counter

3. Return the modified root

Key Insight:
- Cousins are nodes at the same depth with different parents
- For any node: cousin sum = (sum of all nodes at that level) - (sum of siblings)
- Siblings share the same parent, so we calculate sibling sum from parent's perspective
- By subtracting sibling sum from level sum, we exclude the node itself and its sibling
'''

import collections

def replaceValueInTree(root):
    levelSum = []
    queue = collections.deque([root])
    
    while queue:
        currentSum = 0
        qLength = len(queue)
        for i in range(qLength):
            node = queue.popleft()
            currentSum += node.val
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        
        levelSum.append(currentSum)
        
    queue = collections.deque([root])
    root.val = 0
    level = 0
    
    while queue:
        qLength = len(queue)
        for i in range(qLength):
            node = queue.popleft()
            childSum = 0
            if node.left:
                childSum += node.left.val
            if node.right:
                childSum += node.right.val
            if node.left:
                node.left.val = levelSum[level + 1] - childSum
                queue.append(node.left)
            if node.right:
                node.right.val = levelSum[level + 1] - childSum
                queue.append(node.right)
                
        level += 1
    
    return root

'''
TIME COMPLEXITY: O(n)
- First BFS pass: O(n) to calculate all level sums
- Second BFS pass: O(n) to update all node values
- Total: O(n) + O(n) = O(n)

SPACE COMPLEXITY: O(n)
- Queue can hold at most O(n/2) nodes (last level of complete binary tree)
- levelSum array: O(h) where h is height, worst case O(n) for skewed tree
'''

# Test Cases

# Test 1: LeetCode Example 1 - Output: [0,0,0,7,7,null,11]
root1 = [5,4,9,1,10,null,7]

# Test 2: Single node - Output: [0]
root2 = [5]

# Test 3: Two levels only - Output: [0,0,0]
root3 = [1,2,3]

# Test 4: Complete binary tree - Output: [0,0,0,6,6,4,4]
root4 = [1,2,3,4,5,6,7]

# Test 5: Left skewed tree - Output: [0,0,0,0]
root5 = [1,2,null,3,null,4]

# Test 6: Right skewed tree - Output: [0,0,0,0]
root6 = [1,null,2,null,3,null,4]

# Test 7: Unbalanced tree - Output: [0,0,0,5,5,3]
root7 = [1,2,3,4,5,6,null]

# Test 8: All same values - Output: [0,0,0,4,4,4,4]
root8 = [2,2,2,2,2,2,2]

# Test 9: Large values - Output: [0,0,0,700,700,400,400]
root9 = [100,200,300,400,500,600,700]

# Test 10: Three levels with nulls - Output: [0,0,0,9,9,null,5,null,null,null,null]
root10 = [1,2,3,4,5,null,6,null,null,7,null]