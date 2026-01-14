# KTH LARGEST SUM IN A BINARY TREE

'''
You are given the root of a binary tree and a positive integer k.
The level sum in the tree is the sum of the values of the nodes that are on the same level.
Return the kth largest level sum in the tree (not necessarily distinct). If there are fewer than k levels in the tree, return -1.
Note that two nodes are on the same level if they have the same distance from the root.
'''

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

'''
ALGORITHM:

1. Initialize a `queue` using `collections.deque` and add the `root` node to it.
2. Initialize a `minHeap` (min-priority queue) using `heapq` to store the `k` largest level sums.
3. While the `queue` is not empty:
   a. Initialize `levelSum` to `0`.
   b. Get the `qLength` (length of the queue), which represents the number of nodes at the current level.
   c. Iterate `qLength` times (to process all nodes at the current level):
      i. Dequeue a `node` from the left of the `queue`.
      ii. Add `node.val` to `levelSum`.
      iii. If `node.left` exists, enqueue it to the right of the `queue`.
      iv. If `node.right` exists, enqueue it to the right of the `queue`.
   d. After processing all nodes at the current level, push `levelSum` onto the `minHeap`.
   e. If the size of `minHeap` becomes greater than `k`, pop the smallest element from `minHeap` (to maintain only the `k` largest sums).
4. After the `queue` is empty (all levels have been processed):
   a. If the size of `minHeap` is less than `k`, return `-1`.
   b. Otherwise, return the smallest element from `minHeap` (which will be the k-th largest sum).
'''

import collections
import heapq

def kthLargestLevelSum(root, k):
    queue = collections.deque([root])
    minHeap = []
    
    while queue:
        levelSum = 0
        qLength = len(queue)
        for i in range(qLength):
            node = queue.popleft()
            levelSum += node.val
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
                
        heapq.heappush(minHeap, levelSum)
        
        if len(minHeap) > k:
            heapq.heappop(minHeap)
            
    return -1 if len(minHeap) < k else heapq.heappop(minHeap)

'''
Time Complexity: O(N log K), where N is the number of nodes in the binary tree and K is the given integer.
- We perform a BFS traversal, visiting each of the N nodes exactly once. This part is O(N).
- For each level, we calculate its sum. There are at most N levels (in a skewed tree).
- We push each level sum into a min-heap. A push operation takes O(log K) time if the heap size is maintained at K.
- We perform at most N push operations.
- Finally, we pop the smallest element from the heap, which takes O(log K) time.
Therefore, the dominant factor is N * log K.

Space Complexity: O(W + K), where W is the maximum width of the binary tree and K is the given integer.
- The `queue` stores nodes for the current level, which can be up to O(W) in the worst case (for a complete binary tree, W can be N/2).
- The `minHeap` stores at most K level sums, so O(K) space.
'''

# Test Cases
root1 = [5,8,9,2,1,3,7,4,6], k1 = 2
print(kthLargestLevelSum(root1, k1)) # Output: 13

root2 = [1,2,null,3], k2 = 1
print(kthLargestLevelSum(root2, k2)) # Output: 3

root3 = [1], k3 = 1
print(kthLargestLevelSum(root3, k3)) # Output: 1

root4 = [1,2,3,4,5,6,7], k4 = 3
print(kthLargestLevelSum(root4, k4)) # Output: 6

root5 = [1,2,3,4,5,6,7], k5 = 4
print(kthLargestLevelSum(root5, k5)) # Output: -1

root6 = [10,20,30,40,50,60,70,80,90,100], k6 = 1
print(kthLargestLevelSum(root6, k6)) # Output: 210

root7 = [10,20,30,40,50,60,70,80,90,100], k7 = 2
print(kthLargestLevelSum(root7, k7)) # Output: 60

root8 = [10,20,30,40,50,60,70,80,90,100], k8 = 3
print(kthLargestLevelSum(root8, k8)) # Output: 30

root9 = [10,20,30,40,50,60,70,80,90,100], k9 = 4
print(kthLargestLevelSum(root9, k9)) # Output: 10

root10 = [10,20,30,40,50,60,70,80,90,100], k10 = 5
print(kthLargestLevelSum(root10, k10)) # Output: 50