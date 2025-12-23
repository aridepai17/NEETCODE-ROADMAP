# INTERSECTION OF TWO LINKED LISTS

'''
Given the heads of two singly linked-lists headA and headB, return the node at which the two lists intersect. 
If the two linked lists have no intersection at all, return null.
'''

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

'''
Algorithm:

1. Initialize two pointers, `l1` and `l2`, to `headA` and `headB` respectively.
2. Iterate using a `while` loop until `l1` and `l2` are the same.
3. Inside the loop:
    a. If `l1` is None, set `l1` to `headB`. Otherwise, move `l1` to `l1.next`.
    b. If `l2` is None, set `l2` to `headA`. Otherwise, move `l2` to `l2.next`.
4. When the loop terminates, `l1` (and `l2`) will be pointing to the intersection node, or None if no intersection exists.
5. Return `l1`.

This algorithm works by effectively concatenating `listB` to `listA` (for pointer `l1`) and `listA` to `listB` (for pointer `l2`).
If an intersection exists, both pointers will travel the same total distance (length of A + length of B - length of intersection segment) before meeting at the intersection point.
If no intersection exists, both pointers will eventually become None simultaneously after traversing both lists, and the loop will terminate, returning None.
'''

def getIntersectionNode(headA, headB):
    l1 = headA
    l2 = headB
    
    while l1 != l2:
        l1 = l1.next if l1 else headB
        l2 = l2.next if l2 else headA
        
    return l1

'''
Time Complexity: O(M + N), where M and N are the lengths of listA and listB respectively.
- In the worst case, both pointers traverse both lists. For example, if there's no intersection, l1 will traverse listA then listB, and l2 will traverse listB then listA.
- The total distance covered by each pointer before they meet (or both become None) is at most M + N.

Space Complexity: O(1), as we are only using two pointers (l1 and l2) and not allocating any additional data structures.
'''

# Test Cases
intersectVal1 = 8, listA1 = [4,1,8,4,5], listB1 = [5,6,1,8,4,5], skipA1 = 2, skipB1 = 3
print(getIntersectionNode(headA1, headB1)) # Output: node with value 8


intersectVal2 = 2, listA2 = [0,9,1], listB2 = [3], skipA2 = 0, skipB2 = 0
print(getIntersectionNode(headA2, headB2)) # Output: node with value 2

intersectVal3 = 0, listA3 = [7,0,8], listB3 = [7,0,1], skipA3 = 0, skipB3 = 2
print(getIntersectionNode(headA3, headB3)) # Output: node with value 0

intersectVal4 = 6, listA4 = [6,5,4,3,2,1], listB4 = [6,5,4,3,2,1], skipA4 = 0, skipB4 = 0
print(getIntersectionNode(headA4, headB4)) # Output: node with value 6

intersectVal5 = 1, listA5 = [1], listB5 = [1], skipA5 = 0, skipB5 = 0
print(getIntersectionNode(headA5, headB5)) # Output: node with value 1

intersectVal6 = 10, listA6 = [1,2,3,4,5], listB6 = [6,7,8,9,10], skipA6 = 3, skipB6 = 2
print(getIntersectionNode(headA6, headB6)) # Output: node with value 10

intersectVal7 = 1, listA7 = [1,2,3,4,5], listB7 = [6,7,8,9,10], skipA7 = 3, skipB7 = 10
print(getIntersectionNode(headA7, headB7)) # Output: node with value 1

intersectVal8 = 1, listA8 = [1,2,3,4,5], listB8 = [6,7,8,9,10], skipA8 = 10, skipB8 = 3
print(getIntersectionNode(headA8, headB8)) # Output: node with value 1

intersectVal9 = 1, listA9 = [1,2,3,4,5,6], listB9 = [7,8,9,10,11,1], skipA9 = 0, skipB9 = 6
print(getIntersectionNode(headA9, headB9)) # Output: node with value 1

intersectVal10 = 1, listA10 = [1,2,3,4,5,6], listB10 = [7,8,9,10,11,1], skipA10 = 6, skipB10 = 0
print(getIntersectionNode(headA10, headB10)) # Output: node with value 1