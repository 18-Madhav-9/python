""" 
Three Cups Left = 1 , middle = 2 , right = 3
A = left to middle  B = middle to right C= right to left 
orginal ball loaction at left 

"""

ball_location = 1

raw_input = input("Enter Order :")

for i in raw_input :
    if i == 'A' and ball_location == 1 :
        ball_location = 2 
    elif i == 'B' and ball_location == 2 :
        ball_location = 3
    elif i == 'C' and ball_location == 3 :
        ball_location = 1 

print(ball_location)