# count the number of available parking space 
""" 
first line contains n ,  the number of parking spaces 
'C' represent car present and '.' means empty space
second line contains string of characters for yesterday information 
third line contains string of characters for today information  
"""
# output count parkin space that were occupied on both days 

n = int(input("Enter Number of parkign space - "))
yesterday = input("Enter Yesterdat Information : " )
today = input("Enter Today Information :")

park_count = 0 

for i in range(n) :
    if yesterday[i].lower() == 'c' and today[i].lower() == 'c' :
        park_count += 1

print(park_count) 
