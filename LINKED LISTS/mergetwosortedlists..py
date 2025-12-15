# MERGE TWO SORTED LISTS

'''
You are given the heads of two sorted linked lists list1 and list2.
Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.
Return the head of the merged linked list.
'''

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeTwoLists(l1, l2):
    dummyNode = ListNode()
    tail = dummyNode
    
    while l1 and l2:
        if l1.val < l2.val:
            tail.next = l1
            l1 = l1.next
        else:
            tail.next = l2
            l2 = l2.next
        tail = tail.next
        
    if l1:
        tail.next = l1
    elif l2:
        tail.next = l2
        
    return dummyNode.next

'''
Time complexity: O(m + n), where m and n are the lengths of list1 and list2 respectively.
In the worst case, we traverse both lists once, so the time complexity is O(m + n).

Space complexity: O(1), as we are only using a few extra pointers and not creating new nodes proportional to the input size.
'''

# Test Cases
l1 = [1,2,4], l2 = [1,3,4]
print(mergeTwoLists(l1, l2)) # Output: [1, 1, 2, 3, 4, 4]


l1 = [], l2 = []
print(mergeTwoLists(l1, l2)) # Output: []

l1 = [0], l2 = []
print(mergeTwoLists(l1, l2)) # Output: [0]

l1 = [], l2 = [0]
print(mergeTwoLists(l1, l2)) # Output: [0]

l1 = [1], l2 = [0]
print(mergeTwoLists(l1, l2)) # Output: [0, 1]

l1 = [0], l2 = [1]
print(mergeTwoLists(l1, l2)) # Output: [0, 1]

l1 = [1,3], l2 = [2]
print(mergeTwoLists(l1, l2)) # Output: [1, 2, 3]

l1 = [2], l2 = [1,3]
print(mergeTwoLists(l1, l2)) # Output: [1, 2, 3]

l1 = [1,3,5], l2 = [2,4]
print(mergeTwoLists(l1, l2)) # Output: [1, 2, 3, 4, 5]

l1 = [1,3,5], l2 = [2,4,6]
print(mergeTwoLists(l1, l2)) # Output: [1, 2, 3, 4, 5, 6]