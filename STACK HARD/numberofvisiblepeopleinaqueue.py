# NUMBER OF VISIBLE PEOPLE IN A QUEUE

'''
There are n people standing in a queue, and they numbered from 0 to n - 1 in left to right order.
You are given an array heights of distinct integers where heights[i] represents the height of the ith person.
A person can see another person to their right in the queue if everybody in between is shorter than both of them. 
More formally, the ith person can see the jth person if i < j and min(heights[i], heights[j]) > max(heights[i+1], heights[i+2], ..., heights[j-1]).
Return an array answer of length n where answer[i] is the number of people the ith person can see to their right in the queue.
'''

def canSeePersonsCount(heights):
    n = len(heights)
    answer = [0] * n
    stack = []
    
    for i in range(n - 1, -1, -1):
        count = 0
        while stack and stack[-1] < heights[i]:
            stack.pop()
            count += 1
        if stack:
            count += 1
        answer[i] = count
        stack.append(heights[i])
        
    return answer

'''
Time Complexity: O(n)
Let n be the length of the heights array.
- We iterate through the heights array once from right to left, which takes O(n) time.
- For each element, we may pop elements from the stack. However, each element can be pushed onto the stack at most once and popped at most once across all iterations.
- Therefore, the total number of stack operations (push and pop) across all iterations is O(n).
- The overall time complexity is O(n).

Space Complexity: O(n)
- We use a stack to store heights. In the worst case (e.g., when heights are in increasing order from left to right), the stack can contain all n elements.
- We also use an answer array of size n to store the results.
- Therefore, the space complexity is O(n).
'''

# Test Cases
heights1 = [10, 6, 8, 5, 11, 9]
print(canSeePersonsCount(heights1)) # Output: [3, 1, 2, 1, 1, 0]

heights2 = [5, 1, 2, 3, 10]
print(canSeePersonsCount(heights2)) # Output: [4, 1, 1, 1, 0]

heights3 = [1, 2, 3, 4, 5]
print(canSeePersonsCount(heights3)) # Output: [1, 1, 1, 1, 0]

heights4 = [5, 4, 3, 2, 1]
print(canSeePersonsCount(heights4)) # Output: [4, 3, 2, 1, 0]

heights5 = [3, 1, 4, 2, 5]
print(canSeePersonsCount(heights5)) # Output: [2, 1, 2, 1, 0]

heights6 = [1]
print(canSeePersonsCount(heights6)) # Output: [0]

heights7 = [10, 5]
print(canSeePersonsCount(heights7)) # Output: [1, 0]

heights8 = [7, 3, 5, 9, 2, 8, 6]
print(canSeePersonsCount(heights8)) # Output: [3, 1, 2, 2, 1, 1, 0]

heights9 = [15, 10, 20, 5, 25]
print(canSeePersonsCount(heights9)) # Output: [2, 1, 2, 1, 0]

heights10 = [8, 7, 6, 5, 4, 3, 2, 1]
print(canSeePersonsCount(heights10)) # Output: [7, 6, 5, 4, 3, 2, 1, 0]