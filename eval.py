from prob import prob

data=open("rosalind_eval.txt","r").readlines()
n=int(data[0].strip())
seq=data[1].strip()
gc=list(map(float,data[2].strip().split()))

N=n-len(seq)+1


with open("eval.txt","w") as f:
    for i in gc:
        P=prob(seq,i)
        f.write(f"{N*10**(P):.3f} ")
