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

dogs[3:1]=["Test1","Test2","Ts3"]
#[3:1] 3 is no. of initial index and 1 is the number of times it will be printed 
print(dogs)
dogs[3:2]=["Test1","Test2","Ts3"]
#[3:1] 3 is no. of initial index and 2 is the number of times it will be printed 
print(dogs)
dogs[3:3]=["Test1","Test2","Ts3"]
#[3:1] 3 is no. of initial index and 3 is the number of times it will be printed 
print(dogs)
print(dogs.pop())

print(dogs)

#List Sorting
items=["roger","Beau","syd","True","Quincy"]

print(items)

#using global function sorted 
print(sorted(items,key=str.lower)) 
#sorted() function maintains original data sequence in original list and 
#creates a new list in which sorted data is arranged in sorted format such that 'key'. 



itemscopy = items[:] #it will copy list at the instance



#sorting not supported between instances of 'int' and 'str'
items.sort()
print(items) #in str their is also priority to words start from Capital letter.

#to create non caring sorting about lower case and upper case
items.sort(key=str.lower)
print(items)
 

#it will print list content copied at that instance.
print(itemscopy)





