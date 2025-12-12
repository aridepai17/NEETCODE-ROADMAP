# REVERSE LINKED LIST

# Given the head of a singly linked list, reverse the list, and return the reversed list.

'''
Step-by-step algorithm:
    1. Initialize three pointers: `prev` to None, `current` to the head of the list, and `front` to store the next node.
    2. Iterate through the list using a `while` loop as long as `current` is not None.
    3. Inside the loop:
        a. Store the next node of `current` in `front` (i.e., `front = current.next`). This is crucial to not lose the rest of the list.
        b. Reverse the `next` pointer of `current` to point to `prev` (i.e., `current.next = prev`).
        c. Move `prev` one step forward to `current` (i.e., `prev = current`).
        d. Move `current` one step forward to `front` (i.e., `current = front`).
    4. After the loop finishes, `prev` will be pointing to the new head of the reversed list.
    5. Return `prev`.
'''

# Iterative Solution
def reverseList(head):
    prev = None    
    current = head
    
    while current:
        front = current.next
        current.next = prev
        prev = current
        current = front
        
    return prev

'''
Step-by-step algorithm (Recursive):
    1. Base Case: If the head is None or head.next is None (meaning the list is empty or has only one node),
        the list is already reversed, so return the head.
    2. Recursive Step:
            a. Recursively call `reverseList` on `head.next`. This will reverse the rest of the list and return the new head of the reversed sublist. Let's call this `newHead`.
            b. The `head.next` node (which is now the tail of the reversed sublist) should point back to the current `head`.
                So, `head.next.next = head`.
            c. The current `head` node's `next` pointer should be set to `None` to break the original link and make it the new tail.
                So, `head.next = None`.
    3. Return `newHead`, which is the head of the fully reversed list.
'''

# Recursive Solution
def reverseList(head):
    if head is None and head.next is None:
        return head
    
    newHead = self.reverseList(head.next)
    front = head.next
    front.next = head
    head.next = None
    
    return newHead

# Test Cases
head1 = [1,2,3,4,5]
print(reverseList(head1)) # Output: [5,4,3,2,1]

head2 = [1]
print(reverseList(head2)) # Output: [1]

head3 = []
print(reverseList(head3)) # Output: []

head4 = [1, 2]
print(reverseList(head4)) # Output: [2, 1]

head5 = [1, 2, 3]
print(reverseList(head5)) # Output: [3, 2, 1]

head6 = [10, 20, 30, 40, 50, 60]
print(reverseList(head6)) # Output: [60, 50, 40, 30, 20, 10]

head7 = [7, 6, 5, 4, 3, 2, 1]
print(reverseList(head7)) # Output: [1, 2, 3, 4, 5, 6, 7]

head8 = [100]
print(reverseList(head8)) # Output: [100]

head9 = [1, 1, 1, 1, 1]
print(reverseList(head9)) # Output: [1, 1, 1, 1, 1]

head10 = [0, -1, -2, -3]
print(reverseList(head10)) # Output: [-3, -2, -1, 0]