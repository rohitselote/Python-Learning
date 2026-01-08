# fruits=["apple","banana","cherry"]
# upper_list=[i.upper() for i in fruits]
# print(upper_list)
# text="a1b2c3d4e5f6asg67"
# dig = [i for i in text if i.isdigit()]
# print(dig)

# sentence="python is very easy to learn"
# new=(sentence.split(" "))
# print(new)
# hello = [i[0] for i in new]
# print(hello)

# hi="whiteboard"
# vovels=['a','e','i','o','u']
# hello=[ i for i in hi if i in vovels]
# print(hello)

# hi=['1','2','3','4','5','6','7','8','9','10']
# hello = (i**2 for i in hi if i%2==0)
# print(hello)

# sen="learn python easily"
# m=sen.split(" ")
# g=[i[::-1] for i in sen]

# print(g)


# hi=[(i,i**2) for i in range(1,6)]
# print(hi)

# sen="this is a test sentence"
# r=sen.split(" ")
# print(r)

# hi=[i for i in r  if len(i)>3]
# print(hi)

# items=[1,"hello",3,5,5,"world"]
# y=[i for i in items if type(i)==int]
# print(y)

# char=['A','B','C']
# y=[ord(i) for i in char ]
# print(y)


# keys=['a','b','c']
# value=[1,2,3]
# my_dict={ k:v for k,v in zip(keys,value)}
# print(my_dict)

# word=["madam","racecar","apple","noon"]
# ho=[i for i in word if i==i[::-1]]
# print(ho)

# x=[5,3,88,90,1]
# print(max(x))
# print(min(x))
# x=["Raj","Vishal","a"]
# print(max(x))
# print(min(x))
# x=[4,5,7,89,90,34]
# max=x[0]
# x.sort()
# print(x[-1])
# max=x[0]
# for i in x:
#     if(i>max):
#         max=i
# print(max)
# a=["hello","stu"]
# b=','.join(a)
# print(a)
# print(b)

# def add():
#     a=int(input("Enter A:"))
#     b=int(input("Enter B:"))
#     c=a+b
#     print(c)
# add()
# def add(a,b):
#     print(a+b)
# add(int(input()),int(input()))


# def add(a,b,c=None):
#     if c==None:
#         print("Sum of 2 no",a+b)
#     else:
#         print("Sum of 3 no",a+b+c)
# add(1,2)
#keyword only argument 
# def add(*,a,b,c=None):
#     if c==None:
#         print("sum of 2 no",a+b)
#     else:
#         print("sum of 3 no",a+b+c)
# add(b=5,a=10)

# def add(x,y,*a):
#     print(x)
#     print(y)
#     print(a)

# add(10,2,4.5,8,98,)

#kw argument (variabble key word argument)
# def add(**a):
#     print(a) 

# add(x=5,y=10)

# def fun(x,/,y):
#     print(x,y)
# fun(10,y=10)

# def fun(a,b,/):
#     print(a,b)
# print(1,2)

# def fun(a,/,b,*,c):
#     print(a,b,c)

# fun(10,20,c=30)

# fun(100,b=30,c=19)


# def fun():
#     x=20
#     print(x)

# function inside  function is called helper function

# def msg():
#     def x100linecode():
#         print("100 line code")
#     print("Some code")
#     x100linecode()
#     print("Some code")
#     x100linecode()
# msg()

#lambda function (anonymous function)

# sq=lambda x: x*x
# print(sq(5))

# to=lambda x:10+x
# print(to(5))

# o = lambda n1,n2: n1 if n1> n2 else n2
# print(o(1,3))

# g = lambda no:[i*i for i in range(1,no+1)]
# print(g(5))

# nums = [1,2,3,4]
# sq = list(map(lambda x:x*x,nums))
# print(sq)

# nums = [1,2,3,4,5,6]
# even=list(filter(lambda x:x%2==0,nums))
# print(even)

#example


# li=[1,2,3]
# d=list(map(lambda x:x+1,li))
# print(d)

# str=["10","20","30","40"]
# d=list(map(lambda x:int(x),str))
# print(d)


# str=["raj","vishal","kunal"]
# d=list(map(lambda x:x.upper(),str))
# print(d)

# str=[' hi ',' hello ']
# d=list(map(lambda x:x.strip(),str))
# print(d)

# str=[' 5 ',' raj ',' 94 ']
# d=list(map(lambda x:int(x),(filter(lambda x: x.strip().isdigit(),str))))

# print(d)

# str=[1,2,3,4,5,6,7,8,9]
# d=list(filter(lambda x:x%2==0,str))
# print(d)

# str=["madam","hello","level"]
# d=list(filter(lambda x:x==x[::-1],str))
# print(d)

# str=["jay","om","piyush","vikas","suraj"]
# d=list(filter(lambda x: x if len(x) > 3 else 0, str))
# print(d)

# li=[5,6,7,10,11,55]
# d=list(filter(lambda x:x%5==0,li))
# print(d)

# li=["Apple","Banana","Vijay","aakash","Abhi"]
# d=list(filter(lambda x:x[0] in ('aA'),li))
# print(d)

# li=[20,35,40,60,55,90]
# d=list(filter(lambda x:x>=40,li))
# print(d)



# li=[{'roll':3,'age':30,'name':"jay"},
#     {'roll':5,'age':15,'name':"om"},
#     {'roll':6,'age':40,'name':"Vijay"}]
# d=list(filter(lambda x:x['age']>18 ,li))
# print(d)



#Exception Handling

# try:
#     a=10
#     b=0
#     print(a/b)
# except:
#     print("Error Occured")

# try:
#     x=int("hello")
#     print(x)
# except ValueError :
#     print("value error occured")

# try:
#     a=10
#     b=int(input("Enter Number:"))
#     print(a/b)
# except ZeroDivisionError:
#     print("cannot divide bt zero")
# except ValueError:
#     print("invalid input")

# example

# try:
#     a=10
#     b=2
#     print(a/b)

# except ZeroDivisionError:
#     print("Error")
# else:
#     print("No erro occured")

# try:
#     print("Hello")
# except:
#     print("Except block")
# finally:
#     print("finally")