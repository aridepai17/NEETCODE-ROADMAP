# LEMONADE CHANGE

'''
At a lemonade stand, each lemonade costs $5. 
Customers are standing in a queue to buy from you and order one at a time (in the order specified by bills). 
Each customer will only buy one lemonade and pay with either a $5, $10, or $20 bill. 
You must provide the correct change to each customer so that the net transaction is that the customer pays $5.
Note that you do not have any change in hand at first.
Given an integer array bills where bills[i] is the bill the ith customer pays, return true if you can provide every customer with the correct change, or false otherwise.
'''

def lemonadeChange(bills):
    five, ten  = 0, 0
    
    for num in bills:
        if num == 5:
            five += 1
        elif num == 10:
            if five == 0:
                return False
            five -= 1
            ten += 1
        else:
            if five > 0 and ten > 0:
                five -= 1
                ten -= 1
            elif five >= 3:
                five -= 3
            else:
                return False

    return True

'''
Time Complexity: O(N)
Let N be the number of customers, which is the length of the `bills` array.
- The algorithm iterates through the `bills` array exactly once with a single `for` loop.
- Inside the loop, all operations are constant time, O(1). These include:
  - Checking the value of the bill (`num == 5`, `num == 10`).
  - Checking the counts of available change (`five == 0`, `five > 0 and ten > 0`, `five >= 3`).
  - Updating the counts of $5 and $10 bills (`five += 1`, `five -= 1`, `ten += 1`, etc.).
- Since the loop runs N times and each iteration takes constant time, the overall time complexity is O(N).

Space Complexity: O(1)
- The algorithm uses a fixed number of variables (`five`, `ten`, and the loop variable `num`) to store the counts of the bills.
- The amount of memory used does not depend on the number of customers (the length of the `bills` array).
- No additional data structures that scale with the input size are created.
- Therefore, the space complexity is constant, O(1).
'''

# Test Cases
bills1 = [5, 5, 5, 10, 20]
print(lemonadeChange(bills1)) # Output: True

bills2 = [5, 5, 10, 10, 20]
print(lemonadeChange(bills2)) # Output: False

bills3 = [10, 10]
print(lemonadeChange(bills3)) # Output: False

bills4 = [5, 5, 10]
print(lemonadeChange(bills4)) # Output: True

bills5 = [5, 5, 5, 5, 20, 5, 5, 10, 20]
print(lemonadeChange(bills5)) # Output: True

bills6 = []
print(lemonadeChange(bills6)) # Output: True

bills7 = [20]
print(lemonadeChange(bills7)) # Output: False

bills8 = [5, 20]
print(lemonadeChange(bills8)) # Output: False

bills9 = [5, 5, 10, 20, 10]
print(lemonadeChange(bills9)) # Output: False

bills10 = [5, 5, 5, 20]
print(lemonadeChange(bills10)) # Output: True