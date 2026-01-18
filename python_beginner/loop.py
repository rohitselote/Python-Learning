#loops
#in pyhon therre are two kind of looops
# condition = True
# while condition==True:
#     print("True condition")

count=0
#its use too stop iteration afteer some n. of  cycle
while count<10:
    print(count)
    count+=1
print("loop  over")

#its commonly used to iterate items in the list
items=[1,2,3,4]
for i in items:
    print(i)
print("over")
#yu can also iterate using  range function
for item in range(0,10,2):
    print(item)
print("over")

things=[1,2,3,4,5,6]
#wrapping the functionn in enumerate function
for j in enumerate(things):
    print(j)
thing=['leon','mark','alp']
for index,j in enumerate(thing):
    print(index,j)
