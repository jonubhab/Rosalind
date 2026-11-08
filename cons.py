import fasta as fs

data=fs.read("rosalind_cons.txt")
#print(*[i for i in s.values()],sep="\n")

N=len(next(iter(data.values())))
count={i:[0]*N for i in ["A","C","G","T"]}
cons=""
for i in range(N):
    for j in map(lambda x:x[i],data.values()):
        count[j][i]+=1
    cons+=max(count.keys(),key=lambda x:count[x][i])

with open("cons.txt","w") as out:
    out.write(cons)
    for key,values in count.items():
        out.write(f"\n{key}:")
        out.writelines([" "+str(i) for i in values])
