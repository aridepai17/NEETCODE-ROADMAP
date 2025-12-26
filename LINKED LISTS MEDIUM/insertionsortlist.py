# INSERTION SORT LIST

'''
Given the head of a singly linked list, sort the list using insertion sort, and return the sorted list's head.
The steps of the insertion sort algorithm:
- Insertion sort iterates, consuming one input element each repetition and growing a sorted output list.
- At each iteration, insertion sort removes one element from the input data, finds the location it belongs within the sorted list and inserts it there.
- It repeats until no input elements remain.
'''

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

'''
Algorithm:

1. Create a `dummyNode` with a value of 0 and set its `next` pointer to the head of the original list.
   This dummy node simplifies insertions at the beginning of the sorted portion.
2. Initialize `prev` to `head` and `current` to `head.next`.
   - `prev` will always point to the last node of the sorted portion.
   - `current` is the node we are trying to insert into the sorted portion.
3. Iterate through the list using a `while` loop as long as `current` is not `None`.
4. Inside the loop:
    a. If `current.val >= prev.val`:
        - The `current` node is already in its correct sorted position relative to `prev`.
        - Move `prev` one step forward to `current`.
        - Move `current` one step forward to `current.next`.
        - Continue to the next iteration.
    b. Else (`current.val < prev.val`):
        - The `current` node needs to be moved to an earlier position in the sorted portion.
        - Store `current.next` in a temporary variable (e.g., `nextNode`) to avoid losing the rest of the list.
        - Initialize a `temp` pointer to `dummyNode`. This `temp` pointer will traverse the sorted portion to find the correct insertion point.
        - Iterate with an inner `while` loop as long as `current.val >= temp.next.val`:
            - Move `temp` one step forward (`temp = temp.next`).
        - Once the inner loop finishes, `temp.next` is the node that `current` should be inserted before.
        - Adjust pointers to insert `current`:
            - `prev.next = nextNode` (remove `current` from its original position).
            - `current.next = temp.next` (link `current` to the node it's inserted before).
            - `temp.next = current` (link `temp` to `current`).
        - Move `current` to `nextNode` (the next unsorted node).
5. After the loop finishes, return `dummyNode.next`, which is the head of the sorted list.
'''

def insertionSortList(head):
    dummyNode = ListNode(0, head)
    prev = head
    current = head.next
    
    while current:
        if current.val >= prev.val:
            prev = current
            current = current.next
            continue
        
        temp = dummyNode
        while current.val >= temp.next.val:
            temp = temp.next
        prev.next = current.next
        current.next = temp.next
        temp.next = current
        current = prev.next
        
    return dummyNode.next

'''
Time Complexity: O(N^2), where N is the number of nodes in the linked list.
- In the worst case (e.g., a reverse-sorted list), for each node, we might traverse from the beginning of the sorted portion to find its correct insertion position.
- The outer `while current` loop runs N-1 times (for each node starting from the second).
- Inside this loop, if `current.val < prev.val`, the inner `while temp` loop might traverse up to `i` nodes (where `i` is the current index).
- This leads to a quadratic time complexity, similar to array-based insertion sort.

Space Complexity: O(1).
- We only use a few pointers (`dummyNode`, `prev`, `current`, `temp`) which consume constant extra space.
- The sorting is done in-place by rearranging the existing nodes.
'''

# Test Cases
head1 = [4,2,1,3]
print(insertionSortList(head1)) # Output: [1,2,3,4]

head2 = [-1,5,3,4,0]
print(insertionSortList(head2)) # Output: [-1,0,3,4,5]

head3 = []
print(insertionSortList(head3)) # Output: []

head4 = [1]
print(insertionSortList(head4)) # Output: [1]

head5 = [2,1]
print(insertionSortList(head5)) # Output: [1,2]

head6 = [5,4,3,2,1]
print(insertionSortList(head6)) # Output: [1,2,3,4,5]

head7 = [1,1,1,1,1]
print(insertionSortList(head7)) # Output: [1,1,1,1,1]

head8 = [10,2,8,4,6,1,9,3,7,5]
print(insertionSortList(head8)) # Output: [1,2,3,4,5,6,7,8,9,10]

head9 = [100, 50, 200, 10, 150]
print(insertionSortList(head9)) # Output: [10, 50, 100, 150, 200]

head10 = [7, 3, 9, 1, 5]
print(insertionSortList(head10)) # Output: [1, 3, 5, 7, 9]