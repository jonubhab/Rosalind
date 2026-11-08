'''
One parent AA = 1
Aa + Aa = 0.75
Aa + aa = 0.5
aa + aa = 0
'''

popu=map(int,open("rosalind_iev.txt","r").read().strip().split())
prob=[1,1,1,0.75,0.5,0]
s=sum([2*i*j for i,j in zip(popu,prob)])
print(s)
