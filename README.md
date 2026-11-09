# Rosalind Bioinformatics Stronghold Problems

This repository contains 36 problems I solved from Rosalind, and few reusable utility files. 
I have shared the algorithms used and things I learned from each problem.
I have tried not using the predefined modules for bioinformatics as algorithm designing was the main focus.

## Utility Files
|           File           | Description                                                                                                                                                                                                                                                                | Returns                                                 |
|:------------------------:|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:--------------------------------------------------------|
| [`fasta.py`](./fasta.py) | Reads input in fasta format.                                                                                                                                                                                                                                               | a dictionary with ID as keys and DNA strands as values. |
| [`Motif.py`](./Motif.py) | To treat motifs equivalent to strings. It also stores the information of the positions that allow for multiple codons. It has `Inc` as subclass of `Motif` which accounts for [XY]: "either X or Y", and `Exc` as another subclass accounting for {X}: "any amino acid except X" |An object of class `Motif` with behaviours such as len, == operation with strings & indexing defined. 