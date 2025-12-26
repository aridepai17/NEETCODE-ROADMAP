# PARTITION LIST

'''
Given the head of a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.
You should preserve the original relative order of the nodes in each of the two partitions.
'''

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

'''
ALGORITHM:

1. Create two dummy nodes: `left` and `right`.
   - `left` will be the head of the sublist containing nodes with values less than `x`.
   - `right` will be the head of the sublist containing nodes with values greater than or equal to `x`.
2. Create two tail pointers: `leftTail` pointing to `left` and `rightTail` pointing to `right`.
   These tails will be used to append new nodes to their respective sublists.
3. Iterate through the original linked list using a `while` loop as long as `head` is not None:
   a. If `head.val` is less than `x`:
      - Append the current `head` node to the `left` sublist: `leftTail.next = head`.
      - Move `leftTail` forward: `leftTail = leftTail.next`.
   b. Else (if `head.val` is greater than or equal to `x`):
      - Append the current `head` node to the `right` sublist: `rightTail.next = head`.
      - Move `rightTail` forward: `rightTail = rightTail.next`.
   c. Move `head` to the next node in the original list: `head = head.next`.
4. After iterating through the entire original list:
   a. Connect the `left` sublist to the `right` sublist: `leftTail.next = right.next`.
      (Note: `right.next` is the actual head of the `right` sublist, as `right` itself is a dummy node).
   b. Terminate the `right` sublist: `rightTail.next = None`. This is important to prevent cycles if the original list ended with nodes >= x.
5. Return `left.next`, which is the head of the partitioned linked list (skipping the dummy `left` node).
'''

def partition(head, x):
    left = ListNode()
    right = ListNode()
    leftTail = left
    rightTail = right
    
    while head:
        if head.val < x:
            leftTail.next = head
            leftTail = leftTail.next
        else:
            rightTail.next = head
            rightTail = rightTail.next
        head = head.next
        
    leftTail.next = right.next
    rightTail.next = None
    
    return left.next

'''
Time Complexity: O(N), where N is the number of nodes in the linked list.
- We iterate through the original linked list once.
- In each iteration, we perform constant time operations (comparison, assignment of `next` pointers).
- Therefore, the total time complexity is O(N).

Space Complexity: O(1).
- We create two dummy nodes (`left`, `right`) and a few pointers (`leftTail`, `rightTail`, `head`).
- These consume a constant amount of extra space, regardless of the input list size.
- We are not creating new nodes for the partitioned list; we are just rearranging existing nodes.
'''

# Test Cases
head1 = [1,4,3,2,5,2], x1 = 3
print(partition(head1, x1)) # Output: [1,2,2,4,3,5]

head2 = [2,1], x2 = 2
print(partition(head2, x2)) # Output: [1,2]

head3 = [1,1], x3 = 2
print(partition(head3, x3)) # Output: [1,1]

head4 = [1,4,3,2,5,2], x4 = 0
print(partition(head4, x4)) # Output: [1,4,3,2,5,2]

head5 = [1,4,3,2,5,2], x5 = 6
print(partition(head5, x5)) # Output: [1,4,3,2,5,2]

head6 = [1,2,3,4,5], x6 = 3
print(partition(head6, x6)) # Output: [1,2,3,4,5]

head7 = [5,4,3,2,1], x7 = 3
print(partition(head7, x7)) # Output: [2,1,5,4,3]

head8 = [10,20,5,15,25], x8 = 15
print(partition(head8, x8)) # Output: [10,5,20,15,25]

head9 = [1,2,3,4,5], x9 = 1
print(partition(head9, x9)) # Output: [1,2,3,4,5]

head10 = [5,4,3,2,1], x10 = 5
print(partition(head10, x10)) # Output: [4,3,2,1,5]