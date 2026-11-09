import json
codon=json.loads(open("RNA_Codon_Table.txt", "r").read())

rep={}
for code,aa in codon.items():
    if aa not in rep:
        rep[aa]=0
    rep[aa]+=1

mrna=open("rosalind_mrna.txt","r").read().strip()

n=1
for i in mrna:
    n=(n*rep[i])%1_000_000
else:
    n = (n * rep["Stop"]) % 1_000_000

print(n)