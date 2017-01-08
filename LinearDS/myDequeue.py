class Dequeue:
    def __init__(self):
        self.s=[]
    def addFront(self,x):
        self.s.insert(0,x)
    def addRear(self,x):
        self.s.append(x)
    def removeFront(self):
        return self.s.pop(0)
    def removeRear(self):
        return self.s.pop()
    def isEmpty(self):
        return self.s==[]
    def size(self):
        return len(self.s)
