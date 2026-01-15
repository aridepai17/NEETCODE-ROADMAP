# FIND DUPLICATE SUBTREES

'''
Given the root of a binary tree, return all duplicate subtrees.
For each kind of duplicate subtrees, you only need to return the root node of any one of them.
Two trees are duplicate if they have the same structure with the same node values.
'''

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

'''
ALGORITHM:

1. Initialize an empty dictionary `subtrees` to store the string representation of each subtree and its frequency.
2. Initialize an empty list `result` to store the root nodes of duplicate subtrees.
3. Define a helper function `dfs(node)` that performs a post-order traversal:
   a. Base Case: If `node` is `None`, return the string "None" (to represent a null child).
   b. Recursively call `dfs` on the `left` child: `left_subtree_str = dfs(node.left)`.
   c. Recursively call `dfs` on the `right` child: `right_subtree_str = dfs(node.right)`.
   d. Construct a unique string representation `s` for the current subtree:
      - `s = str(node.val) + "," + left_subtree_str + "," + right_subtree_str`.
   e. Check if `s` is already in the `subtrees` dictionary:
      i. If `s` is in `subtrees`:
         - If `subtrees[s]` is `1` (meaning this is the second time we've seen this subtree pattern):
           - Append the current `node` to the `result` list.
         - Increment `subtrees[s]` by `1`.
      ii. If `sis not in `subtrees`:
         - Add `s` to `subtrees` with a frequency of `1`.
   f. Return the string `s`.
4. Call `dfs(root)` to start the traversal.
5. Return the `result` list.
'''

def findDuplicateSubtrees(root):
    subtrees = {}
    result = []
    
    def dfs(node):
        if not node:
            return "None"
        
        s = ",".join([str(node.val), dfs(node.left), dfs(node.right)])
        if s in subtrees:
            if subtrees[s] == 1:
                result.append(node)
            subtrees[s] += 1
        else:
            subtrees[s] = 1
            
        return s
    
    dfs(root)
    return result

'''
Time Complexity: O(N), where N is the number of nodes in the binary tree.
- Each node is visited exactly once during the DFS traversal.
- For each node, we construct a string representation of its subtree. In the worst case, this string can be of length O(N) (for a skewed tree).
- String concatenation using `",".join()` takes time proportional to the length of the resulting string.
- Dictionary operations (insertion, lookup) take O(L) on average, where L is the length of the key (the subtree string).
- Since each node's subtree string is generated once and then used as a key, and the total length of all unique subtree strings could be large, but each character is processed a constant number of times across all string operations.
- The dominant factor is the DFS traversal and string operations.

Space Complexity: O(N^2) in the worst case.
- The `subtrees` dictionary stores string representations of subtrees. In the worst case (e.g., a skewed tree where many subtrees are unique), each string could be of length O(N). Storing N such strings could lead to O(N^2) space.
- The `result` list stores at most N/2 nodes (if all subtrees are duplicates of some other subtree).
- The recursion stack for DFS can go up to O(H), where H is the height of the tree. In the worst case (skewed tree), H can be N.
'''

# Test Cases
root1 = [1,2,3,4,null,2,4,null,null,4]
print(findDuplicateSubtrees(build_tree(root1))) # Output: [[2,4],[4]]

root2 = [2,1,1]
print(findDuplicateSubtrees(build_tree(root2))) # Output: [[1]]

root3 = [2,2,2,3,null,3,null]
print(findDuplicateSubtrees(build_tree(root3))) # Output: [[2,3],[3]]

root4 = [1,1,1,1,1,1,1]
print(findDuplicateSubtrees(build_tree(root4))) # Output: [[1,1,1],[1,1],[1]]

root5 = [0,0,0,0,null,null,0,null,null,null,0]
print(findDuplicateSubtrees(build_tree(root5))) # Output: [[0,0],[0]]

root6 = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
print(findDuplicateSubtrees(build_tree(root6))) # Output: []

root7 = [1,2,3,4,null,5,null,6,null,null,null,7,null,null,null,8]
print(findDuplicateSubtrees(build_tree(root7))) # Output: []

root8 = [1,2,2,3,null,3,null,4,null,null,null,4]
print(findDuplicateSubtrees(build_tree(root8))) # Output: [[2,3,4],[3,4],[4]]

root9 = [1,2,3,4,5,2,4]
print(findDuplicateSubtrees(build_tree(root9))) # Output: [[2,4],[4]]

root10 = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31]
print(findDuplicateSubtrees(build_tree(root10))) # Output: []