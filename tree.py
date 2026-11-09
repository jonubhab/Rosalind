data=open("rosalind_tree.txt","r").read().strip().splitlines()
N=int(data.pop(0).strip())
print(N-len(data)-1)