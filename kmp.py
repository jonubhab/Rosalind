from fasta import read as fs
from Streak import Streak,streak

#Rosalind indexing notation: starts from 1 & both j & k are inclusive

s=list(fs("rosalind_kmp.txt").values()).pop()

buff=Streak(0,"") #For having 0 in case of no streak
streaks=streak(s,"_",lambda st:str(max(st.union({buff}),key=lambda x:x.i).i) + " ")

with open("kmp.txt",'w') as f:
    f.write(next(streaks))
    for i in range(1,len(s)):
        f.write(streaks.send(s[:len(s)-i]))



"""    for k in tqdm(range(len(s))):
        for j in range(1,k+1):
            if s[j:k+1]==s[:k-j+1]:
                f.write(str(k-j+1)+" ")
                break"""
