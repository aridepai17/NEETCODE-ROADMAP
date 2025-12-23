# REMOVE DUPLICATES FROM SORTED LIST 

'''
Given the head of a sorted linked list, delete all duplicates such that each element appears only once. Return the linked list sorted as well.
'''

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

'''
Algorithm:

1. Initialize a `current` pointer to the head of the linked list.
2. Iterate through the list using a `while` loop as long as `current` is not None.
3. Inside the loop:
    a. Initialize an inner `while` loop that continues as long as `current.next` is not None AND the value of `current` is equal to the value of `current.next`.
    b. Inside the inner loop, update `current.next` to `current.next.next`. This effectively skips the duplicate node.
    c. After the inner loop finishes (meaning `current.next` is None or `current.val` is different from `current.next.val`), move `current` one step forward to `current.next`.
4. After the outer loop finishes, return the original `head` of the list.
'''

def deleteDuplicates(head):
    current = head
    
    while current:
        while current.next and current.val == current.next.val:
            current.next = current.next.next
        current = current.next
        
    return head

'''
Time Complexity: O(N), where N is the number of nodes in the linked list.
- The outer while loop iterates through each unique node once.
- The inner while loop skips duplicate nodes. In the worst case, each node is visited a constant number of times (once by the outer loop, and potentially once by the inner loop's condition check).
- Therefore, the total time complexity is O(N).

Space Complexity: O(1), as we are only using a single pointer (`current`) and not allocating any additional data structures that grow with the input size.
'''

# Test Cases
head1 = [1,1,2]
print(deleteDuplicates(head1)) # Output: [1,2]


head2 = [1,1,1,2,2,3]
print(deleteDuplicates(head2)) # Output: [1,2,3]

head3 = [1,1,1,1,2,3,3]
print(deleteDuplicates(head3)) # Output: [1,2,3]

head4 = [1,1,2,2,2,3,3,3]
print(deleteDuplicates(head4)) # Output: [1,2,3]

head5 = [1,1,1,1,1,2,2,2,2,3,3,3,3,3]
print(deleteDuplicates(head5)) # Output: [1,2,3]

head6 = [1,1,1,1,1,1,1,1,1,1]
print(deleteDuplicates(head6)) # Output: [1]

head7 = [1,1,1,1,1,1,1,1,1,1,2,2,2,2,2]
print(deleteDuplicates(head7)) # Output: [1,2]

head8 = [1,1,1,1,1,1,1,1,1,1,2,2,2,2,2,2]
print(deleteDuplicates(head8)) # Output: [1,2]

head9 = [1,1,1,1,1,1,1,1,1,1,2,3,3,3,3,3]
print(deleteDuplicates(head9)) # Output: [1,2,3]

head10 = [1,1,1,1,1,1,1,1,1,1,2,3,4,4,4,4]
print(deleteDuplicates(head10)) # Output: [1,2,3,4]