# MINIMUM PENALTY FOR A SHOP

'''
You are given the customer visit log of a shop represented by a 0-indexed string customers consisting only of characters 'N' and 'Y':
- if the ith character is 'Y', it means that customers come at the ith hour
- whereas 'N' indicates that no customers come at the ith hour.
If the shop closes at the jth hour (0 <= j <= n), the penalty is calculated as follows:
- For every hour when the shop is open and no customers come, the penalty increases by 1.
- For every hour when the shop is closed and customers come, the penalty increases by 1.
Return the earliest hour at which the shop must be closed to incur a minimum penalty.
Note that if a shop closes at the jth hour, it means the shop is closed at the hour j.
'''

# Solution 1: Using Prefix and Postfix Sums
def minimumPenalty(customers):
    n = len(customers)
    prefixN = [0] * (n + 1)
    postfixY = [0] * (n + 1)
    
    for i in range(1, n + 1):
        prefixN[i] = prefixN[i - 1]
        if customers[i - 1] == "N":
            prefixN[i] += 1
            
    for i in range(n - 1, -1, -1):
        postfixY[i] = postfix[i + 1]
        if customers[i] == "Y":
            postfixY[i] += 1
            
    minPenalty = float('inf')
    bestHour = 0
    
    for i in range(n + 1):
        penalty = prefixN[i] + postfixY[i]
        if penalty < minPenalty:
            minPenalty = penalty
            bestHour = i
            
    return bestHour

'''
Time Complexity: O(N)
- Let N be the length of the input string `customers`.
- We iterate through the string twice: once to build the `prefixN` array (O(N)) and once to build the `postfixY` array (O(N)).
- We then iterate through all possible closing hours from 0 to N (O(N)) to calculate the penalty for each hour.
- All operations inside the loops are O(1).
- Therefore, the overall time complexity is O(N) + O(N) + O(N) = O(N).

Space Complexity: O(N)
- We use two auxiliary arrays: `prefixN` and `postfixY`, each of size N+1, which requires O(N) space.
- Other variables (`minPenalty`, `bestHour`, loop indices) use constant space O(1).
- Therefore, the overall space complexity is O(N).
'''

# Solution 2: Using no extra space 
def minimumPenalty(customers):
    n = len(customers)
    currentPenalty = customers.count("Y")
    minimumPenalty = currentPenalty
    bestHour = 0
    
    for i in range(1, n + 1):
        customersAtPrevHour = customers[i - 1]
        if customersAtPrevHour == "Y":
            currentPenalty -= 1
        else:
            currentPenalty += 1
            
        if currentPenalty < minimumPenalty:
            minimumPenalty = currentPenalty
            bestHour = i
            
    return bestHour

'''
Time Complexity: O(N)
- Let N be the length of the input string `customers`.
- We iterate through the string once, from index 1 to N (O(N)).
- Inside the loop, all operations (character comparison, addition, subtraction, assignment) are constant time operations, O(1).
- The initial `count("Y")` operation takes O(N) time.
- Therefore, the overall time complexity is O(N) + O(N) = O(N).

Space Complexity: O(1)
- The algorithm uses a fixed number of variables (`currentPenalty`, `minimumPenalty`, `bestHour`, `n`, loop index) regardless of the input size.
- No additional data structures are created that grow with the input size.
- Therefore, the space complexity is constant, O(1).
'''

# Test Cases
customers1 = "YYNY"
print(minimumPenalty(customers1)) # Output: 2

customers2 = "NNNN"
print(minimumPenalty(customers2)) # Output: 0

customers3 = "YYYY"
print(minimumPenalty(customers3)) # Output: 4

customers4 = "NNNYYY"
print(minimumPenalty(customers4)) # Output: 3

customers5 = "YYYNNN"
print(minimumPenalty(customers5)) # Output: 3

customers6 = "Y"
print(minimumPenalty(customers6)) # Output: 1

customers7 = "N"
print(minimumPenalty(customers7)) # Output: 0

customers8 = "YNYNYN"
print(minimumPenalty(customers8)) # Output: 3

customers9 = "NYNYNY"
print(minimumPenalty(customers9)) # Output: 0

customers10 = "YYYYNNNN"
print(minimumPenalty(customers10)) # Output: 4