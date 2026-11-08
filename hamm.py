def hamm(dna1,dna2):
    ham=0
    for c1,c2 in zip(dna1,dna2):
        if c1!=c2:
            ham+=1
    return ham

if __name__=="__main__":
    dna1, dna2 = open("rosalind_hamm.txt", "r").read().strip().splitlines()
    print(hamm(dna1,dna2))