# MERGE NODES IN BETWEEN ZEROS

'''
You are given the head of a linked list, which contains a series of integers separated by 0's.
The beginning and end of the linked list will have Node.val == 0.
For every two consecutive 0's, merge all the nodes lying in between them into a single node whose value is the sum of all the merged nodes. 
The modified list should not contain any 0's.
Return the head of the modified linked list.
'''

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Extra Space Solution
def mergeNodes(head):
    current = head
    dummyNode = ListNode()
    tail = dummyNode
    
    while current.next:
        node = ListNode()
        while current.next.val != 0:
            node.val += current.next.val
            current = current.next
        tail.next = node
        tail = tail.next
        current = current.next
        
    return dummyNode.next

'''
Time Complexity: O(N), where N is the number of nodes in the linked list.
- We iterate through the linked list once. Each node is visited a constant number of times (once by the outer loop, and potentially once by the inner loop).
- The operations inside the loops (assignments, additions) are all constant time.
- Therefore, the total time complexity is O(N).

Space Complexity: O(1).
- We are performing the modifications in-place, reusing the existing nodes.
- Only a few pointers (`current`, `node`) are used, which consume constant extra space.
'''

# In-Place Solution
'''
1. INITIALIZE CURRENT POINTER:
   - Start with current pointing to the head (first zero node)

2. PROCESS EACH SEGMENT BETWEEN ZEROS:
   - While current.next exists (not at the end):
     a. Set node to current.next (first non-zero node in current segment)
     b. Move current to current.next
     c. Accumulate values until next zero is found:
        - While current.next.val != 0:
          - Add current.next.val to node.val
          - Move current to current.next
     d. Skip the zero node and link to next segment:
        - Set current.next to current.next.next (skip zero)
        - Set node.next to current.next (link to next segment)

3. RETURN RESULT:
   - Return head.next (skip the initial zero node)
'''
def mergeNodes2(head):
    current = head
    
    while current.next:
        node = current.next
        current = current.next
        while current.next.val != 0:
            node.val += current.next.val
            current = current.next
        current.next = current.next
        node.next = current.next
        
    return head.next

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
head1 = [0,3,1,0,4,5,2,0]
print(mergeNodes2(head1)) # Output: [4, 11]

head2 = [0,1,0,3,0,2,2,0]
print(mergeNodes2(head2)) # Output: [1, 3, 4]

head3 = [0,1,2,0,3,4,0,5,6,0]
print(mergeNodes2(head3)) # Output: [3, 7, 11]

head4 = [0,0]
print(mergeNodes2(head4)) # Output: []

head5 = [0,1,0]
print(mergeNodes2(head5)) # Output: [1]

head6 = [0,1,1,1,0,2,2,2,0]
print(mergeNodes2(head6)) # Output: [3, 6]

head7 = [0,5,0,5,0,5,0]
print(mergeNodes2(head7)) # Output: [5, 5, 5]

head8 = [0,10,20,30,0,1,2,3,0]
print(mergeNodes2(head8)) # Output: [60, 6]

head9 = [0,1,0,1,0,1,0,1,0]
print(mergeNodes2(head9)) # Output: [1, 1, 1, 1]

head10 = [0,100,0]
print(mergeNodes2(head10)) # Output: [100]