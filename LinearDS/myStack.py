class Stack:
    def __init__(self):
        self.s=[]
    def isEmpty(self):
        return self.s==[]
    def push(self,x):
        self.s.append(x)
    def pop(self):
        return self.s.pop()
    def peek(self):
        return self.s[len(self.s)-1]
    def size(self):
        return len(self.s)
