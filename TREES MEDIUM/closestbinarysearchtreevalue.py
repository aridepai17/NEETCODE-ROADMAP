# CLOSEST BINARY SEARCH TREE VALUE

'''
Given a non-empty binary search tree and a target value, find the value in the BST that is closest to the target.
'''

'''
ALGORITHM:
1. Initialize 'closest' with the root's value as our initial best guess
2. Start traversing from the root using a pointer 'current'
3. While current node exists:
   a. If the absolute difference between current node's value and target
      is smaller than the current closest, update closest
   b. Use BST property to decide direction:
      - If target < current.val, go left (smaller values)
      - Else go right (larger values)
4. Return the closest value found
'''

def closestValue(root, target):
    closest = root.val
    current = root
    
    while current:
        if abs(current.val - target) < abs(closest - target):
            closest = current.val 
        if target < current.val:
            current = current.left
        else:
            current = current.right
    
    return closest

'''
Time Complexity: O(H), where H is the height of the BST.
In the worst case (a skewed tree), H can be N, where N is the number of nodes.
In the best case (a balanced tree), H is log N.
This is because we traverse down the tree from the root to find the closest value.

Space Complexity: O(1).
We are only using a few pointers (closest, current) and not allocating any additional data structures that grow with the input size.
'''

'''
TEST CASES:

Test Case 1: Basic BST
Input: root = [4,2,5,1,3], target = 3.714286
Output: 4
Explanation: Target 3.714286 is closest to 4 (distance 0.285714) vs 3 (distance 0.714286)

Test Case 2: Target matches a node exactly
Input: root = [4,2,5,1,3], target = 3.0
Output: 3
Explanation: Target exactly matches node value 3

Test Case 3: Single node tree
Input: root = [1], target = 100.5
Output: 1
Explanation: Only one node exists, so it's the closest

Test Case 4: Target smaller than all nodes
Input: root = [10,5,15,3,7], target = 1.0
Output: 3
Explanation: 3 is the smallest value and closest to target 1.0

Test Case 5: Target larger than all nodes
Input: root = [10,5,15,3,7], target = 20.0
Output: 15
Explanation: 15 is the largest value and closest to target 20.0

Test Case 6: Left-skewed tree
Input: root = [5,4,null,3,null,2,null,1], target = 2.3
Output: 2
Explanation: In this left-skewed tree, 2 is closest to 2.3

Test Case 7: Right-skewed tree
Input: root = [1,null,2,null,3,null,4,null,5], target = 3.7
Output: 4
Explanation: In this right-skewed tree, 4 is closest to 3.7

Test Case 8: Negative values in BST
Input: root = [0,-5,5,-10,-3,3,10], target = -4.0
Output: -5 or -3
Explanation: Both -5 and -3 are equidistant from -4.0 (distance = 1), return either

Test Case 9: Target is between two close values
Input: root = [8,4,12,2,6,10,14], target = 5.0
Output: 4 or 6
Explanation: Both 4 and 6 are equidistant from 5.0, return either (algorithm returns 6)

Test Case 10: Large difference in values
Input: root = [100,50,150,25,75,125,175], target = 74.9
Output: 75
Explanation: 75 is closest to 74.9 with distance 0.1
'''