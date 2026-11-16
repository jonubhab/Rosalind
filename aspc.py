from math import comb as C
n,m=map(int,open("rosalind_aspc.txt","r").read().split())
s=0
for i in range(m,n+1):
    s=(s+C(n,i))%1_000_000
print(s)