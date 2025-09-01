# NUMBER OF SENIOR CITIZENS

'''
You are given a 0-indexed array of strings details. Each element of details provides information about a given passenger compressed into a string of length 15. 
The system is such that:
The first ten characters consist of the phone number of passengers.
The next character denotes the gender of the person.
The following two characters are used to indicate the age of the person.
The last two characters determine the seat allotted to that person.
Return the number of passengers who are strictly more than 60 years old.
'''

def countSeniors(details):
    count = 0
    
    for detail in details:
        if int(detail[11:13]) > 60:
            count += 1
            
    return count

# Test Cases
details1 = ["7868190130M7522","5303914400F9211","9273338290F4010"]
print(countSeniors(details1)) # Output: 2

details2 = ["1313579440F2036","2921522980M5644"]
print(countSeniors(details2)) # Output: 0

details3 = ["7868190130M7522"]
print(countSeniors(details3)) # Output: 1

details4 = ["5303914400F9211"]
print(countSeniors(details4)) # Output: 1

details5 = ["9273338290F4010"]
print(countSeniors(details5)) # Output: 0

details6 = ["1234567890M6501","9876543210F7002","5555555555M8003"]
print(countSeniors(details6)) # Output: 3

details7 = ["1111111111F2001","2222222222M3002","3333333333F4003"]
print(countSeniors(details7)) # Output: 0

details8 = ["4444444444M6101","5555555555F6202","6666666666M6303"]
print(countSeniors(details8)) # Output: 3

details9 = ["7777777777F5901","8888888888M6002","9999999999F6103"]
print(countSeniors(details9)) # Output: 2

details10 = ["0000000000M9001","1111111111F9102","2222222222M9203"]
print(countSeniors(details10)) # Output: 3