# REMOVE LINKED LIST ELEMENTS

'''
Given the head of a linked list and an integer val, remove all the nodes of the linked list that has Node.val == val, and return the new head.
'''

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

'''
Algorithm:

1. Create a dummy node and set its `next` pointer to the head of the original list. This dummy node simplifies handling cases where the head itself needs to be removed.
2. Initialize two pointers: `prev` to the dummy node and `current` to the head of the list.
3. Iterate through the list using a `while` loop as long as `current` is not None.
4. Inside the loop:
    a. If `current.val` is equal to the `val` to be removed:
        i. Update `prev.next` to `current.next`, effectively skipping the `current` node.
    b. Else (if `current.val` is not equal to `val`):
        i. Move `prev` one step forward to `current` (i.e., `prev = current`).
    c. Move `current` one step forward to `current.next` (i.e., `current = current.next`).
5. After the loop finishes, return `dummyNode.next`, which will be the new head of the modified list.
'''

def removeElements(head, val):
    dummyNode = ListNode(0, head)
    prev = dummyNode
    current = head
    
    while current:
        if current.val == val:
            prev.next = current.next 
        else:
            prev = current
        current = current.next
        
    return dummyNode.next



# Test Cases
head1 = [1,2,6,3,4,5,6], val1 = 6
print(removeElements(head1, val1)) # Output: [1, 2, 3, 4, 5]


head2 = [], val2 = 1
print(removeElements(head2, val2)) # Output: []

head3 = [1], val3 = 1
print(removeElements(head3, val3)) # Output: []

head4 = [1, 2, 2, 3], val4 = 2
print(removeElements(head4, val4)) # Output: [1, 3]

head5 = [1, 2, 2, 3, 3], val5 = 3
print(removeElements(head5, val5)) # Output: [1, 2, 2]

head6 = [1, 1, 2, 2, 3, 3, 3], val6 = 1
print(removeElements(head6, val6)) # Output: [2, 2, 3, 3, 3]

head7 = [1, 2, 2, 3, 3, 3, 4, 5], val7 = 3
print(removeElements(head7, val7)) # Output: [1, 2, 2, 4, 5]

head8 = [1, 2, 2, 3, 3, 3, 4, 4, 5], val8 = 4
print(removeElements(head8, val8)) # Output: [1, 2, 2, 3, 3, 3, 5]

head9 = [1, 2, 2, 3, 3, 3, 4, 4, 5, 5], val9 = 5
print(removeElements(head9, val9)) # Output: [1, 2, 2, 3, 3, 3, 4, 4]

head10 = [1, 2, 2, 3, 3, 3, 4, 4, 5, 5, 5], val10 = 5
print(removeElements(head10, val10)) # Output: [1, 2, 2, 3, 3, 3, 4, 4]