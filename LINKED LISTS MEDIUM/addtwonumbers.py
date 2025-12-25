# ADD TWO NUMBERS

'''
You are given two non-empty linked lists representing two non-negative integers. 
The digits are stored in reverse order, and each of their nodes contains a single digit. 
Add the two numbers and return the sum as a linked list.
You may assume the two numbers do not contain any leading zero, except the number 0 itself.
'''

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

'''
Algorithm:

1. Initialize a `dummyNode` with a value of 0. This node will serve as the head of the new linked list that stores the sum.
2. Initialize a `current` pointer to `dummyNode`. This pointer will be used to build the new linked list.
3. Initialize a `carry` variable to 0. This will store any carry-over from adding digits.
4. Loop while there are still nodes in `l1`, `l2`, or if there's a `carry`:
   a. Get the value of the current node in `l1` (if `l1` exists, otherwise 0). Store it in `v1`.
   b. Get the value of the current node in `l2` (if `l2` exists, otherwise 0). Store it in `v2`.
   c. Calculate the `value` by adding `v1`, `v2`, and `carry`.
   d. Update `carry` to `value // 10` (integer division to get the carry-over).
   e. Update `value` to `value % 10` (modulo to get the current digit).
   f. Create a new `ListNode` with the calculated `value` and set `current.next` to this new node.
   g. Move `current` to the newly created node (`current = current.next`).
   h. Move `l1` to its next node if it exists, otherwise set `l1` to `None`.
   i. Move `l2` to its next node if it exists, otherwise set `l2` to `None`.
5. After the loop finishes, return `dummyNode.next`, which is the head of the linked list representing the sum.
'''

def addTwoNumbers(l1, l2):
    dummyNode = ListNode()
    current = dummyNode
    carry = 0
    
    while l1 or l2 or carry:
        v1 = l1.val if l1 else 0
        v2 = l2.val if l2 else 0
        value = v1 + v2 + carry
        carry = value // 10
        value %= 10
        current.next = ListNode(value)
        current = current.next
        l1 = l1.next if l1 else None
        l2 = l2.next if l2 else None
    
    return dummyNode.next

'''
Time Complexity: O(max(M, N)), where M and N are the lengths of the two input linked lists `l1` and `l2` respectively.
- The `while` loop continues as long as there are nodes in either `l1` or `l2`, or if there's a `carry`.
- In each iteration, we process one node from `l1` (if available) and one node from `l2` (if available).
- Therefore, the number of iterations is proportional to the length of the longer list.

Space Complexity: O(max(M, N)).
- The new linked list created to store the sum will have at most `max(M, N) + 1` nodes (in case of an extra carry).
- This new list consumes space proportional to its length.
- The `dummyNode`, `current`, `l1`, `l2`, `carry`, `v1`, `v2`, `value` variables consume constant extra space.
- Therefore, the total space complexity is O(max(M, N)).
'''

# Test Cases
l1 = [2,4,3], l2 = [5,6,4]
print(addTwoNumbers(l1, l2)) # Output: [7,0,8]

l1 = [0], l2 = [0]
print(addTwoNumbers(l1, l2)) # Output: [0]

l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
print(addTwoNumbers(l1, l2)) # Output: [8,9,9,9,0,0,0,1]

l1 = [1], l2 = [9,9]
print(addTwoNumbers(l1, l2)) # Output: [0,0,1]

l1 = [5], l2 = [5]
print(addTwoNumbers(l1, l2)) # Output: [0,1]

l1 = [1,8], l2 = [0]
print(addTwoNumbers(l1, l2)) # Output: [1,8]

l1 = [7,2,4,3], l2 = [5,6,4]
print(addTwoNumbers(l1, l2)) # Output: [2,9,8,3]

l1 = [2,4,9], l2 = [5,6,4,9]
print(addTwoNumbers(l1, l2)) # Output: [7,0,4,0,1]

l1 = [9], l2 = [1]
print(addTwoNumbers(l1, l2)) # Output: [0,1]

l1 = [8,9,9], l2 = [2]
print(addTwoNumbers(l1, l2)) # Output: [0,0,0,1]