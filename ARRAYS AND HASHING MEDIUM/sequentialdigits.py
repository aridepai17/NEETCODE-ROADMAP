# SEQUENTIAL DIGITS

'''
An integer has sequential digits if and only if each digit in the number is one more than the previous digit.
Return a sorted list of all the integers in the range [low, high] inclusive that have sequential digits.
'''

def sequentialDigits(low, high):
    result = []
    queue = deque(range(1, 10))
    
    whlie queue:
        n = queue.popleft()
        if n > high:
            break
        if low <= n <= high:
            result.append(n)
        lastDigit = n % 10
        if lastDigit < 9:
            newDigit = lastDigit + 1
            queue.append(n * 10 + newDigit)
            
    return result

'''
Time Complexity: O(log(high) * log(high))
- At most, every sequential digit number with at most log10(high) digits is generated and checked.
- The number of sequential digits numbers is less than 45 (since there are at most 9 choose 2 possible sequential numbers), but the dominant term is the range of digits up to high, so it's effectively O(log(high)^2).

Space Complexity: O(log(high))
- The space used by the queue and the result is proportional to the number of digits, i.e., O(log(high)), since that's the maximum length a sequential digit number can have.
'''

# Test Cases
low1 = 100
high1 = 300


low2 = 10
high2 = 99
print(sequentialDigits(low2, high2)) # Output: [12, 23, 34, 45, 56, 67, 78, 89]

low3 = 1000
high3 = 13000
print(sequentialDigits(low3, high3)) # Output: [1234, 2345, 3456, 4567, 5678, 6789, 12345]

low4 = 58
high4 = 155
print(sequentialDigits(low4, high4)) # Output: [67, 78, 89, 123]

low5 = 1
high5 = 9
print(sequentialDigits(low5, high5)) # Output: [1, 2, 3, 4, 5, 6, 7, 8, 9]

low6 = 987
high6 = 9876
print(sequentialDigits(low6, high6)) # Output: [1234, 2345, 3456, 4567, 5678, 6789]

low7 = 234
high7 = 2345
print(sequentialDigits(low7, high7)) # Output: [234, 345, 456, 567, 678, 789, 1234, 2345]

low8 = 100
high8 = 1000
print(sequentialDigits(low8, high8)) # Output: [123, 234, 345, 456, 567, 678, 789, 1234]

low9 = 500
high9 = 1500
print(sequentialDigits(low9, high9)) # Output: [567, 678, 789, 1234]

low10 = 10
high10 = 1000000
print(sequentialDigits(low10, high10)) # Output: [12, 23, 34, 45, 56, 67, 78, 89, 123, 234, 345, 456, 567, 678, 789, 1234, 2345, 3456, 4567, 5678, 6789, 12345, 23456, 34567, 45678, 56789, 123456, 234567, 345678, 456789, 1234567, 2345678, 3456789, 12345678, 23456789, 123456789]