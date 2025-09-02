# UNIQUE EMAIL ADDRESSES

'''
Every valid email consists of a local name and a domain name, separated by the '@' sign. Besides lowercase letters, the email may contain one or more '.' or '+'.
For example, in "alice@leetcode.com", "alice" is the local name, and "leetcode.com" is the domain name.
If you add periods '.' between some characters in the local name part of an email address, mail sent there will be forwarded to the same address without dots in the local name. 
Note that this rule does not apply to domain names.
For example, "alice.z@leetcode.com" and "alicez@leetcode.com" forward to the same email address.
If you add a plus '+' in the local name, everything after the first plus sign will be ignored. This allows certain emails to be filtered. 
Note that this rule does not apply to domain names.
For example, "m.y+name@email.com" will be forwarded to "my@email.com".
It is possible to use both of these rules at the same time.
Given an array of strings emails where we send one email to each emails[i], return the number of different addresses that actually receive mails.
'''

# Solution 1: Using InBuilt Functions

def numUniqueEmails1(emails):
    unique = set()
    
    for email in emails:
        local, domain = email.split("@")
        local = local.split("+")[0]
        local = local.replace(".", "")
        unique.add((local, domain))
        
    return len(unique)

# Time Complexity: O(n * m) where n is the number of emails and m is the length of the longest email
# Space Complexity: O(n) since we are using a set to store the unique emails

# Solution 2: Using Manual Traverse

def numUniqueEmails2(emails):
    unique = set()
    
    for email in emails:
        i, local = 0, ""
        
        while email[i] not in ["@", "+"]:
            if email[i] != ".":
                local += email[i]
            i += 1
            
        while email[i] != "@":
            i += 1
            
        domain = email[i+1:]
        
        unique.add((local, domain))
        
    return len(unique)

# Time Complexity: O(n * m) where n is the number of emails and m is the length of the longest email
# Space Complexity: O(n) since we are using a set to store the unique emails

# Test Cases
emails1 = ["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]
print(numUniqueEmails2(emails1)) # Output: 2

emails2 = ["a.b+c@x.com","ab@x.com"]
print(numUniqueEmails2(emails2)) # Output: 1

emails3 = ["user+tag+spam@domain.com","user@domain.com"]
print(numUniqueEmails2(emails3)) # Output: 1

emails4 = ["user.name+foo@domain.com","username@domain.com","user.name@another.com"]
print(numUniqueEmails2(emails4)) # Output: 2

emails5 = ["u@d.com","u+xyz@d.com","u.x.y.z@d.com"]
print(numUniqueEmails2(emails5)) # Output: 1

emails6 = ["test.email+alex@leetcode.com","test.email.leet+alex@code.com"]
print(numUniqueEmails2(emails6)) # Output: 2

emails7 = ["a@b.com","a@b.com","a+b@b.com","a.b@b.com"]
print(numUniqueEmails2(emails7)) # Output: 1

emails8 = []
print(numUniqueEmails2(emails8)) # Output: 0

emails9 = ["simple@example.com"]
print(numUniqueEmails2(emails9)) # Output: 1

emails10 = ["x.y+z@d.com","xy@d.com","x.y@d.com","x.y+abc@d.com","xy+def@d.com"]
print(numUniqueEmails2(emails10)) # Output: 1