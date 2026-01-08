# UNIQUE BINARY SEARCH TREES

'''
Given an integer n, return the number of structurally unique BST's (binary search trees) which has exactly n nodes of unique values from 1 to n.
'''

'''
ALGORITHM:

This problem can be solved using dynamic programming.
Let `numTree[i]` be the number of structurally unique BSTs that can be formed with `i` nodes.

1. Initialize a list `numTree` of size `n + 1` with all elements set to 0.
2. Base Cases:
   - `numTree[0] = 1`: There is one way to form an empty BST (no nodes).
   - `numTree[1] = 1`: There is one way to form a BST with one node.
3. Iterate `nodes` from 2 to `n` (inclusive):
   - For each `nodes`, we want to calculate `numTree[nodes]`.
   - Iterate `root` from 1 to `nodes` (inclusive):
     - Consider `root` as the value of the root node of the BST.
     - The number of nodes in the left subtree will be `root - 1`.
     - The number of nodes in the right subtree will be `nodes - root`.
     - The number of unique BSTs with `root` as the root node is `numTree[root - 1] * numTree[nodes - root]`.
     - Add this product to `numTree[nodes]`.
4. Return `numTree[n]`.
'''

def numTrees(n):
    numTree = [0] * (n + 1)
    numTree[0] = 1
    numTree[1] = 1
    
    for nodes in range(2, n + 1):
        for root in range(1, nodes + 1):
            numTree[nodes] = numTree[root - 1] * numTree[nodes - root]
            
    return numTree[n]

'''
Time Complexity: O(N^2), where N is the input integer.
The outer loop runs N times (from 2 to N).
The inner loop runs `nodes` times (from 1 to `nodes`), which is at most N times.
Thus, the total time complexity is proportional to N * N = N^2.

Space Complexity: O(N), where N is the input integer.
We use a list `numTree` of size N+1 to store the number of unique BSTs for each `i` from 0 to N.
'''

# Test Cases
print(numTrees(1)) # Output: 1
print(numTrees(2)) # Output: 2
print(numTrees(3)) # Output: 5
print(numTrees(4)) # Output: 14
print(numTrees(5)) # Output: 42
print(numTrees(6)) # Output: 132
print(numTrees(7)) # Output: 429
print(numTrees(8)) # Output: 1430
print(numTrees(9)) # Output: 4862
print(numTrees(10)) # Output: 16796