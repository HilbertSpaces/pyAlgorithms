def binarySearch(lst,target):
    first=0
    found=False
    last=len(lst)-1
    while first<=last and not found:
        midpoint=(first+last)//2
        if lst[midpoint]==target:
            found=True
        else:
            if lst[midpoint]<target:
                first=midpoint+1
            else:
                last=midpoint-1
    return found
print(binarySearch([1,2,3,4,5],4))
