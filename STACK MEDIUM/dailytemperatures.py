# DAILY TEMPERATURES

'''
Given an array of integers temperatures represents the daily temperatures, 
return an array answer such that answer[i] is the number of days you have to wait after the ith day to get a warmer temperature. 
If there is no future day for which this is possible, keep answer[i] == 0 instead.
'''

def dailyTemperatures(temperatures):
    stack = []
    answer = [0] * len(temperatures)
    i = 0
    
    while i < len(temperatures):
        currentTemp = temperatures[i]
        while stack and currentTemp > temperatures[stack[-1]]:
            prevIndex = stack.pop()
            answer[prevIndex] = i - prevIndex
        stack.append(i)
        i += 1
        
    return answer

'''
Time Complexity: O(n)
- The algorithm iterates through the input array `temperatures` of length `n` exactly once.
- Although there is a nested `while` loop, its total number of executions is bounded. Each index is pushed onto the stack exactly once.
- An index is only popped from the stack inside the inner loop. Since each index can be popped at most once, the total number of operations performed by the inner loop across all iterations of the outer loop is at most `n`.
- This means each index is processed (pushed and potentially popped) a constant number of times.
- Therefore, the amortized time complexity is O(n).

Space Complexity: O(n)
- The space complexity is determined by the `stack` used to store indices.
- In the worst-case scenario, if the temperatures are in a strictly decreasing order (e.g., [90, 80, 70, 60]), no temperature will be warmer than a previous one in the stack.
- In this case, every index will be pushed onto the stack, and the stack will grow to a size of `n`.
- The `answer` array also requires O(n) space, but this is often considered part of the output space. The auxiliary space is dominated by the stack.
- Therefore, the space complexity is O(n).
'''

# Test Cases
temperatures1 = [73,74,75,71,69,72,76,73]
print(dailyTemperatures(temperatures1)) # Output: [1,1,4,2,1,1,0,0]

temperatures2 = [30,40,50,60]
print(dailyTemperatures(temperatures2)) # Output: [1,1,1,0]

temperatures3 = [30,60,90]
print(dailyTemperatures(temperatures3)) # Output: [1,1,0]

temperatures4 = [89,62,70,58,47,47,46,76,100,70]
print(dailyTemperatures(temperatures4)) # Output: [8,1,5,4,3,2,1,1,0,0]

temperatures5 = [55,38,53,81,61,93,97,32,43,78]
print(dailyTemperatures(temperatures5)) # Output: [3,1,1,2,1,1,0,1,1,0]

temperatures6 = [1]
print(dailyTemperatures(temperatures6)) # Output: [0]

temperatures7 = []
print(dailyTemperatures(temperatures7)) # Output: []

temperatures8 = [90,80,70,60,50]
print(dailyTemperatures(temperatures8)) # Output: [0,0,0,0,0]

temperatures9 = [10,20,30,25,35]
print(dailyTemperatures(temperatures9)) # Output: [1,1,2,1,0]

temperatures10 = [70,70,70,70]
print(dailyTemperatures(temperatures10)) # Output: [0,0,0,0]