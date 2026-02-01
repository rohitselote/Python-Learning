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
# try:
#     result=2/0

# except ZeroDivisionError:
#     print("cannot devide by zero!")
# finally:
#     result=1

# print(result)
# try:
#     raise Exception("An Error!")

#this raises an general exception
#and you can intercept it
# except:
#     print("error")


#you can also define your own exception class extending
#from exception
class DogNotFoundException(Exception):
    print("inside")



try:
    raise DogNotFoundException()
except DogNotFoundException:
    print('Dog not found !')
