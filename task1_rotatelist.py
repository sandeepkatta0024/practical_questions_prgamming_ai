def rotate_right( l, k):
    n = len(l)
    k %= n               # handle k > n
    al = l[:]  
    for i in range(0,len(l)):
        l[i]=al[i-k]
    return l
print(rotate_right([1,2,3,4,5],1))