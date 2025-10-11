# DEFUSE THE BOMB

'''
You have a bomb to defuse, and your time is running out! Your informer will provide you with a circular array code of length of n and a key k.
To decrypt the code, you must replace every number. All the numbers are replaced simultaneously.
If k > 0, replace the ith number with the sum of the next k numbers.
If k < 0, replace the ith number with the sum of the previous k numbers.
If k == 0, replace the ith number with 0.
As code is circular, the next element of code[n-1] is code[0], and the previous element of code[0] is code[n-1].
Given the circular array code and an integer key k, return the decrypted code to defuse the bomb!
'''

def decrypt(code, k):
    n = len(code)
    currentSum = 0
    result = [0] * n
    left = 0
    
    for right in range(n + abs(k)):
        currentSum += code(right % n)
        
        if right - left + 1 > abs(k):
            currentSum -= code(left % n)
            left = (left + 1) % n
            
        if right - left + 1 == abs(k):
            if k > 0:
                result[(left - 1) % n] = currentSum
            else:
                result[(right + 1) % n] = currentSum
                
    return result


'''
Time Complexity: O(n + |k|)
The algorithm's runtime is dominated by the single `for` loop, which runs `n + abs(k)` times. 
Inside the loop, all operations—such as list access, arithmetic operations, and modulo—are performed in constant time, O(1). 
The initialization of the `result` array also takes O(n) time. 
Therefore, the total time complexity is O(n + |k|).

Space Complexity: O(n)
The primary space requirement comes from the `result` array, which is created to store the decrypted code and has a size of `n`. 
The other variables used (`n`, `currentSum`, `left`, `right`) occupy a constant amount of space, O(1). 
Consequently, the overall space complexity is O(n).
'''

# Test Cases
code1 = [5,7,1,4], k1 = 3
print(decrypt(code1, k1)) # Output: [12,10,16,13]

code2 = [2,4,9,3], k2 = -2
print(decrypt(code2, k2)) # Output: [12,5,6,13]

code3 = [1,2,3,4], k3 = 0
print(decrypt(code3, k3)) # Output: [0,0,0,0]

code4 = [10, 5, 7, 6], k4 = 1
print(decrypt(code4, k4)) # Output: [5,7,6,10]

code5 = [10, 5, 7, 6], k5 = -3
print(decrypt(code5, k5)) # Output: [18,23,21,22]

code6 = [1, 2, 3], k6 = 4
print(decrypt(code6, k6)) # Output: [8,9,7]

code7 = [1, 2, 3], k7 = -4
print(decrypt(code7, k7)) # Output: [9,7,8]

code8 = [-1, -2, -3, -4], k8 = 2
print(decrypt(code8, k8)) # Output: [-5,-7,-5,-3]

code9 = [10, -10, 10, -10], k9 = -1
print(decrypt(code9, k9)) # Output: [-10,10,-10,10]

code10 = [100], k10 = 10
print(decrypt(code10, k10)) # Output: [1000]