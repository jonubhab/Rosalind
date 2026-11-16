from math import log10

def prob(dna,x):
    try:
        return sum(log10((1 - x) / 2) if j in "AT" else log10(x / 2) for j in dna)
    except ValueError:
        return -float("inf")

if __name__=="__main__":
    dna,gc=open("rosalind_prob.txt","r").read().strip().splitlines()
    gc=map(float,gc.split())
    with open("prob.txt","w") as out:
        for x in gc:
            out.write(f"{prob(dna,x):.3f} ")