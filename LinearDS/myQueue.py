class Queue:
    def __init__(self):
        self.s=[]
    def enqueue(self,x):
        self.s.append(x)
    def dequeue(self):
        return self.s.pop(0)
    def size(self):
        return len(self.s)
    def isEmpty(self):
        return self.s==[]
