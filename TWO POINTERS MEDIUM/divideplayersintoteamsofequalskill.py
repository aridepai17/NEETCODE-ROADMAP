# DIVIDE PLAYERS INTO TEAMS OF EQUAL SKILL

'''
You are given a positive integer array skill of even length n where skill[i] denotes the skill of the ith player. 
Divide the players into n / 2 teams of size 2 such that the total skill of each team is equal.
The chemistry of a team is equal to the product of the skills of the players on that team.
Return the sum of the chemistry of all the teams, or return -1 if there is no way to divide the players into teams such that the total skill of each team is equal.
'''
# Solution 1: Using Sorting
def dividePlayers(skill):
    n = len(skill)
    skill.sort()
    
    numberofTeams = n // 2
    totalSkill = sum(skill)
    
    teamSum = totalSkill // numberofTeams
    
    left = 0
    right = n - 1
    totalChemistry = 0
    
    while left < right:
        currentSum = skill[left] + skill[right]
        if currentSum != teamSum:
            return - 1
        chemistry = skill[left] * skill[right]
        totalChemistry += chemistry
        
        left += 1
        right -= 1
    
    return totalChemistry

'''
Time Complexity: O(N log N)
- The first and most significant step is sorting the input array `skill`. In Python, this uses Timsort, which has an average and worst-case time complexity of O(N log N), where N is the number of players.
- Calculating the sum of all skills using `sum(skill)` takes O(N) time.
- The two-pointer approach involves a single `while` loop that iterates from both ends of the array towards the center. Since each pointer moves one step per iteration, the loop runs N/2 times. This traversal takes O(N) time.
- The sorting step is the bottleneck, so the overall time complexity is dominated by it.
- Therefore, the time complexity is O(N log N).

Space Complexity: O(log N) or O(N)
- The space complexity is primarily determined by the sorting algorithm used.
- Python's `sort()` method is performed in-place, but it can use auxiliary space for its implementation (Timsort). The space complexity of Timsort can range from O(log N) to O(N) in the worst case.
- Apart from the space used by sorting, the algorithm uses only a few variables (`n`, `left`, `right`, `totalChemistry`, etc.), which occupy a constant amount of space, O(1).
- Therefore, the dominant factor for space is the sorting algorithm, resulting in a space complexity of O(log N) to O(N).
'''

# Test Cases
skill1 = [3, 2, 5, 1, 3, 4]
print(dividePlayers(skill1)) # Output: 22

skill2 = [1, 2, 3, 5]
print(dividePlayers(skill2)) # Output: -1

skill3 = [10, 20]
print(dividePlayers(skill3)) # Output: 200

skill4 = [5, 5, 5, 5, 5, 5]
print(dividePlayers(skill4)) # Output: 75

skill5 = [1, 1, 2, 3]
print(dividePlayers(skill5)) # Output: -1

skill6 = [1, 1, 1, 9, 9, 9]
print(dividePlayers(skill6)) # Output: 27

skill7 = [6, 1, 5, 2]
print(dividePlayers(skill7)) # Output: 16

skill8 = [1, 4, 5, 10]
print(dividePlayers(skill8)) # Output: -1

skill9 = [10, 1, 2, 9, 3, 8, 4, 7, 5, 6]
print(dividePlayers(skill9)) # Output: 110

skill10 = [1, 10, 4, 9]
print(dividePlayers(skill10)) # Output: -1