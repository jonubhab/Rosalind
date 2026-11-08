#using odometer logic
def Odo(n,k):
    ctr = [0] * k
    ctr[-1] = 1
    while True:
        s="".join([chr(i+64) if i>0 else " " for i in ctr])
        if s.strip()==s.replace(" ",""): #Removing invalid cases where 0 is in between the counter somewhere
            yield ctr[::-1]
        carry = True
        i = 0
        while carry and i < len(ctr):
            ctr[i] = (ctr[i] + 1) % n
            carry = ctr[i] == 0
            i += 1
        if sum(ctr)==0: break

lex,k=open("rosalind_lexv.txt","r").read().strip().splitlines()
lex=[" "]+lex.split()
k=int(k)
odo=Odo(len(lex),k)
open("lexv.txt","w").writelines(["".join([lex[j] for j in i])+"\n" for i in odo])
