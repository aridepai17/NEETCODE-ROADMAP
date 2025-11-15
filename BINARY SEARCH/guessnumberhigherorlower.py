# GUESS NUMBER HIGHER OR LOWER

'''
We are playing the Guess Game. The game is as follows:
I pick a number from 1 to n. You have to guess which number I picked (the number I picked stays the same throughout the game).
Every time you guess wrong, I will tell you whether the number I picked is higher or lower than your guess.

You call a pre-defined API int guess(int num), which returns three possible results:
-1: Your guess is higher than the number I picked (i.e. num > pick).
1: Your guess is lower than the number I picked (i.e. num < pick).
0: your guess is equal to the number I picked (i.e. num == pick).

Return the number that I picked.
'''

def guessNumber(n):
    left = 1
    right = n
    
    while left <= right:
        mid = (left + right) // 2
        result = guess(mid)
        if result > 0:
            left = mid + 1
        elif result < 0:
            right = mid - 1
        else:
            return mid
        
'''
Time Complexity: O(log n)
Let n be the upper bound of the range [1, n].
- The algorithm uses binary search, which repeatedly divides the search space in half.
- In each iteration of the while loop, we either move the `left` pointer up or the `right` pointer down, effectively halving the remaining elements to search.
- The maximum number of iterations needed is log₂(n), as we can divide n by 2 at most log₂(n) times before the search space becomes empty.
- All operations inside the loop (calculating `mid`, calling `guess()`, comparisons, pointer updates) take constant time, O(1).
- Therefore, the overall time complexity is O(log n).

Space Complexity: O(1)
- The algorithm uses a constant amount of extra space for the variables `left`, `right`, `mid`, and `result`.
- No additional data structures are created, and the space used does not depend on the size of the input range.
- Therefore, the space complexity is O(1).
'''

# Test Cases
n1 = 10, pick1 = 6
print(guessNumber(n1)) # Output: 6

n2 = 1, pick2 = 1
print(guessNumber(n2)) # Output: 1

n3 = 2, pick3 = 1
print(guessNumber(n3)) # Output: 1

n4 = 2, pick4 = 2
print(guessNumber(n4)) # Output: 2

n5 = 100, pick5 = 50
print(guessNumber(n5)) # Output: 50

n6 = 100, pick6 = 1
print(guessNumber(n6)) # Output: 1

n7 = 100, pick7 = 100
print(guessNumber(n7)) # Output: 100

n8 = 1000, pick8 = 500
print(guessNumber(n8)) # Output: 500

n9 = 50, pick9 = 25
print(guessNumber(n9)) # Output: 25

n10 = 75, pick10 = 60
print(guessNumber(n10)) # Output: 60