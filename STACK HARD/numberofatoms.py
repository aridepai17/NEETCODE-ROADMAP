# NUMBER OF ATOMS

'''
Given a string formula representing a chemical formula, return the count of each atom.
The atomic element always starts with an uppercase character, then zero or more lowercase letters, representing the name.
One or more digits representing that element's count may follow if the count is greater than 1.
If the count is 1, no digits will follow.
For example, "H2O" and "H2O2" are possible, but "H1O2" is impossible.
Two formulas are concatenated together to produce another formula.
For example, "H2O2He3Mg4" is also a formula.
A formula placed in parentheses, and a count (optionally added) is also a formula.
For example, "(H2O2)" and "(H2O2)3" are formulas.
Return the count of all elements as a string in the following form: 
- the first name (in sorted order), followed by its count (if that count is more than 1), followed by the second name (in sorted order), followed by its count (if that count is more than 1), and so on.
The test cases are generated so that all the values in the output fit in a 32-bit integer.
'''

from collections import defaultdict

def countOfAtoms(formula):
    """Return a canonical string representing the total count of each atom
    present in the given chemical *formula*.

    Algorithm overview (single left-to-right pass):
    1. Maintain a *stack* of defaultdict(int).  Each level of the stack
       corresponds to the current parentheses depth.
       • `stack[-1]` always holds the counts for the sub-formula we are
         currently parsing.
    2. When we encounter an opening parenthesis '(', push a **new** empty
       defaultdict onto the stack so future counts are isolated inside the
       group.
    3. When we encounter a closing parenthesis ')', pop the top defaultdict
       (sub-formula counts), read the integer multiplier that immediately
       follows the ')', multiply every count inside the popped map by that
       multiplier, and merge the scaled counts into the *parent* map now at
       `stack[-1]`.
    4. When we read an element symbol (uppercase followed by lowercase*),
       read its optional numeric multiplier; default to 1; add the count to
       `stack[-1]`.

    The final result lives in `stack[0]` after the loop.  We then build the
    output string by concatenating element symbols in *alphabetical* order
    followed by their counts (omit count when it is 1).
    """
    
    stack = [defaultdict(int)]
    i = 0
    
    while i < len(formula):
        if formula[i] == "(":
            # Start a new scope for the sub-formula inside parentheses
            stack.append(defaultdict(int))
        elif formula[i] == ")":
            # Close current parentheses scope and collect its counts
            currentMap = stack.pop()
            count = ""
            # Read full integer immediately following ')' (if any)
            while i + 1 < len(formula) and formula[i + 1].isdigit():
                count += formula[i + 1]
                i += 1
            count = 1 if not count else int(count)
            
            # Merge scaled counts into parent scope
            previousMap = stack[-1]
            for element in currentMap:
                previousMap[element] += currentMap[element] * count
        else:
            # Parse element symbol: uppercase followed by zero or more lowercase letters
            element = formula[i]
            j = i + 1
            # Consume trailing lowercase letters (part of the symbol)
            while j < len(formula) and formula[j].islower():
                j += 1
            element = formula[i:j]

            # Parse optional numeric count following the element symbol
            countNo = ""
            # Read full integer multiplier for this element (if any)
            while j < len(formula) and formula[j].isdigit():
                countNo += formula[j]
                j += 1
            count = int(countNo) if countNo else 1

            # Record element count in current (innermost) scope
            currentMap = stack[-1]
            currentMap[element] += count

            # Move i to the position before j because the outer loop will increment it
            # Step back so outer loop's i += 1 lands on first unprocessed char
            i = j - 1
        i += 1
        
    # All parsing done; aggregate counts are in bottom of stack
    result = stack[-1]
    final = ""
    
    # Build the canonical output string (elements in alphabetical order)
    for element in sorted(result.keys()):
        final += element
        if result[element] > 1:
            final += str(result[element])

    return final

'''
Time Complexity: O(n)
Let n be the length of the formula string.
- We iterate through the formula string once with a single while loop, processing each character at most once.
- For each character, we perform constant-time operations:
  - Pushing/popping from the stack: O(1)
  - Reading digits or lowercase letters: Each character is read once, contributing to the overall O(n)
  - Dictionary operations (insertion, access): O(1) on average
  - Merging counts when closing parentheses: Each element is processed proportional to its occurrences
- After parsing, we sort the elements in the result dictionary. In the worst case, there could be O(n) unique elements, so sorting takes O(n log n).
- Building the final string involves iterating through sorted elements, which is O(n) in the worst case.
- The overall time complexity is dominated by O(n) for parsing and O(n log n) for sorting, giving us O(n log n).
- However, in practice, the number of unique elements is typically much smaller than n, making the effective complexity closer to O(n).

Space Complexity: O(n)
- The stack can have at most O(d) levels, where d is the maximum depth of nested parentheses. In the worst case, d can be O(n) (e.g., "((((A))))").
- Each level in the stack is a defaultdict that stores element counts. Across all levels, the total number of element entries is bounded by O(n).
- The result dictionary stores the final counts of unique elements, which is at most O(n).
- The final output string has length proportional to the number of unique elements and their counts, which is O(n) in the worst case.
- Therefore, the overall space complexity is O(n).
'''

# Test Cases
formula1 = "H20"
print(countOfAtoms(formula1)) # Output: "H2O"

formula2 = "Mg(OH)2"
print(countOfAtoms(formula2)) # Output: "H2MgO2"

formula3 = "K4(ON(SO3)2)2"
print(countOfAtoms(formula3)) # Output: "K4N2O14S4"

formula4 = "Ca(OH)2"
print(countOfAtoms(formula4)) # Output: "CaH2O2"

formula5 = "((N2)3)4"
print(countOfAtoms(formula5)) # Output: "N24"

formula6 = "Be32"
print(countOfAtoms(formula6)) # Output: "Be32"

formula7 = "H2O2He3Mg4"
print(countOfAtoms(formula7)) # Output: "H2He3Mg4O2"

formula8 = "(H2O2)"
print(countOfAtoms(formula8)) # Output: "H2O2"

formula9 = "((H2O)2)"
print(countOfAtoms(formula9)) # Output: "H4O2"

formula10 = "C6H12O6"
print(countOfAtoms(formula10)) # Output: "C6H12O6"