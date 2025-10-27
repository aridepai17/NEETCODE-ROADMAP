# REMOVE K DIGITS

'''
Given string num representing a non-negative integer num, and an integer k, 
return the smallest possible integer after removing k digits from num.
'''

def removeKdigits(num, k):
    stack = []
    
    for char in num:
        while k > 0 and stack and stack[-1] > char:
            k -= 1
            stack.pop()
        stack.append(char)
        
    stack = stack[:len(stack) - k]
    result = "".join(stack)
    result = result.lstrip("0")
    
    return result or "0"

'''
Time Complexity: O(N), where N is the length of the input string `num`.
- We iterate through each digit of the input string `num` exactly once.
- For each digit, we perform a series of stack operations. The `while` loop might seem like it could lead to a higher complexity, but it's important to note that each digit is pushed onto the stack at most once and popped from the stack at most once.
- Therefore, the total number of stack operations (push and pop) across the entire execution is proportional to N. This is an amortized O(1) time for each digit in the input string.
- The final steps, such as slicing the stack (`stack[:len(stack) - k]`), joining the stack into a string (`"".join(stack)`), and converting the string to an integer and back, all take O(N) time in the worst case.
- Thus, the overall time complexity is dominated by the single pass through the input string, resulting in O(N).

Space Complexity: O(N)
- We use a `stack` to store the digits of the result.
- In the worst-case scenario, where no digits are removed during the iteration (e.g., `num` is "12345" and `k` is small), the stack can grow to hold all N digits of the input string.
- Therefore, the space required is proportional to the length of the input string, making the space complexity O(N).
'''

# Test Cases
num1, k1 = "1432219", 3
print(removeKdigits(num1, k1)) # Output: "1219"

num2, k2 = "10200", 1
print(removeKdigits(num2, k2)) # Output: "200"

num3, k3 = "10", 2
print(removeKdigits(num3, k3)) # Output: "0"

num4, k4 = "9", 1
print(removeKdigits(num4, k4)) # Output: "0"

num5, k5 = "12345", 0
print(removeKdigits(num5, k5)) # Output: "12345"

num6, k6 = "12345", 5
print(removeKdigits(num6, k6)) # Output: "0"

num7, k7 = "112", 1
print(removeKdigits(num7, k7)) # Output: "11"

num8, k8 = "54321", 2
print(removeKdigits(num8, k8)) # Output: "321"

num9, k9 = "1234567890", 9
print(removeKdigits(num9, k9)) # Output: "0"

num10, k10 = "43214321", 4
print(removeKdigits(num10, k10)) # Output: "1321"
