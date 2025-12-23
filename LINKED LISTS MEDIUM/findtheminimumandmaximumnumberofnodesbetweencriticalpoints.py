# FIND THE MINIMUM AND MAXIMUM NUMBER OF NODES BETWEEN CRITICAL POINTS

'''
A critical point in a linked list is defined as either a local maxima or a local minima.
A node is a local maxima if the current node has a value strictly greater than the previous node and the next node.
A node is a local minima if the current node has a value strictly smaller than the previous node and the next node.
Note that a node can only be a local maxima/minima if there exists both a previous node and a next node.
Given a linked list head, return an array of length 2 containing [minDistance, maxDistance] where minDistance is the minimum distance between any two distinct critical points and maxDistance is the maximum distance between any two distinct critical points. 
If there are fewer than two critical points, return [-1, -1].
'''

'''
ALGORITHM:

1. Define a helper function `critical(prev, current, front)`:
    - This function takes three `ListNode` objects: `prev`, `current`, and `front`.
    - It returns `True` if `current` is a critical point (local maxima or local minima), `False` otherwise.
    - A node is a local maxima if `prev.val < current.val > front.val`.
    - A node is a local minima if `prev.val > current.val < front.val`.

2. Initialize pointers:
    - `prev = head`
    - `current = head.next`
    - `front = current.next`
    - These pointers will traverse the linked list, always maintaining a window of three consecutive nodes.

3. Initialize distance variables:
    - `minDistance = float("inf")` (to store the minimum distance between critical points)
    - `maxDistance = float("-inf")` (to store the maximum distance between critical points)

4. Initialize index variables:
    - `prevCriticalIndex = 0` (to store the index of the most recently found critical point)
    - `firstCriticalIndex = 0` (to store the index of the very first critical point found)
    - `i = 1` (to keep track of the current node's index, starting from the second node as `current` starts at `head.next`)

5. Traverse the linked list using a `while` loop:
    - The loop continues as long as `front` is not `None` (ensuring there are always three nodes to check for criticality).

6. Inside the loop, for each `current` node:
    - Call `critical(prev, current, front)` to check if `current` is a critical point.
    - If `current` is a critical point:
        - If `firstCriticalIndex` is not 0 (meaning at least one critical point has been found before):
            - Update `maxDistance = i - firstCriticalIndex` (the distance from the first critical point to the current one).
            - Update `minDistance = min(minDistance, i - prevCriticalIndex
'''

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def findMinAndMaxDistance(head):
    def critical(prev, current, front):
        return (
            prev.val > current.val < front.val or 
            prev.val < current.val > front.val
        )
        
    prev = head
    current = head.next
    front = current.next
    
    minDistance = float("inf")
    maxDistance = float("-inf")
    
    prevCriticalIndex = 0
    firstCriticalIndex = 0
    i = 1 # Index of current
    
    while front:
        if critical(prev, current, front):
            if firstCriticalIndex:
                maxDistance = i - firstCriticalIndex
                minDistance = min(minDistance, i - prevCriticalIndex)
            else:
                firstCriticalIndex = i
            prevCriticalIndex = i
            
        prev = current
        current = front
        front = front.next
        i += 1
        
    if minDistance == float("inf"):
        minDistance = -1
        maxDistance = -1
        
    return [minDistance, maxDistance]

'''
Time Complexity: O(N), where N is the number of nodes in the linked list.
- We iterate through the linked list once. Each node is visited a constant number of times (once by the outer loop, and potentially once by the inner loop).
- The operations inside the loops (assignments, additions) are all constant time.
- Therefore, the total time complexity is O(N).

Space Complexity: O(1).
- We are performing the modifications in-place, reusing the existing nodes.
- Only a few pointers (`current`, `node`) are used, which consume constant extra space.
'''

# Test Cases
head1 = [3,1]
print(findMinAndMaxDistance(head1)) # Output: [-1, -1]

head2 = [1,3,2,2,3,2,2,2,7]
print(findMinAndMaxDistance(head2)) # Output: [3, 3]

head3 = [5,3,1,2,5,1,2]
print(findMinAndMaxDistance(head3)) # Output: [1, 5]

head4 = [1,2,3,4,5]
print(findMinAndMaxDistance(head4)) # Output: [-1, -1]

head5 = [5,4,3,2,1]
print(findMinAndMaxDistance(head5)) # Output: [-1, -1]

head6 = [1,5,2,6,3,7,4]
print(findMinAndMaxDistance(head6)) # Output: [2, 4]

head7 = [1,2,1,2,1,2,1]
print(findMinAndMaxDistance(head7)) # Output: [2, 6]

head8 = [1,1,1,1,1]
print(findMinAndMaxDistance(head8)) # Output: [-1, -1]

head9 = [1,3,2,4,3,5,4,6]
print(findMinAndMaxDistance(head9)) # Output: [2, 6]

head10 = [2,1,2,1,2]
print(findMinAndMaxDistance(head10)) # Output: [2, 4]