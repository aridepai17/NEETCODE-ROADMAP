# MINIMUM CHANGES TO MAKE ALTERNATING BINARY STRING

'''
You are given a string s consisting only of the characters '0' and '1'. 
In one operation, you can change any '0' to '1' or vice versa.
The string is called alternating if no two adjacent characters are equal. 
For example, the string "010" is alternating, while the string "0100" is not.
Return the minimum number of operations needed to make s alternating.
'''

def minOperations(s):
    count0 = 0
    count1 = 0
    
    for i in range(len(s)):
        if i % 2 == 0:
            if s[i] == "0":
                count0 += 1
            else:
                count1 += 1
        else:
            if s[i] == "1":
                count0 += 1
            else:
                count1 += 1
        
    return min(count0, count1)

'''
Time Complexity: O(N)
- Let N be the length of the input string `s`.
- The algorithm iterates through the string once using a single for loop, which runs N times.
- Inside the loop, all operations (modulo, string indexing, comparison, and incrementing counters) take constant time, O(1).
- Therefore, the overall time complexity is directly proportional to the length of the string, resulting in O(N).

Space Complexity: O(1)
- The algorithm uses a fixed number of variables (`count0`, `count1`, `i`) to store counts and the loop index.
- The amount of extra space required does not grow with the size of the input string `s`.
- Thus, the space complexity is constant, O(1).
'''

# Test Cases
s1 = "0100"
print(minOperations(s1)) # Output: 1

s2 = "1001"
print(minOperations(s2)) # Output: 2

s3 = "10"
print(minOperations(s3)) # Output: 0

s4 = "1111"
print(minOperations(s4)) # Output: 2

s5 = "00000"
print(minOperations(s5)) # Output: 2

s6 = "1"
print(minOperations(s6)) # Output: 0

s7 = ""
print(minOperations(s7)) # Output: 0

s8 = "010101"
print(minOperations(s8)) # Output: 0

s9 = "110010"
print(minOperations(s9)) # Output: 2

s10 = "00110011"
print(minOperations(s10)) # Output: 4