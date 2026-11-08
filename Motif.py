class Motif:
    def __init__(self,s):
        if isinstance(s,Motif):
            s=s.s
        self.s = s
        self.seq=[]
        inc=False
        exc=False
        for i in s:
            if i=='[':
                inc=True
                sub = ""
                continue
            if i==']':
                inc=False
                self.seq.append(Inc(f"[{sub}]"))
                continue
            if i=='{':
                exc=True
                sub = ""
                continue
            if i=='}':
                exc=False
                self.seq.append(Exc(f"{{{sub}}}"))
                continue
            if not (inc or exc):
                self.seq.append(i)
            else:
                sub+=i

    def list_to_motif(self,l):
        return Motif("".join(l))

    def __len__(self):
        return len(self.seq)

    def __repr__(self):
        return self.s

    def __eq__(self,other):
        if type(other)==Motif:
            return self.s == other.s
        elif type(other)==str:
            if len(self.seq)!=len(other):
                return False
            for i,j in zip(other,self.seq):
                if i!=j:
                    return False
            else:
                return True

    def __getitem__(self,i):
        if isinstance(i, slice):
            start, stop, step = i.indices(len(self.seq))
            return Motif("".join([str(self.seq[i]) for i in range(start, stop, step)]))
        return Motif(self.seq[i])



class Exc(Motif):
    def __init__(self,s):
        self.s = s
        self.seq=[s]

    def __eq__(self,other):
        if isinstance(other,Motif):
            return self.s == other.s
        elif isinstance(other,str):
            if len(other)!=1:
                return False
            for i in self.s[1:len(self.s)-1]:
                if i==other:
                    return False
            else:
                return True

class Inc(Motif):
    def __init__(self,s):
        self.s = s
        self.seq=[s]

    def __eq__(self,other):
        if isinstance(other,Motif):
            return self.s == other.s
        elif isinstance(other,str):
            if len(other)!=1:
                return False
            if other in self.s[1:len(self.s)-1]:
                return True
            return False
