callStack = []  # The explicit call stack, which holds "frame objects"
callStack.append({'returnAddr': 'start', 'number': 5})  # "Call" the factorial(5)
returnValue = None

while len(callStack) > 0:
    # Get current function frame
    number = callStack[-1]['number']
    returnAddr = callStack[-1]['returnAddr']
    
    if returnAddr == 'start':
        if number == 1:
            # BASE CASE
            returnValue = 1
            callStack.pop()  # "Return" from function
            continue
        else:
            # RECURSIVE CASE
            callStack[-1]['returnAddr'] = 'after recursive call'
            # "Call" factorial(number - 1)
            callStack.append({'returnAddr': 'start', 'number': number - 1})
            continue

    elif returnAddr == 'after recursive call':
        returnValue = number * returnValue  # Multiply with the return from deeper call
        callStack.pop()  # "Return" from function
        continue

# Final result
print(returnValue)

