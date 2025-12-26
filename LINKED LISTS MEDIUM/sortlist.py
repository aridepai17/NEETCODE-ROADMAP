# SORT LIST 

'''
Given the head of a linked list, return the list after sorting it in ascending order.
'''

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

'''
ALGORITHM:

This problem can be solved using a merge sort approach for linked lists.
The main idea is to recursively divide the linked list into two halves until single nodes are reached,
then merge these sorted halves back together.

1. BASE CASE:
   - If the list is empty (`head` is None) or has only one node (`head.next` is None), it's already sorted. Return `head`.

2. FIND THE MIDDLE OF THE LINKED LIST:
   - Use the `middle` helper function.
   - Initialize `slow` to `head` and `fast` to `head.next`.
   - Move `slow` one step at a time and `fast` two steps at a time.
   - When `fast` reaches the end (or `fast.next` is None), `slow` will be at the middle of the list.
   - Return `slow`.

3. SPLIT THE LIST INTO TWO HALVES:
   - Call `middle(head)` to get the middle node. Let's call it `right_start_prev`.
   - The second half starts at `right_start_prev.next`. Store this in a temporary variable `temp`.
   - Break the link between the first and second halves: `right_start_prev.next = None`.
   - The first half is `head`.
   - The second half is `temp`.

4. RECURSIVELY SORT THE TWO HALVES:
   - Call `sortList(left)` to sort the first half.
   - Call `sortList(right)` to sort the second half.

5. MERGE THE TWO SORTED HALVES:
   - Use the `merge` helper function.
   - Create a `dummyNode` and a `tail` pointer pointing to `dummyNode`.
   - While both `left` and `right` sublists have nodes:
     - Compare `left.val` and `right.val`.
     - Append the smaller node to `tail.next`.
     - Move the pointer of the appended list forward.
     - Move `tail` forward.
   - If any nodes remain in `left` or ` right` sublists, append them to `tail.next`.
   - Return `dummyNode.next`.
'''

def sortList(head):
    if not head or not head.next:
        return head
    
    def middle(head):
        slow = head
        fast = head.next
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
        return slow
    
    def merge(left, right):
        dummyNode = ListNode()
        tail = dummyNode
        
        while left and right:
            if left.val < right.val:
                tail.next = left
                left = left.next
            else:
                tail.next = right
                right = right.next
            tail = tail.next
            
        if left:
            tail.next = left
        if right:
            tail.next = right
            
        return dummyNode.next
    
    left = head
    right = middle(head)
    temp = right.next
    right.next = None
    right = temp
    
    left = sortList(left)
    right = sortList(right)
    
    return merge(left, right)

'''
Time Complexity: O(N log N), where N is the number of nodes in the linked list.
- The `sortList` function recursively divides the list into two halves until single nodes are reached. This division process takes O(log N) levels.
- At each level of recursion, the `merge` function is called. Merging two lists of total length K takes O(K) time. Since at each level, we merge sublists that collectively cover all N nodes, the merging step at each level takes O(N) time.
- Therefore, the total time complexity is O(N log N).

Space Complexity: O(log N) due to recursion stack.
- The recursion depth for `sortList` is O(log N) because the list is repeatedly halved.
- Each recursive call adds a frame to the call stack.
- The `dummyNode`, `tail`, `left`, `right`, `temp` pointers in the `merge` function consume constant space per call.
- Therefore, the total space complexity is O(log N).
'''

# Test Cases
head1 = [4,2,1,3]
print(sortList(head1)) # Output: [1,2,3,4]

head2 = [-1,5,3,4,0]
print(sortList(head2)) # Output: [-1,0,3,4,5]

head3 = []
print(sortList(head3)) # Output: []

head4 = [1]
print(sortList(head4)) # Output: [1]

head5 = [2,1]
print(sortList(head5)) # Output: [1,2]

head6 = [5,4,3,2,1]
print(sortList(head6)) # Output: [1,2,3,4,5]

head7 = [1,1,1,1,1]
print(sortList(head7)) # Output: [1,1,1,1,1]

head8 = [10,2,8,4,6,1,9,3,7,5]
print(sortList(head8)) # Output: [1,2,3,4,5,6,7,8,9,10]

head9 = [100, 50, 200, 10, 150]
print(sortList(head9)) # Output: [10, 50, 100, 150, 200]

head10 = [7, 3, 9, 1, 5]
print(sortList(head10)) # Output: [1, 3, 5, 7, 9]