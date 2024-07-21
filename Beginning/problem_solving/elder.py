"""
he first line contains an uppercase letter of the English alphabet, the label of the wizard that the wand obeyed at the beginning.
The second line contains an integer number N ( 1 ≤ N ≤ 100 ) , the number of duels from the text of the task.
In the next N rows there are two different uppercase letters of the English alphabet Z 1 and Z 2 separated by a space,
whereas the wizard with the label Z 1 defeated the wizard with the label Z 2 in the i th duel.
"""
#output will be current owner and count of total owners 

x= input("Enter Which Wizard :")
n = int(input("Enter No of Battles :"))

change = False 
count = 1
winner =  x

str = ""
for i in range(n):
    z = input("Enter Duels of Wizard :")
    for char in z :
        if char != ' ' :
            str += char
    if str [2*i] == winner :
        change = False
    elif str[2*i+1] == winner :
        change = True
        count += 1 
        winner = str[2*i]

print("current winner " ,winner)
print("Number of owners count",count)
