# n= int(input("Enter number"))
# n=str(n)
# p = n[::-1]
# if n==p:
#     print("yes")
# else:
#     print("no")






#armstrong

# num= int(input("Enter number"))
# rev= 0
# temp=num
# z=str(num)
# x=len(z)
# while num>0:
#     digit = num%10
#     rev = rev +digit**x
#     num= num//10

# if temp == rev:
#     print("yes")
# else:
#     print("no")
    
# class Node:
#     def __init__(self,data):
#         self.data=data
#         self.next=None
# n1=Node(5)
# n2=Node(10)
# n3=Node(15)

# n1.next=n2
# n2.next=n3

# t=n1
# while t!=None:
#     print(t.data,end=" ")
#     t=t.next
 


#  



# class Node:
#     def __init__(self,data):
#         self.data=data
#         self.next=None
# n1=Node(5)
# n2=Node(10)
# n3=Node(15)

# n1.next=n2
# n2.next=n3

# print(n1.next.data)
# print(n1.next.next.data)

# class Node:
#     def __init__(self,data):
#         self.data = data
#         self.next = None

# n1 = Node(5)
# n2 = Node(10)
# n3= Node(15)

# print(n1.data)
# print(n2.data)
# print(n3.data)




# class Node:
#     def fun1(self):
#         self.x=50
#     def fun2(self):
#         self.y=100

# n1=Node()
# n1.fun1()
# n1.fun2()
# print(n1.x)
# print(n1.y)



# class Node:
#     def __init__(self,data):
#         self.data =data
#         self.next =None
# head=Node(5)
# head.next=Node(10)
# head.next.next=Node(10)
# head.next.next.next=Node(30)

# t=head
# while t!=None:
#     print(t.data,end=" ")
    
class Node:
    def __init__(self,data):
        self.data =data
        self.next =None
class SingyLinkedList:
    def __init__(self):
        self.head=None
    def InsertAtFirst(self):
        n=Node(int(input("Enter data")))
        n.next=self.head
        self.head=n
    def DisplayNode(self):
        t=self.head
        if t==None:
            print("No node available")
        else:
            while t!=None:
                print(t.data)
                t=t.next

    def InsertNodeAtLast(self):
        if self.head==None:
            self.head=int(input("Enter data:"))
        else:
            t=self.head
            while t.next != None:
                t=t.next
                t.next=Node(int(input("Enter Data:")))

    def DeleteFirstNode(self):
        if self.head==None:
            print("No Node")
        else:
            temp=self.head
            self.head=self.head.next
            temp=None

    def CountNode(self):
        t=self.head
        if self.head==None:
            print("No node")
        else:
            count=1
            while t!=None:
                t=t.next
                count+=1
                print("Count Node is :",count)

    def sum(self):
        t=self.head
        if self.head==None:
            print("No Node")
        else:
            sum=0
            while t!=None:
                sum=t.data
                t=t.next
                print(sum)
    def min(self):
        t=self.head
        if self.head==None:
            print("No Node")
        else:
            min=self.head.data
            while t!=None:
                if(t.data<min):
                    min=t.data
                else:
                    t=t.next

    def max(self):        
        t=self.head
        if self.head==None:
            print("No Node")
        else:
            max=self.head.data
            while t!=None:
                if(t.data>max):
                    max=t.data
                else:
                    t=t.next

    def even(self):
        t=self.head
        if self.head==None:
            print("No Node")
        else:
            if()
n1=SingyLinkedList()
n1.InsertAtFirst()
n1.DisplayNode
