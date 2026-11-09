from fasta import read as fs
from revc import revc
import json

codon=json.loads(open("RNA_Codon_Table.txt", "r").read())

def scan(rna):
    rf=[[],[],[]]
    reg=""
    for i,c in enumerate(rna):
        reg = reg[1:] + c if len(reg)==3 else reg+c
        if len(reg)<3:
            continue
        if codon[reg] == "Stop" and len(rf[i%3])>0:
            yield rf[i % 3]
            rf[i % 3] = []
        else:
            for j in range(len(rf[i % 3])):
                rf[i % 3][j] += codon[reg]
        if reg=="AUG":
            rf[i%3].append("M")

def orf(rna):
    prot = set()
    read = scan(rna.replace("T", "U"))
    for i in read:
        prot = prot.union(i)
    read = scan(revc(rna).replace("T", "U"))
    for i in read:
        prot = prot.union(i)
    return prot

if __name__=="__main__":
    rna=list(fs("rosalind_orf.txt").values()).pop()
    open("orf.txt","w").writelines([i + "\n" for i in orf(rna)])
