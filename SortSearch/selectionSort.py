def selSort(a):
    for i in range(len(a)-1,0,-1):
        big=0
        for j in range(i+1):
            if a[j]>big:
                big=a[j]
                save=j
        temp=a[i]
        a[i]=big
        a[save]=temp
    return a

print(selSort([3,9,1,2,4,7,8]))
