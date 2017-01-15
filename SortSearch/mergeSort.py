def merge(A,p,q,r):
    n1=q-p
    n2=r-q-1
    infinity=10000000
    L=[]
    R=[]
    for i in range(n1+1):
        L.append(A[p+i])
    for j in range(n2+1):
        R.append(A[q+j+1])
    L.append(infinity)
    R.append(infinity)
    k=p
    i=0
    j=0
    while k<=r:
        if L[i]<=R[j]:
            A[k]=L[i]
            i+=1
        else:
            A[k]=R[j]
            j+=1
        k+=1
def mergeSort(A,p,r):
    if p<r:
        q=(p+r)//2
        mergeSort(A,p,q)
        mergeSort(A,q+1,r)
        merge(A,p,q,r)
    return A
A=[7,44,10,5,22,19,2,12,11,4,6,1]
print(mergeSort(A,0,len(A)-1))
