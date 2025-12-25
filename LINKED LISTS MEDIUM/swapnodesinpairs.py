# SWAP NODES IN PAIRS

'''
Given a linked list, swap every two adjacent nodes and return its head. 
You must solve the problem without modifying the values in the list's nodes (i.e., only nodes themselves may be changed.)
'''

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

'''
Algorithm:

1. Create a `dummyNode` with a value of 0 and set its `next` pointer to the head of the original list.
   This dummy node simplifies handling cases where the head itself is part of a swapped pair.
2. Initialize `prev` to `dummyNode` and `current` to `head`.
3. Iterate through the list using a `while` loop as long as `current` and `current.next` are not None.
   This ensures there's at least a pair of nodes to swap.
4. Inside the loop:
   a. Store `current.next.next` in `nextPair`. This is the start of the next pair (or None).
   b. Store `current.next` in `second`. This is the second node of the current pair.
   c. Reverse the link for the second node: `second.next = current`. Now `second` points to `current`.
   d. Link the first node of the pair to the `nextPair`: `current.next = nextPair`.
   e. Link the `prev` node (which is either `dummyNode` or the first node of the previous pair) to `second`: `prev.next = second`.
   f. Move `prev` to `current` (the first node of the current pair, which is now the second node in the swapped pair).
   g. Move `current` to `nextPair` (the start of the next pair).
5. After the loop finishes, return `dummyNode.next`, which is the head of the modified linked list.
'''

def swapPairs(head):
    dummyNode = ListNode(0, head)
    prev = dummyNode
    current = head
    
    while current and current.next:
        nextPair = current.next.next
        second = current.next
        second.next = current
        current.next = nextPair
        prev.next = second
        prev = current
        current = nextPair
        
    return dummyNode.next

'''
Time Complexity: O(N), where N is the number of nodes in the linked list.
- We iterate through the linked list once, processing pairs of nodes.
- Each node is visited and its pointers are adjusted a constant number of times.
- Therefore, the total time complexity is O(N).

Space Complexity: O(1).
- We only use a few pointers (`dummyNode`, `prev`, `current`, `nextPair`, `second`), which consume constant extra space.
'''

# Test Cases
head1 = [1,2,3,4]
print(swapPairs(head1)) # Output: [2,1,4,3]

head2 = []
print(swapPairs(head2)) # Output: []

head3 = [1]
print(swapPairs(head3)) # Output: [1]

head4 = [1,2,3,4,5]
print(swapPairs(head4)) # Output: [2,1,4,3,5]

head5 = [1,2]
print(swapPairs(head5)) # Output: [2,1]

head6 = [1,2,3]
print(swapPairs(head6)) # Output: [2,1,3]

head7 = [10,20,30,40,50,60]
print(swapPairs(head7)) # Output: [20,10,40,30,60,50]

head8 = [100,200,300,400]
print(swapPairs(head8)) # Output: [200,100,400,300]

head9 = [5,4,3,2,1]
print(swapPairs(head9)) # Output: [4,5,2,3,1]

head10 = [1,1,1,1]
print(swapPairs(head10)) # Output: [1,1,1,1]