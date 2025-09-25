# BAG OF TOKENS

'''
You start with an initial power of power, an initial score of 0, and a bag of tokens given as an integer array tokens, where each tokens[i] denotes the value of tokeni.
Your goal is to maximize the total score by strategically playing these tokens. In one move, you can play an unplayed token in one of the two ways (but not both for the same token):
Face-up: If your current power is at least tokens[i], you may play tokeni, losing tokens[i] power and gaining 1 score.
Face-down: If your current score is at least 1, you may play tokeni, gaining tokens[i] power and losing 1 score.
Return the maximum possible score you can achieve after playing any number of tokens.
'''

def bagofTokens(tokens, power):
    result = 0
    score = 0
    tokens.sort()
    left = 0
    right = len(tokens) - 1
    
    while left <= right:
        if power >= tokens[left]:
            power -= tokens[left]
            score += 1
            left += 1
            result = max(result, score)
        elif score > 0:
            power += tokens[right]
            score -= 1
            right -= 1
        else:
            break
        
    return result

'''
Time Complexity: O(N log N)
- The first step is to sort the `tokens` array. In Python, this uses Timsort, which has an average and worst-case time complexity of O(N log N), where N is the number of tokens.
- After sorting, the algorithm uses a two-pointer approach (`left` and `right`) to traverse the array.
- The `while` loop runs as long as `left <= right`. In each iteration, either the `left` pointer moves forward or the `right` pointer moves backward. This means the loop will execute at most N times. The operations inside the loop are all constant time.
- The traversal part of the algorithm takes O(N) time.
- Since the sorting step (O(N log N)) is the bottleneck, the overall time complexity is dominated by it.
- Therefore, the time complexity is O(N log N).

Space Complexity: O(log N) or O(N)
- The space complexity is primarily determined by the sorting algorithm used.
- Python's `sort()` method is performed in-place, but its implementation (Timsort) can require auxiliary space. The space complexity of Timsort can range from O(log N) to O(N) in the worst case.
- Apart from the space used by sorting, the algorithm uses only a few variables (`result`, `score`, `left`, `right`), which occupy a constant amount of space, O(1).
- Therefore, the dominant factor for space is the sorting algorithm, resulting in a space complexity of O(log N) to O(N).
'''

# Test Cases
tokens1 = [100], power1 = 50
print(bagofTokens(tokens1, power1)) # Output: 1

tokens2 = [100, 200], power2 = 150
print(bagofTokens(tokens2, power2)) # Output: 1

tokens3 = [100, 200, 300, 400], power3 = 200
print(bagofTokens(tokens3, power3)) # Output: 2

tokens4 = [], power4 = 100
print(bagofTokens(tokens4, power4)) # Output: 0

tokens5 = [100, 200], power5 = 0
print(bagofTokens(tokens5, power5)) # Output: 0

tokens6 = [20, 30, 40], power6 = 100
print(bagofTokens(tokens6, power6)) # Output: 3

tokens7 = [100, 200], power7 = 500
print(bagofTokens(tokens7, power7)) # Output: 2

tokens8 = [71, 55, 82], power8 = 54
print(bagofTokens(tokens8, power8)) # Output: 0

tokens9 = [26], power9 = 51
print(bagofTokens(tokens9, power9)) # Output: 1

tokens10 = [100, 200, 300], power10 = 150
print(bagofTokens(tokens10, power10)) # Output: 1