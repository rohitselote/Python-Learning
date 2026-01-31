
#annotations
#python is dynamically typed
#so we do not have to specify the type of a variable or
#parameter or a function return value 
#annotations allows us to optionally do that
def increment(n: int) -> int:
#we are going to specify that this function receives
# an int and then its also going to return an end 
# you can do the same things with variables
    return n+1

count :int = 0
#we are specifying that this integer goiing to be an integer
# python will atually ignore this annotation a seperate tool 
# #mypi can be run stand alone or integreted by IDEs  
