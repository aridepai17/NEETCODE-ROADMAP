# MERGE IN BETWEEN LINKED LISTS

'''
You are given two linked lists: list1 and list2 of sizes n and m respectively.
Remove list1's nodes from the ath node to the bth node, and put list2 in their place.
Build the result list and return its head.
'''

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
'''
1. FIND THE NODE BEFORE THE REMOVAL SEGMENT:
   - Start from the head of list1
   - Move (a-1) steps to reach the node at position a-1
   - This node will be the connection point before the removal

2. FIND THE NODE AFTER THE REMOVAL SEGMENT:
   - From the previous node, move (b-a+2) steps
   - This reaches the node after position b (the connection point after removal)

3. CONNECT LIST2 TO THE FIRST SEGMENT:
   - Set the next pointer of the node at position a-1 to point to list2's head

4. FIND THE TAIL OF LIST2:
   - Traverse list2 until reaching the last node (where next is None)

5. CONNECT THE TAIL OF LIST2 TO THE REMAINING LIST1:
   - Set the next pointer of list2's tail to point to the node after position b

6. RETURN THE MODIFIED LIST1 HEAD
'''

def mergeInBetween(list1, a, b, list2):
    prev = list1
    for _ in range(a - 1):
        prev = prev.next
        
    current = prev 
    for _ in range(b - a + 2):
        current = current.next
        
    prev.next = list2
    
    tail = list2
    while tail.next:
        tail = tail.next
        
    tail.next = current
    
    return list1

# Test Cases
list1 = [10,1,13,6,9,5], a1 = 3, b1 = 4, list2 = [1000000,1000001,1000002]
print(list1, a1, b1, list2) # Output: [10, 1, 13, 1000000, 1000001, 1000002, 5]


list1 = [1,2,3,4,5], a1 = 2, b1 = 3, list2 = [100,101]
print(list1, a1, b1, list2) # Output: [1, 2, 100, 101, 4, 5]

list1 = [1,2,3,4,5], a1 = 2, b1 = 4, list2 = [100,101]
print(list1, a1, b1, list2) # Output: [1, 2, 100, 101]

list1 = [1,2,3,4,5], a1 = 1, b1 = 4, list2 = [100,101]
print(list1, a1, b1, list2) # Output: [1, 100, 101]

list1 = [1,2,3,4,5], a1 = 1, b1 = 5, list2 = [100,101]
print(list1, a1, b1, list2) # Output: [1, 100, 101]

list1 = [1,2,3,4,5], a1 = 5, b1 = 5, list2 = [100,101]
print(list1, a1, b1, list2) # Output: [1, 2, 3, 4, 5]

list1 = [1,2,3,4,5], a1 = 1, b1 = 1, list2 = [100,101]
print(list1, a1, b1, list2) # Output: [1, 100, 101, 2, 3, 4, 5]

list1 = [1,2,3,4,5], a1 = 3, b1 = 3, list2 = [100,101]
print(list1, a1, b1, list2) # Output: [1, 2, 100, 101, 4, 5]

list1 = [1,2,3,4,5], a1 = 5, b1 = 1, list2 = [100,101]
print(list1, a1, b1, list2) # Output: [1, 2, 3, 4, 5]

list1 = [1,2,3,4,5], a1 = 1, b1 = 5, list2 = []
print(list1, a1, b1, list2) # Output: [1, 2, 3, 4, 5]