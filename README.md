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

**Algorithm:** Loop through each character of the string and count number of 'A','C','G' and 'T' using a dictionary.

---

### 2. Transcribing DNA into RNA

**Code:** [`rna.py`](./rna.py)

**Algorithm:** Replace 'T' with 'U' using `dna.replace('T','U')`

---

### 3. Complementing a Strand of DNA

**Code:** [`revc.py`](./revc.py)

**Algorithm:** Loop through every character in the reverse of the string and build another string using the complements of the characters.

---

### 4. Mendel's First Law

**Code:** [`iprb.py`](./iprb.py)

**Mathematics:**

$
\begin{align} \text{Notation: } &\text{A is the dominant allele,} \\&\text{a is the recessive allele,} \\&\text{X means can be any allele of the gene.}\end{align} 
$

$$
\begin{flalign*}
& \text{Given}, && \\
& k = n(AA) && \\
& m = n(Aa) && \\
& n = n(aa) 
\end{flalign*}
$$

$\text{Let Total population }N = k+m+n$


Considering different cases of pairs mating:
- Case 1: One of the parents is homozygous dominant $(AA\times XX)$

*Punett Square:*

|       | X  | X  |
|-------|----|----|
| **A** | AX | AX |
| **A** | AX | AX |

$\therefore P(AX|AA\times XX) = 1 $

$P(AA\times XX) = 1-\frac{{}^{N-k}C_2}{{}^NC_2}$

- Case 2: Both parents are heterozygous dominant $(Aa\times Aa)$

*Punett Square:*

|       | A  | a  |
|-------|----|----|
| **A** | AA | Aa |
| **a** | Aa | aa |

$\therefore P(AX|Aa\times Aa) = 0.75 $

$P(Aa\times Aa) = \frac{{}^mC_2}{{}^NC_2}$

- Case 3: One parent is heterozygous dominant and other is homozygous recessive $(Aa\times aa)$

*Punett Square:*

|       | a  | a  |
|-------|----|----|
| **A** | Aa | Aa |
| **a** | aa | aa |

$\therefore P(AX|Aa\times aa) = 0.5 $

$P(Aa\times aa) = \frac{m \cdot n}{{}^NC_2}$

- Case 4: Both parents are homozygous recessive $(aa\times aa)$

*Punett Square:*

|       | a  | a  |
|-------|----|----|
| **a** | aa | aa |
| **a** | aa | aa |

$\therefore P(AX|aa\times aa) = 0 $

$\therefore \boxed{P(AX)=1-\frac{{}^{N-k}C_2 - 0.75^mC_2 - 0.5m n}{{}^NC_2}}$


**Algorithm:** Calculated the probability using the above formula directly

**Learning:** How a trait in a population passes on to the next generation.

---

### 5. Calculating Expected Offspring

**Code:** [`iev.py`](./iev.py)

**Mathematics:** 
$$
\boxed{E[AX] = \sum{n(i)\cdot P(AX|i)}}
$$

Here, $i \in \{X\times Y: X,Y \in \{AA,Aa,aa\}\}$

$P(AX|i)$ follows from [`iprb`](#4-mendels-first-law) (Mendel's first law)

**Algorithm:** Calculated using the above formula, multiplying each of its term by 2, as each couple give 2 offsprings:`sum([2*i*j for i,j in zip(n,P)])`

**Learning:** This combined with [`iprb`](#4-mendels-first-law) can be used to model the genotypic ratio in a population.

---

### 5. Rabbits and Recurrence Relations

[**Problem Statement**](https://rosalind.info/problems/fib/)

**Code:** [`fib.py`](./fib.py)

**Algorithm:** Built the following function using recursion:

$$
f(n) = \begin{cases} 
  0 & \text{if } n \le 0 \\
  1 & \text{if } n = 1 \\ 
  f(n-1) + k \cdot f(n-2) & \text{if } n > 1
\end{cases}
$$

As `f(n-1)` are all the rabbits who are surviving from the previous generation. To account for new births, `f(n-2)` are the total number of rabbits which have reached reproductive age now, and each give birth to `k` rabbits

*Base Cases:*
- At `n < 1`, population is 0. 
- At `n = 1`, population is 1. (Given)

**Learning:** 
- The motive behind Fibonacci series.
- The simplest model of population growth.

---

### 6. Mortal Fibonacci Rabbits

[**Problem Statement**](https://rosalind.info/problems/fibd/)

**Code:** [`fibd.py`](./fibd.py)

**Mathematics:**

$$
\begin{flalign*}
\text{Let } &P_n = \text{Population of rabbits in }n^{th}\text{ generation} && \\
            &B_n = \text{Number of births in }n^{th}\text{ generation} && \\
            &D_n = \text{Number of deaths while transitioning from }(n-1)^{th}\text{ to }n^{th}\text{ generation} && \\
\end{flalign*}
$$

- The number of rabbits in $n^{th}$ generation are the rabbits from the previous generation after some deaths and births.

$$\therefore P_n = P_{n-1} + B_n - D_n$$

- The number of births in $n^{th}$ generation are given by the rabbits in $(n-2)^{th}$ generation as all of them have reached reproductive age, except for the rabbits which died while transitioning to next generation.

$$\therefore B_n = P_{n-2} - D_{n-1}$$

- The number of deaths in $n^{th}$ generation is the number of rabbits born in $(n-k)^{th}$

$$\therefore D_n = B_{n-k}$$


**Algorithm:** Defined the following three functions with some base cases:

$$
P(n) = \begin{cases} 
  0 & \text{if } n \le 0 \\
  1 & \text{if } n = 1 \\ 
  P(n-1) + B(n) - D(n) & \text{if } n > 1
\end{cases}
$$

$$
B(n) = \begin{cases} 
  0 & \text{if } n \le 0 \\
  1 & \text{if } n = 1 \\ 
  P(n-2) - D(n-1) & \text{if } n > 1
\end{cases}
$$

$$
D(n) = \begin{cases} 
  0 & \text{if } n \le 0 \\
  B(n-k) & \text{if } n > 1
\end{cases}
$$

**Learning:** Constructing ecological models from the scratch using simple logic.

---


### 4. Computing GC Content

**Code:** [`gc.py`](./gc.py)

**Algorithm:**

**Learning:**




---

### 6. Counting Point Mutations

**Code:** [`hamm.py`](./hamm.py)

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

### 12. Overlap Graphs

**Code:** [`grph.py`](./grph.py)

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