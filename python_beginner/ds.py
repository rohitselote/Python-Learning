lass Node:
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
           

n1=SingyLinkedList()
n1.InsertAtFirst()
