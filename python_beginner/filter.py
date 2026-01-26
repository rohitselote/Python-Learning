#filter()
numbers=[1,2,3]
#filter takes an iterable and returns an iterrable object which is  another iterble 
#but witout some of the original items so you can do  so byreurnin true or false
#from the filter function
# def isEven(n):
#     return  n%2==0

result=filter(lambda a : a%2==0 ,numbers)
print(list(result))
