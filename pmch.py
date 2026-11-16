from fasta import read as fs
for _,data in fs("rosalind_pmch.txt").items():pass
F=lambda x:1  if x<=1 else x*F(x-1)
print(F(data.count("A"))*F(data.count("G")))