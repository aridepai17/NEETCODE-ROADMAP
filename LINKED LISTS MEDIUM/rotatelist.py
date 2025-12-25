# ROTATE LIST

'''
Given the head of a linked list, rotate the list to the right by k places.
'''

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

'''
Algorithm:

1. Handle edge cases: If the list is empty (`head` is None), return `head` as there's nothing to rotate.
2. Calculate the length of the linked list and find its tail:
   - Initialize `length = 1` and `tail = head`.
   - Traverse the list using a `while` loop until `tail.next` is None.
   - In each iteration, move `tail` one step forward and increment `length`.
3. Adjust `k`:
   - Calculate `k = k % length`. This handles cases where `k` is greater than or equal to the list's length.
   - If `k` becomes 0 after the modulo operation, it means no rotation is needed, so return the original `head`.
4. Find the new head and the new tail of the rotated list:
   - Initialize `current = head`.
   - Traverse the list `length - k - 1` steps forward from the `head`. This `current` node will become the new tail of the rotated list.
   - The node `current.next` will be the `newHead` of the rotated list.
5. Perform the rotation:
   - Set `current.next = None` to break the link and make `current` the new tail.
   - Set `tail.next = head` to connect the original tail to the original head, forming a cycle.
6. Return `newHead`, which is the head of the rotated linked list.
'''

def rotateRight(head, k):
    if not head:
        return head
    
    length = 1
    tail = head
    
    while tail.next:
        tail = tail.next
        length += 1
        
    k = k % length
    if k == 0:
        return head
    
    current = head
    for i in range(length - k - 1):
        current = current.next
        
    newHead = current.next
    current.next = None
    tail.next = head
    
    return newHead

'''
Time Complexity: O(N), where N is the number of nodes in the linked list.
- The first loop iterates through the entire list to find its length and tail, taking O(N) time.
- The second loop iterates `length - k - 1` times to find the new tail, taking O(N) time in the worst case.
- The operations for linking nodes are constant time.
- Therefore, the total time complexity is O(N).

Space Complexity: O(1).
- We only use a few pointers (`head`, `tail`, `current`, `newHead`) and integer variables (`length`, `k`), which consume constant extra space.
'''

# Test Cases
head1 = [1,2,3,4,5], k1 = 2
print(rotateRight(head1, k1)) # Output: [4,5,1,2,3]

head2 = [0,1,2], k2 = 4
print(rotateRight(head2, k2)) # Output: [2,0,1]

head3 = [], k3 = 0
print(rotateRight(head3, k3)) # Output: []

head4 = [1], k4 = 1
print(rotateRight(head4, k4)) # Output: [1]

head5 = [1,2], k5 = 0
print(rotateRight(head5, k5)) # Output: [1,2]

head6 = [1,2], k6 = 1
print(rotateRight(head6, k6)) # Output: [2,1]

head7 = [1,2,3], k7 = 1
print(rotateRight(head7, k7)) # Output: [3,1,2]

head8 = [1,2,3,4,5], k8 = 5
print(rotateRight(head8, k8)) # Output: [1,2,3,4,5]

head9 = [1,2,3,4,5], k9 = 6
print(rotateRight(head9, k9)) # Output: [5,1,2,3,4]

head10 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], k10 = 10
print(rotateRight(head10, k10)) # Output: [10, 1, 2, 3, 4, 5, 6, 7, 8, 9]