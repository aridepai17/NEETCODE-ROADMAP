# REORDER LIST

'''
You are given the head of a singly linked-list. The list can be represented as:
L0 → L1 → … → Ln - 1 → Ln
Reorder the list to be on the following form:
L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …
You may not modify the values in the list's nodes. Only nodes themselves may be changed.
'''

def reorderList(head):
    slow = head
    fast = head.next
    
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        
    second = slow.next
    slow.next = None
    prev = None
    
    while second:
        front = second.next
        second.next = prev
        prev = second
        second = front
        
    first = head
    second = prev
    
    while second:
        temp1 = first.next
        temp2 = second.next
        first.next = second
        second.next = temp1
        first = temp1
        second = temp2

'''
Time Complexity: O(N), where N is the number of nodes in the linked list.
- Finding the middle of the list takes O(N) time.
- Reversing the second half of the list takes O(N) time.
- Merging the two halves takes O(N) time.
- Therefore, the total time complexity is O(N).

Space Complexity: O(1).
- We are performing the modifications in-place, reusing the existing nodes.
- Only a few pointers (`slow`, `fast`, `second`, `prev`, `first`, `temp1`, `temp2`) are used, which consume constant extra space.
'''

# Test Cases
head1 = [1,2,3,4]
print(reorderList(head1)) # Output: [1,4,2,3]

