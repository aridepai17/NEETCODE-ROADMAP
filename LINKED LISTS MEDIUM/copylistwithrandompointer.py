# COPY LIST WITH RANDOM POINTER

'''
A linked list of length n is given such that each node contains an additional random pointer, which could point to any node in the list, or null.
Construct a deep copy of the list. The deep copy should consist of exactly n brand new nodes, where each new node has its value set to the value of its corresponding original node. 
Both the next and random pointer of the new nodes should point to new nodes in the copied list such that the pointers in the original list and copied list represent the same list state. 
None of the pointers in the new list should point to nodes in the original list.

For example, if there are two nodes X and Y in the original list, where X.random --> Y, then for the corresponding two nodes x and y in the copied list, x.random --> y.
Return the head of the copied linked list.

The linked list is represented in the input/output as a list of n nodes. Each node is represented as a pair of [val, random_index] where:
val: an integer representing Node.val
random_index: the index of the node (range from 0 to n-1) that the random pointer points to, or null if it does not point to any node.

Your code will only be given the head of the original linked list.
'''

class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

'''
ALGORITHM:

1. CREATE A HASH MAP TO STORE MAPPINGS:
   - Initialize an empty hash map (dictionary in Python) called `hashMap`.
   - Add a mapping for `None` to `None` to handle null random pointers gracefully: `hashMap[None] = None`.

2. FIRST PASS - CREATE COPIED NODES AND POPULATE HASH MAP:
   - Initialize a `current` pointer to the `head` of the original linked list.
   - Iterate through the original list using a `while` loop as long as `current` is not `None`:
     a. Create a new `Node` (copy) with the same `val` as the `current` original node: `copy = Node(current.val)`.
     b. Store the mapping from the original node to its copy in the `hashMap`: `hashMap[current] = copy`.
     c. Move `current` to the next node in the original list: `current = current.next`.

3. SECOND PASS - SET NEXT AND RANDOM POINTERS FOR COPIED NODES:
   - Reset `current` back to the `head` of the original linked list.
   - Iterate through the original list again using a `while` loop as long as `current` is not `None`:
     a. Retrieve the corresponding copied node from the `hashMap`: `copy = hashMap[current]`.
     b. Set the `next` pointer of the `copy` node to the copied version of `current.next` (retrieved from `hashMap`): `copy.next = hashMap[current.next]`.
     c. Set the `random` pointer of the `copy` node to the copied version of `current.random` (retrieved from `hashMap`): `copy.random = hashMap[current.random]`.
     d. Move `current` to the next node in the original list: `current = current.next`.

4. RETURN THE HEAD OF THE COPIED LIST:
   - The head of the copied list is the copy of the original `head`, which can be retrieved from the `hashMap`: `return hashMap[head]`.
'''

def copyRandomList(head):
    hashMap = {None : None}
    current = head
    
    while current:
        copy = Node(current.val)
        hashMap[current] = copy
        current = current.next
        
    current = head
    while current:
        copy = hashMap[current]
        copy.next = hashMap[current.next]
        copy.random = hashMap[current.random]
        current = current.next
        
    return hashMap[head]

'''
Time Complexity: O(N), where N is the number of nodes in the linked list.
- The first pass iterates through the original list to create new nodes and populate the hash map, taking O(N) time.
- The second pass iterates through the original list again to set the `next` and `random` pointers of the copied nodes, taking O(N) time.
- Hash map operations (insertion and lookup) take O(1) on average.
- Therefore, the total time complexity is O(N).

Space Complexity: O(N), where N is the number of nodes in the linked list.
- The hash map stores N key-value pairs (original node -> copied node), taking O(N) space.
- The newly created copied list also takes O(N) space.
- Therefore, the total space complexity is O(N).
'''

# Test Cases
head1 = [[7,null],[13,0],[11,4],[10,2],[1,0]]
print(copyRandomList(head1)) # Output: [[7,null],[13,0],[11,4],[10,2],[1,0]]

head2 = [[1,1],[2,1]]
print(copyRandomList(head2)) # Output: [[1,1],[2,1]]

head3 = [[3,null],[3,0],[3,null]]
print(copyRandomList(head3)) # Output: [[3,null],[3,0],[3,null]]

head4 = []
print(copyRandomList(head4)) # Output: []

head5 = [[1,0]]
print(copyRandomList(head5)) # Output: [[1,0]]

head6 = [[1,null]]
print(copyRandomList(head6)) # Output: [[1,null]]

head7 = [[1,null],[2,null],[3,null]]
print(copyRandomList(head7)) # Output: [[1,null],[2,null],[3,null]]

head8 = [[1,2],[2,1],[3,0]]
print(copyRandomList(head8)) # Output: [[1,2],[2,1],[3,0]]

head9 = [[1,4],[2,0],[3,null],[4,2],[5,1]]
print(copyRandomList(head9)) # Output: [[1,4],[2,0],[3,null],[4,2],[5,1]]

head10 = [[10,null],[20,0],[30,1],[40,2],[50,3]]
print(copyRandomList(head10)) # Output: [[10,null],[20,0],[30,1],[40,2],[50,3]]