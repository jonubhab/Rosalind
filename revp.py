from fasta import read as fs
from revc import revc
from long import overlap as ol

for _, dna in fs("rosalind_revp.txt").items():
    pass

with open("revp.txt","w") as f:
    for i in range(len(dna)):
        L=4
        while L<=len(dna)-i and L<=12:
            if dna[i:i+L]==revc(dna[i:i+L]):
                f.write(f"{i+1} {L}\n")
                L+=2
            else:
                L+=L-ol(dna[i:i+L],revc(dna[i:i+L]))