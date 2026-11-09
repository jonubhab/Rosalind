import json
pms=list(map(float,open("rosalind_spec.txt","r").read().strip().splitlines()))
mass=json.loads(open("Monoisotopic_Mass_Table.txt", "r").read())
inv={v:k for k,v in mass.items()}
prt=[""]
with open("spec.txt","w") as f:
    for i in range(len(pms)-1):
        dm=pms[i+1]-pms[i]
        f.write(inv[min(mass.values(),key=lambda x:abs(x-dm))])
