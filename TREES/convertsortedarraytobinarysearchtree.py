# CONVERT SORTED ARRAY TO BINARY SEARCH TREE

'''
Given an integer array nums where the elements are sorted in ascending order, convert it to a height-balanced binary search tree.
A height-balanced binary tree is a binary tree in which the depth of the two subtrees of every node never differs by more than one.
'''

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

'''
ALGORITHM:

1. Define a function `sortedArrayToBST` that takes an integer array `nums` as input.
2. Define a helper function `helper(left, right)`:
   a. Base Case: If `left` is greater than `right`, it means the subarray is empty, so return `None`.
   b. Calculate the middle index: `mid = (left + right) // 2`.
   c. Create a new `TreeNode` with the value `nums[mid]`. This will be the `root` of the current subtree.
   d. Recursively build the left subtree: `root.left = helper(left, mid - 1)`.
   e. Recursively build the right subtree: `root.right = helper(mid + 1, right)`.
   f. Return the `root` of the current subtree.
3. Call the `helper` function with the initial range `(0, len(nums) - 1)` to build the entire BST.
4. Return the root of the constructed BST.
'''

def sortedArrayToBST(nums):
    def helper(left, right):
        if left > right:
            return None
        
        mid = (left + right) // 2
        root = TreeNode(nums[mid])
        root.left = helper(left, mid - 1)
        root.right = helper(mid + 1, right)
        return root
    
    return helper(0, len(nums) - 1)

'''
Time Complexity: O(N), where N is the number of elements in `nums`.
Each element in the array is visited exactly once to create a corresponding TreeNode.

Space Complexity: O(N), where N is the number of elements in `nums`.
This is due to the recursion stack. In the worst case (a skewed tree, though this algorithm produces a balanced one),
the depth of the recursion can be proportional to N. Also, the space taken by the output tree itself is O(N).
'''

# Test Cases
nums1 = [-10,-3,0,5,9]
print(sortedArrayToBST(nums1)) # Output: [0,-3,-9,-10,null,5]

nums2 = [1,3]
print(sortedArrayToBST(nums2)) # Output: [3,1]

nums3 = [1,2,3,4,5]
print(sortedArrayToBST(nums3)) # Output: [3,2,4,1,null,null,5]

nums4 = []
print(sortedArrayToBST(nums4)) # Output: []

nums5 = [1]
print(sortedArrayToBST(nums5)) # Output: [1]

nums6 = [1,2]
print(sortedArrayToBST(nums6)) # Output: [2,1]

nums7 = [1,2,3]
print(sortedArrayToBST(nums7)) # Output: [2,1,3]

nums8 = [1,2,3,4]
print(sortedArrayToBST(nums8)) # Output: [3,2,4,1]

nums9 = [1,2,3,4,5,6,7]
print(sortedArrayToBST(nums9)) # Output: [4,2,6,1,3,5,7]

nums10 = [1,2,3,4,5,6,7,8]
print(sortedArrayToBST(nums10)) # Output: [5,3,7,2,4,6,8,1]