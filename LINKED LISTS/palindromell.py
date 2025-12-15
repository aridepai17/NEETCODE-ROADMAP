# PALINDROME LINKED LIST

'''
Given the head of a singly linked list, return true if it is a palindrome or false otherwise.
'''


# Extra space solution
def isPalindrome1(head):
    num = []
    current = head
    
    while current:
        num.append(current.val)
        current = current.next
        
    left = 0
    right = len(num) - 1
    
    while left < right:
        if num[left] != num[right]:
            return False
        left += 1
        right -= 1
        
    return True


'''
Time Complexity: O(N)
Let N be the number of nodes in the linked list.
- The first while loop iterates through the linked list once, which takes O(N) time.
- The second while loop iterates half of the number of nodes in the linked list, which is O(N/2) = O(N) time.
- Therefore, the total time complexity is dominated by the first loop, resulting in O(N).

Space Complexity: O(N)
- The `num` list contains all the values of the linked list.
- The size of the `num` list is N, which is the total number of nodes in the linked list.
- Thus, the space complexity is O(N).
'''

'''
Algorithm (No Extra Space Solution):

1. Find the middle of the linked list using the slow and fast pointer approach. When the fast pointer reaches the end, the slow pointer will be at the middle.
2. Reverse the second half of the linked list starting from the slow pointer.
3. Initialize two pointers, `left` at the head of the original list and `right` at the head of the reversed second half.
4. Compare the values of `left` and `right` nodes.
5. If at any point `left.val` is not equal to `right.val`, the linked list is not a palindrome, so return `False`.
6. Move `left` one step forward (`left = left.next`) and `right` one step forward (`right = right.next`).
7. Continue this comparison until `right` becomes `None` (meaning we have traversed the entire reversed second half).
8. If the loop completes, it means all corresponding values matched, so the linked list is a palindrome. Return `True`.
'''

# No Extra Space Solution
def isPalindrome2(head):
    slow = head
    fast = head
    
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        
    prev = None
    while slow:
        front = slow.next
        slow.next = prev
        prev = slow
        slow = front
        
    left = head
    right = prev
    
    while right:
        if left.val != right.val:
            return False
        left = left.next
        right = right.next
        
    return True

'''
Time Complexity: O(N)
Let N be the number of nodes in the linked list.
- Finding the middle of the linked list using slow and fast pointers takes O(N/2) = O(N) time.
- Reversing the second half of the linked list takes O(N/2) = O(N) time.
- Comparing the first half with the reversed second half takes O(N/2) = O(N) time.
- Therefore, the total time complexity is O(N).

Space Complexity: O(1)
- We are only using a few pointers (slow, fast, prev, front, left, right) and not allocating any additional data structures that grow with the input size.
- The reversal of the second half is done in-place, modifying the existing linked list structure.
- Thus, the space complexity is O(1).
'''

# Test Cases
head1 = [1, 2, 2, 1]
print(isPalindrome2(head1)) # Output: True


head2 = [1, 2, 3, 2, 1]
print(isPalindrome2(head2)) # Output: True

head3 = [1, 2, 3, 4, 3, 2, 1]
print(isPalindrome2(head3)) # Output: True

head4 = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 3, 2, 1]
print(isPalindrome2(head4)) # Output: True

head5 = [1, 2, 3, 3, 2, 1]
print(isPalindrome2(head5)) # Output: True

head6 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 8, 7, 6, 5, 4, 3, 2, 1]
print(isPalindrome2(head6)) # Output: True

head7 = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 3, 2, 1, 2]
print(isPalindrome2(head7)) # Output: False

head8 = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 3, 2, 1, 1]
print(isPalindrome2(head8)) # Output: False

head9 = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 3, 2, 1, 2, 3]
print(isPalindrome2(head9)) # Output: False

head10 = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 3, 2, 1, 2, 3, 4]
print(isPalindrome2(head10)) # Output: False