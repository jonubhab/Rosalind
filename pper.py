n,k=map(int,open("rosalind_pper.txt","r").read().strip().split())

P=lambda x:1 if x<=n-k else (x*P(x-1))%1_000_000

print(P(n))