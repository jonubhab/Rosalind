from fasta import read as fs

for _,data in fs("rosalind_mmch.txt").items():pass
n={i:data.count(i) for i in "ACGU"}
P=lambda n,r:1 if r==0 else n*P(n-1,r-1)

print(P(max(n["A"],n["U"]),min(n["A"],n["U"]))*P(max(n["G"],n["C"]),min(n["G"],n["C"])))
