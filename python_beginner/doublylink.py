class Node:
    def __init__(self,data):
        self.prev=None
        self.data=data
        self.prev=None
        
class DoublyLinkedList:
    def __init__(self):
        self.head=None
head=Node(5)
head.next=Node(10)
head.next.next=Node(15)
head.next.next.next=Node(20)

print(head.data)
print(head.next.data)
print(head.next.next.data)
print(head.next.next.next.data)
        
