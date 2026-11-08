from fasta import read as fs
from itertools import permutations

O3=lambda s1,s2:s1!=s2 and s1[-3:]==s2[:3]

data=fs("rosalind_grph.txt")

with open("grph.txt","w") as f:
    for i,j in permutations(data,2):
        if O3(data[i],data[j]):
            f.write(f"{i} {j}\n")
