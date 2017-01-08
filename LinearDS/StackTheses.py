import myStack as ms 

def parenCheck(pstring,ds):
    i=0
    while pstring[i]=='(':
        ds.push(pstring[i])
        i+=1
    while pstring[i]==')':
        if ds.isEmpty():
            return False
        else:
            ds.pop()
            i+=1
            empty=(ds.isEmpty())
            equaLen=(i==len(pstring))
        if empty and equaLen:
            print("True")
            return True
        if not empty and equaLen:
            print("False")
            return False
    return parenCheck(pstring[i:],ds)
ds=ms.Stack()
parenCheck('((((()())))',ds)
