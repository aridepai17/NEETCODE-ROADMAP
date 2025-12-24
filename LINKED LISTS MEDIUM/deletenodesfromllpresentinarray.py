# DELETE NDOES FROM LL PRESENT IN ARRAY

'''
You are given an array of integers nums and the head of a linked list.
Return the head of the modified linked list after removing all nodes from the linked list that have a value that exists in nums.
'''

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

'''
Algorithm:

1. Convert the `nums` array into a hash set for efficient O(1) average time lookups.
2. Create a dummy node `dummyNode` and set its `next` pointer to the head of the original linked list.
   This dummy node simplifies handling cases where the head itself needs to be removed.
3. Initialize two pointers: `prev` to `dummyNode` and `current` to `head`.
4. Iterate through the linked list using a `while` loop as long as `current` is not `None`.
5. Inside the loop:
    a. Check if `current.val` exists in the `nums` set.
    b. If `current.val` is in `nums` (meaning it should be removed):
        i. Update `prev.next` to `current.next`. This effectively skips the `current` node, removing it from the list.
    c. Else (if `current.val` is not in `nums`, meaning it should be kept):
        i. Move `prev` one step forward to `current` (i.e., `prev = current`). This ensures `prev` always points to the last *kept* node.
    d. Move `current` one step forward to `current.next` (i.e., `current = current.next`).
6. After the loop finishes, return `dummyNode.next`, which will be the head of the modified linked list.
'''

def modifiedList(nums, head):
    nums = set(nums)
    dummyNode = ListNode(0, head)
    prev = dummyNode
    current = head
    
    while current:
        if current.val in nums:
            prev.next = current.next
        else:
            prev = prev.next
        current = current.next
        
    return dummyNode.next

'''
Time Complexity: O(N + M), where N is the number of nodes in the linked list and M is the number of elements in `nums`.
- Converting `nums` to a set takes O(M) time on average.
- Iterating through the linked list takes O(N) time.
- Checking `current.val in nums` takes O(1) on average for a set.
- Therefore, the total time complexity is O(N + M).

Space Complexity: O(M), where M is the number of elements in `nums`.
- We use a set to store the elements of `nums`, which can take up to O(M) space.
- The `dummyNode`, `prev`, and `current` pointers consume constant extra space.
- Therefore, the space complexity is O(M).
'''

# Test Cases
nums1 = [1,2,3], head1 = [1,2,3,4,5]
print(modifiedList(nums1, head1)) # Output: [4, 5]

nums2 = [1], head2 = [1,1,1,2,3,4]
print(modifiedList(nums2, head2)) # Output: [2, 3, 4]

nums3 = [5], head3 = [1,2,3,4,5]
print(modifiedList(nums3, head3)) # Output: [1, 2, 3, 4]

nums4 = [1,2,3,4,5], head4 = [1,2,3,4,5]
print(modifiedList(nums4, head4)) # Output: []

nums5 = [10,20], head5 = [1,5,10,15,20,25]
print(modifiedList(nums5, head5)) # Output: [1, 5, 15, 25]

nums6 = [100], head6 = [100,200,300]
print(modifiedList(nums6, head6)) # Output: [200, 300]

nums7 = [1,3,5], head7 = [2,4,6,8]
print(modifiedList(nums7, head7)) # Output: [2, 4, 6, 8]

nums8 = [], head8 = [1,2,3,4,5]
print(modifiedList(nums8, head8)) # Output: [1, 2, 3, 4, 5]

nums9 = [0], head9 = [0,0,0,1,2,3]
print(modifiedList(nums9, head9)) # Output: [1, 2, 3]

nums10 = [7,8,9], head10 = [1,2,3,4,5,6,7,8,9,10]
print(modifiedList(nums10, head10)) # Output: [1, 2, 3, 4, 5, 6, 10]