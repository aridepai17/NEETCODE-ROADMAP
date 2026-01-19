# SMALLEST STRING STARTING FROM LEAF

'''
You are given the root of a binary tree where each node has a value in the range [0, 25] representing the letters 'a' to 'z'.
Return the lexicographically smallest string that starts at a leaf of this tree and ends at the root.
As a reminder, any shorter prefix of a string is lexicographically smaller.
For example, "ab" is lexicographically smaller than "aba".
A leaf of a node is a node that has no children.
'''

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

'''
Algorithm:
1. Use DFS to traverse from root to all leaf nodes
2. At each node, prepend the current character (converted from node value) to the path string
3. If the node has both children, recursively explore both and return the lexicographically smaller result
4. If the node has only one child, continue DFS on that child
5. If the node is a leaf (no children), return the accumulated string as a candidate
6. The min() function compares strings lexicographically to find the smallest
'''

def smallestFromLeaf(root):
    def dfs(root, current):
        if not root:
            return 
        
        current = chr(ord('a') + root.val) + current
        if root.left and root.right:
            return min(dfs(root.left, current), dfs(root.right, current))
        if root.right:
            return dfs(root.right, current)
        if root.left:
            return dfs(root.left, current)
        
        return current
    
    return dfs(root, "")

'''
Time Complexity: O(N * H) in the worst case, where N is the number of nodes and H is the height of the tree.
- In the worst case (a skewed tree), H can be N.
- For each node, we perform string concatenation. The length of the string `current` can be up to H.
- String concatenation `chr(ord('a') + root.val) + current` takes O(length of current string) time, which is O(H).
- In the worst case, we might visit N nodes, and for each, perform an O(H) string operation.
- The `min` operation on strings also takes time proportional to the length of the strings, which is O(H).

Space Complexity: O(H^2) in the worst case, where H is the height of the tree.
- The recursion stack for DFS can go up to O(H) in the worst case (a skewed tree).
- At each level of recursion, a new `current` string is created. The length of this string can be up to H.
- In the worst case, if we have a skewed tree, we could have H distinct strings on the stack, each of length up to H. This leads to O(H^2) space for storing these strings.
'''

# Test Cases
# Test Case 1: Given example [0,1,2,3,4,3,4]
root1 = TreeNode(0, TreeNode(1, TreeNode(3), TreeNode(4)), TreeNode(2, TreeNode(3), TreeNode(4)))
print(smallestFromLeaf(root1)) # Output: "dba"

# Test Case 2: Single node tree
root2 = TreeNode(0)
print(smallestFromLeaf(root2)) # Output: "a"

# Test Case 3: Left skewed tree [2,1,None,0]
root3 = TreeNode(2, TreeNode(1, TreeNode(0), None), None)
print(smallestFromLeaf(root3)) # Output: "abc"

# Test Case 4: Right skewed tree [0,None,1,None,2]
root4 = TreeNode(0, None, TreeNode(1, None, TreeNode(2)))
print(smallestFromLeaf(root4)) # Output: "cba"

# Test Case 5: [25,1,3] representing 'z','b','d'
root5 = TreeNode(25, TreeNode(1), TreeNode(3))
print(smallestFromLeaf(root5)) # Output: "bz"

# Test Case 6: [0,1,1] symmetric tree
root6 = TreeNode(0, TreeNode(1), TreeNode(1))
print(smallestFromLeaf(root6)) # Output: "ba"

# Test Case 7: [4,0,1,1,None,None,None]
root7 = TreeNode(4, TreeNode(0, TreeNode(1), None), TreeNode(1))
print(smallestFromLeaf(root7)) # Output: "bae"

# Test Case 8: [0,None,1]
root8 = TreeNode(0, None, TreeNode(1))
print(smallestFromLeaf(root8)) # Output: "ba"

# Test Case 9: [3,9,20,None,None,15,7]
root9 = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
print(smallestFromLeaf(root9)) # Output: "jd"

# Test Case 10: [2,2,1,None,1,0,None,0]
root10 = TreeNode(2, TreeNode(2, None, TreeNode(1, TreeNode(0), None)), TreeNode(1, TreeNode(0), None))
print(smallestFromLeaf(root10)) # Output: "abc"