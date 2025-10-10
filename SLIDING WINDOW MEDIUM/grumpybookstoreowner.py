# GRUMPY BOOKSTORE OWNER

'''
There is a bookstore owner that has a store open for n minutes. You are given an integer array customers of length n where customers[i] is the number of the customers that enter the store at the start of the ith minute and all those customers leave after the end of that minute.
During certain minutes, the bookstore owner is grumpy. You are given a binary array grumpy where grumpy[i] is 1 if the bookstore owner is grumpy during the ith minute, and is 0 otherwise.
When the bookstore owner is grumpy, the customers entering during that minute are not satisfied. Otherwise, they are satisfied.
The bookstore owner knows a secret technique to remain not grumpy for minutes consecutive minutes, but this technique can only be used once.
Return the maximum number of customers that can be satisfied throughout the day.
'''

def maxSatisified(customers, grumpy, minutes):
    window = 0
    satisfied = 0
    maxWindow = 0
    left = 0
    
    for right in range(len(customers)):
        if grumpy[right] == 1:
            window += customers[right]
        else:
            satisfied += customers[right]
            
        if right - left + 1 > minutes:
            if grumpy[left] == 1:
                window -= customers[left]
            left += 1
            
        maxWindow = max(window, maxWindow)
        
    return satisfied + maxWindow

'''
Time Complexity: O(n)
We iterate through the `customers` and `grumpy` arrays once using a single for loop, where 'n' is the number of elements in the input arrays. 
This is a classic sliding window approach. The operations inside the loop are all constant time.

Space Complexity: O(1)
We only use a constant amount of extra space for variables like `window`, `satisfied`, `maxWindow`, and `left`, regardless of the input size.
'''

# Test Cases
customers1 = [1,0,1,2,1,1,7,5], grumpy1 = [0,1,0,1,0,1,0,1], minutes1 = 3
print(maxSatisified(customers1, grumpy1, minutes1)) # Output: 16

customers2 = [10, 20, 30], grumpy2 = [0, 0, 0], minutes2 = 2
print(maxSatisified(customers2, grumpy2, minutes2)) # Output: 60

# All grumpy
customers3 = [5, 8, 3, 10], grumpy3 = [1, 1, 1, 1], minutes3 = 2
print(maxSatisified(customers3, grumpy3, minutes3)) # Output: 13

# minutes is equal to the length of the arrays
customers4 = [4, 10, 10], grumpy4 = [1, 1, 0], minutes4 = 3
print(maxSatisified(customers4, grumpy4, minutes4)) # Output: 24

# minutes is 1
customers5 = [2, 6, 8, 5], grumpy5 = [1, 0, 1, 1], minutes5 = 1
print(maxSatisified(customers5, grumpy5, minutes5)) # Output: 14

# minutes is 0
customers6 = [1, 2, 3, 4, 5], grumpy6 = [1, 1, 0, 1, 1], minutes6 = 0
print(maxSatisified(customers6, grumpy6, minutes6)) # Output: 3

# Edge case: empty arrays
customers7 = [], grumpy7 = [], minutes7 = 5
print(maxSatisified(customers7, grumpy7, minutes7)) # Output: 0

# minutes is larger than the length of the arrays
customers8 = [10, 1, 7], grumpy8 = [0, 0, 1], minutes8 = 5
print(maxSatisified(customers8, grumpy8, minutes8)) # Output: 18

# Large customer numbers
customers9 = [1000, 2000, 500, 3000], grumpy9 = [0, 1, 1, 0], minutes9 = 2
print(maxSatisified(customers9, grumpy9, minutes9)) # Output: 6500

# Best window at the beginning
customers10 = [9, 10, 4, 5], grumpy10 = [1, 1, 0, 1], minutes10 = 2
print(maxSatisified(customers10, grumpy10, minutes10)) # Output: 23