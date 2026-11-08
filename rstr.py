from prob import prob

with open("rosalind_rstr.txt","r") as f:
    l=f.readlines()
    N,gc=l[0].strip().split()
    N=int(N)
    gc=float(gc)
    dna=l[1].strip()

P=prob(dna,gc)

print(f"{1-(1-10**P)**N:.3f}")