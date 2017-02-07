import numpy as np
def partition(A,l,r):
    p=A[l]
    i=l+1
    print(A)
    for j in range(l+1,r):
        if A[j]<p:
            save=A[i]
            A[i]=A[j]
            A[j]=save
            i+=1
    save=A[i-1]
    A[i-1]=A[l]
    A[l]=save
    return i-1
def quickSort(A,n):
    if n>1:
        split=partition(A,0,n)
        M=A[:split]
        N=A[split+1:]
        quickSort(M,len(M))
        quickSort(N,len(N))
        print(A)
    return A

A=np.array([3,4,5,2,10,7,6,9,1])
print(quickSort(A,len(A)))
