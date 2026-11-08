from fasta import read as fs
from itertools import permutations
from copy import deepcopy as copy

def overlap(s1,s2):
    if s1==s2:
        return 0
    for i in range(min(len(s1),len(s2)),min(len(s1),len(s2))//2,-1):
        if s1[-i:]==s2[:i]:
            return i
    else:
        return 0

class Walker:
    reports=[]

    def __init__(self):
        self.nodes=[]
        self.score=0
        self.visited=0

    @property
    def loop(self):
        for i in range(2,len(self.nodes)//2):
            if self.nodes[-i:]==self.nodes[-2*i:-i]:
                return True
        else:
            return False


class Node:
    ctr=0
    def __init__(s,label:str,strand:str):
        s.label=label
        s.strand=strand
        s.mark=1<<Node.ctr
        s.weight=len(strand)
        s.edges=[]
        Node.ctr+=1

    def traverse(s,walker:Walker):
        walker.nodes.append(s.label)
        if walker.visited & s.mark==0:
            walker.visited|=s.mark
        else:
            walker.score-=s.weight
        if walker.visited==2**Node.ctr-1:
            Walker.reports.append(walker)
        else:
            if not walker.loop:
                for i in s.edges:
                    i.traverse(copy(walker))
            del walker

    def interact(self,other):
        weight=overlap(self.strand,other.strand)
        if weight>0:
            self.edges.append(Edge(weight,other))

class Edge:
    def __init__(self,weight:int,node:Node):
        self.weight=weight
        self.node=node

    def traverse(s,walker:Walker):
        walker.score+=s.weight
        s.node.traverse(walker)

data=fs("rosalind_long.txt")
start=Node("start","")
for k in data:
    data[k]=Node(k,data[k])
    start.edges.append(Edge(0, data[k]))

for i, j in permutations(data, 2):
    data[i].interact(data[j])

start.traverse(Walker())

best=max(Walker.reports,key=lambda x:x.score)

def stitch(s1,s2):
    i=overlap(s1,s2)
    if i==0: return s1+s2
    return s1[:-i]+s2

seq=""
for i in best.nodes:
    if i=="start": continue
    seq=stitch(seq,data[i].strand)

open("long.txt","w").write(seq)
