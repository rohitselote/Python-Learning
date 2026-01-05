dogs=["roger",1,"syd",True,"Quincy",7]
print(dogs) #"roger",1,"syd",True,"Quincy",7
dogs[2]="beau"
print(dogs) #"roger",1,"beau",True,"Quincy",7
dogs += ["judah",5]
print(dogs) #append  "roger",1,"beau",True,"Quincy",7,"judah",5
dogs.insert(2,"Test")
print(dogs)#  "roger",1,"Test","beau",True,"Quincy",7,"judah",5
dogs.remove("Quincy")
print(dogs)#  "roger",1,"Test","beau",True,7,"judah",5



print(dogs.pop())

print(dogs)

#List Sorting
items=["roger","Beau","syd","True","Quincy"]

print(items)

#using global function sorted 
print(sorted(items,key=str.lower)) 



itemscopy = items[:] #it will copy list at the instance



#sorting not supported between instances of 'int' and 'str'
items.sort()
print(items) #in str their is also priority to words start from Capital letter.

#to create non caring sorting about lower case and upper case
items.sort(key=str.lower)
print(items)
 

#it will print list content copied at that instance.
print(itemscopy)

