#Skiena Graph Design
class node:
    def __init__(self,y,weight):
        self.y=y
        self.weight=weight
        self.next=None
    def setNext(self,node,weight):
        self.next=node
    def getNext(self):
        return self.next
class edgenode:
    def __init__(self):
        self.head=None
    def add(self,item,weight):
        temp=node(item,weight)
        temp.setNext(self.head,weight)
        self.head=temp
    def grab(self):
        return self.head
class graph:
    def __init__(self,direct,vertices,edges):
        self.nedges=edges
        self.directed=direct
        self.nvertices=vertices
        self.edges=[edgenode()]*edges
        self.degree=[0]*vertices
    def insert_edge(self,x,y,weight):
        p=self.edges[x]
        p.add(y,weight)
        self.degree[x]+=1
        if self.directed==False:
            self.directed=True
            insert_edge(y,x)
        else:
            self.nedges+=1
    def print_graph(self):
        for i in range(self.nvertices):
            p=self.edges[i].head
            while(p!=None):
                print(p)
                p.getNext()

g=graph(True,4,4)
g.insert_edge(3,2,None)
g.insert_edge(3,1,None)
g.print_graph()
e=edgenode()
e.add(3,4)
