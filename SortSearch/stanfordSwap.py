import numpy as np
global B
B=0
def partition(A,l,r):
    global B
    A[0],A[l]=A[l],A[0]
    l=0
    p=A[l]
    i=l+1
    B+=len(A)-1
    print(B)
    for j in range(l+1,r):
        if A[j]<p:
            A[i],A[j]=A[j],A[i]
            i+=1
    A[i-1],A[l]=A[l],A[i-1]
    return B,i-1
def quickSort(A,n):
    global B
    C=A.tolist()
    if len(A)==0:
        p=0
    elif len(A)%2==1:
        medArr=[A[0],A[len(A)//2],A[-1]]
        medArr.sort()
        if len(medArr)>1:
            p=C.index(medArr[1])
        else:
            p=C.index(medArr[0])
    else:
        medArr=[A[0],A[len(A)//2-1],A[-1]]
        medArr.sort()
        if len(medArr)>1:
            p=C.index(medArr[1])
        else:
            p=C.index(medArr[0])
    if n>1:
        part=partition(A,p,n)
        split=part[1]
        B=part[0]
        M=A[:split]
        N=A[split+1:]
        quickSort(M,len(M))
        quickSort(N,len(N))
    return B

with open('stanfordArray.txt') as f:
    content=f.readlines()
A=([int(x.strip()) for x in content])
R=np.array(A)
total=quickSort(R,len(R))
A=R.tolist()
print(B)
