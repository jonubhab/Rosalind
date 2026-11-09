from Motif import Motif as mf
from uniprot import uniprot as up
from Streak import streak as st

codes=open("rosalind_mprt.txt","r").readlines()
N=mf("N{P}[ST]{P}")

with open("mprt.txt","w") as f:
    for i in codes:
        seq=up(i.strip().split("_")[0])["sequence"]["value"]
        streaks=st(seq,N,interact=False)
        if len(streaks)>0:
            f.write(i.strip()+"\n"+" ".join([str(i.pos) for i in sorted(streaks,key=lambda x:x.pos) if i.i==len(N)])+"\n")