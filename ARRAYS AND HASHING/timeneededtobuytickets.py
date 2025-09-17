# TIME NEEDED TO BUY TICKETS

'''
There are n people in a line queuing to buy tickets, where the 0th person is at the front of the line and the (n - 1)th person is at the back of the line.
You are given a 0-indexed integer array tickets of length n where the number of tickets that the ith person would like to buy is tickets[i].
Each person takes exactly 1 second to buy a ticket. A person can only buy 1 ticket at a time and has to go back to the end of the line (which happens instantaneously) in order to buy more tickets. 
If a person does not have any tickets left to buy, the person will leave the line.
Return the time taken for the person initially at position k (0-indexed) to finish buying tickets.
'''

def timeRequiredToBuy(tickets, k):
    time = 0
    n = len(tickets)
    
    for i in range(n):
        if i <= k:
            time += min(tickets[i], tickets[k])
        else:
            time += min(tickets[i], tickets[k] - 1)
            
    return time

'''
Time Complexity: O(n)
The code iterates through the 'tickets' array once, where n is the length of the array. Inside the loop, all operations are constant time. Thus, the total time complexity is directly proportional to the number of people in the line.

Space Complexity: O(1)
The algorithm uses a constant amount of extra space. It only requires a few variables (time, n, i) to store the result and loop counters, and their memory usage does not depend on the size of the input array.
'''

# Test Cases
tickets1 = [2,3,2], k1 = 21
print(timeRequiredToBuy(tickets1, k1)) # Output: 6

tickets2 = [5,1,1,1], k2 = 0
print(timeRequiredToBuy(tickets2, k2)) # Output: 8

tickets3 = [8,4,4,2,1], k3 = 4
print(timeRequiredToBuy(tickets3, k3)) # Output: 5

tickets4 = [100], k4 = 0
print(timeRequiredToBuy(tickets4, k4)) # Output: 100

tickets5 = [3,3,3,3], k5 = 1
print(timeRequiredToBuy(tickets5, k5)) # Output: 10

tickets6 = [1,1,1,10,1], k6 = 3
print(timeRequiredToBuy(tickets6, k6)) # Output: 14

tickets7 = [2,6,3,4,5], k7 = 1
print(timeRequiredToBuy(tickets7, k7)) # Output: 20

tickets8 = [4,3,2,5,1], k8 = 3
print(timeRequiredToBuy(tickets8, k8)) # Output: 15

tickets9 = [5,2,3,4], k9 = 1
print(timeRequiredToBuy(tickets9, k9)) # Output: 6

tickets10 = [1,1,1,1,1,1,1], k10 = 3
print(timeRequiredToBuy(tickets10, k10)) # Output: 4