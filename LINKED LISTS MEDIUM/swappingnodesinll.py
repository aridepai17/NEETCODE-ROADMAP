# SWAPPING NODES IN A LINKED LIST

'''
You are given the head of a linked list, and an integer k.
Return the head of the linked list after swapping the values of the kth node from the beginning and the kth node from the end (the list is 1-indexed).
'''

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

'''
Algorithm:

1. Initialize three pointers: `current`, `left`, and `right`.
2. Traverse the list with `current` for `k-1` steps to find the `k`-th node from the beginning.
   - Set `left` to this `k`-th node.
3. Initialize `right` to the head of the list.
4. Continue traversing the list with `current` until it reaches the end (i.e., `current.next` is None).
   - Simultaneously, move `right` one step forward for each step `current` takes.
   - When `current` reaches the end, `right` will be pointing to the `k`-th node from the end.
5. Swap the values of the `left` and `right` nodes.
6. Return the `head` of the linked list.
'''

def swapNodes(head, k):
    current = head
    for i in range(k - 1):
        current = current.next
        
    left = current
    right = head
    
    while current.next:
        current = current.next
        right = right.next
    left.val, right.val = right.val, left.val
    
    return head

'''
Time Complexity: O(N), where N is the number of nodes in the linked list.
- The first loop iterates `k-1` times.
- The second loop iterates `N-k` times.
- The total number of traversals is approximately `(k-1) + (N-k) = N-1`, which is O(N).
- Swapping values is a constant time operation.
- Therefore, the total time complexity is O(N).

Space Complexity: O(1).
- We only use a few pointers (`current`, `left`, `right`) which consume constant extra space.
'''

# Test Cases
head1 = [1,2,3,4,5], k1 = 2
print(swapNodes(head1, k1)) # Output: [1,4,3,2,5]

head2 = [7,9,6,6,7,8,3,0,9,5], k2 = 5
print(swapNodes(head2, k2)) # Output: [7,9,6,6,7,8,3,0,9,5]

head3 = [1,2,3,4,5], k3 = 1
print(swapNodes(head3, k3)) # Output: [5,2,3,4,1]

head4 = [1,2,3,4,5], k4 = 5
print(swapNodes(head4, k4)) # Output: [5,2,3,4,1]

head5 = [1], k5 = 1
print(swapNodes(head5, k5)) # Output: [1]

head6 = [1,2], k6 = 1
print(swapNodes(head6, k6)) # Output: [2,1]

head7 = [1,2], k7 = 2
print(swapNodes(head7, k7)) # Output: [2,1]

head8 = [10,20,30,40,50,60], k8 = 3
print(swapNodes(head8, k8)) # Output: [10,20,40,30,50,60]

head9 = [100,200,300,400,500], k9 = 2
print(swapNodes(head9, k9)) # Output: [100,400,300,200,500]

head10 = [1,2,3,4,5,6,7,8,9,10], k10 = 4
print(swapNodes(head10, k10)) # Output: [1,2,3,7,5,6,4,8,9,10]