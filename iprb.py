'''
N=k+m+n

One parent AA = 1   [1-C(N-k,2)/C(N,2)]
Aa + Aa = 0.75      [C(m,2)/C(N,2)]
Aa + aa = 0.5       [m*n/C(N,2)]
aa + aa = 0         [C(n,2)/C(N,2)]
'''

k,m,n=map(int,open("rosalind_iprb.txt","r").read().strip().split())
C=lambda x:x*(x-1)/2
N=k+m+n
print(f"{1+(-C(N-k)+0.75*C(m)+0.5*m*n)/C(N):.5f}")
