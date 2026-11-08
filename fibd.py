n,m=map(int,open("rosalind_fibd.txt","r").read().strip().split())
#n,m=6,3

g,b,d={},{},{}

def grow(n):
    if n<=1: return 1 if n==1 else 0
    if n in g: return g[n]
    g[n]=grow(n-1)+birth(n)-death(n)
    return g[n]

def birth(n):
    if n<=1: return 1 if n==1 else 0
    if n in b: return b[n]
    b[n]=grow(n-2)-death(n-1)
    return b[n]

def death(n):
    if n<=1: return 0
    if n in d: return d[n]
    d[n]=birth(n-m)
    return d[n]

print(grow(n))