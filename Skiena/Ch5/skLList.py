class node:
    def __init__(self,payload):
        self.y=payload
        self.next=None
    def setNext(self,newnext):
        self.next=newnext
    def getNext(self):
        return self.next

class edgelist:
    def __init__(self):
        self.head=None
        self.count=0
    def add(self,enode):
        temp=node(enode)
        temp.setNext(self.head)
        self.head=temp
        self.count+=1
    def show(self):
        return self.head.y
    def printLL(self):
        current=self.head
        for i in range(self.count):
            print(current.y,end=" ")
            current=current.getNext()
    def reverse(self):
        prev=None
        current=self.head
        while current is not None:
            next=current.next
            current.next=prev
            prev=current
            current=next
        self.head=prev
m=edgelist()
m.add(3)
m.add(4)
m.add(7)
m.add(10)
m.printLL()
m.reverse()
m.printLL()
m.reverse()
m.printLL()
