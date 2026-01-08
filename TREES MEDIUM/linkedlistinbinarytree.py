# LINKED LIST IN BINARY TREE

'''
Given a binary tree root and a linked list with head as the first node. 
Return True if all the elements in the linked list starting from the head correspond to some downward path connected in the binary tree otherwise return False.
In this context downward path means a path that starts at some node and goes downwards.
'''

def isSubPath(head, root):
    def helper(listNode, treeNode):
        if not listNode:
            return True
        if not treeNode:
            return False
        if listNode.val != treeNode.val:
            return False
        
        return (
            helper(listNode.next, treeNode.left) or
            helper(listNode.next, treeNode.right)
        )
        
    if helper(head, root):
        return True
    if not root:
        return False
    return (
        isSubPath(head, root.left) or
        isSubPath(head, root.right)
    )

'''
Time Complexity: O(N * min(L, H)), where N is the number of nodes in the binary tree, L is the length of the linked list, and H is the height of the binary tree.
In the worst case, the `helper` function might be called for every node in the tree. For each call to `helper`, it traverses the linked list and potentially down the tree. The depth of this traversal is limited by `min(L, H)`.

Space Complexity: O(min(L, H)) due to the recursion stack for the `helper` function.
The `isSubPath` function also uses a recursion stack, which can go up to O(H).
'''

# Test Cases
head1 = [4,2,8], root1 = [1,4,4,null,2,2,null,1,null,6,8,null,null,null,1,3]
print(isSubPath(head1, root1)) # Output: True

head2 = [1,4,2,6], root2 = [1,4,4,null,2,2,null,1,null,6,8,null,null,null,1,3]
print(isSubPath(head2, root2)) # Output: True

head3 = [1,4,2,8], root3 = [1,4,4,null,2,2,null,1,null,6,8,null,null,null,1,3]
print(isSubPath(head3, root3)) # Output: False

head4 = [1,2,3], root4 = [1,1,1,1,2,3]
print(isSubPath(head4, root4)) # Output: True

head5 = [1,2,3], root5 = [1,1,1,1,2,4]
print(isSubPath(head5, root5)) # Output: False

head6 = [1], root6 = [1]
print(isSubPath(head6, root6)) # Output: True

head7 = [1], root7 = [2]
print(isSubPath(head7, root7)) # Output: False

head8 = [1,2], root8 = [1,null,2]
print(isSubPath(head8, root8)) # Output: True

head9 = [1,2], root9 = [2,1]
print(isSubPath(head9, root9)) # Output: False

head10 = [1,1,1], root10 = [1,1,1,1,1,1,1]
print(isSubPath(head10, root10)) # Output: True