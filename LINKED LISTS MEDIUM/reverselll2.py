# REVERSE LINKED LIST II

'''
Given the head of a singly linked list and two integers left and right where left <= right, 
reverse the nodes of the list from position left to position right, and return the reversed list.
'''

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

'''
Algorithm:

1. Create a `dummyNode` with a value of 0 and set its `next` pointer to the head of the original list.
   This dummy node simplifies handling cases where the reversal starts from the head.
2. Initialize `leftPrev` to `dummyNode` and `current` to `head`.
3. Traverse the list `left - 1` times to find the node *before* the `left`-th node.
   - After this loop, `leftPrev` will point to the node just before the sublist to be reversed.
   - `current` will point to the `left`-th node (the start of the sublist to be reversed).
4. Initialize `prev` to `None`. This `prev` pointer will be used to reverse the sublist.
5. Traverse the sublist `right - left + 1` times to reverse it:
   - In each iteration:
     a. Store `current.next` in `front` (to avoid losing the rest of the list).
     b. Reverse the `current` node's `next` pointer to `prev` (`current.next = prev`).
     c. Move `prev` one step forward to `current` (`prev = current`).
     d. Move `current` one step forward to `front` (`current = front`).
   - After this loop, `prev` will be the new head of the reversed sublist.
   - `current` will be the node immediately after the reversed sublist.
6. Connect the reversed sublist back to the main list:
   - The node `leftPrev.next` was originally the start of the sublist. After reversal, it becomes the tail of the reversed sublist.
     Its `next` pointer should now point to `current` (the node after the reversed sublist).
     So, `leftPrev.next.next = current`.
   - The `leftPrev` node's `next` pointer should now point to `prev` (the new head of the reversed sublist).
     So, `leftPrev.next = prev`.
7. Return `dummyNode.next`, which is the head of the modified linked list.
'''

def reverseBetween(head, left, right):
    dummyNode = ListNode(0, head)
    leftPrev = dummyNode
    current = head
    
    for i in range(left - 1):
        leftPrev = current
        current = current.next
        
    prev = None
    for i in range(right - left + 1):
        front = current.next
        current.next = prev
        prev = current
        current = front
        
    leftPrev.next.next = current
    leftPrev.next = prev
    
    return dummyNode.next

'''
Time Complexity: O(N), where N is the number of nodes in the linked list.
- The first loop iterates `left - 1` times to find the node before the reversal segment.
- The second loop iterates `right - left + 1` times to reverse the sublist.
- The final linking operations are constant time.
- In the worst case (reversing the entire list), both loops combined traverse the entire list once.
- Therefore, the total time complexity is O(N).

Space Complexity: O(1).
- We only use a few pointers (`dummyNode`, `leftPrev`, `current`, `prev`, `front`), which consume constant extra space.
'''

# Test Cases
head1 = [1,2,3,4,5], left1 = 2, right1 = 4
print(reverseBetween(head1, left1, right1)) # Output: [1,4,3,2,5]

head2 = [5], left2 = 1, right2 = 1
print(reverseBetween(head2, left2, right2)) # Output: [5]

head3 = [1,2,3,4,5], left3 = 1, right3 = 5
print(reverseBetween(head3, left3, right3)) # Output: [5,4,3,2,1]

head4 = [1,2], left4 = 1, right4 = 2
print(reverseBetween(head4, left4, right4)) # Output: [2,1]

head5 = [1,2,3], left5 = 1, right5 = 1
print(reverseBetween(head5, left5, right5)) # Output: [1,2,3]

head6 = [1,2,3,4,5,6,7,8,9,10], left6 = 3, right6 = 7
print(reverseBetween(head6, left6, right6)) # Output: [1,2,7,6,5,4,3,8,9,10]

head7 = [10,20,30,40,50], left7 = 2, right7 = 4
print(reverseBetween(head7, left7, right7)) # Output: [10,40,30,20,50]

head8 = [1,2,3,4,5], left8 = 1, right8 = 5
print(reverseBetween(head8, left8, right8)) # Output: [5,4,3,2,1]

head9 = [1,2,3,4,5], left9 = 2, right9 = 4
print(reverseBetween(head9, left9, right9)) # Output: [1,4,3,2,5]

head10 = [1,2,3,4,5], left10 = 2, right10 = 2
print(reverseBetween(head10, left10, right10)) # Output: [1,2,3,4,5]