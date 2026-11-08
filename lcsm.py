from fasta import read as fs

data=fs("rosalind_lcsm.txt")

samplbl=min(data.keys(),key=lambda x:len(data[x]))
samp=data[samplbl]
del data[samplbl]

class Unit:
    def __init__(self,seq,pos):
        self.seq=seq
        self.pos=pos
        self.loc={i:-1 for i in self.data}
        self.end=False

    @classmethod
    def set(cls,master,data):
        cls.master=master
        cls.data=data

    def check(self):
        if self.end:
            return False
        for key,value in self.data.items():
            if len(self.seq) != 1 and value[self.loc[key] + len(self.seq) - 1] == self.seq[-1]:
                continue
            loc = value.find(self.seq,self.loc[key]+1)
            if loc != -1:
                self.loc[key] = loc
            else:
                return False
        else:
            return True

    def update(self):
        if self.pos+len(self.seq)==len(self.master):
            self.end=True
            self.seq +=" "
            return
        self.seq+=self.master[self.pos+len(self.seq)]


Unit.set(samp,data)
units={Unit(samp[i],i) for i in range(len(samp))}
die=set()
end=set()
while len(units)!=len(die):
    units-=die
    die=set()
    for i in units:
        if not i.check():
            die.add(i)
            continue
        i.update()

open("lcsm.txt","w").write(units.pop().seq[:-1])
