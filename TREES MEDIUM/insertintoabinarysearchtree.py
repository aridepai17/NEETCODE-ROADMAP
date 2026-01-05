# INSERT INTO A BINARY SEARCH TREE

'''
You are given the root node of a binary search tree (BST) and a value to insert into the tree. Return the root node of the BST after the insertion. 
It is guaranteed that the new value does not exist in the original BST.
Notice that there may exist multiple valid ways for the insertion, as long as the tree remains a BST after insertion. You can return any of them.
'''



# Iterative Solution
def insertIntoBST(root, val):
    if not root:
        return TreeNode(val)
    
    current = root
    while True:
        if val > current.right:
            if not current.right:
                current.right = TreeNode(val)
                return root
            current = current.right
        else:
            if not current.left:
                current.left = TreeNode(val)
                return root
            current = current.left

'''
Time Complexity: O(H), where H is the height of the BST.
In the worst case (a skewed tree), H can be N, where N is the number of nodes.
In the best case (a balanced tree), H is log N.
This is because in we traverse down the tree from the root to find the insertion point.

Space Complexity: O(1).
We are only using a few pointers (current) and not allocating any additional data structures that grow with the input size.
'''

# Recursive Solution
def insertIntoBST(root, val):
    if not root:
        return TreeNode(val)
    
    if val > root.val:
        root.right = insertIntoBST(root.right, val)
    else:
        root.left = insertIntoBST(root.left, val)
        
    return root

'''
Time Complexity: O(H), where H is the height of the BST.
In the worst case (a skewed tree), H can be N, where N is the number of nodes.
In the best case (a balanced tree), H is log N.
This is because in each recursive call, we move down one level in the tree.

Space Complexity: O(H), where H is the height of the BST.
This is due to the recursion stack. In the worst case (a skewed tree), H can be N.
In the best case (a balanced tree), H is log N.
'''

# Test Cases
root1 = [4,2,7,1,3], val1 = 5
print(insertIntoBST(root1, val1)) # Output: [4,2,7,1,3,5]

root2 = [40,20,60,10,30,50,70], val2 = 25
print(insertIntoBST(root2, val2)) # Output: [40,20,60,10,30,50,70,null,null,25]

root3 = [4,2,7,1,3], val3 = 0
print(insertIntoBST(root3, val3)) # Output: [4,2,7,1,3,0]

root4 = [4,2,7,1,3], val4 = 8
print(insertIntoBST(root4, val4)) # Output: [4,2,7,1,3,null,8]

root5 = [4,2,7,1,3], val5 = 6
print(insertIntoBST(root5, val5)) # Output: [4,2,7,1,3,6]

root6 = [], val6 = 5
print(insertIntoBST(root6, val6)) # Output: [5]

root7 = [10,5,15], val7 = 7
print(insertIntoBST(root7, val7)) # Output: [10,5,15,null,7]

root8 = [10,5,15], val8 = 12
print(insertIntoBST(root8, val8)) # Output: [10,5,15,null,null,12]

root9 = [10,5,15], val9 = 3
print(insertIntoBST(root9, val9)) # Output: [10,5,15,3]

root10 = [10,5,15], val10 = 18
print(insertIntoBST(root10, val10)) # Output: [10,5,15,null,null,null,18]