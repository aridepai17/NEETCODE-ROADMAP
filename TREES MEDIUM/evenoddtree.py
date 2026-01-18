# EVEN ODD TREE

'''
A binary tree is named Even-Odd if it meets the following conditions:
- The root of the binary tree is at level index 0, its children are at level index 1, their children are at level index 2, etc.
- For every even-indexed level, all nodes at the level have odd integer values in strictly increasing order (from left to right).
- For every odd-indexed level, all nodes at the level have even integer values in strictly decreasing order (from left to right).
Given the root of a binary tree, return true if the binary tree is Even-Odd, otherwise return false.
'''

'''
ALGORITHM:
1. Use BFS (level-order traversal) with a queue starting from the root
2. Track the current level number (starting at 0)
3. For each level, process all nodes in the queue:
   a. For even levels (0, 2, 4...): check that all values are ODD and STRICTLY INCREASING
   b. For odd levels (1, 3, 5...): check that all values are EVEN and STRICTLY DECREASING
4. Use a 'prev' variable to track the previous node's value for comparison
5. If any condition is violated, return False immediately
6. Add children to queue for next level processing
7. Increment level after processing all nodes at current level
8. If all levels pass the checks, return True
'''

import collections


def isEvenOddTree(root):
    queue = collections.deque([root])
    level = 0
    
    while queue:
        qLength = len(queue)
        prev = None
        for i in range(qLength):
            node = queue.popleft()
            value = node.val
            
            if level % 2 == 0:
                if value % 2 == 0:
                    return False
            else:
                if value % 2 == 1:
                    return False
                
            if prev:
                if level % 2 == 0 and value <= prev:
                    return False
                if level % 2 == 1 and value >= prev:
                    return False
            
            prev = value
        
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        
        level += 1
        
    return True

'''
Time Complexity: O(N), where N is the number of nodes in the binary tree.
Each node is visited and processed exactly once during the BFS traversal.
For each node, we perform constant time operations (checking value, comparing with previous, appending children to queue).

Space Complexity: O(W), where W is the maximum width of the binary tree.
The `queue` can hold up to W nodes at any given time.
In the worst case (a complete binary tree), the maximum width is at the last level, which can be up to N/2 nodes.
Therefore, the space complexity is O(N) in the worst case.
'''

# Test Cases
root1 = [1,10,4,3,null,7,9,12,8,6,null,null,2]
print(isEvenOddTree(root1)) # Output: True

root2 = [5,4,2,3,3,7]
print(isEvenOddTree(root2)) # Output: False

root3 = [5,9,1,3,5,7]
print(isEvenOddTree(root3)) # Output: False

root4 = [1]
print(isEvenOddTree(root4)) # Output: True

root5 = [2]
print(isEvenOddTree(root5)) # Output: False

root6 = [1,8,6]
print(isEvenOddTree(root6)) # Output: True

root7 = [1,4,4]
print(isEvenOddTree(root7)) # Output: False

root8 = [1,10,4,3,5,7,9]
print(isEvenOddTree(root8)) # Output: True

root9 = [1,10,4,2]
print(isEvenOddTree(root9)) # Output: False

root10 = [1,10,4,5,3,7]
print(isEvenOddTree(root10)) # Output: False