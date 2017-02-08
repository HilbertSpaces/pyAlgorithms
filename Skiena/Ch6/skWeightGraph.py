class Graph:
    def __init__(self,direct):
        self.gDict={}
        self.direct=direct
        self.nVertices=0
        self.vertSet=set()
    def add_vert(self,vert):
        if vert not in self.gDict.keys():
            self.gDict[vert]=[]
    def add_edge(self,iVert,eVert,weight=0):
        if iVert not in self.gDict:
            self.gDict[iVert]=[(eVert,weight)]
            self.vertSet.add(iVert)
        else:
            self.gDict[iVert].append((eVert,weight))
            self.vertSet.add(eVert)
        if self.direct:
            if eVert not in self.gDict:
                self.gDict[eVert]=[(iVert,weight)]
                self.vertSet.add(eVert)
            else:
                self.gDict[eVert].append((iVert,weight))
                self.vertSet.add(eVert)

    def printG(self):
        print(self.gDict,self.vertSet)
def primTree(graph):
    pTree={}
    mstSet=set()
    for key in graph.gDict:
        min=0
        edges=graph.gDict[key]
        for edge in edges:
            
g=Graph(True)
g.add_edge(3,4,2)
g.add_edge(3,5,1)
g.add_edge(2,3,4)
g.add_edge(2,4,7)
g.add_vert(4)
g.add_edge(4,6,3)
g.add_edge(4,5,8)
g.printG()
