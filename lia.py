from numpy import array as np

k,N=map(int,open("rosalind_lia.txt","r").read().strip().split())
#print(k,N)

'''M=np([[0.5,0.25,0  ],
     [0.5,0.5 ,0.5],
     [0  ,0.25,0.5]])
geno=np([0,1,0]).T

for i in range(k):
     geno=M@geno'''
     #print(geno)

AaBb=0.25
#print(AaBb)

C=lambda n,r: 0 if n<r else 1 if n==r else n/(n-r)*C(n-1,r)
print(f"{sum(C(2**k,i)*AaBb**i*(1-AaBb)**(2**k-i) for i in range(N,2**k+1)):.3f}")