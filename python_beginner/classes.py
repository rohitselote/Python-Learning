#class
#object is an instance of classes


#inheritance
class animals:
    def walk(self):
        print("Walking")

class dog(animals): #dog class is  goin to inherit from animal class

    #speial type of method  called __init__ which is
    #called constructor
    def __init__(self,name,age):
        self.name=name
        self.age=age
    #so we can use this  constructor to initialize one more
    #property to initialize

    def bark(self): #self is an argument of the method  will point to the current object instance
        
        print("Wooof!")

roger = dog("roger",8)
print(type(roger))

print(roger.name)
print(roger.age)
print(roger.bark())
print(roger.walk())

#in the end it gonna print None
#cause function/mehod is not return anything
#for avoiding it do  use of return instead of print
