# class Car:
#     def __init__(self):
#         self.brand="BMW"
#         self.model="m5"

#     def display(self):
#         print(f"brand : {self.brand} model : {self.model}")

# s=Car()
# s.display()






# class Car:
#     def __init__(self,brand,model,yr):
#         self.brand=brand
#         self.model=model
#         self.yr=yr
#         print(self.brand,self.model,self.yr)

# s=Car("mic",34,45)

# class Person:
#     def name(self):
#         print("hello")

# class Employee(Person):
#     def salary(self):
#         print("hi")

# class Manager(Employee):
#     def role(self):
#         print("ham")

# m = Manager()
# m.role()
# m.salary()
# m.name()


# class Father:
#     def skills(self):
#         print("hello")

# class Mother:
#     def hobby(self):
#         print("hi")

# class Manager(Mother,Father):
#     def interest(self):
#         print("ham")

# m = Manager()
# m.role()
# m.salary()
# m.name()

# class Father:
#     def skills(self):
#         print("hello")

# class Child1(Father):
#     def hobby(self):
#         print("hi")

# class Child2(Father):
#     def interest(self):
#         print("ham")

# m = Child1()
# N= Child2()
# m.skills()
# N.skills()


# class Parent1:
#     def skills2(self):
#         print("hew")


# class Child1(Parent1):
#     def hobby(self):
#         print("hi")

# class Child2(Parent1):
#     def interest(self):
#         print("ham")

# class Parent2(Child1,Child2):
#     def skills1(self):
#         print("hello")

# r=Parent2()
# m = Child1()
# N= Child2()

# r.interest()






                                           #ENCAPSULATION


                                    # Class = methods+variables

# class Students:
#     def __init__(self,name,marks):
#         self.__marks = marks
#         self.name= name
    
#     def show(self):
#         print("Name",self.name)
#         print("Marks",self.__marks)
#     def set_marks(self,m):
#         if m>=0:
#             self.__marks=m

# s=Students("John",90)
# s.show()





                      #POLYMORPHISM


#same method name ,but different  behaviour

# class Animal:
#     def sound(self):
#         print("Animal make sound")

# class Dog:
#     def sound(self):
#         print("Dog barks")

# class Cat:
#     def sound(self):
#         print("Cat meows")

# d = [Animal(),Dog(),Cat()]

# for a in d:
#     a.sound()




                             #Dunder method  

#__init__
#__str__ = Decides what to show when we print an object

# class BankAccount:
#     def __init__(self,name,balance):
#         self.name=name
#         self.balance=balance
#     def __str__(self):
#         return self.name + str(self.balance)
    
# s=BankAccount("mog","100")
# print(s)


#__len__ = used when len() is called 

# class Mydata:
#     def __init__(self,data):
#         self.data=data
#     def __len__(self):
#         return len(self.data)
# d=Mydata([1,2,3])

# print(len(d))


#__add__ = +

# class Number:
#     def __init__(self,x):
#         self.x=x
#     def __add__(self,n2):
#         return self.x + n2.x
# n1=Number(20)
# n2 =Number(10)
# print(n1 + n2)

# class Number:
#     def __init__(self,x):
#         self.x=x
#     def __sub__(self,n2):
#         return self.x - n2.x
# n1=Number(20)
# n2 =Number(10)
# print(n1 - n2)


# class Number:
#     def __init__(self,x):
#         self.x=x
#     def __truediv__(self,n2):
#         return self.x / n2.x
# n1=Number(20)
# n2 =Number(10)
# print(n1 / n2)

# class Number:
#     def __init__(self,x):
#         self.x=x
#     def __mul__(self,n2):
#         return self.x * n2.x
# n1=Number(20)
# n2 =Number(10)
# print(n1 * n2)


# class Number:
#     def __init__(self,x):
#         self.x=x
#     def __eq__(self,n2):
#         return self.x == n2.x
# n1=Number(20)
# n2 =Number(10)
# print(n1 == n2)