import sys

c={"A":"T","C":"G","G":"C","T":"A"}

def revc(seq):
    s=""
    for i in seq[::-1]:
        s+=i.replace(i,c[i])
    return s

if __name__ == "__main__":
    s=open("rosalind_revc.txt","r").read().strip()
    with open("revc.txt","w") as sc:
        sc.write(revc(s))