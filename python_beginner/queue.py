class Node:
    def __init__(self,data):
        self.data = data
        self.next=None
class Queue:
    def __init__(self):
        self.head=None
        
    def Enqueue(self):
        n=Node(int(input("Enter no. to enqueue")))
        t=self.head
        if t==None:
            self.head=n
        else:
            while t.next!=None:
                t=t.next
            t.next=n
    
    def dequeue(self):
        t=self.head
        if t==None:
            print("Nothing to dequeue")
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
            print("Nothing to print")
        else:
            while t.next!=None:
                t=t.next
            print(t.data)   
                  
r1=Queue()
r1.Enqueue()
r1.Enqueue()
r1.Enqueue()
r1.dequeue()
r1.display()
r1.peek()
