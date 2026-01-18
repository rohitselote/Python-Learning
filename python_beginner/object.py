#objects

#everything in python is an object

#objects have attributes and methods ,can be acessed by dot operator
age=8

print(age.real)
print(age.imag)
print(age.bit_length()) #retuns the nunber of bits necessary to represent his no. in  binary notation

items=[2,3]
items.append(1)
#append and pop are methods used or object
items.pop()
print(items)
print(id(items))
#id = location of memory of particular  object

#soome oobject are mutable and some immutable
#if he  object prooides  method to change its content then it is mutable
#otherwise its immutable

