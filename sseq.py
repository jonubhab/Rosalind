from fasta import read as fs

data=fs("rosalind_sseq.txt")

dna=str(max(data.values(),key=len))
seq=str(min(data.values(),key=len))

with open("sseq.txt","w") as f:
    j=0
    for i in range(len(dna)):
        if dna[i]==seq[j]:
            f.write(f"{i+1} ")
            j+=1
            if j==len(seq): break