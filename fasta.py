def read(file):
    with open(file,"r") as data:
        dna=data.read().split('>')[1:]
    data={}
    for s in dna:
        label,strand=s.splitlines()[0].strip(),"".join(map(lambda x:x.strip(),s.splitlines()[1:]))
        data[label]=strand
    return data