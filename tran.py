from fasta import read as fs

data=fs("rosalind_tran.txt")

ts=tv=0
transit={"A":"G","G":"A","T":"C","C":"T"}
for i,j in zip(*[data[k] for k in data]):
    if i!=j:
        if i==transit[j]: ts+=1
        else: tv+=1
        
print(ts/tv)