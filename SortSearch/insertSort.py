def inSort(a):
    for i in range(len(a)):
        for j in range(i,0,-1):
            if a[j]<a[j-1]:
                save=a[j]
                a[j]=a[j-1]
                a[j-1]=save
    return a

print(inSort([5,8,3,11,200,10,6,7]))
