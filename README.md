# Rosalind Bioinformatics Stronghold Problems

This repository contains 36 problems I solved from Rosalind, and few reusable utility files. 
I have shared the algorithms used and things I learned from each problem.
I have tried not using the predefined modules for bioinformatics as algorithm designing was the main focus.

---

## Utility Files

---

### 1. [`fasta.py`](./fasta.py)

**Description:** Reads input in FASTA format.

**Returns:** A dictionary with sequence IDs as keys and DNA strands as values.

---

### 2. [`Motif.py`](./Motif.py)

**Description:** Treats motifs as equivalent to strings while storing information about positions that allow multiple amino acids.
- Subclass `Inc` of `Motif` accounts for [XY]: either X or Y.
- Subclass `Exc` of `Motif` accounts for {X}: any amino acid except X.
- `list_to_motif` function converts any list of motifs or strings to `Motif` object.

**Returns:** An object of class `Motif`, with behaviours such as `len()`, equality comparisons (`==`) with strings, and indexing defined.

---

### 3. [`Streak.py`](./Streak.py)

**Description:** Maintains character streaks while finding substrings.

- `streak`: Finds all occurrences of a substring.
- `istreak`: Allows interactive streaking, updating the substring in each iteration and producing output according to a specified query (a function operating on the `streaks` set can be passed as a parameter)
- `multi`: Finds all occurrences of multiple substrings in a given string.

**Returns:**

- `streak` returns a set of all starting indices of the substring.
- `istreak` returns a generator object that yields the output of a query after checking each character of the string.
- `multi` returns a dictionary containing substrings as keys and sets of their initial occurrence indices as values.

---

### 4. [`uniprot.py`](./uniprot.py)
[Credit: Generated using Google Gemini.]

**Description:** Fetches protein data from the UniProt database using the protein ID.

**Returns:** A dictionary containing all available data about the protein.<br>
`uniprot(f"{ID}")["sequence"]["value"]` returns the protein sequence as a string.

---

### 5. [`RNA_Codon_Table.txt`](./RNA_Codon_Table.txt)

**Description:** A table indicating the translation of individual RNA codons into amino acids, stored in JSON format.

**Returns:** `json.loads(open("RNA_Codon_Table.txt").read())` returns a dictionary with RNA codons as keys and their corresponding amino acids as values.

---

### 6. [`Monoisotopic_Mass_Table.txt`](./Monoisotopic_Mass_Table.txt)

**Description:** Stores the monoisotopic masses of amino acids in JSON format.

**Returns:** `json.loads(open("Monoisotopic_Mass_Table.txt").read())` returns a dictionary with amino acids as keys and their corresponding masses as values.

---

## Problems Solved

---

### 1. Counting DNA Nucleotides

**Code:** [`dna.py`](./dna.py)

**Algorithm:**

**Learning:**

---

### 2. Transcribing DNA into RNA

**Code:** [`rna.py`](./rna.py)

**Algorithm:**

**Learning:**

---

### 3. Complementing a Strand of DNA

**Code:** [`revc.py`](./revc.py)

**Algorithm:**

**Learning:**

---

### 4. Rabbits and Recurrence Relations

**Code:** [`fib.py`](./fib.py)

**Algorithm:**

**Learning:**

---

### 5. Computing GC Content

**Code:** [`gc.py`](./gc.py)

**Algorithm:**

**Learning:**

---

### 6. Counting Point Mutations

**Code:** [`hamm.py`](./hamm.py)

**Algorithm:**

**Learning:**

---

### 7. Mendel's First Law

**Code:** [`iprb.py`](./iprb.py)

**Algorithm:**

**Learning:**

---

### 8. Translating RNA into Protein

**Code:** [`prot.py`](./prot.py)

**Algorithm:**

**Learning:**

---

### 9. Finding a Motif in DNA

**Code:** [`subs.py`](./subs.py)

**Algorithm:**

**Learning:**

---

### 10. Consensus and Profile

**Code:** [`cons.py`](./cons.py)

**Algorithm:**

**Learning:**

---

### 11. Mortal Fibonacci Rabbits

**Code:** [`fibd.py`](./fibd.py)

**Algorithm:**

**Learning:**

---

### 12. Overlap Graphs

**Code:** [`grph.py`](./grph.py)

**Algorithm:**

**Learning:**

---

### 13. Calculating Expected Offspring

**Code:** [`iev.py`](./iev.py)

**Algorithm:**

**Learning:**

---

### 14. Finding a Shared Motif

**Code:** [`lcsm.py`](./lcsm.py)

**Algorithm:**

**Learning:**

---

### 15. Independent Alleles

**Code:** [`lia.py`](./lia.py)

**Algorithm:**

**Learning:**

---

### 16. Finding a Protein Motif

**Code:** [`mprt.py`](./mprt.py)

**Algorithm:**

**Learning:**

---

### 17. Inferring mRNA from Protein

**Code:** [`mrna.py`](./mrna.py)

**Algorithm:**

**Learning:**

---

### 18. Open Reading Frames

**Code:** [`orf.py`](./orf.py)

**Algorithm:**

**Learning:**

---

### 19. Enumerating Gene Orders

**Code:** [`perm.py`](./perm.py)

**Algorithm:**

**Learning:**

---

### 20. Calculating Protein Mass

**Code:** [`prtm.py`](./prtm.py)

**Algorithm:**

**Learning:**

---

### 21. RNA Splicing

**Code:** [`splc.py`](./splc.py)

**Algorithm:**

**Learning:**

---

### 22. Enumerating k-mers Lexicographically

**Code:** [`lexf.py`](./lexf.py)

**Algorithm:**

**Learning:**

---

### 23. Longest Increasing Subsequence

**Code:** [`lgis.py`](./lgis.py)

**Algorithm:**

**Learning:**

---

### 24. Genome Assembly as Shortest Superstring

**Code:** [`long.py`](./long.py)

**Algorithm:**

**Learning:**

---

### 25. Partial Permutations

**Code:** [`pper.py`](./pper.py)

**Algorithm:**

**Learning:**

---

### 26. Introduction to Random Strings

**Code:** [`prob.py`](./prob.py)

**Algorithm:**

**Learning:**

---

### 27. Enumerating Oriented Gene Orderings

**Code:** [`sign.py`](./sign.py)

**Algorithm:**

**Learning:**

---

### 28. Finding a Spliced Motif

**Code:** [`sseq.py`](./sseq.py)

**Algorithm:**

**Learning:**

---

### 29. Completing a Tree

**Code:** [`tree.py`](./tree.py)

**Algorithm:**

**Learning:**

---

### 30. Error Correction in Reads

**Code:** [`corr.py`](./corr.py)

**Algorithm:**

**Learning:**

---

### 31. Counting Phylogenetic Ancestors

**Code:** [`inod.py`](./inod.py)

**Algorithm:**

**Learning:**

---

### 32. Speeding Up Motif Finding

**Code:** [`kmp.py`](./kmp.py)

**Algorithm:**

**Learning:**

---

### 33. Ordering Strings of Varying Length Lexicographically

**Code:** [`lexv.py`](./lexv.py)

**Algorithm:**

**Learning:**

---

### 34. Matching Random Motifs

**Code:** [`rstr.py`](./rstr.py)

**Algorithm:**

**Learning:**

---

### 35. Inferring Protein from Spectrum

**Code:** [`spec.py`](./spec.py)

**Algorithm:**

**Learning:**

---

### 36. Introduction to Pattern Matching

**Code:** [`trie.py`](./trie.py)

**Algorithm:**

**Learning:**

---