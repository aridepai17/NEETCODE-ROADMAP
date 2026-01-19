# DISTRIBUTE COINS IN BINARY TREE

'''
You are given the root of a binary tree with n nodes where each node in the tree has node.val coins. There are n coins in total throughout the whole tree.
In one move, we may choose two adjacent nodes and move one coin from one node to another. A move may be from parent to child, or from child to parent.
Return the minimum number of moves required to make every node have exactly one coin.
'''

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

'''
Algorithm:
1. Use post-order DFS traversal to process children before the parent
2. For each subtree, track two values: the number of nodes (size) and total coins
3. At each node, calculate the excess or deficit: (coins - size)
4. If coins > size, excess coins must flow out (to parent); if coins < size, coins must flow in
5. The number of moves for each edge equals |size - coins| (absolute difference)
6. Accumulate all moves across every edge in the tree
7. Return the total number of moves required
'''

def distributeCoins(root):
    result = 0
    def dfs(current):
        nonlocal result
        if not current:
            return [0, 0] # [TreeSize, Coins]

        leftSize, leftCoins = dfs(current.left)
        rightSize, rightCoins = dfs(current.right)

        size = 1 + leftSize + rightSize
        coins = current.val + leftCoins + rightCoins
        result += abs(size - coins)

        return [size, coins]

    dfs(root)
    return result

'''
Time Complexity: O(N), where N is the number of nodes in the tree.
- We visit each node exactly once during the DFS traversal.
- At each node, we perform O(1) operations (additions, subtractions, absolute value).

Space Complexity: O(H), where H is the height of the tree.
- The recursion stack can go as deep as the height of the tree.
- In the worst case (skewed tree), H = N, so space complexity is O(N).
- In a balanced tree, H = log(N), so space complexity is O(log N).
- Each recursive call uses O(1) extra space for local variables.
'''

# Test Cases

# Test Case 1: [3,0,0] - root has 3 coins, children have 0
root1 = TreeNode(3, TreeNode(0), TreeNode(0))
print(distributeCoins(root1)) # Output: 2

# Test Case 2: [0,3,0] - left child has all coins
root2 = TreeNode(0, TreeNode(3), TreeNode(0))
print(distributeCoins(root2)) # Output: 3

# Test Case 3: Single node with 1 coin
root3 = TreeNode(1)
print(distributeCoins(root3)) # Output: 0

# Test Case 4: [1,0,2] - uneven distribution
root4 = TreeNode(1, TreeNode(0), TreeNode(2))
print(distributeCoins(root4)) # Output: 1

# Test Case 5: [1,0,0,None,3] - deeper tree
root5 = TreeNode(1, TreeNode(0, None, TreeNode(3)), TreeNode(0))
print(distributeCoins(root5)) # Output: 4

# Test Case 6: [0,0,0,3,0,0,0] - all coins at one leaf
root6 = TreeNode(0, TreeNode(0, TreeNode(4), TreeNode(0)), TreeNode(0, TreeNode(0), TreeNode(0)))
print(distributeCoins(root6)) # Output: 6

# Test Case 7: [1,1,1] - already balanced
root7 = TreeNode(1, TreeNode(1), TreeNode(1))
print(distributeCoins(root7)) # Output: 0

# Test Case 8: [4,0,0,0,0,None,None] - root heavy with deeper left
root8 = TreeNode(4, TreeNode(0, TreeNode(0), TreeNode(0)), TreeNode(0))
print(distributeCoins(root8)) # Output: 6

# Test Case 9: [0,0,2,0,2,None,None] - multiple excess nodes
root9 = TreeNode(0, TreeNode(0, TreeNode(0), TreeNode(2)), TreeNode(2))
print(distributeCoins(root9)) # Output: 4

# Test Case 10: [2,0,2,0,0,None,None] - symmetric excess
root10 = TreeNode(2, TreeNode(0, TreeNode(0), TreeNode(0)), TreeNode(2))
print(distributeCoins(root10)) # Output: 4