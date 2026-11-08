seq=open("rosalind_dna.txt","r").read().strip()
count={"A":0,"C":0,"G":0,"T":0}
for i in seq:count[i]+=1
print(count["A"],count["C"],count["G"],count["T"])


