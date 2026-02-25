# MINIMUM COST FOR TICKETS

'''
You have planned some train traveling one year in advance. The days of the year in which you will travel are given as an integer array days. Each day is an integer from 1 to 365.
Train tickets are sold in three different ways:
a 1-day pass is sold for costs[0] dollars,
a 7-day pass is sold for costs[1] dollars, and
a 30-day pass is sold for costs[2] dollars.
The passes allow that many days of consecutive travel.
For example, if we get a 7-day pass on day 2, then we can travel for 7 days: 2, 3, 4, 5, 6, 7, and 8.
Return the minimum number of dollars you need to travel every day in the given list of days.
'''

def mincostTickets(days, costs):
    travelDays = set(days)
    lastDay = days[-1]
    
    dp = [0] * (lastDay + 1)
    
    for day in range(1, lastDay + 1):
        if day not in travelDays:
            dp[day] = dp[day - 1]
        else:
            dp[day] = min(
                dp[day - 1] + costs[0],
                dp[max(0, day - 7)] + costs[1],
                dp[max(0, day - 30)] + costs[2]
            )
            
    return dp[lastDay]

'''
ALGORITHM:

This problem is solved using dynamic programming where dp[day] represents the minimum cost to cover all travel days up to that day.

Algorithm:
1. Create a set of travel days for O(1) lookup
2. Find the last travel day
3. Create dp array of size lastDay + 1
4. For each day from 1 to lastDay:
    a. If it's not a travel day: dp[day] = dp[day - 1] (no cost needed)
    b. If it is a travel day, take minimum of:
        - Buy 1-day ticket: dp[day - 1] + costs[0]
        - Buy 7-day ticket: dp[max(0, day - 7)] + costs[1]
        - Buy 30-day ticket: dp[max(0, day - 30)] + costs[2]
5. Return dp[lastDay]

Key insight: We consider all three ticket options at each travel day and pick the minimum.
'''

'''
Time Complexity: O(D), where D is the last day number (max 365). We iterate through each day once.
Space Complexity: O(D), for the dp array.
'''

# Test Cases

# Test Case 1: Basic case
days1 = [1, 4, 6]
costs1 = [2, 7, 15]
result1 = mincostTickets(days1, costs1)
print(result1)  # Expected: 6 (buy 1-day for day 1, 1-day for day 4, 1-day for day 6 = 6)

# Test Case 2: All days
days2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
costs2 = [2, 7, 15]
result2 = mincostTickets(days2, costs2)
print(result2)  # Expected: 14 (buy 7-day pass for $7)

# Test Case 3: Sparse days
days3 = [1, 3, 5, 7, 9, 11, 13, 15]
costs3 = [2, 7, 15]
result3 = mincostTickets(days3, costs3)
print(result3)  # Expected: 14 (buy 7-day twice)

# Test Case 4: Only 1-day passes cheaper
days4 = [1, 2, 3]
costs4 = [2, 3, 10]
result4 = mincostTickets(days4, costs4)
print(result4)  # Expected: 6 (buy three 1-day passes)

# Test Case 5: 7-day pass worth it
days5 = [1, 2, 3, 4, 5, 6, 7]
costs5 = [3, 10, 30]
result5 = mincostTickets(days5, costs5)
print(result5)  # Expected: 10 (buy one 7-day pass)

# Test Case 6: 30-day pass worth it
days6 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]
costs6 = [2, 7, 20]
result6 = mincostTickets(days6, costs6)
print(result6)  # Expected: 20 (buy one 30-day pass)

# Test Case 7: Edge case - first day only
days7 = [1]
costs7 = [2, 7, 15]
result7 = mincostTickets(days7, costs7)
print(result7)  # Expected: 2

# Test Case 8: Mix of passes
days8 = [1, 4, 5, 6, 7, 8, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31]
costs8 = [2, 7, 20]
result8 = mincostTickets(days8, costs8)
print(result8)  # Expected: 27 (7-day + 7-day + 7-day or 7+20)

# Test Case 9: Days far apart
days9 = [1, 100, 200, 300]
costs9 = [5, 20, 50]
result9 = mincostTickets(days9, costs9)
print(result9)  # Expected: 65 (1-day for day 1 = 5, 7-day for day 100 = 20, 7-day for day 200 = 20, 7-day for day 300 = 20)

# Test Case 10: Single day multiple times
days10 = [1, 2]
costs10 = [5, 6, 20]
result10 = mincostTickets(days10, costs10)
print(result10)  # Expected: 10 (two 1-day passes)