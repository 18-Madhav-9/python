def power_with_stack(a ,b) :
    stack = [] 
    while b > 1 :
        if ( b % 2 == 0 ) :
            stack.append("square")
            b //=2 
        else :
            stack.append("multiply")
            b -=1 

    power = a
    while stack :
        var = stack.pop()
        if var == "square" :
            power *= power
        else :
            power *= a

    return power

print(power_with_stack(2,4)) 




