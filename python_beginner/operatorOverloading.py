# Operator Overloading

#we can use operator oveloading  to add a 
#custom way to compare these two objects

class Dog:
    # the Dog class
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def __gt__(self,other):
        return True if self.age>other.age else False 
    
    #here function gt is going to compae things 
    #as to figure out what is greater than you can
    #now we'll be able to compare
roger = Dog('Roger',8)
syd = Dog('Syd',7)

#we can use operator oveloading  to add a 
#custom way to compare these two objects
print(roger<syd)
