import math
A=[False,False]
def eratos(n):
    B=[]
    for i in range(2,n+1):
        A.append(True)
    for i in range(2,int(math.sqrt(n))+1):
        if A[i]:
            s=int(math.pow(i,2))
            mult=0
            j=s
            while j<=n:
                A[j]=False
                j=s+mult*i
                mult+=1
    for x in range(len(A)):
        if A[x]:
            B.append(x)
    print(B)

eratos(100)
