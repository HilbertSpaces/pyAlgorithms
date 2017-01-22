class BinaryTree:
    def __init__(self,rootObj):
        self.key=rootObj
        self.leftChild=None
        self.rightChild=None
    def insertLeft(self,newNode):
        if self.leftChild==None:
            self.leftChild=BinaryTree(newNode)
        else:
            t=BinaryTree(newNode)
            t.leftChild=self.leftChild
            self.leftChild=t
    def insertRight(self,newNode):
        if self.rightChild==None:
            self.rightChild=BinaryTree(newNode)
        else:
            t=BinaryTree(newNode)
            t.rightChild=self.rightChild
            self.rightChild=t
    def getRightChild(self):
        return self.rightChild
    def getLeftChild(self):
        return self.leftChild
    def setRootVal(self,obj):
        self.key=obj
    def getRootVal(self):
        return self.key
    def getRoot(self):
        return self

def preorder(tree):
    if tree:
        print(tree.getRootVal())
        preorder(tree.getLeftChild())
        preorder(tree.getRightChild())
tree=BinaryTree('Book')
tree.insertLeft('Chapter1')
tree.insertRight('Chapter2')
tree.getLeftChild().insertLeft('Section1.1')
tree.getLeftChild().insertRight('Section1.2')
tree.getLeftChild().getRightChild().insertLeft('Section1.2.1')
tree.getLeftChild().getRightChild().insertRight('Section1.2.2')
tree.getRightChild().insertLeft('Section2.1')
tree.getRightChild().insertRight('Section2.2')
tree.getRightChild().getRightChild().insertLeft('Section2.2.1')
tree.getRightChild().getRightChild().insertRight('Section2.2.2')
preorder(tree)
