n,k=map(int,open("rosalind_fib.txt","r").read().strip().split())

def grow(n):
    if n<=1: return n
    return grow(n-1)+k*grow(n-2)

print(grow(n))