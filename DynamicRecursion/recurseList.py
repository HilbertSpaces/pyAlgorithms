def reverse(x,m):
    if len(x)<=1:
        m.append(x[0])
    else:
        reverse(x[len(x)//2:],m)
        reverse(x[:len(x)//2],m)
    return m

print(reverse([1,2,3,4,5],[]))
