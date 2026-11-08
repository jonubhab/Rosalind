from fasta import read as fs
from revc import revc
from hamm import hamm

data=fs("rosalind_corr.txt")
corr={key:False for key in data.keys()}

def check(key,value):
    if corr[key]:
        return True
    for i, j in data.items():
        if key == i: continue
        if j==value or j==revc(value):
            corr[key]=True
            corr[i]=True
            return True
    else:
        return False

def correct(key,value):
    for i, j in data.items():
        if key == i or not corr[i]: continue
        if hamm(j,value)==1:
            data[key]=j
            corr[key]=True
            return j
        elif hamm(revc(j), value) == 1:
            data[key] = revc(j)
            corr[key] = True
            return revc(j)

change={}
while not all(corr.values()):
    for key, value in data.items():
        if not (check(key, value)):
            change[value]=correct(key,value)

with open("corr.txt","w") as f:
    for key, value in change.items():
        f.write(f"{key}->{value}\n")