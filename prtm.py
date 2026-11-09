import json

mass=json.loads(open("Monoisotopic_Mass_Table.txt").read())

M=0
for i in open("rosalind_prtm.txt","r").read().strip():
    M+=mass[i]
#M+=mass["H2O"]

print(f"{M:.3f}")