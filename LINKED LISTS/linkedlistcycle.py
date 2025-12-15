# LINKED LIST CYCLE


'''
Given head, the head of a linked list, determine if the linked list has a cycle in it.
There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. 
Internally, pos is used to denote the index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.
Return true if there is a cycle in the linked list. Otherwise, return false.
'''

'''
Algorithm: Floyd's Cycle-Finding Algorithm (Tortoise and Hare)

1. Initialize two pointers, `slow` and `fast`, both pointing to the head of the linked list.
2. Iterate through the list using a `while` loop as long as `fast` and `fast.next` are not None.
3. Inside the loop:
    a. Move `slow` one step forward: `slow = slow.next`.
    b. Move `fast` two steps forward: `fast = fast.next.next`.
    c. If `slow` and `fast` meet (i.e., `slow == fast`), it means a cycle is detected, so return `True`.
4. If the loop finishes without `slow` and `fast` meeting, it means there is no cycle, so return `False`.
'''

def hasCycle(head):
    slow = head
    fast = head
    
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        
        if slow == fast:
            return True
        
    return False

'''
Time Complexity: O(N), where N is the number of nodes in the linked list.
In the worst case, the fast pointer traverses the entire list, and the slow pointer traverses half of it.

Space Complexity: O(1), as we are only using two pointers (slow and fast) and not allocating any additional data structures.
'''

# Test Cases
head1 = [3,2,0,-4], pos1 = 1
print(hasCycle(head1)) # Output: True

head2 = [1,2], pos2 = 0
print(hasCycle(head2)) # Output: True

head3 = [1], pos3 = -1
print(hasCycle(head3)) # Output: False

head4 = [], pos4 = -1
print(hasCycle(head4)) # Output: False

head5 = [1,2,3,4,5], pos5 = -1
print(hasCycle(head5)) # Output: False

head6 = [1,2,3,4,5], pos6 = 2
print(hasCycle(head6)) # Output: True

head7 = [1,2,3,4,5,6,7,8,9,10], pos7 = 5
print(hasCycle(head7)) # Output: True

head8 = [1,2,3,4,5,6,7,8,9,10], pos8 = -1
print(hasCycle(head8)) # Output: False

head9 = [1,2,3,4,5,6,7,8,9,10], pos9 = 9
print(hasCycle(head9)) # Output: True