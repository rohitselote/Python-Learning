class Node:
    def __init__(self,data):
       self.data= data
       self.next=None
class Stack:
    def __init__(self):
        self.head=None
    def push(self):
        n=Node(int(input("Enter a number ")))
        n.next=self.head
        self.head=n
        
    def pop(self):
        if self.head==None:
            print("Nothing to delete")
        else:
            temp=self.head
            self.head=self.head.next
            temp=None    
    
    def display(self):
        t=self.head
        if t==None:
            print("Nothing to display")
        else:
            while t!=None:
                print(t.data,end=" ")
                t=t.next    
    
    def peek(self):
        t=self.head
        if t==None:
            print("Nothing to peek")
        else:
            print(self.head.data)
        
r1=Stack()
r1.push()
r1.push()
r1.push()
#r1.pop()
r1.peek()
r1.display()
