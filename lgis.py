from functools import total_ordering
from bisect import bisect_right as bs
from copy import copy
from tqdm import tqdm

data=open("rosalind_lgis.txt","r").readlines()
N=int(data[0].strip())
perm=list(map(int,data[1].strip().split()))

@total_ordering
class Graph:
    def __init__(self,n):
        self.n=n
        self.nodes=[]
        self.lpath=None

    def check(self,n):
        if len(self.nodes)==0 or self.nodes[0].n>n:
            return True
        return False

    def join(self,n):
        self.nodes.append(n)

    def __eq__(self,other):
        return self.n==other.n

    def __lt__(self,other):
        return self.n<other.n

    def __repr__(self):
        return str(self.n)+"\n"+str([i.n for i in self.nodes])

    def traverse(self):
        if self.lpath is not None:
            return self.lpath
        if len(self.nodes)==0:
                return [self.n]
        else:
            self.lpath=[]
            for i in self.nodes:
                lpath=[self.n]+i.traverse()
                if len(lpath)>len(self.lpath):
                    self.lpath=lpath
            return self.lpath



def lgis(perm):
    ele=[Graph(0)]
    for i in perm:
        g=Graph(i)
        j=bs(ele,g)
        ele.insert(j,g)
        for k in ele[:j]:
            if k.check(i): k.join(g)
    ele[0].traverse()
    return ele[0].lpath[1:]


with open("lgis.txt","w") as f:
    f.write(" ".join(str(i) for i in lgis(perm))+"\n")
    f.write(" ".join(str(i) for i in lgis(perm[::-1])[::-1]))