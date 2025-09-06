# CAN PLACE FLOWERS

'''
You have a long flowerbed in which some of the plots are planted, and some are not. 
However, flowers cannot be planted in adjacent plots.

Given an integer array flowerbed containing 0's and 1's, 
where 0 means empty and 1 means not empty, and an integer n, 
return true if n new flowers can be planted in the flowerbed without 
violating the no-adjacent-flowers rule and false otherwise.
'''

# Solution 1: Brute Force
def canPlaceFlowers1(flowerbed, n):
    flowerbed = [0] + flowerbed + [0]
    
    for i in range(1, len(flowerbed) - 1):
        if flowerbed[i - 1] == 0 and flowerbed[i] == 0 and flowerbed[i + 1] == 0:
            flowerbed[i] = 1
            n -= 1
            
    return n <= 0

'''
Time Complexity: O(n) where n is the number of plots in the flowerbed.
We iterate through the flowerbed once.
Space Complexity: O(n) where n is the number of plots in the flowerbed.
We create a new list that is a copy of the original flowerbed with padding.
'''

# Solution 2: One-Pass
def canPlaceFlowers2(flowerbed, n):
    length = len(flowerbed)
    
    for i in range(length):
        if (flowerbed[i] == 0 and (i == 0 or flowerbed[i - 1] == 0) and (i == length-1 or flowerbed[i + 1] == 0)):
            flowerbed[i] = 1
            n -= 1
            
    return n <= 0

'''
Time Complexity: O(n) where n is the number of plots in the flowerbed.
We iterate through the flowerbed once.
Space Complexity: O(1)
We do not use any extra space that scales with the input size. The modifications are done in-place.
'''

# Test Cases
flowerbed1 = [1, 0, 0, 0, 1]
n1 = 1
print(canPlaceFlowers1(flowerbed1, n1))  # Output: True

flowerbed2 = [1, 0, 0, 0, 1]
n2 = 2
print(canPlaceFlowers1(flowerbed2, n2))  # Output: False

flowerbed3 = [0, 0, 0, 0, 0]
n3 = 3
print(canPlaceFlowers1(flowerbed3, n3))  # Output: True

flowerbed4 = [0]
n4 = 1
print(canPlaceFlowers1(flowerbed4, n4))  # Output: True

flowerbed5 = [1]
n5 = 0
print(canPlaceFlowers1(flowerbed5, n5))  # Output: True

flowerbed6 = [0, 0, 1, 0, 1]
n6 = 1
print(canPlaceFlowers1(flowerbed6, n6))  # Output: True

flowerbed7 = [1, 0, 0, 0, 0, 1]
n7 = 2
print(canPlaceFlowers1(flowerbed7, n7))  # Output: False

flowerbed8 = [0, 0, 0]
n8 = 2
print(canPlaceFlowers1(flowerbed8, n8))  # Output: True

flowerbed9 = []
n9 = 1
print(canPlaceFlowers1(flowerbed9, n9))  # Output: False

flowerbed10 = [1, 0, 1, 0, 1]
n10 = 0
print(canPlaceFlowers1(flowerbed10, n10)) # Output: True