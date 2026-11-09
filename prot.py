import json
codon=json.loads(open("RNA_Codon_Table.txt", "r").read().strip())

def prot(seq):
    prtn = ""
    for i in range(0, len(seq), 3):
        T = codon[seq[i:i + 3]]
        if T == "Stop":
            break
        prtn += T
    return prtn

if __name__=="__main__":
    seq=open("rosalind_prot.txt","r").read().strip()
    with open("prot.txt","w") as f:
        f.write(prot(seq))