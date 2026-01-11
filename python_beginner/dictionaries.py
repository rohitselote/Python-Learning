#dictionaries
dog = {"name":"rager","age":18,"color":"green"}
print(dog.keys())
print(list(dog.keys()))
print(dog.values)
print(list(dog.values()))
print(list(dog.items()))
print(dog.get("name"))
print(dog.get("color"))
print(dog.get("color","brown"))
print(dog.pop("name"))
print(dog)
print(dog.popitem()) #remove the last item
dog["Favourite food"]="meat"
del dog["age"]
go=dog.copy()
