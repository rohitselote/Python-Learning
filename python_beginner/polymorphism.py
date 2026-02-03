#Polymorphism

class Dog:
    def eat(self):
        print("eating dog food")

class Cat:
    def eat(self):
        print("eating cat food")

animal1=Dog()
animal2=Cat()

#different classes to share the same method name while having unique implementations

animal1.eat()
animal2.eat()

#we build a generalized interface and 
#we do not need to know that animal is a cat o dog 
