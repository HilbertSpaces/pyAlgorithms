#Skiena Graph Design
class Queue:
    def __init__(self):
        self.q=[]
    def enqueue(self,node):
        self.q.append(node)
    def dequeue(self):
        return self.q.pop(0)
    def notEmpty(self):
        return not self.q==[]
class Stack:
    def __init__(self):
        self.s=[]
    def push(self,vert):
        self.s.append(vert)
    def pop(self):
        return self.s.pop()
    def notEmpty(self):
        return not self.s==[]
class node:
    def __init__(self,y):
        self.y=y
        self.next=None
    def setNext(self,node):
        self.next=node
    def getNext(self):
        return self.next
class edgenode:
    def __init__(self):
        self.head=None
    def add(self,item):
        temp=node(item)
        temp.setNext(self.head)
        self.head=temp
    def grab(self):
        return self.head
    def printOut(self):
        content=self.head
        while content.next!=None:
            print(content.y)
            content=content.next
    def reverse(self):
        prev=None
        current=self.head
        while current is not None:
            temp=current.next
            current.next=prev
            prev=current
            current=temp
        self.head=prev
class graph:
    def __init__(self,direct,vertices,edges):
        self.nedges=edges
        self.directed=direct
        self.nvertices=vertices+1
        self.edges=[None]*(edges+1)
        self.degree=[0]*(vertices+1)
    def insert_edge(self,x,y):
        if self.edges[x] is None:
            e=edgenode()
            e.add(y)
            self.edges[x]=e
            self.degree[x]+=1
        else:
            p=self.edges[x]
            p.add(y)
            self.degree[x]+=1
            self.edges[x]=p
        if self.directed==False:
            self.directed=True
            self.insert_edge(y,x)
        else:
            self.nedges+=1
    def print_graph(self):
        for i in range(1,self.nvertices):
            try:
                p=self.edges[i].head
            except:
                continue
            while(p is not None):
                print(i,p.y)
                p=p.getNext()
    def BFS(self,s):
        state=["hold"]
        p=["hold"]
        for i in range(1,self.nvertices):
            state.append("undiscovered")
            p.append(None)
        state[s]="discovered"
        p[s]=None
        Q=Queue()
        Q.enqueue(s)
        print(Q.notEmpty())
        while Q.notEmpty():
            u=Q.dequeue()
            try:
                x=self.edges[u].head
            except:
                continue
            while x is not None:
                if state[x.y]=="undiscovered":
                    print("Edge, "+str(u)+" "+str(x.y))
                    state[x.y]="discovered"
                    p[x.y]=u
                    Q.enqueue(x.y)
                x=x.next
                state[u]="processed"
        print(p)
    def DFS(self,s):
        time=0
        p=[0]*self.nvertices
        state=["undiscovered"]*self.nvertices
        entry=[0]*self.nvertices
        exit=[0]*self.nvertices
        S=Stack()
        S.push(s)
        save=s
        while S.notEmpty():
            time+=1
            u=S.pop()
            entry[u]=time
            if state[u]=="undiscovered":
                state[u]="discovered"
                print(p[u],u)
            try:
                x=self.edges[u].head
            except:
                continue
            while x is not None:
                S.push(x.y)
                if state[x.y]=="undiscovered":
                    p[x.y]=u
                x=x.next
            state[u]="processed"
            exit[u]=time
            time+=1
        print(p)
        print(entry)
        print(exit)
g=graph(True,8,7)
g.insert_edge(1,2)
g.insert_edge(2,6)
g.insert_edge(6,7)
g.insert_edge(7,4)
g.insert_edge(1,3)
g.insert_edge(1,5)
g.BFS(1)
g.DFS(1)
