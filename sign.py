from itertools import permutations
from numpy import array as np
import math

n=int(open("rosalind_sign.txt","r").read().strip())

with open("sign.txt","w") as f:
    f.write(str(2**n*math.factorial(n))+"\n")
    for i in permutations(range(1,n+1),n):
        for j in range(2**n):
            sign=np([-2]*n)
            k=bin(j)[2:].zfill(n)
            for c in range(n): #enumerate(
                sign[c]=-2*int(k[c])+1
            f.write("".join(map(lambda x:str(x)+" ",sign*np(i)))+"\n")