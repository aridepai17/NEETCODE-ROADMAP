# MINIMUM NUMBER OF OPERATIONS TO SORT A BINARY TREE BY LEVEL

'''
You are given the root of a binary tree with unique values.
In one operation, you can choose any two nodes at the same level and swap their values.
Return the minimum number of operations needed to make the values at each level sorted in a strictly increasing order.
The level of a node is the number of edges along the path between it and the root node.
'''

'''
ALGORITHM:
1. Use BFS (Level Order Traversal) to traverse the tree level by level
2. For each level, collect all node values into an array
3. Count minimum swaps needed to sort each level array using cycle detection:
   - Create a sorted copy of the level array
   - Build an index map to track current positions of elements
   - For each position, if the element is not in its correct sorted position:
     - Swap it with the element that belongs at current position
     - Update the index map after each swap
     - Increment swap counter
4. Sum up swaps from all levels and return the total

The key insight is that minimum swaps to sort an array equals the number of elements
out of place when we greedily place each element in its correct position.
'''

import collections

def minimumOperations(root):
    def countSwaps(level):
        swaps = 0
        sortedLevel = sorted(level)
        indexMap = {}
        levelLength = len(level)
        
        for i in range(levelLength):
            indexMap[level[i]] = i
            
        for i in range(levelLength):
            if level[i] != sortedLevel[i]:
                swaps += 1
                correctValue = sortedLevel[i]
                correctIndex = indexMap[correctValue]
                level[i], level[correctIndex] = level[correctIndex], level[i]
                indexMap[level[correctIndex]] = correctIndex
                indexMap[level[i]] = i
                
        return swaps
    
    queue = collections.deque([root])
    result = 0
    while queue:
        level = []
        qLength = len(queue)
        for i in range(qLength):
            node = queue.popleft()
            level.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
                
        result += countSwaps(level)
        
    return result

'''
TIME COMPLEXITY: O(n log n)
- BFS traversal visits each node once: O(n)
- For each level with k nodes, sorting takes O(k log k)
- Across all levels, total sorting cost is O(n log n) in worst case
- The swap counting is O(k) per level, O(n) total

SPACE COMPLEXITY: O(n)
- Queue holds at most O(n/2) nodes (last level of complete binary tree)
- Level array: O(n) in worst case
- Sorted level array: O(n) in worst case
- Index map: O(n) in worst case
'''

# Test Cases

# Test 1: LeetCode Example 1 - Output: 3
root1 = [1,4,3,7,6,8,5,null,null,null,null,9,null,10]

# Test 2: Single node - Output: 0
root2 = [5]

# Test 3: Already sorted tree - Output: 0
root3 = [1,2,3,4,5]

# Test 4: Two levels, children swapped - Output: 1
root4 = [1,5,2]

# Test 5: Completely reversed at each level - Output: 3
root5 = [10,20,15,40,35,30,25]

# Test 6: Left skewed tree - Output: 0
root6 = [1,2,null,3,null]

# Test 7: Right skewed tree - Output: 0
root7 = [1,null,2,null,3]

# Test 8: Only last level needs sorting - Output: 2
root8 = [1,2,3,8,6,5,4]

# Test 9: Zigzag pattern - Output: 3
root9 = [5,8,2,1,9,7,3]

# Test 10: Perfect binary tree, all levels need swaps - Output: 3
root10 = [1,6,2,12,9,7,4]