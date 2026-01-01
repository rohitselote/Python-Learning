print(1 or 0) #1
print(False or 'hey') #hey
print('hi' or 'hey') #
#or using an expession returns the 
# value of first operator 
# operand that is not false value or a falsie value
# otherwise it returns  the last operand
print([] or False) #False
print(False or []) #[]
# if it is empty bracket it will be considered as false
#if it is false last value will be selected