import myDequeue as md

def palinCheck(string):
    dq=md.Dequeue()
    i=0
    while i<len(string):
        sFront=string[i]
        sRear=string[len(string)-1-i]
        dq.addFront(sFront)
        dq.addRear(sRear)
        i+=1
    j=0
    totLen=dq.size()/2
    if totLen!=int(totLen):
        return False
    totLen=int(totLen)
    for j in range(totLen):
        front=dq.removeFront()
        rear=dq.removeRear()
        if front !=rear:
            return False
    return True

print(palinCheck("borob"))
