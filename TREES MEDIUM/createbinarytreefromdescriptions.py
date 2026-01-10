# CREATE BINARY TREE FROM DESCRIPTIONS

'''
You are given a 2D integer array descriptions where descriptions[i] = [parenti, childi, isLefti] indicates that parenti is the parent of childi in a binary tree of unique values. Furthermore,
If isLefti == 1, then childi is the left child of parenti.
If isLefti == 0, then childi is the right child of parenti.
Construct the binary tree described by descriptions and return its root.
The test cases will be generated such that the binary tree is valid.
'''

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

'''
ALGORITHM:

1. Initialize an empty dictionary `nodes` to store `TreeNode` objects, keyed by their values.
2. Initialize an empty set `children` to keep track of all child node values.
3. Iterate through each `description` in the `descriptions` array:
   a. Extract `parent`, `child`, and `isLeft` from the current description.
   b. Add `child` to the `children` set.
   c. If `parent` is not in `nodes`:
      - Create a new `TreeNode(parent)` and add it to `nodes` with `parent` as the key.
   d. If `child` is not in `nodes`:
      - Create a new `TreeNode(child)` and add it to `nodes` with `child` as the key.
   e. If `isLeft` is `1`:
      - Set `nodes[parent].left` to `nodes[child]`.
   f. Else (`isLeft` is `0`):
      - Set `nodes[parent].right` to `nodes[child]`.
4. After processing all descriptions, iterate through the `descriptions` array again (or iterate through the keys of the `nodes` dictionary).
   a. For each `parent` value:
      - If `parent` is not present in the `children` set:
         - This `parent` node is the root of the entire binary tree (as it is not a child of any other node).
         - Return `nodes[parent]`.
'''

def createBinaryTree(descriptions):
    nodes = {}
    children = set()
    
    for parent, child, isLeft in descriptions:
        children.add(child)
        if parent not in nodes:
            nodes[parent] = TreeNode(parent)
        if child not in nodes:
            nodes[child] = TreeNode(child)
        if isLeft:
            nodes[parent].left = nodes[child]
        else:
            nodes[parent].right = nodes[child]
            
    for p, c, l in descriptions:
        if p not in children:
            return nodes[p]

'''
Time Complexity: O(N), where N is the number of descriptions.
- The first loop iterates through `descriptions` once (O(N)).
  - Inside the loop, dictionary operations (insertion, lookup) and set operations (insertion) take O(1) on average.
- The second loop iterates through `descriptions` once (O(N)).
  - Inside the loop, set lookup takes O(1) on average.
Overall, the dominant factor is the iteration through descriptions.

Space Complexity: O(M), where M is the total number of unique nodes in the tree.
- `nodes` dictionary stores all unique TreeNodes, so O(M) space.
- `children` set stores all child node values, so O(M) space.
In the worst case, M can be up to 2 * N (if each description introduces two new nodes).
'''

# Test Cases
descriptions1 = [[20,15,1],[20,17,0],[50,20,1],[50,80,0],[80,19,1]]
print(createBinaryTree(descriptions1)) # Output: [50,20,80,15,17,19]

descriptions2 = [[1,2,1],[1,3,0]]
print(createBinaryTree(descriptions2)) # Output: [1,2,3]

descriptions3 = [[1,2,1]]
print(createBinaryTree(descriptions3)) # Output: [1,2]

descriptions4 = [[1,2,0]]
print(createBinaryTree(descriptions4)) # Output: [1,null,2]

descriptions5 = [[10,20,1],[10,30,0],[20,40,1],[20,50,0]]
print(createBinaryTree(descriptions5)) # Output: [10,20,30,40,50]

descriptions6 = [[3,1,1],[3,2,0]]
print(createBinaryTree(descriptions6)) # Output: [3,1,2]

descriptions7 = [[100,50,1],[100,150,0],[50,25,1],[50,75,0],[150,125,1],[150,175,0]]
print(createBinaryTree(descriptions7)) # Output: [100,50,150,25,75,125,175]

descriptions8 = [[1,2,1],[2,3,1],[3,4,1]]
print(createBinaryTree(descriptions8)) # Output: [1,2,null,3,null,4]

descriptions9 = [[1,2,0],[2,3,0],[3,4,0]]
print(createBinaryTree(descriptions9)) # Output: [1,null,2,null,3,null,4]

descriptions10 = [[7,4,1],[7,8,0],[4,2,1],[4,6,0],[8,9,1],[8,10,0]]
print(createBinaryTree(descriptions10)) # Output: [7,4,8,2,6,9,10]