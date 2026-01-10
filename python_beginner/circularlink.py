class Node:
    def __init__(self,data):
       self.data= data
       self.next=None
       
class CircularLinkedList:
    head=None
    def InsertNodeAtLast(self):
        if self.head == None:
            self.head=Node(int(input("Enter Data:")))
            self.head.next = self.head
        else:
            t=self.head
            while t.next!=self.head:
                t=t.next
            t.next=Node(int(input("Enter Data:")))
            t.next.next=self.head
    
    def Display(self):
        t=self.head
        if self.head == None:
            print("Nothing to print")
        else:
            while True:
                print(t.data,end=" ")
                t=t.next
                if t==self.head:
                    break
    def InsertNodeAtFirst(self):
        if self.head == None:
             self.head=Node(int(input("Enter Data:")))
             self.head.next=self.head      
        else:
            t=self.head
            self.head=Node(int(input("Enter Data:")))
            self.head.next=t
            while t.next!=self.head.next:
                t=t.next
            t.next=self.head
            
    def countNode(self):
        t=self.head
        if self.head==None:
            print("No Node")
        else:
            count = 0
            while True:
                t=t.next
                count+=1
                if t==self.head:
                    break
            print(count)
    def DeleteFirstNode(self):
        if self.head.next==self.head:
            self.head=None
        else:
            t=self.head
            while t.next!=self.head:
                t=t.next
            self.head=self.head.next
            t.next=self.head
                  
r1=CircularLinkedList()
r1.InsertNodeAtLast()
r1.InsertNodeAtLast()
r1.InsertNodeAtLast()
r1.InsertNodeAtLast()
r1.InsertNodeAtFirst()
r1.DeleteFirstNode()
r1.Display()
r1.countNode()
