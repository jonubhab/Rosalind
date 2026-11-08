#using odometer logic
def Odo(n,k):
    ctr = [0] * k
    while True:
        yield ctr[::-1]
        carry = True
        i = 0
        while carry and i < len(ctr):
            ctr[i] = (ctr[i] + 1) % n
            carry = ctr[i] == 0
            i += 1
        if sum(ctr)==0: break

lex,k=open("rosalind_lexf.txt","r").read().strip().splitlines()
lex=lex.split()
k=int(k)

odo=Odo(len(lex),k)
open("lexf.txt","w").writelines(["".join([lex[j] for j in i])+"\n" for i in odo])
