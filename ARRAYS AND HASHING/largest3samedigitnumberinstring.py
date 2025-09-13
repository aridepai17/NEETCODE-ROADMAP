# LARGEST 3-SAME-DIGIT NUMBER IN STRING

'''
You are given a string num representing a large integer. 
An integer is good if it meets the following conditions:
- It is a substring of num with length 3.
- It consists of only one unique digit.
Return the maximum good integer as a string or an empty string "" if no such integer exists.
Note:
- A substring is a contiguous sequence of characters within a string.
- There may be leading zeroes in num or a good integer.
'''

def largestGoodInteger(num):
    result = ""
    
    for i in range(len(num) - 2):
        if num[i] == num[i + 1] == num[i + 2]:
            result = max(result, num[i:i+3])
            
    return result

'''
Time Complexity: O(N)
Let N be the length of the input string `num`.
- The algorithm iterates through the string from the first character up to the third-to-last character. This loop runs N - 2 times, which is O(N).
- Inside the loop, all operations are constant time:
  - Accessing characters by index (e.g., `num[i]`) is O(1).
  - Slicing a substring of a fixed length 3 (`num[i:i+3]`) is O(1).
  - Comparing two strings of length 3 (`max(result, ...)`), where `result` is either empty or of length 3, is also O(1).
- Therefore, the total time complexity is dominated by the loop, resulting in O(N).

Space Complexity: O(1)
- The algorithm uses a single variable `result` to store the largest "good" integer found. The maximum length of this string is 3.
- The space required for this variable is constant and does not depend on the length of the input string `num`.
- The substring created by the slice `num[i:i+3]` also occupies constant space.
- Thus, the space complexity is O(1).
'''

# Test Cases
num1 = "6777133339"
print(largestGoodInteger(num1)) # Output: "777"

num2 = "2300019"
print(largestGoodInteger(num2)) # Output: "000"

num3 = "42352338"
print(largestGoodInteger(num3)) # Output: ""

num4 = "111"
print(largestGoodInteger(num4)) # Output: "111"

num5 = "999888777"
print(largestGoodInteger(num5)) # Output: "999"

num6 = "12345"
print(largestGoodInteger(num6)) # Output: ""

num7 = "000"
print(largestGoodInteger(num7)) # Output: "000"

num8 = "8888"
print(largestGoodInteger(num8)) # Output: "888"

num9 = "1"
print(largestGoodInteger(num9)) # Output: ""

num10 = "11"
print(largestGoodInteger(num10)) # Output: ""