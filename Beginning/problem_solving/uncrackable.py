# design a password verificator
"""
password must be a string between 8 and 12 characters long (inclusive),
such that every character is either a lowercase letter (a … z), uppercase letter (A … Z), or digit (0 … 9).
Furthermore, it must contain at least three lowercase letters, 
at least two uppercase letters, and at least one digit.

"""
password = input("Enter your password  : ")

count = 0
count_upper = 0
count_lower = 0 
count_digit = 0

for i in password :
    if i.islower() :
        count_lower += 1
        count += 1
    elif i.isupper() :
        count_upper += 1
        count += 1
    elif i.isdigit() :
        count_digit +=  1
        count += 1
    else :
        count += 1

if count_lower >=3 and count_upper >=2  and count_digit >=1 :
    if (8 <= count <= 12) :
        print(" Valid Password ")
    else :
        print(" Invalid Password")
else :
    print("Invalid Password")