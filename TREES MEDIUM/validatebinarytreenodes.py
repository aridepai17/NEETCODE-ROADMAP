# VALIDATE BINARY TREE NODES

'''
You have n binary tree nodes numbered from 0 to n - 1 where node i has two children leftChild[i] and rightChild[i], return true if and only if all the given nodes form exactly one valid binary tree.
If node i has no left child then leftChild[i] will equal -1, similarly for the right child.
Note that the nodes have no values and that we only use the node numbers in this problem.

ALGORITHM:
Step 1: Build the set of nodes that have a parent
        - Combine all children from leftChild and rightChild arrays into a set
        - Remove -1 since it represents "no child"
        - Any node in this set has at least one parent

Step 2: Check if there's exactly one root
        - If all n nodes have parents, there's no root -> invalid
        - A valid tree must have exactly one node without a parent (the root)

Step 3: Find the root node
        - The root is the node that doesn't appear as any other node's child
        - Iterate through nodes 0 to n-1 and find the one not in hasParent set

Step 4: DFS traversal to validate tree structure
        - Start DFS from root
        - If we revisit a node -> cycle exists or node has multiple parents -> invalid
        - Mark each visited node
        - Recursively check left and right children

Step 5: Final validation
        - dfs(root): Ensures no cycles and no node has multiple parents
        - len(visited) == n: Ensures all nodes are connected (no disconnected components)

KEY CONDITIONS FOR A VALID BINARY TREE:
        1. Exactly one root (one node with no parent)
        2. No cycles
        3. No node has multiple parents
        4. All nodes are reachable from the root (connected)
'''

def validateBinaryTreeNodes(n, leftChild, rightChild):
    hasParent = set(leftChild + rightChild)
    hasParent.discard(-1)
    if len(hasParent) >= n:
        return False
    
    root = -1
    for i in range(n):
        if i not in hasParent:
            root = i
            break
        
    visited = set()
    def dfs(node):
        if node == -1:
            return True
        if node in visited:
            return False
        visited.add(node)
        return dfs(leftChild[node]) and dfs(rightChild[node])
    
    return dfs(root) and len(visited) == n

'''
Time Complexity: O(N), where N is the number of nodes.
- Building the `hasParent` set takes O(N) because `leftChild` and `rightChild` arrays have N elements each.
- Finding the root takes O(N) in the worst case.
- The DFS traversal visits each node and edge at most once. Each node is added to `visited` once.
- The final check `len(visited) == n` is O(1).

Space Complexity: O(N), where N is the number of nodes.
- The `hasParent` set can store up to N unique child nodes.
- The `visited` set can store up to N nodes.
- The recursion stack for DFS can go up to O(N) in the worst case (a skewed tree).
'''

# Test Cases
n1, leftChild1, rightChild1 = 4, [1,-1,3,-1], [2,-1,-1,-1]
print(validateBinaryTreeNodes(n1, leftChild1, rightChild1)) # Output: True

# Test Case 2: Node with two parents (invalid)
n2, leftChild2, rightChild2 = 4, [1,-1,3,-1], [2,3,-1,-1]
print(validateBinaryTreeNodes(n2, leftChild2, rightChild2)) # Output: False

# Test Case 3: Single node tree (valid)
n3, leftChild3, rightChild3 = 1, [-1], [-1]
print(validateBinaryTreeNodes(n3, leftChild3, rightChild3)) # Output: True

# Test Case 4: Disconnected nodes (two separate trees)
n4, leftChild4, rightChild4 = 4, [1,-1,-1,-1], [-1,-1,-1,-1]
print(validateBinaryTreeNodes(n4, leftChild4, rightChild4)) # Output: False

# Test Case 5: Cycle in tree (invalid)
n5, leftChild5, rightChild5 = 2, [1], [0]
print(validateBinaryTreeNodes(n5, leftChild5, rightChild5)) # Output: False

# Test Case 6: Linear chain (valid - skewed tree)
n6, leftChild6, rightChild6 = 3, [1,2,-1], [-1,-1,-1]
print(validateBinaryTreeNodes(n6, leftChild6, rightChild6)) # Output: True

# Test Case 7: No root exists (all nodes have parents)
n7, leftChild7, rightChild7 = 3, [1,2,0], [-1,-1,-1]
print(validateBinaryTreeNodes(n7, leftChild7, rightChild7)) # Output: False

# Test Case 8: Complete binary tree (valid)
n8, leftChild8, rightChild8 = 7, [1,3,5,-1,-1,-1,-1], [2,4,6,-1,-1,-1,-1]
print(validateBinaryTreeNodes(n8, leftChild8, rightChild8)) # Output: True

# Test Case 9: Multiple roots (invalid - disconnected)
n9, leftChild9, rightChild9 = 4, [-1,0,-1,2], [-1,-1,-1,-1]
print(validateBinaryTreeNodes(n9, leftChild9, rightChild9)) # Output: False

# Test Case 10: Two nodes valid tree
n10, leftChild10, rightChild10 = 2, [1,-1], [-1,-1]
print(validateBinaryTreeNodes(n10, leftChild10, rightChild10)) # Output: True