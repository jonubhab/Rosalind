from itertools import permutations
import math

n=int(open("rosalind_perm.txt","r").read().strip())

with open("perm.txt","w") as f:
    f.write(str(math.factorial(n))+"\n")
    for i in permutations(range(1,n+1),n):
        f.write("".join(map(lambda x:str(x)+" ",i))+"\n")