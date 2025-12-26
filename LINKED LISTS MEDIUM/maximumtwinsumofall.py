# MAXIMUM TWIN SUM OF A LINKED LIST

'''
In a linked list of size n, where n is even, the ith node (0-indexed) of the linked list is known as the twin of the (n-1-i)th node, if 0 <= i <= (n / 2) - 1.
For example, if n = 4, then node 0 is the twin of node 3, and node 1 is the twin of node 2. These are the only nodes with twins for n = 4.
The twin sum is defined as the sum of a node and its twin.
Given the head of a linked list with even length, return the maximum twin sum of the linked list.
'''

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

'''
ALGORITHM:

1. FIND THE MIDDLE OF THE LINKED LIST AND REVERSE THE FIRST HALF:
   - Use two pointers, `slow` and `fast`. `slow` moves one step, `fast` moves two steps.
   - While `fast` and `fast.next` are not None, we are effectively reversing the first half of the list.
   - `prev` will store the head of the reversed first half.
   - `slow` will eventually point to the head of the second half.
   - Example: For `1->2->3->4->5->6`:
     - Initial: `slow=1`, `fast=1`, `prev=None`
     - Iter 1: `fast=3`, `temp=2`, `slow.next=None`, `prev=1`, `slow=2` (List: `None<-1`, `2->3->4->5->6`)
     - Iter 2: `fast=5`, `temp=3`, `slow.next=1`, `prev=2`, `slow=3` (List: `None<-1<-2`, `3->4->5->6`)
     - Loop ends. `prev` is `2` (head of reversed first half), `slow` is `3` (head of second half).

2. CALCULATE TWIN SUMS:
   - Initialize `result = 0`.
   - Iterate while `slow` is not None (meaning we are traversing the second half and the reversed first half simultaneously).
   - In each iteration:
     a. Calculate the twin sum: `prev.val + slow.val`.
     b. Update `result = max(result, prev.val + slow.val)`.
     c. Move `prev` to `prev.next` (to traverse the reversed first half).
     d. Move `slow` to `slow.next` (to traverse the second half).

3. RETURN `result`.
'''

def maximumTwinSum(head):
    slow = head
    fast = head
    prev = None
    
    while fast and fast.next:
        fast = fast.next.next
        temp = slow.next
        slow.next = prev
        prev = slow
        slow = temp
        
    result = 0
    while slow:
        result = max(result, prev.val + slow.val)
        prev = prev.next
        slow = slow.next
        
    return result

'''
Time Complexity: O(N), where N is the number of nodes in the linked list.
- The first `while` loop (reversing the first half) iterates N/2 times. In each iteration, a constant number of operations are performed.
- The second `while` loop (calculating twin sums) iterates N/2 times. In each iteration, a constant number of operations are performed.
- Therefore, the total time complexity is O(N).

Space Complexity: O(1).
- We are performing the reversal in-place and only using a few pointers (`slow`, `fast`, `prev`, `temp`, `result`).
- These pointers consume constant extra space.
'''

# Test Cases
head1 = [5,4,2,1]
print(maximumTwinSum(head1)) # Output: 6

head2 = [4,2,2,3]
print(maximumTwinSum(head2)) # Output: 7

head3 = [1,100000]
print(maximumTwinSum(head3)) # Output: 100001

head4 = [1,2,3,4,5,6]
print(maximumTwinSum(head4)) # Output: 7

head5 = [1,2,3,4]
print(maximumTwinSum(head5)) # Output: 5

head6 = [10,20,30,40,50,60]
print(maximumTwinSum(head6)) # Output: 70

head7 = [1,2,10,20]
print(maximumTwinSum(head7)) # Output: 22

head8 = [1,2,3,10,9,8]
print(maximumTwinSum(head8)) # Output: 13

head9 = [1,5,2,8,3,7]
print(maximumTwinSum(head9)) # Output: 13

head10 = [100,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23]
print(maximumTwinSum(head10)) # Output: 23