

def tribonacci(n):
    tri = {0: 0, 1: 1, 2:1}
    
    for i in range(3,n+1):
        tri[i] = tri[i-1] + tri[i-2] + tri[i-3]

    print(tri)


    return tri[n]
    
print(tribonacci(25))