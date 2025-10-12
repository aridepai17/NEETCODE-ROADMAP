# FRUITS INTO BASKETS

'''
You are visiting a farm that has a single row of fruit trees arranged from left to right.
The trees are represented by an integer array fruits where fruits[i] is the type of fruit the ith tree produces.
You want to collect as much fruit as possible. 
However, the owner has some strict rules that you must follow:
- You only have two baskets, and each basket can only hold a single type of fruit. 
- There is no limit on the amount of fruit each basket can hold.
- Starting from any tree of your choice, you must pick exactly one fruit from every tree (including the start tree) while moving to the right. 
- The picked fruits must fit in one of your baskets.
- Once you reach a tree with fruit that cannot fit in your baskets, you must stop.
Given the integer array fruits, return the maximum number of fruits you can pick.
'''

def totalFruit(fruits):
    hashMap = {}
    total = 0
    left = 0
    result = 0
    
    for right in range(len(fruits)):
        hashMap[fruits[right]] = hashMap.get(fruits[right], 0) + 1
        total += 1
        while len(hashMap) > 2:
            fruit = fruits[left]
            hashMap[fruit] -= 1
            total -= 1
            left += 1
            if not hashMap[fruit]:
                hashMap.pop(fruit)               
        result = max(result, total)

    return result

'''
Time Complexity: O(n)
The outer for loop runs for all elements of the fruits array, and the inner while loop processes each element at most once.
This gives us a total time complexity of O(n + n), which is asymptotically equivalent to O(n).
The right pointer iterates from left to right, and the left pointer also iterates from left to right.
Each element is visited by the right pointer once and the left pointer at most once.

Space Complexity: O(1)
We use a hash map to store the frequency of fruit types.
In any given window, we can have at most two types of fruits. The while loop ensures that if we have more than two types,
we shrink the window. So, the hash map will store at most 3 fruit types at any given time.
This means the space required is constant, not dependent on the input size.
Therefore, the space complexity is O(1).
'''

# Test Cases
fruits1 = [1,2,1]
print(totalFruit(fruits1)) # Output: 3

fruits2 = [0,1,2,2]
print(totalFruit(fruits2)) # Output: 3

fruits3 = [1,2,3,2,2]
print(totalFruit(fruits3)) # Output: 4

fruits4 = [3,3,3,3,3]
print(totalFruit(fruits4)) # Output: 5

fruits5 = [1,0,1,0,1,0]
print(totalFruit(fruits5)) # Output: 6

fruits6 = [4, 4, 1, 2, 1, 2, 1, 2]
print(totalFruit(fruits6)) # Output: 6

fruits7 = []
print(totalFruit(fruits7)) # Output: 0

fruits8 = [5]
print(totalFruit(fruits8)) # Output: 1

fruits9 = [0, 1, 2, 2, 3, 3, 2, 2, 2, 4]
print(totalFruit(fruits9)) # Output: 5

fruits10 = [3, 3, 3, 1, 2, 1, 1, 2, 3, 3, 4]
print(totalFruit(fruits10)) # Output: 5