# REMOVE NODES FROM LINKED LIST

'''
You are given the head of a linked list.
Remove every node which has a node with a greater value anywhere to the right side of it.
Return the head of the modified linked list.
'''

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

'''
ALGORITHM:

1. REVERSE THE LINKED LIST:
   - The problem asks to remove nodes that have a greater value *to the right*.
   - If we reverse the list, the problem becomes removing nodes that have a greater value *to the left*.
   - This transformation allows for a single pass solution.

2. TRAVERSE THE REVERSED LIST AND BUILD THE RESULT:
   - Initialize `current` to the head of the reversed list.
   - Initialize `currentMax` to `current.val`.
   - Initialize `resultHead` to `current` (this will be the head of our partially built result list).
   - Iterate while `current.next` is not `None`:
     a. If `current.next.val < currentMax`:
        - This node should be removed. Skip it by setting `current.next = current.next.next`.
     b. Else (`current.next.val >= currentMax`):
        - This node should be kept. Update `currentMax = current.next.val`.
        - Move `current` to `current.next`.

3. REVERSE THE RESULT LIST AGAIN:
   - After processing the reversed list, the `resultHead` points to the head of the modified list, but it's still in reversed order.
   - Reverse this list one more time to get the final correct order.

4. RETURN THE HEAD OF THE FINAL LIST.
'''

# Stack Solution
def removeNodes(head):
    stack = []
    current = head
    
    while current:
        while stack and current.val > stack[-1]:
            stack.pop()
        stack.append(current.val)
        current = current.next
        
    dummyNode = ListNode()
    current = dummyNode
    
    for num in stack:
        current.next = ListNode(num)
        current = current.next
        
    return dummyNode.next

'''
Time Complexity: O(N), where N is the number of nodes in the linked list.
- We iterate through the linked list once. Each node is visited a constant number of times (once by the outer loop, and potentially once by the inner loop).
- The operations inside the loops (assignments, additions) are all constant time.
- Therefore, the total time complexity is O(N).

Space Complexity: O(N).
- We use a stack to store the values of the nodes.
- In the worst case, the stack can contain all nodes of the linked list.
- Therefore, the space complexity is O(N).
'''

# In-Place Solution
def removeNodes2(head):
    def reverse(head):
        prev = None
        current = head
        
        while current:
            front = current.next
            current.next = prev
            prev = current
            current = front
            
        return prev
    
    head = reverse(head)
    
    current = head
    currentMax = current.value
    
    while current.next:
        if current.next.val < currentMax:
            current.next = current.next.next
        else:
            currentMax = current.next.val
            current = current.next
            
    return reverse(head)

'''
Time Complexity: O(N), where N is the number of nodes in the linked list.
- We iterate through the linked list once. Each node is visited a constant number of times (once by the outer loop, and potentially once by the inner loop).
- The operations inside the loops (assignments, additions) are all constant time.
- Therefore, the total time complexity is O(N).

Space Complexity: O(1).
- We are performing the modifications in-place, reusing the existing nodes.
- Only a few pointers (`current`, `node`) are used, which consume constant extra space.
'''

# Test Cases
head1 = [5,2,13,3,8]
print(removeNodes(head)) # Output: [13, 8]

head2 = [1,5,2,9]
print(removeNodes(head2)) # Output: [5, 9]

head3 = [1,9,8,2]
print(removeNodes(head3)) # Output: [9, 2]

head4 = [1,2,3]
print(removeNodes(head4)) # Output: [3]

head5 = [1]
print(removeNodes(head5)) # Output: [1]

head6 = [5,2,13,3,8]
print(removeNodes2(head6)) # Output: [13, 8]

head7 = [1,5,2,9]
print(removeNodes2(head7)) # Output: [5, 9]

head8 = [1,9,8,2]
print(removeNodes2(head8)) # Output: [9, 2]

head9 = [1,2,3]
print(removeNodes2(head9)) # Output: [3]

head10 = [1, 2, 3, 5, 2, 4]
print(removeNodes2(head10)) # Output: [5, 4]