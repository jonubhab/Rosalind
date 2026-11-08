'''dna,subs=map(lambda x:x.strip(),open("rosalind_subs.txt","r").read().strip().splitlines())

with open("subs.txt","w") as f:
    pos=dna.find(subs)+1
    while pos!=0:
        f.write(str(pos)+" ")
        dna=dna[:pos-1]+'#'+dna[pos:]
        pos=dna.find(subs)+1'''

from Streak import streak

dna,subs=open("rosalind_subs.txt","r").read().strip().splitlines()
streaks=streak(dna,subs,interact=False)

with open("subs.txt","w") as f:
    f.writelines([str(i.pos)+" " for i in sorted(streaks,key=lambda x:x.pos) if i.i==len(subs)])