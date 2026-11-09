data=open("rosalind_trie.txt","r").read().strip().splitlines()

class Trie:
    ctr=1
    def __init__(self,ele):
        self.ele=ele
        self.n=self.ctr
        Trie.ctr+=1
        self.nodes=[]

    @classmethod
    def reset(cls):
        cls.ctr=1

    def join(self,ele):
        self.nodes.append(ele)

    def __eq__(self,other):
        if isinstance(other,str):
            return self.ele==other
        elif isinstance(other,Trie):
            return self.ele==other.ele

with open("trie.txt","w") as f:
    tree=Trie("root")
    for i in data:
        curr = tree
        for j in i:
            for c in curr.nodes:
                if c==j:
                    curr = c
                    break
            else:
                curr.join(Trie(j))
                f.write(f"{curr.n} {Trie.ctr-1} {j}\n")
                curr=curr.nodes[-1]