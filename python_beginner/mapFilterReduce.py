#map()
#lobal functions ,we can use withh collection

#map()
#it is used to  run a function upon  each item in an iterable item in a list
#and create a new list with same no. of items but the values of each item  can  be
numbes=[1,2,3,4]
# def double(a):
#     return a*2

# result=map(double,numbes)
result=map(lambda a : a*2, numbes )

#when the function is one  liner so its common too use lambda function

print(list(result))
#so whenever you want to do run a function n a each item in a list you can use map#map ,Filter , Reduce
