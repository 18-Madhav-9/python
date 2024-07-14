"""
number of megabytes of data that user uses in each of
the first n months. Our task is to determine the number of megabytes avail-
able for the following month
"""

x = int(input("Enter Number of monthly Data Given :"))
n = int(input("Enter number of months in data used :"))

data_avail = 0 

for i in range(n):
    data_used = int(input("Enter data each month used :"))
    data_avail = x + data_avail - data_used

print("data available for next month ", data_avail + x )
