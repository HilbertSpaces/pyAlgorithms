#Skiena Graph Design
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
class graph:
    def __init__(self,direct,vertices,edges):
        self.nedges=edges
        self.directed=direct
        self.nvertices=vertices
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
        for i in range(1,self.nvertices+1):
            try:
                p=self.edges[i].head
            except:
                continue
            while(p is not None):
                print(i,p.y)
                p=p.getNext()

g=graph(True,4,4)
g.insert_edge(1,3)
g.insert_edge(2,1)
g.insert_edge(1,2)
g.insert_edge(1,4)
g.print_graph()
