# MIDDLE OF LINKED LIST

'''
Given the head of a singly linked list, return the middle node of the linked list.
If there are two middle nodes, return the second middle node.
'''

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

'''
Algorithm:

1. Initialize two pointers, `slow` and `fast`, both pointing to the head of the linked list.
2. Iterate through the list using a `while` loop as long as `fast` and `fast.next` are not None.
3. Inside the loop:
    a. Move `slow` one step forward: `slow = slow.next`.
    b. Move `fast` two steps forward: `fast = fast.next.next`.
4. When the loop terminates, `slow` will be pointing to the middle node of the linked list.
5. Return `slow`.
'''

def middleNode(head):
    slow = head
    fast = head
    
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        
    return slow

'''
Time Complexity: O(N), where N is the number of nodes in the linked list.
- The fast pointer traverses the entire list, and the slow pointer traverses half of it.
- Therefore, the total time complexity is O(N).

Space Complexity: O(1), as we are only using two pointers (slow and fast) and not allocating any additional data structures.
'''

# Test Cases
head1 = [1,2,3,4,5]
print(middleNode(head1)) # Output: 3

head2 = [1,2,3,4,5,6]
print(middleNode(head2)) # Output: 4

head3 = [1]
print(middleNode(head3)) # Output: 1

head4 = [1,2]
print(middleNode(head4)) # Output: 2

head5 = [1,2,3]
print(middleNode(head5)) # Output: 2

head6 = [1,2,3,4,5,6,7]
print(middleNode(head6)) # Output: 4

head7 = [1,2,3,4,5,6,7,8]
print(middleNode(head7)) # Output: 5

head8 = [10,20,30,40,50]
print(middleNode(head8)) # Output: 30

head9 = [10,20,30,40,50,60]
print(middleNode(head9)) # Output: 40

head10 = [100]
print(middleNode(head10)) # Output: 100