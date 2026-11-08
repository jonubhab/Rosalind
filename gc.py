from fasta import read

data=read("rosalind_gc.txt")
gc,lbl=0,""
for label,strand in data.items():
    curr=len(strand.replace("A","").replace("T",""))/len(strand)
    if curr>gc:
        gc=curr
        lbl=label

print(lbl,f"{gc*100:.6f}",sep="\n")

