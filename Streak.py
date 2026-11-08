class Streak():
    def __init__(self,pos,subs):
        self.pos=pos
        self.subs=subs
        self.i=0

    def check(self,ch):
        if self.i==len(self.subs): return True
        if ch==self.subs[self.i]:
            self.i+=1
            return True
        return False

def streak(dna,sub=None,out=None,interact=True):
    if interact:
        return istreak(dna,sub,out)
    if not interact and sub is None:
        raise "sub cannot be None in non-interactive mode"
    subs = sub
    streaks = set()
    for i in range(len(dna)):
        if dna[i] == subs[0]:
            streaks.add(Streak(i + 1, subs))
        die = set()
        for j in streaks:
            if not j.check(dna[i]):
                die.add(j)
        streaks -= die
    return streaks

def istreak(dna,sub=None,out=None):
    streaks = set()
    if sub is None:
        subs = yield
        if subs is None:
            subs = sub
    else:
        subs=sub
    for i in range(len(dna)):
        if dna[i] == subs[0]:
            streaks.add(Streak(i + 1, subs))
        die = set()
        for j in streaks:
            if not j.check(dna[i]):
                die.add(j)
        streaks -= die
        if out is None:
            subs = yield
        else:
            subs = yield out(streaks)
        if sub is not None:
            if subs is None:
                subs = sub

    return streaks


def multi(dna,sub=[]):
    streaks = {i:set() for i in sub}
    for i in range(len(dna)):
        for subs in streaks.keys():
            if dna[i] == subs[0]:
                streaks[subs].add(Streak(i + 1, subs))
            die = set()
            for j in streaks[subs]:
                if not j.check(dna[i]):
                    die.add(j)
            streaks[subs] -= die
    return streaks