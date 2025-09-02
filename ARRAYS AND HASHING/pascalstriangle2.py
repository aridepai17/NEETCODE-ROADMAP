# PASCALS TRIANGLE 2

# Given two integres r and c, return the value at the rth row and cth column (1-indexed) in a Pascal's Triangle.

def nCr(n, r):
    result = 1
    
    for i in range(r):
        result *= (n - i)
        result //= (i + 1)
        
    return result

def pascalsTriangle2(r, c):
    return nCr(r-1, c-1)

# Time Complexity: O(r) because we compute the binomial coefficient in O(r) time
# Space Complexity: O(1) because we are not using any additional space

# Test Cases
r1 = 4
c1 = 2
print(pascalsTriangle2(r1, c1)) # Output: 3 

r2 = 1
c2 = 1
print(pascalsTriangle2(r2, c2)) # Output: 1

r3 = 5
c3 = 1
print(pascalsTriangle2(r3, c3)) # Output: 1

r4 = 5
c4 = 5
print(pascalsTriangle2(r4, c4)) # Output: 1

r5 = 6
c5 = 3
print(pascalsTriangle2(r5, c5)) # Output: 10

r6 = 10
c6 = 5
print(pascalsTriangle2(r6, c6)) # Output: 126

r7 = 8
c7 = 5
print(pascalsTriangle2(r7, c7)) # Output: 35

r8 = 8
c8 = 2
print(pascalsTriangle2(r8, c8)) # Output: 7

r9 = 8
c9 = 7
print(pascalsTriangle2(r9, c9)) # Output: 7

r10 = 11
c10 = 3
print(pascalsTriangle2(r10, c10)) # Output: 45 