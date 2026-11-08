from fasta import read as fs
from Streak import multi
from prot import prot

data=fs("rosalind_splc.txt")

lbl=max(data.keys(),key=lambda x:len(data[x]))
dna=data[lbl]
del data[lbl]

streaks=multi(dna,data.values())
introns = sorted((i.pos-1, i.pos + len(j)-1) for j in streaks for i in streaks[j] if i.i == len(i.subs))

merged = []
for s, e in introns:
    if merged and s <= merged[-1][1]:
        merged[-1][1] = max(merged[-1][1], e)
    else:
        merged.append([s, e])

exon, pos = [], 0
for s, e in merged:
    exon.append(dna[pos:s])
    pos = e
exon.append(dna[pos:])
rna = "".join(exon).replace("T","U")

open("splc.txt","w").write(prot(rna))

'''open("splc.txt","w").writelines([i+"\n" for i in orf(exon)])'''
