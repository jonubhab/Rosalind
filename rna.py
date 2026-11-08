t=open("rosalind_rna.txt","r").read().strip()
with open("u.txt","w") as u:
    u.write(t.replace("T","U"))