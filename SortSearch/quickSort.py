import numpy as np
global B
B=0
def partition(A,l,r):
    global B
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
    if n>1:
        part=partition(A,0,n)
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
