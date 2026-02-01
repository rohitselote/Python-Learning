#exceptions
#so for exception handling you would wrap lines of code in a try block
#and inside the block you will put the lines of code then if an error occurs
#python will alert you and you can determine which kind of error occured using an except block 
#try:
    #some lines of code
#except <ERROR1>:
    #handler <ERROR1>
#except <ERROR2>:
    #handler <ERROR2>
#else:
    #it will run if no exceptions are found

#finally:
    #always run at the end whether there are
    # exceptions or not 
try:
    result=2/0

except ZeroDivisionError:
    print("cannot devide by zero!")
finally:
    result=1

print(result)
