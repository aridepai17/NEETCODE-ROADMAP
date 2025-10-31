# AVERAGE WAITING TIME

'''
There is a restaurant with a single chef. You are given an array customers, where customers[i] = [arrivali,timei]:
- arrivali is the arrival time of the ith customer. 
- The arrival times are sorted in non-decreasing order.
- timei is the time needed to prepare the order of the ith customer.
When a customer arrives, he gives the chef his order, and the chef starts preparing it once he is idle. 
The customer waits till the chef finishes preparing his order. 
The chef does not prepare food for more than one customer at a time. 
The chef prepares food for customers in the order they were given in the input.
Return the average waiting time of all customers. 
Solutions within 10-5 from the actual answer are considered accepted.
'''

def averageWaitingTime(customers):
    freeTime = 0
    totalTime = 0
    
    for arrivalTime, prepTime in customers:
        freeTime = max(freeTime, arrivalTime)
        finishTime = freeTime + prepTime
        totalTime += (finishTime - arrivalTime)
        freeTime = finishTime
        
    return totalTime / len(customers)

'''
Time Complexity: O(N)
- Let N be the number of customers in the input array `customers`.
- The algorithm iterates through the `customers` array exactly once.
- Inside the loop, all operations (max, addition, subtraction, assignment) are constant time operations, O(1).
- Therefore, the total time complexity is directly proportional to the number of customers, making it O(N).

Space Complexity: O(1)
- The algorithm uses a fixed number of variables (`freeTime`, `totalTime`, `arrivalTime`, `prepTime`, loop index) regardless of the input size.
- No additional data structures are created that grow with the input size.
- Therefore, the space complexity is constant, O(1).
'''

# Test Cases
customers1 = [[1,2],[2,5],[4,3]]
print(averageWaitingTime(customers1)) # Output: 5.0

customers2 = [[5,2],[5,4],[10,3],[20,1]]
print(averageWaitingTime(customers2)) # Output: 3.75

customers3 = [[1,9]]
print(averageWaitingTime(customers3)) # Output: 9.0

customers4 = [[1,1],[1,1],[1,1]]
print(averageWaitingTime(customers4)) # Output: 2.0

customers5 = [[1,100000]]
print(averageWaitingTime(customers5)) # Output: 100000.0

customers6 = [[1,1],[2,1],[3,1],[4,1],[5,1]]
print(averageWaitingTime(customers6)) # Output: 1.0

customers7 = [[1,5],[2,4],[3,3],[4,2],[5,1]]
print(averageWaitingTime(customers7)) # Output: 4.0

customers8 = [[10,1],[10,1],[10,1]]
print(averageWaitingTime(customers8)) # Output: 2.0

customers9 = [[1,2],[1,2],[1,2],[1,2],[1,2]]
print(averageWaitingTime(customers9)) # Output: 6.0

customers10 = [[1,1],[5,1],[10,1],[15,1],[20,1]]
print(averageWaitingTime(customers10)) # Output: 1.0