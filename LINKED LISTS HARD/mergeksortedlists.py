# MERGE K SORTED LISTS

'''
You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.
Merge all the linked-lists into one sorted linked-list and return it.
'''

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

'''
ALGORITHM:

This problem can be solved using a divide and conquer approach, similar to merge sort.
The main idea is to repeatedly merge pairs of linked lists until only one sorted linked list remains.

1. BASE CASE:
   - If the `lists` array is empty or contains no lists, return `None`.

2. MERGE PAIRS OF LISTS:
   - Use a `while` loop that continues as long as there is more than one list in the `lists` array.
   - Inside the loop:
     a. Create an empty list called `mergedLists` to store the results of merging pairs.
     b. Iterate through the `lists` array with a step of 2 using a `for` loop (e.g., `for i in range(0, len(lists), 2)`).
     c. Get the first list of the pair: `l1 = lists[i]`.
     d. Get the second list of the pair: `l2 = lists[i + 1]` if `i + 1` is within the bounds of `lists`, otherwise `None`.
     e. Call a helper function `mergeList(l1, l2)` to merge these two lists.
     f. Append the result of `mergeList` to `mergedLists`.
   - After the `for` loop, update `lists = mergedLists`. This replaces the original `lists` with the newly merged pairs, effectively reducing the number of lists by half in each iteration.

3. MERGE LIST HELPER FUNCTION (`mergeList(l1, l2)`):
   - This function takes two sorted linked lists, `l1` and `l2`, and merges them into a single sorted linked list.
   - Create a `dummyNode` with a value of 0. This will be the head of the merged list.
   - Initialize a `tail` pointer to `dummyNode`. This pointer will be used to append nodes to the merged list.
   - Iterate using a `while` loop as long as both `l1` and `l2` are not `None`:
     a. Compare `l1.val` and `l2.val`.     b. Append the smaller node to `tail.next`.
     c. Move the pointer of the appended list forward.
     d. Move `tail` forward.
   - If any nodes remain in `l1` or `l2`, append them to `tail.next`.
   - Return `dummyNode.next`.
'''

def mergeKLists(lists):
    def mergeList(l1, l2):
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
        if l2:
            tail.next = l2
            
        return dummyNode.next 
    
    if not lists or len(lists) == 0:
        return None
    
    while len(lists) > 1:
        mergedLists = []
        for i in range(0, len(lists), 2):
            l1 = lists[i]
            l2 = lists[i + 1] if (i + 1) < len(lists) else None
            mergedLists.append(mergeList(l1, l2))
        lists = mergedLists
        
    return lists[0]

'''
Time Complexity: O(N log k) where N is the total number of nodes across all linked lists and k is the number of linked lists.
In each step of the while loop, we merge pairs of lists. There are log k levels of merging.
In each level, we traverse all N nodes once.

Space Complexity: O(1) if we consider the output list not part of the space complexity, as we are reusing existing nodes.
If we consider the recursion stack for mergeList (though it's iterative here) or the `mergedLists` array,
the space complexity would be O(k) in the worst case for `mergedLists` (when k is odd and one list is left alone).
However, since we are modifying the `lists` array in place (conceptually, by reassigning it), and `mergedLists`
temporarily holds at most k/2 lists, it's often considered O(1) auxiliary space if we don't count the output.
If we count the space for the new merged lists created, it would be O(N).
'''

# Test Cases
lists1 = [[1,4,5],[1,3,4],[2,6]]
print(mergeKLists(lists1)) # Output: [1,1,2,3,4,4,5,6]

lists2 = []
print(mergeKLists(lists2)) # Output: []

lists3 = [[]]
print(mergeKLists(lists3)) # Output: []

lists4 = [[1]]
print(mergeKLists(lists4)) # Output: [1]

lists5 = [[1,2,3],[4,5,6],[7,8,9]]
print(mergeKLists(lists5)) # Output: [1,2,3,4,5,6,7,8,9]

lists6 = [[], [1]]
print(mergeKLists(lists6)) # Output: [1]

lists7 = [[10, 20], [1, 5], [15, 25]]
print(mergeKLists(lists7)) # Output: [1, 5, 10, 15, 20, 25]

lists8 = [[-1, 0, 1], [-2, 5, 10], [-5, -3, 2]]
print(mergeKLists(lists8)) # Output: [-5, -3, -2, -1, 0, 1, 2, 5, 10]

lists9 = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]
print(mergeKLists(lists9)) # Output: [1, 1, 1, 1, 1, 1, 1, 1, 1]

lists10 = [[], [], []]
print(mergeKLists(lists10)) # Output: []