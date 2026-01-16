#functions
#a se of instrucion we can run when needed 
def hello():
    print('hello !')
hello()
def hola(name="amigo"):
    #calling the functions using arguments
    print("hola " + name)
#we call the parameters the value accepted by
#funcion inside the function defination
hola("mark")
#and arguments are values we pass to the function
#we can set default value for a function
hola()  
def hi(name,age):
    print("hi "+ name + " you are " +str(age) +" year old.")

hi("mark",39)

def change(value):
    value=2 #it doesnt change anything outside  the function

val=1

print(change(val)) #it will print none

print(val) #it will print 1


def changee2(value1):
    value1["name"]="syd"
val1={"name":"Beau"}
print(changee2(val1))
print(val1)


#variable scope
age=8
def test():
    print(age)

test()
