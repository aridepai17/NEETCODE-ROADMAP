# REMOVE NTH NODE FROM END OF LIST

'''
Given the head of a linked list, remove the nth node from the end of the list and return its head.
'''

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

'''
Algorithm:

1. Create a dummy node `dummyNode` and set its `next` pointer to the head of the original list.
   This dummy node simplifies handling edge cases, especially when the head itself needs to be removed.
2. Initialize two pointers: `left` to `dummyNode` and `right` to `head`.
3. Move the `right` pointer `n` steps forward. This creates a gap of `n` nodes between `left` and `right`.
   - Iterate using a `while` loop as long as `n > 0` and `right` is not `None`.
   - In each iteration, move `right` one step forward (`right = right.next`) and decrement `n`.
4. Move both `left` and `right` pointers simultaneously until `right` reaches the end of the list (i.e., `right` becomes `None`).
   - Iterate using a `while` loop as long as `right` is not `None`.
   - In each iteration, move both `left` and `right` one step forward (`left = left.next`, `right = right.next`).
5. When the second `while` loop terminates, the `left` pointer will be pointing to the node *before* the `n`-th node from the end.
   The node to be removed is `left.next`.
6. Remove the `n`-th node from the end by updating `left.next` to `left.next.next`. This effectively skips the node that needs to be removed.
7. Return `dummyNode.next`, which is the head of the modified linked list.
'''

def removeNthNodeFromEnd(head, n):
    dummyNode = ListNode(0, head)
    left = dummyNode
    right = head
    
    while n > 0 and right:
        right = right.next
        n -= 1
        
    while right:
        left = left.next
        right = right.next
        
    left.next = left.next.next
    
    return dummyNode.next

'''
Time Complexity: O(N), where N is the number of nodes in the linked list.
- The first `while` loop iterates `n` times in the worst case (if `n` is less than or equal to the list length) or until `right` becomes `None`.
- The second `while` loop iterates `N - n` times in the worst case.
- Both loops traverse the list at most once.
- Therefore, the total time complexity is O(N).

Space Complexity: O(1).
- We only use a few pointers (`dummyNode`, `left`, `right`, `n`), which consume constant extra space.
'''

# Test Cases
head1 = [1,2,3,4,5], n1 = 2
print(removeNthNodeFromEnd(head1, n1)) # Output: [1,2,3,5]

head2 = [1], n2 = 1
print(removeNthNodeFromEnd(head2, n2)) # Output: []

head3 = [1,2], n3 = 1
print(removeNthNodeFromEnd(head3, n3)) # Output: [1]

head4 = [1,2,3,4,5], n4 = 1
print(removeNthNodeFromEnd(head4, n4)) # Output: [1,2,3,4]

head5 = [1,2,3,4,5], n5 = 5
print(removeNthNodeFromEnd(head5, n5)) # Output: [2,3,4,5]

head6 = [1,2,3], n6 = 3
print(removeNthNodeFromEnd(head6, n6)) # Output: [2,3]

head7 = [1,2,3,4,5,6,7,8,9,10], n7 = 3
print(removeNthNodeFromEnd(head7, n7)) # Output: [1,2,3,4,5,6,7,9,10]

head8 = [10,20,30,40,50], n8 = 2
print(removeNthNodeFromEnd(head8, n8)) # Output: [10,20,30,50]

head9 = [100,200,300,400,500,600], n9 = 6
print(removeNthNodeFromEnd(head9, n9)) # Output: [200,300,400,500,600]

head10 = [5], n10 = 1
print(removeNthNodeFromEnd(head10, n10)) # Output: []