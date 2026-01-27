#Decoators
#whenever we call  the function the decorator is going to called
#the decorator is function that takes a funcion ass a parmeter wraps the functioon in a
#inner function that performs the job it has to do and returns that inner funcion 
def logtime(func):
    def wrapper():
        print("Before")
        val = func()
        print("After")
    return wrapper 
@logtime
def hello():
    print("hello")

hello()
