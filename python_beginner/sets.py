#sets
set1={"Roger","Beau"}
set2={"Roger","Luna"}
set3={"Beau"}

intersect = set1 & set2
#intersection of two sets
print(intersect)

union = set1 | set2
#union of two sets
print(union)

#difference of two sets
difference = set1-set2
print(difference)

#you can check a set is a superset of another
supa=set1>set3
print(supa)

#you can also get a list from the items in a set
# by passing the set list to the constructor 
print(list[set1]) 
