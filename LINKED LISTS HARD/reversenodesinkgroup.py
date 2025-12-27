# REVERSE NODES IN K GROUP

'''
Given the head of a linked list, reverse the nodes of the list k at a time, and return the modified list.
k is a positive integer and is less than or equal to the length of the linked list. 
If the number of nodes is not a multiple of k then left-out nodes, in the end, should remain as it is.
You may not alter the values in the list's nodes, only nodes themselves may be changed.
'''

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

'''
ALGORITHM:

1. Define a helper function `findKthNode(current, k)`:
   - This function takes a `current` node and an integer `k`.
   - It iterates `k-1` times, moving `current` forward.
   - It returns the `k`-th node from the starting `current` node. If it reaches the end before finding the `k`-th node, it returns `None`.

2. Define a helper function `reverseList(head)`:
   - This function takes the `head` of a sublist and reverses it.
   - It uses three pointers: `prev` (initialized to `None`), `current` (initialized to `head`), and `front` (to store `current.next`).
   - It iterates while `current` is not `None`, reversing the `next` pointer of `current` to `prev`, then moving `prev` and `current` forward.
   - It returns `prev`, which will be the new head of the reversed sublist.

3. Initialize `current` to the `head` of the main linked list.
4. Initialize `prevNode` to `None`. This pointer will keep track of the node just before the current group being processed, to link the reversed group back.

5. Iterate through the linked list using a `while` loop as long as `current` is not `None`:
   a. Call `findKthNode(current, k)` to find the `k`-th node of the current group. Let's call it `kNode`.
   b. If `kNode` is `None`:
      - This means there are fewer than `k` nodes remaining in the list.
      - If `prevNode` is not `None`, link `prevNode.next` to `current` (the start of the remaining un-reversed nodes).
      - Break out of the loop, as these remaining nodes should not be reversed.
   c. Store `kNode.next` in `nextNode`. This is the head of the next group (or `None` if it's the last group).
   d. Set `kNode.next = None`. This effectively cuts off the current group from the rest of the list, making it an independent sublist for reversal.
   e. Call `reverseList(current)` to reverse this sublist. Let the new head of the reversed sublist be `newHead`.
   f. If this is the very first group being processed (`current == head`), update the main `head` to `newHead`.
   g. Otherwise (if `prevNode` exists), link `prevNode.next` to `newHead` to connect the previously processed group with the current reversed group.
   h. Update `prevNode` to `current`. This `current` is now the tail of the just-reversed group.
   i. Set `current = nextNode` to move to the beginning of the next group.

6. Return the (potentially updated) `head` of the linked list.
'''

def reverseKGroup(head, k):
    def findKthNode(current, k):
        while current and k > 1:
            k -= 1
            current = current.next
        return current
    
    def reverseList(head):
        current = head
        prev = None
        
        while current:
            front = current.next
            current.next = prev
            prev = current
            current = front
            
        return prev
        
    current = head
    prevNode = None
    
    while current:
        kNode = findKthNode(current, k)
        if not kNode:
            if prevNode:
                prevNode.next = current
            break
        
        nextNode = kNode.next
        kNode.next = None
        
        newHead = reverseList(current)
        if current == head:
            head = newHead
        else:
            prevNode.next = newHead
            
        prevNode = current
        current = nextNode
        
    return head

'''
Time Complexity: O(N) where N is the total number of nodes in the linked list.
We iterate through the linked list multiple times.
- `findKthNode` takes O(k) time.
- `reverseList` takes O(k) time.
Since we process each group of k nodes, and there are N/k such groups, the total time complexity is (N/k) * O(k) = O(N).

Space Complexity: O(1)
We are only using a few extra pointers, so the space complexity is constant.
'''

# Test Cases
head1 = [1,2,3,4,5], k = 2
print(reverseKGroup(head1, k)) # Output: [2,1,4,3,5]

head2 = [1,2,3,4,5], k = 3
print(reverseKGroup(head2, k)) # Output: [3,2,1,4,5]

head3 = [1,2,3,4,5], k = 1
print(reverseKGroup(head3, k)) # Output: [1,2,3,4,5]

head4 = [1,2,3,4,5], k = 5
print(reverseKGroup(head4, k)) # Output: [5,4,3,2,1]

head5 = [1,2,3,4,5,6,7,8], k = 3
print(reverseKGroup(head5, k)) # Output: [3,2,1,6,5,4,7,8]

head6 = [1,2,3,4,5,6,7], k = 4
print(reverseKGroup(head6, k)) # Output: [4,3,2,1,5,6,7]

head7 = [1,2], k = 2
print(reverseKGroup(head7, k)) # Output: [2,1]

head8 = [1], k = 1
print(reverseKGroup(head8, k)) # Output: [1]

head9 = [], k = 1
print(reverseKGroup(head9, k)) # Output: []

head10 = [1,2,3,4,5,6,7,8,9,10], k = 4
print(reverseKGroup(head10, k)) # Output: [4,3,2,1,8,7,6,5,9,10]