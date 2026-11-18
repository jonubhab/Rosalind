# Rosalind Bioinformatics Stronghold Problems

This repository contains 43 problems I solved from Rosalind, and a few reusable utility files.
I have shared the algorithms used and things I learned from each problem.
I have tried not using the predefined modules for bioinformatics, as algorithm design was the main focus.

---

## Index of Problems

| # | Code | Problem | Solution | Description |
|--:|:-----|:--------|:---------|:------------|
| 1 | `DNA` | [Counting DNA Nucleotides](https://rosalind.info/problems/dna/) | [`dna.py`](./dna.py) | [Notes](#1-counting-dna-nucleotides) |
| 2 | `RNA` | [Transcribing DNA into RNA](https://rosalind.info/problems/rna/) | [`rna.py`](./rna.py) | [Notes](#2-transcribing-dna-into-rna) |
| 3 | `REVC` | [Complementing a Strand of DNA](https://rosalind.info/problems/revc/) | [`revc.py`](./revc.py) | [Notes](#3-complementing-a-strand-of-dna) |
| 4 | `FIB` | [Rabbits and Recurrence Relations](https://rosalind.info/problems/fib/) | [`fib.py`](./fib.py) | [Notes](#4-rabbits-and-recurrence-relations) |
| 5 | `GC` | [Computing GC Content](https://rosalind.info/problems/gc/) | [`gc.py`](./gc.py) | [Notes](#5-computing-gc-content) |
| 6 | `HAMM` | [Counting Point Mutations](https://rosalind.info/problems/hamm/) | [`hamm.py`](./hamm.py) | [Notes](#6-counting-point-mutations) |
| 7 | `IPRB` | [Mendel's First Law](https://rosalind.info/problems/iprb/) | [`iprb.py`](./iprb.py) | [Notes](#7-mendels-first-law) |
| 8 | `PROT` | [Translating RNA into Protein](https://rosalind.info/problems/prot/) | [`prot.py`](./prot.py) | [Notes](#8-translating-rna-into-protein) |
| 9 | `SUBS` | [Finding a Motif in DNA](https://rosalind.info/problems/subs/) | [`subs.py`](./subs.py) | [Notes](#9-finding-a-motif-in-dna) |
| 10 | `CONS` | [Consensus and Profile](https://rosalind.info/problems/cons/) | [`cons.py`](./cons.py) | [Notes](#10-consensus-and-profile) |
| 11 | `FIBD` | [Mortal Fibonacci Rabbits](https://rosalind.info/problems/fibd/) | [`fibd.py`](./fibd.py) | [Notes](#11-mortal-fibonacci-rabbits) |
| 12 | `GRPH` | [Overlap Graphs](https://rosalind.info/problems/grph/) | [`grph.py`](./grph.py) | [Notes](#12-overlap-graphs) |
| 13 | `IEV` | [Calculating Expected Offspring](https://rosalind.info/problems/iev/) | [`iev.py`](./iev.py) | [Notes](#13-calculating-expected-offspring) |
| 14 | `LCSM` | [Finding a Shared Motif](https://rosalind.info/problems/lcsm/) | [`lcsm.py`](./lcsm.py) | [Notes](#14-finding-a-shared-motif) |
| 15 | `LIA` | [Independent Alleles](https://rosalind.info/problems/lia/) | [`lia.py`](./lia.py) | [Notes](#15-independent-alleles) |
| 16 | `MPRT` | [Finding a Protein Motif](https://rosalind.info/problems/mprt/) | [`mprt.py`](./mprt.py) | [Notes](#16-finding-a-protein-motif) |
| 17 | `MRNA` | [Inferring mRNA from Protein](https://rosalind.info/problems/mrna/) | [`mrna.py`](./mrna.py) | [Notes](#17-inferring-mrna-from-protein) |
| 18 | `ORF` | [Open Reading Frames](https://rosalind.info/problems/orf/) | [`orf.py`](./orf.py) | [Notes](#18-open-reading-frames) |
| 19 | `PERM` | [Enumerating Gene Orders](https://rosalind.info/problems/perm/) | [`perm.py`](./perm.py) | [Notes](#19-enumerating-gene-orders) |
| 20 | `PRTM` | [Calculating Protein Mass](https://rosalind.info/problems/prtm/) | [`prtm.py`](./prtm.py) | [Notes](#20-calculating-protein-mass) |
| 21 | `SPLC` | [RNA Splicing](https://rosalind.info/problems/splc/) | [`splc.py`](./splc.py) | [Notes](#21-rna-splicing) |
| 22 | `LEXF` | [Enumerating k-mers Lexicographically](https://rosalind.info/problems/lexf/) | [`lexf.py`](./lexf.py) | [Notes](#22-enumerating-k-mers-lexicographically) |
| 23 | `LGIS` | [Longest Increasing Subsequence](https://rosalind.info/problems/lgis/) | [`lgis.py`](./lgis.py) | [Notes](#23-longest-increasing-subsequence) |
| 24 | `LONG` | [Genome Assembly as Shortest Superstring](https://rosalind.info/problems/long/) | [`long.py`](./long.py) | [Notes](#24-genome-assembly-as-shortest-superstring) |
| 25 | `PPER` | [Partial Permutations](https://rosalind.info/problems/pper/) | [`pper.py`](./pper.py) | [Notes](#25-partial-permutations) |
| 26 | `PROB` | [Introduction to Random Strings](https://rosalind.info/problems/prob/) | [`prob.py`](./prob.py) | [Notes](#26-introduction-to-random-strings) |
| 27 | `SIGN` | [Enumerating Oriented Gene Orderings](https://rosalind.info/problems/sign/) | [`sign.py`](./sign.py) | [Notes](#27-enumerating-oriented-gene-orderings) |
| 28 | `SSEQ` | [Finding a Spliced Motif](https://rosalind.info/problems/sseq/) | [`sseq.py`](./sseq.py) | [Notes](#28-finding-a-spliced-motif) |
| 29 | `TREE` | [Completing a Tree](https://rosalind.info/problems/tree/) | [`tree.py`](./tree.py) | [Notes](#29-completing-a-tree) |
| 30 | `CORR` | [Error Correction in Reads](https://rosalind.info/problems/corr/) | [`corr.py`](./corr.py) | [Notes](#30-error-correction-in-reads) |
| 31 | `INOD` | [Counting Phylogenetic Ancestors](https://rosalind.info/problems/inod/) | [`inod.py`](./inod.py) | [Notes](#31-counting-phylogenetic-ancestors) |
| 32 | `KMP` | [Speeding Up Motif Finding](https://rosalind.info/problems/kmp/) | [`kmp.py`](./kmp.py) | [Notes](#32-speeding-up-motif-finding) |
| 33 | `LEXV` | [Ordering Strings of Varying Length Lexicographically](https://rosalind.info/problems/lexv/) | [`lexv.py`](./lexv.py) | [Notes](#33-ordering-strings-of-varying-length-lexicographically) |
| 34 | `RSTR` | [Matching Random Motifs](https://rosalind.info/problems/rstr/) | [`rstr.py`](./rstr.py) | [Notes](#34-matching-random-motifs) |
| 35 | `SPEC` | [Inferring Protein from Spectrum](https://rosalind.info/problems/spec/) | [`spec.py`](./spec.py) | [Notes](#35-inferring-protein-from-spectrum) |
| 36 | `TRIE` | [Introduction to Pattern Matching](https://rosalind.info/problems/trie/) | [`trie.py`](./trie.py) | [Notes](#36-introduction-to-pattern-matching) |
| 37 | `ASPC` | [Introduction to Alternative Splicing](https://rosalind.info/problems/aspc/) | [`aspc.py`](./aspc.py) | [Notes](#37-introduction-to-alternative-splicing) |
| 38 | `EVAL` | [Expected Number of Restriction Sites](https://rosalind.info/problems/eval/) | [`eval.py`](./eval.py) | [Notes](#38-expected-number-of-restriction-sites) |
| 39 | `MMCH` | [Maximum Matchings and RNA Secondary Structures](https://rosalind.info/problems/mmch/) | [`mmch.py`](./mmch.py) | [Notes](#39-maximum-matchings-and-rna-secondary-structures) |
| 40 | `PMCH` | [Perfect Matchings and RNA Secondary Structures](https://rosalind.info/problems/pmch/) | [`pmch.py`](./pmch.py) | [Notes](#40-perfect-matchings-and-rna-secondary-structures) |
| 41 | `REVP` | [Locating Restriction Sites](https://rosalind.info/problems/revp/) | [`revp.py`](./revp.py) | [Notes](#41-locating-restriction-sites) |
| 42 | `SSET` | [Counting Subsets](https://rosalind.info/problems/sset/) | [`sset.py`](./sset.py) | [Notes](#42-counting-subsets) |
| 43 | `TRAN` | [Transitions and Transversions](https://rosalind.info/problems/tran/) | [`tran.py`](./tran.py) | [Notes](#43-transitions-and-transversions) |

---

## Utility Files

---

### 1. [`fasta.py`](./fasta.py)

**Description:** Reads input in FASTA format.

**Returns:** A dictionary with sequence IDs as keys and DNA strands as values.

---

### 2. [`Motif.py`](./Motif.py)

**Description:** Treats motifs as equivalent to strings while storing information about positions that allow multiple amino acids.

- Subclass `Inc` of `Motif` accounts for `[XY]`: either X or Y.
- Subclass `Exc` of `Motif` accounts for `{X}`: any amino acid except X.
- `list_to_motif` function converts any list of motifs or strings to a `Motif` object.

**Returns:** An object of class `Motif`, with behaviours such as `len()`, equality comparisons (`==`) with strings, and indexing defined.

---

### 3. [`Streak.py`](./Streak.py)

**Description:** Maintains character streaks while finding substrings.

- `streak`: Finds all occurrences of a substring.
- `istreak`: Allows interactive streaking, updating the substring in each iteration and producing output according to a specified query (a function operating on the `streaks` set can be passed as a parameter).
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

[**Problem Statement**](https://rosalind.info/problems/dna/)

**Code:** [`dna.py`](./dna.py)

**Algorithm:** Loop through each character of the string and count the number of `A`, `C`, `G` and `T` nucleotides using a dictionary.

---

### 2. Transcribing DNA into RNA

[**Problem Statement**](https://rosalind.info/problems/rna/)

**Code:** [`rna.py`](./rna.py)

**Algorithm:** Replace every occurrence of `T` with `U` using `dna.replace('T', 'U')`.

---

### 3. Complementing a Strand of DNA

[**Problem Statement**](https://rosalind.info/problems/revc/)

**Code:** [`revc.py`](./revc.py)

**Algorithm:** Iterate through the DNA string in reverse order and build a new string by replacing each nucleotide with its complement.

---

### 4. Rabbits and Recurrence Relations

[**Problem Statement**](https://rosalind.info/problems/fib/)

**Code:** [`fib.py`](./fib.py)

**Mathematics:**

Let $f(n)$ be the rabbit population in generation $n$, and let $k$ be the number of offspring produced by each reproductive pair.

$$
f(n)=
\begin{cases}
0 & n\leq 0\\
1 & n=1\\
f(n-1)+k f(n-2) & n>1
\end{cases}
$$

The $f(n-1)$ term accounts for the rabbits surviving from the previous generation. The $f(n-2)$ term counts the rabbits that have reached reproductive age, each producing $k$ new pairs.

**Algorithm:** Implement the recurrence relation directly using recursion, with the base cases shown above.

**Learning:**

- The recurrence relation underlying the Fibonacci sequence.
- A simple model of population growth.

---

### 5. Computing GC Content

[**Problem Statement**](https://rosalind.info/problems/gc/)

**Code:** [`gc.py`](./gc.py)

**Mathematics:**

The GC content of a DNA sequence is the percentage of its nucleotides that are either Guanine or Cytosine.

$$
\text{GC}(\text{percent})=\frac{N_G+N_C}{N_A+N_C+N_G+N_T}\times 100
$$

**Algorithm:**

- Read the sequences using [`fasta.py`](./fasta.py).
- For each sequence, remove all occurrences of `A` and `T`. The remaining length gives the total number of `G` and `C` nucleotides.
- Divide this by the original sequence length to obtain the GC fraction.
- Keep track of the sequence with the maximum GC content.

---

### 6. Counting Point Mutations

[**Problem Statement**](https://rosalind.info/problems/hamm/)

**Code:** [`hamm.py`](./hamm.py)

**Mathematics:**

The Hamming distance between two strings of equal length is the number of positions at which their corresponding characters differ.

$$
d_H(s_1,s_2)=\sum_{i=1}^{n}[s_{1,i}\neq s_{2,i}]
$$

**Algorithm:**

- Iterate through both DNA strings simultaneously using `zip()`.
- Compare the characters at each position.
- Increment the counter whenever the two characters differ.

**Learning:** The Hamming distance provides a simple measure of sequence dissimilarity and is useful when comparing aligned DNA or protein sequences.

---

### 7. Mendel's First Law

[**Problem Statement**](https://rosalind.info/problems/iprb/)

**Code:** [`iprb.py`](./iprb.py)

**Mathematics:**

**Notation:**

- `A` is the dominant allele.
- `a` is the recessive allele.
- `X` can be either allele of the gene.

Given:

$$
k=n(AA),\qquad m=n(Aa),\qquad n=n(aa)
$$

Let the total population be:

$$
N=k+m+n
$$

Considering the possible pairs of parents:

**Case 1:** At least one parent is homozygous dominant, $AA\times XX$. The offspring will always have the dominant phenotype.

$$
P(AA\times XX)=1-\frac{\binom{N-k}{2}}{\binom{N}{2}}
$$

**Case 2:** Both parents are heterozygous, $Aa\times Aa$. The probability of a dominant phenotype is $3/4$.

$$
P(Aa\times Aa)=\frac{\binom{m}{2}}{\binom{N}{2}}
$$

**Case 3:** One parent is heterozygous and the other homozygous recessive, $Aa\times aa$. The probability of a dominant phenotype is $1/2$.

$$
P(Aa\times aa)=\frac{mn}{\binom{N}{2}}
$$

**Case 4:** Both parents are homozygous recessive, $aa\times aa$. The probability of a dominant phenotype is zero.

Combining the cases:

$$
\boxed{P(\text{dominant phenotype})=1-\frac{\binom{N-k}{2}-\frac34\binom{m}{2}-\frac12mn}{\binom{N}{2}}}
$$

**Algorithm:** Calculate the probability using the above formula directly.

**Learning:** How a trait is inherited across generations through the possible combinations of parental alleles.

---

### 8. Translating RNA into Protein

[**Problem Statement**](https://rosalind.info/problems/prot/)

**Code:** [`prot.py`](./prot.py)

**Algorithm:**

- Read the RNA codon table from [`RNA_Codon_Table.txt`](./RNA_Codon_Table.txt).
- Iterate through the RNA sequence in steps of three, extracting one codon at a time.
- Use the codon table to obtain the corresponding amino acid.
- Append the amino acid to the protein sequence.
- Stop translation when a stop codon is encountered.

**Learning:**

- The genetic code is degenerate: multiple codons can encode the same amino acid.
- Translation operates on non-overlapping triplets, with each codon specifying an amino acid or a termination signal.

---

### 9. Finding a Motif in DNA

[**Problem Statement**](https://rosalind.info/problems/subs/)

**Code:** [`subs.py`](./subs.py)

**Algorithm:**

- Use the `streak()` function from [`Streak.py`](./Streak.py) to find all occurrences of the motif.
- Maintain active `Streak` objects, each tracking a starting position and how many characters of the motif have matched.
- Extend a streak when the next character matches the corresponding motif character.
- Discard a streak when a mismatch occurs.
- Retain the starting positions of streaks that match the entire motif.

**Learning:** Maintaining multiple active partial matches allows overlapping occurrences of a motif to be detected during a scan.

---

### 10. Consensus and Profile

[**Problem Statement**](https://rosalind.info/problems/cons/)

**Code:** [`cons.py`](./cons.py)

**Mathematics:**

For a collection of aligned DNA sequences of length $n$, define the profile matrix:

$$
P_{b,i}=\text{Number of occurrences of nucleotide }b\text{ at position }i
$$

where $b\in\lbrace A,C,G,T\rbrace $.

The consensus sequence is constructed by selecting the most frequent nucleotide at every position:

$$
C_i=\underset{b\in\lbrace A,C,G,T\rbrace }{\mathrm{argmax}} P_{b,i}
$$

**Algorithm:**

- Read the sequences using [`fasta.py`](./fasta.py).
- Initialise a profile matrix with four rows, one for each nucleotide, and one column for every sequence position.
- Iterate through the aligned sequences and increment the corresponding nucleotide count at each position.
- Construct the consensus sequence by selecting the nucleotide with the maximum count in each column.

**Learning:**

- A consensus sequence summarises the most common nucleotide at each position in a collection of aligned sequences.
- The profile matrix retains more information than the consensus sequence alone, as it also captures variation at each position.

---

### 11. Mortal Fibonacci Rabbits

[**Problem Statement**](https://rosalind.info/problems/fibd/)

**Code:** [`fibd.py`](./fibd.py)

**Mathematics:**

Let:

- $P_n$ be the population of rabbits in generation $n$.
- $B_n$ be the number of births in generation $n$.
- $D_n$ be the number of deaths while transitioning from generation $(n-1)$ to generation $n$.

The population in generation $n$ is:

$$
P_n=P_{n-1}+B_n-D_n
$$

The number of births is determined by the rabbits that reached reproductive age, excluding those that died:

$$
B_n=P_{n-2}-D_{n-1}
$$

The number of deaths is the number of rabbits born $k$ generations earlier:

$$
D_n=B_{n-k}
$$

**Algorithm:** Define three recursive functions with appropriate base cases:

$$
P(n)=
\begin{cases}
0 & n\leq0\\
1 & n=1\\
P(n-1)+B(n)-D(n) & n>1
\end{cases}
$$

$$
B(n)=
\begin{cases}
0 & n\leq0\\
1 & n=1\\
P(n-2)-D(n-1) & n>1
\end{cases}
$$

$$
D(n)=
\begin{cases}
0 & n\leq0\\
B(n-k) & n\geq1
\end{cases}
$$

**Learning:** Constructing an ecological population model from simple birth and death rules.

---

### 12. Overlap Graphs

[**Problem Statement**](https://rosalind.info/problems/grph/)

**Code:** [`grph.py`](./grph.py)

**Algorithm:**

- Read the DNA sequences using [`fasta.py`](./fasta.py).
- Generate all ordered pairs of distinct sequences using `permutations(data, 2)`.
- For each pair, check whether the last three nucleotides of the first sequence match the first three nucleotides of the second sequence.
- If they match, add a directed edge from the first sequence to the second sequence.

**Learning:**

- DNA sequence assembly can be represented using directed graphs, where vertices represent sequences and edges represent overlaps.
- The direction of an edge matters because the suffix of one sequence must match the prefix of another.

---

### 13. Calculating Expected Offspring

[**Problem Statement**](https://rosalind.info/problems/iev/)

**Code:** [`iev.py`](./iev.py)

**Mathematics:**

The expected number of offspring with a dominant phenotype is:

$$
E[X]=\sum_i n(i) P(\text{dominant phenotype}\mid i)
$$

Here, $i$ represents one of the six possible genotype pairings supplied by the problem. The conditional probabilities follow from Mendel's first law, described in [`iprb.py`](./iprb.py).

Since each couple produces two offspring, the expected number is:

$$
E[X]=2\sum_i n(i) P(\text{dominant phenotype}\mid i)
$$

**Algorithm:** Calculate the expected number using the above expression, multiplying each term by two because each couple produces two offspring.

**Learning:** Combining Mendel's first law with expectation allows the expected number of offspring showing a particular phenotype to be calculated from the parental genotype distribution.

---

### 14. Finding a Shared Motif

[**Problem Statement**](https://rosalind.info/problems/lcsm/)

**Code:** [`lcsm.py`](./lcsm.py)

**Data Structure:**

- The DNA strings are stored in a dictionary `data`.
- An object of class `Unit` stores a substring from the DNA string of minimum length and the position of its first occurrence in every other string.
- A set of all active `Unit` objects is maintained as `units`.
- All `Unit` objects read from the shared class variables `master` and `data`.

**Algorithm:**

- Read the data using [`fasta.py`](./fasta.py).
- Separate the shortest DNA string from `data` and set it as `Unit.master`. The remaining sequences are stored in `Unit.data`.
- Initially, every character of `Unit.master` becomes a substring in a different `Unit` object.
- In each iteration, `Unit_obj.check()` finds occurrences of the substring in the other DNA strings and stores their positions.
- If `Unit_obj.check()` returns `False`, the substring does not exist in all the DNA strings, and the unit is marked for removal.
- If it returns `True`, the unit is updated using `Unit_obj.update()`. The next character from `master` is appended to its substring, increasing its length.
- In subsequent checks, only the newly appended character needs to be checked when extending a previously located occurrence. The rest of the substring is already known to match.
- If the next character does not match, the next occurrence of the substring is searched for in that DNA string. If no occurrence is found, the unit is marked for removal.
- After each iteration, units marked for removal are deleted, ensuring that all surviving substrings have equal lengths.
- Continue until no further extensions are possible. The surviving substring is the longest shared motif found by this procedure.

**Learning:**

- Long substrings repeated across several DNA strings are potential motifs.
- Starting with the shortest DNA sequence reduces the initial candidate search space, since a shared substring cannot be longer than the shortest input sequence.

---

### 15. Independent Alleles

[**Problem Statement**](https://rosalind.info/problems/lia/)

**Code:** [`lia.py`](./lia.py)

**Mathematics:**

For a cross between two $AaBb$ parents, the probability of an offspring being heterozygous at both loci is:

$$
P(AaBb)=P(Aa)\cdot P(Bb)=\frac12\cdot\frac12=\frac14
$$

Each generation contains $2^k$ individuals. Under the specified mating model, the number of $AaBb$ individuals follows a binomial distribution:

$$
X\sim\mathrm{Binomial}\left(2^k,\frac14\right)
$$

The required probability is:

$$
P(X\geq N)= \sum_{i=N}^{2^k} \binom{2^k}{i}
\left(\frac14\right)^i
\left(\frac34\right)^{2^k-i}
$$

**Algorithm:**

- Calculate the total number of individuals as $2^k$.
- Calculate the binomial coefficient $\binom{2^k}{i}$ using a recursive function.
- Sum the binomial probabilities for all values $i\geq N$.

**Learning:**

- Under the specified $AaBb\times AaBb$ mating model, the probability of an offspring being $AaBb$ remains $1/4$ in every generation.
- This does not mean that the expected counts of all genotypes remain constant. The population size doubles each generation, while genotype probabilities are determined by the mating model.
- Independent assortment allows probabilities at two loci to be multiplied.

---

### 16. Finding a Protein Motif

[**Problem Statement**](https://rosalind.info/problems/mprt/)

**Code:** [`mprt.py`](./mprt.py)

**Motif:**

The required N-glycosylation motif is:

```text
N{P}[ST]{P}
```

This means:

- The first amino acid must be `N`.
- The second amino acid can be anything except `P`.
- The third amino acid must be either `S` or `T`.
- The fourth amino acid can be anything except `P`.

**Algorithm:**

- Fetch the protein sequence from UniProt using [`uniprot.py`](./uniprot.py).
- Represent the motif using the `Motif` class from [`Motif.py`](./Motif.py).
- Use `streak()` from [`Streak.py`](./Streak.py) to find all occurrences of the motif.
- Retain complete matches and report their starting positions.

**Learning:**

- Protein motifs can be represented using patterns with both inclusion and exclusion constraints, rather than only exact amino-acid sequences.
- Such motifs can indicate potential functional or structural sites in proteins. A sequence match identifies a potential site, not necessarily a confirmed biological modification.

---

### 17. Inferring mRNA from Protein

[**Problem Statement**](https://rosalind.info/problems/mrna/)

**Code:** [`mrna.py`](./mrna.py)

**Mathematics:**

Since the genetic code is degenerate, an amino acid may be encoded by multiple RNA codons.

Let $r(a)$ denote the number of codons encoding amino acid $a$. For a protein sequence $p_1p_2\ldots p_n$, the number of possible RNA sequences is:

$$
M=r(\text{Stop})\prod_{i=1}^{n}r(p_i)
$$

The stop codon is included because translation must terminate.

**Algorithm:**

- Read the RNA codon table and construct a dictionary containing the number of codons corresponding to each amino acid.
- Iterate through the protein sequence and multiply the number of possible codons for each amino acid.
- Multiply by the number of possible stop codons.
- Take the result modulo $10^6$ after every multiplication.

**Learning:**

- The degeneracy of the genetic code means that a protein sequence does not uniquely determine its corresponding mRNA sequence.
- The number of possible coding sequences can be calculated using the multiplication principle of combinatorics.

---

### 18. Open Reading Frames

[**Problem Statement**](https://rosalind.info/problems/orf/)

**Code:** [`orf.py`](./orf.py)

**Algorithm:**

- Read the DNA sequence and RNA codon table.
- Define a `scan()` generator that scans the sequence one nucleotide at a time while maintaining a rolling three-character codon.
- Maintain three reading-frame lists, corresponding to the three possible reading frames.
- Whenever an `AUG` codon is encountered, start a new protein sequence with methionine (`M`).
- For every subsequent codon, extend all currently active protein sequences in that reading frame.
- When a stop codon is encountered, yield the completed protein sequences and clear that reading frame.
- Repeat the process for both the original DNA strand and its reverse complement.
- Combine the resulting proteins into a set to remove duplicates.

**Learning:**

- A DNA sequence has three possible reading frames on each strand, giving six possible reading frames in total.
- Translation can begin at multiple start codons, and different open reading frames can overlap.
- The reverse complement must also be examined because genes can be encoded on either DNA strand.

---

### 19. Enumerating Gene Orders

[**Problem Statement**](https://rosalind.info/problems/perm/)

**Code:** [`perm.py`](./perm.py)

**Mathematics:**

The number of permutations of $n$ distinct elements is:

$$
P(n)=n!
$$

**Algorithm:**

- Calculate $n!$ using `math.factorial()`.
- Use `itertools.permutations()` to generate every permutation of the integers from $1$ to $n$.
- Write the total number of permutations followed by all generated permutations.

---

### 20. Calculating Protein Mass

[**Problem Statement**](https://rosalind.info/problems/prtm/)

**Code:** [`prtm.py`](./prtm.py)

**Mathematics:**

The mass of a protein sequence is the sum of the monoisotopic masses of its constituent amino-acid residues.

$$
M=\sum_{i=1}^{n}m(a_i)
$$

where $m(a_i)$ is the monoisotopic mass of the amino acid at position $i$.

**Algorithm:**

- Read the monoisotopic mass table from [`Monoisotopic_Mass_Table.txt`](./Monoisotopic_Mass_Table.txt).
- Iterate through the protein sequence and add the corresponding amino-acid mass to the total.
- Print the total mass to three decimal places.

**Learning:** Protein mass can be estimated from its amino-acid sequence using the monoisotopic masses of individual residues.

---

### 21. RNA Splicing

[**Problem Statement**](https://rosalind.info/problems/splc/)

**Code:** [`splc.py`](./splc.py)

**Algorithm:**

- Read the DNA sequences using [`fasta.py`](./fasta.py).
- Identify the longest sequence as the original DNA strand and treat the remaining sequences as introns.
- Use `multi()` from [`Streak.py`](./Streak.py) to locate occurrences of the introns in the original strand.
- Collect the starting and ending positions of complete intron matches.
- Sort the intervals and merge overlapping or adjacent intervals.
- Extract the regions outside the merged intron intervals to obtain the exons.
- Join the exons, replace `T` with `U`, and translate the resulting RNA using [`prot.py`](./prot.py).

**Learning:**

- RNA splicing removes introns from pre-mRNA and joins the remaining exons.
- Splicing changes the sequence that is ultimately translated into a protein.
- Merging intervals prevents overlapping intron matches from causing the same region to be removed more than once.

---

### 22. Enumerating k-mers Lexicographically

[**Problem Statement**](https://rosalind.info/problems/lexf/)

**Code:** [`lexf.py`](./lexf.py)

**Algorithm:**

- Define an `Odo()` generator that maintains a list of counters, initially filled with zeroes.
- Interpret the counter list as a number written in base $n$, where $n$ is the size of the supplied alphabet.
- Increment the counter from the least significant position, carrying over whenever a position reaches $n$.
- Reverse the counter list before yielding it so that the generated strings follow the required lexicographic order.
- Convert each counter into its corresponding alphabet character and write the resulting strings.

**Learning:**

- A fixed-length string over an alphabet of size $n$ can be represented as a base-$n$ number.
- Incrementing such a number systematically enumerates all possible strings of that length.

---

### 23. Longest Increasing Subsequence

[**Problem Statement**](https://rosalind.info/problems/lgis/)

**Code:** [`lgis.py`](./lgis.py)

**Data Structure:**

- Each element of the permutation is represented by an object of class `Graph`.
- Every object stores its value, a list of nodes that can follow it, and a cached longest path.
- The nodes are maintained in sorted order.

**Algorithm:**

- Insert each element into the sorted node list using `bisect_right()`.
- For every newly inserted element $x$, connect it to earlier elements that can precede it in an increasing subsequence.
- The `check()` method determines whether a node can be connected to the new element.
- Once the graph is constructed, recursively traverse the graph to find the longest path starting from each node.
- Cache the longest path in `lpath` to avoid recomputing it.
- Repeat the process for the reversed permutation and reverse the resulting sequence to obtain the longest decreasing subsequence.

**Mathematics:**

The graph is directed from smaller elements to larger elements. Every directed path therefore represents an increasing subsequence.

The length of the longest increasing subsequence starting at a node $v$ can be expressed as:

$$
L(v)=
\begin{cases}
1, & \text{if }v\text{ has no outgoing edges}\\
1+\max\limits_{u\in N(v)}L(u), & \text{otherwise}
\end{cases}
$$

where $N(v)$ is the set of nodes connected from $v$.

**Learning:**

- A sequence problem can be transformed into a graph problem by representing valid transitions as directed edges.
- Finding the longest increasing subsequence then becomes finding the longest directed path in the constructed graph.

---

### 24. Genome Assembly as Shortest Superstring

[**Problem Statement**](https://rosalind.info/problems/long/)

**Code:** [`long.py`](./long.py)

**Data Structure:**

- Each DNA read is represented by a `Node` containing its label, sequence, weight and outgoing edges.
- An `Edge` stores the overlap length between two reads and the node it connects to.
- A `Walker` stores the current path, its score and a bitmask indicating which nodes have been visited.

**Algorithm:**

- Read the DNA sequences using [`fasta.py`](./fasta.py).
- Create a node for each sequence and a starting node connected to every sequence.
- For every ordered pair of distinct reads, calculate the maximum suffix-prefix overlap using `overlap()`.
- Add a directed edge whenever a valid overlap exists. The overlap length is used as the edge weight.
- Start traversing the graph from the artificial starting node.
- During traversal, add the overlap weight whenever an edge is followed.
- If a node is visited more than once, subtract the length of its sequence from the score.
- Store paths that have visited every node.
- Select the path with the maximum score.
- Stitch the reads together using their overlaps to reconstruct the sequence.

**Mathematics:**

Suppose a path contains reads $S_1,S_2,\ldots,S_r$, and let $w_i$ denote the overlap between consecutive reads.

If every read appears at least once, the assembled sequence length is:

$$
L=\sum_{i=1}^{r}\lvert S_i\rvert-\sum_{i=1}^{r-1}w_i
$$

Thus, maximising the total overlap minimises the assembled length.

To account for repeated reads, the score is defined as:

$$
S=\sum_{\text{edges}}w(e)
-\sum_{\text{repeated reads }j}\lvert S_j\rvert
$$

The penalty accounts for the additional sequence contribution introduced by revisiting a read. Under this scoring construction, maximising the score is intended to minimise the resulting assembled length.

**Learning:**

- Sequence assembly can be formulated as an optimisation problem over overlaps between reads.
- Maximising overlap is equivalent to minimising the number of nucleotides added while stitching sequences together.
- Repeated reads can be accommodated by penalising their additional sequence contribution rather than prohibiting their repetition outright.

---

### 25. Partial Permutations

[**Problem Statement**](https://rosalind.info/problems/pper/)

**Code:** [`pper.py`](./pper.py)

**Mathematics:**

The number of ways to arrange $k$ elements selected from $n$ distinct elements is:

$$
P(n,k)=\frac{n!}{(n-k)!}
$$

Equivalently,

$$
P(n,k)=n(n-1)(n-2)\cdots(n-k+1)
$$

**Algorithm:**

- Define a recursive function that multiplies the integers from $n-k+1$ to $n$.
- Take the result modulo $10^6$ during each recursive multiplication.

---

### 26. Introduction to Random Strings

[**Problem Statement**](https://rosalind.info/problems/prob/)

**Code:** [`prob.py`](./prob.py)

**Mathematics:**

Let $x$ be the GC-content probability of a randomly generated DNA sequence.

Then:

$$
P(A)=P(T)=\frac{1-x}{2}
$$

$$
P(G)=P(C)=\frac{x}{2}
$$

For a particular DNA sequence $s=s_1s_2\ldots s_n$, assuming independent nucleotide generation:

$$
P(s)=\prod_{i=1}^{n}P(s_i)
$$

Taking the base-10 logarithm:

$$
\log_{10}P(s)=\sum_{i=1}^{n}\log_{10}P(s_i)
$$

**Algorithm:**

- Define `prob(dna,x)` to calculate the logarithm of the probability of generating the given DNA sequence for a specified GC content.
- For every nucleotide, add the logarithm of its corresponding probability.
- If a nucleotide has zero probability under the specified GC content, return negative infinity.
- Repeat for every supplied GC-content value.

**Learning:** Logarithms convert products of probabilities into sums, making probability calculations easier and more numerically stable.

---

### 27. Enumerating Oriented Gene Orderings

[**Problem Statement**](https://rosalind.info/problems/sign/)

**Code:** [`sign.py`](./sign.py)

**Mathematics:**

An oriented permutation consists of a permutation of the integers $1,\ldots,n$ and an independent choice of positive or negative sign for each element.

The number of possible oriented permutations is:

$$
2^n n!
$$

**Algorithm:**

- Generate all permutations of the integers from $1$ to $n$.
- Generate all $2^n$ possible sign combinations using the binary representation of an integer.
- Convert each binary digit into either $+1$ or $-1$.
- Multiply the sign array element-wise with each permutation to obtain all oriented permutations.

**Learning:** Independent binary choices can be enumerated using bit representations. Combining permutations with sign choices produces a combinatorial space whose size follows the multiplication principle.

---

### 28. Finding a Spliced Motif

[**Problem Statement**](https://rosalind.info/problems/sseq/)

**Code:** [`sseq.py`](./sseq.py)

**Mathematics:**

A sequence $t$ is a subsequence of $s$ if there exist indices

$$
1\leq i_1<i_2<\cdots<i_k\leq \lvert s\rvert
$$

such that

$$
t_j=s_{i_j}
$$

for every $j$.

**Algorithm:**

- Read the DNA sequences using [`fasta.py`](./fasta.py).
- Select the longest sequence as the main DNA string and the shortest sequence as the subsequence to locate.
- Scan the main DNA string from left to right.
- Whenever the current character matches the next required character of the shorter sequence, record its position and advance to the next character.
- Stop when every character of the shorter sequence has been found.

**Learning:** A subsequence preserves the relative order of characters but does not require them to be adjacent. A greedy left-to-right scan finds a valid embedding whenever one exists.

---

### 29. Completing a Tree

[**Problem Statement**](https://rosalind.info/problems/tree/)

**Code:** [`tree.py`](./tree.py)

**Mathematics:**

A tree with $n$ vertices has exactly:

$$
E=n-1
$$

edges.

For a forest with $n$ vertices and $E$ edges, the number of connected components is:

$$
c=n-E
$$

The minimum number of additional edges required to connect all components is therefore:

$$
c-1=n-E-1
$$

**Algorithm:**

- Read the number of vertices and the existing edges.
- Calculate the number of connected components as $n-E$, using the fact that the given graph is a forest.
- Subtract one to obtain the number of additional edges required.

**Learning:** Every additional edge connecting two separate components reduces the number of connected components by exactly one.

---

### 30. Error Correction in Reads

[**Problem Statement**](https://rosalind.info/problems/corr/)

**Code:** [`corr.py`](./corr.py)

**Algorithm:**

- Read the DNA reads using [`fasta.py`](./fasta.py).
- Maintain a dictionary `corr` that records whether each read is already considered correct.
- For each read, compare it against the other reads and their reverse complements.
- If an identical read or reverse complement exists, mark it as correct.
- For every read that remains uncorrected, search among the reads already marked correct.
- Calculate the Hamming distance using [`hamm.py`](./hamm.py).
- If the distance is exactly one, replace the incorrect read with the matching correct read.
- Also check the reverse complement of the correct read.
- Write the resulting corrections.

**Mathematics:**

Two reads are identical if:

$$
d_H(s_1,s_2)=0
$$

A read is considered correctable if its Hamming distance from a correct read or its reverse complement is:

$$
d_H(s_{\text{incorrect}},s_{\text{correct}})=1
$$

**Learning:**

- Sequencing errors can be identified by comparing reads against repeated observations.
- Reverse complements must be considered because DNA reads may originate from either strand.
- Hamming distance provides a simple way to identify reads differing by a single nucleotide.

---

### 31. Counting Phylogenetic Ancestors

[**Problem Statement**](https://rosalind.info/problems/inod/)

**Code:** [`inod.py`](./inod.py)

**Mathematics:**

For an unrooted binary tree with $n$ leaves, let $I$ be the number of internal vertices.

Every internal vertex has degree three, and every leaf has degree one. By the handshaking lemma:

$$
2E=n+3I
$$

Since a tree with $n+I$ vertices has $n+I-1$ edges:

$$
2(n+I-1)=n+3I
$$

Therefore:

$$
\boxed{I=n-2}
$$

**Algorithm:** Read the number of leaves $n$ and subtract two to obtain the number of internal vertices.

**Learning:** The number of internal vertices in a binary phylogenetic tree can be derived using the relationship between vertices, edges and vertex degrees.

---

### 32. Speeding Up Motif Finding

[**Problem Statement**](https://rosalind.info/problems/kmp/)

**Code:** [`kmp.py`](./kmp.py)

**Mathematics:**

For a string $s$, the prefix function at position $i$ is:

$$
\pi(i)= \max\lbrace k : s[0:k]=s[i-k+1:i+1]\rbrace 
$$

where $k$ is restricted to proper prefixes of the substring ending at position $i$.

**Algorithm:**

- Initialise an interactive streak generator using `streak()` from [`Streak.py`](./Streak.py).
- The generator scans the DNA string once.
- At each position, existing streaks are extended if the current character matches their next required character.
- New streaks are initiated using the prefix supplied to the generator.
- The prefixes supplied to the generator become progressively shorter, allowing candidate prefixes to be introduced at different positions during the scan.
- At every position, the query returns the maximum length among the active streaks, giving the longest prefix that is also a suffix of the substring scanned so far.

**Learning:**

- The prefix function tracks the longest proper prefix that is also a suffix.
- Maintaining active partial matches allows prefixes and suffixes to grow together during a scan, rather than repeatedly comparing entire substrings.
- This is the central idea behind the Knuth-Morris-Pratt pattern-matching algorithm.

---

### 33. Ordering Strings of Varying Length Lexicographically

[**Problem Statement**](https://rosalind.info/problems/lexv/)

**Code:** [`lexv.py`](./lexv.py)

**Algorithm:**

- Define an `Odo()` generator similar to the one in [`lexf.py`](./lexf.py).
- Add a blank character to the alphabet to represent the absence of a character.
- Use a counter array to enumerate strings of lengths up to the specified maximum.
- Reject counter combinations in which a blank character appears before a non-blank character. This ensures that the generated strings contain no internal gaps.
- Reverse the counter array before yielding it to maintain the required lexicographic order.
- Convert the remaining counter values into their corresponding alphabet characters.

**Learning:** Strings of varying lengths can be enumerated using a fixed-length representation by introducing a special symbol to represent an absent character and restricting where that symbol can occur.

---

### 34. Matching Random Motifs

[**Problem Statement**](https://rosalind.info/problems/rstr/)

**Code:** [`rstr.py`](./rstr.py)

**Mathematics:**

Let $p$ be the probability of generating the given DNA motif under a specified GC content.

The probability that the motif does not occur at a particular starting position is:

$$
1-p
$$

There are $N$ possible starting positions. Using the independent-trial model:

$$
P(\text{at least one occurrence})=1-(1-p)^N
$$

**Algorithm:**

- Use `prob()` from [`prob.py`](./prob.py) to calculate the logarithm of the probability of generating the motif.
- Convert the logarithmic probability back to ordinary probability using $10^{P}$.
- Calculate the number of possible starting positions as $N=n-\lvert s\rvert+1$.
- Use the complementary probability to calculate the probability of at least one occurrence.

**Learning:** Complementary probability simplifies calculations involving the probability of at least one occurrence. The independent-trial expression is the model used here; overlapping motif windows are not generally independent.

---

### 35. Inferring Protein from Spectrum

[**Problem Statement**](https://rosalind.info/problems/spec/)

**Code:** [`spec.py`](./spec.py)

**Mathematics:**

The difference between two consecutive prefix masses corresponds to the monoisotopic mass of the amino-acid residue added between them.

$$
m_i=M_{i+1}-M_i
$$

**Algorithm:**

- Read the prefix masses and the monoisotopic mass table.
- Construct a reverse dictionary mapping amino-acid masses to amino-acid symbols.
- Calculate the difference between every pair of consecutive prefix masses.
- Find the amino acid whose monoisotopic mass is closest to the calculated difference.
- Append the corresponding amino acid to the inferred protein sequence.

**Learning:** A protein can be inferred from its mass spectrum by examining differences between consecutive prefix masses.

---

### 36. Introduction to Pattern Matching

[**Problem Statement**](https://rosalind.info/problems/trie/)

**Code:** [`trie.py`](./trie.py)

**Data Structure:**

- Each node of class `Trie` stores a character, a unique node number and a list of child nodes.
- The root node represents the beginning of all strings.
- Every subsequent character is represented by a child node.

**Algorithm:**

- Initialise the trie with a root node.
- Insert each input string character by character.
- At every node, check whether a child containing the next character already exists.
- If it exists, move to that child.
- Otherwise, create a new node, connect it to the current node and write the corresponding directed edge.
- Continue until the entire string has been inserted.

**Learning:** A trie stores strings by sharing common prefixes. Instead of storing every string independently, common prefixes are represented only once, reducing redundant storage and allowing efficient prefix-based searches.

---

## Additional Problems

---

### 37. Introduction to Alternative Splicing

[**Problem Statement**](https://rosalind.info/problems/aspc/)

**Code:** [`aspc.py`](./aspc.py)

**Mathematics:**

For a sequence containing $n$ exons, the number of ways to select exactly $i$ exons is:

$$
\binom{n}{i}=\frac{n!}{i!(n-i)!}
$$

The total number of selections containing at least $m$ exons is:

$$
\sum_{i=m}^{n}\binom{n}{i}
$$

**Algorithm:**

- Use `math.comb()` to calculate the binomial coefficient for each value of $i$ from $m$ to $n$.
- Add the coefficients while taking the result modulo $10^6$.

**Learning:** Alternative splicing allows different combinations of exons to be included in mature mRNA. Counting these combinations is an application of binomial coefficients.

---

### 38. Expected Number of Restriction Sites

[**Problem Statement**](https://rosalind.info/problems/eval/)

**Code:** [`eval.py`](./eval.py)

**Mathematics:**

For a DNA sequence of length $n$, a motif of length $k$ has:

$$
N=n-k+1
$$

possible starting positions.

If the probability of generating the motif at a particular position is $p$, the expected number of occurrences is:

$$
E[X]=Np
$$

Using [`prob.py`](./prob.py), the motif probability is obtained from the logarithmic probability:

$$
p=10^{\mathrm{prob}(s,x)}
$$

Therefore:

$$
E[X]=(n-k+1)\cdot10^{\mathrm{prob}(s,x)}
$$

**Algorithm:**

- Read the DNA length, motif and GC-content values.
- Calculate the number of possible starting positions.
- For each GC-content value, calculate the motif probability using `prob()` from [`prob.py`](./prob.py).
- Multiply the probability by the number of possible starting positions to obtain the expected number of occurrences.

**Learning:** Linearity of expectation allows the expected number of occurrences to be calculated by summing the probabilities of occurrence at each possible starting position. Independence between positions is not required for this expectation calculation.

---

### 39. Maximum Matchings and RNA Secondary Structures

[**Problem Statement**](https://rosalind.info/problems/mmch/)

**Code:** [`mmch.py`](./mmch.py)

**Mathematics:**

The possible complementary base pairs are:

$$
A\leftrightarrow U,\qquad G\leftrightarrow C
$$

For a maximum matching, every nucleotide of the less frequent type must be paired with a distinct nucleotide of the more frequent type.

If there are $a$ adenines and $u$ uracils, the number of possible maximum matchings is:

$$
P(\max(a,u),\min(a,u)) =
\frac{\max(a,u)!}{(\max(a,u)-\min(a,u))!}
$$

Similarly, for guanine and cytosine:

$$
P(\max(g,c),\min(g,c)) =
\frac{\max(g,c)!}{(\max(g,c)-\min(g,c))!}
$$

The two types of base pairs are independent, so:

$$
M= P(\max(a,u),\min(a,u)) \cdot
P(\max(g,c),\min(g,c))
$$

**Algorithm:**

- Count the occurrences of `A`, `U`, `G` and `C`.
- Define a recursive function to calculate the falling factorial $P(n,r)=n(n-1)\cdots(n-r+1)$.
- Calculate the maximum matching count independently for the A-U and G-C pairs.
- Multiply the two results.

**Learning:** Counting maximum matchings is a combinatorial problem involving permutations of distinct elements. The two complementary nucleotide pairs can be treated independently.

---

### 40. Perfect Matchings and RNA Secondary Structures

[**Problem Statement**](https://rosalind.info/problems/pmch/)

**Code:** [`pmch.py`](./pmch.py)

**Mathematics:**

A perfect matching pairs every nucleotide with exactly one complementary nucleotide. Therefore, the number of adenines must equal the number of uracils, and the number of guanines must equal the number of cytosines.

For $n$ A-U pairs and $m$ G-C pairs, the number of perfect matchings is:

$$
M=n!\cdot m!
$$

**Algorithm:**

- Count the number of adenines and guanines in the RNA sequence.
- Calculate the factorial of each count using a recursive function.
- Multiply the two factorials.

**Learning:** A perfect matching requires every element to be paired exactly once. When the two sets being paired have equal sizes, the number of possible one-to-one pairings is the factorial of either set's size.

---

### 41. Locating Restriction Sites

[**Problem Statement**](https://rosalind.info/problems/revp/)

**Code:** [`revp.py`](./revp.py)

**Mathematics:**

A reverse-complement palindrome satisfies:

$$
s=\mathrm{revcomp}(s)
$$

Let $x$ be the current substring of length $L$, and let $q$ be the maximum suffix-prefix overlap between $x$ and its reverse complement:

$$
x[L-q:L]=\mathrm{revcomp}(x)[0:q]
$$

Suppose a longer substring of length $L+t$ is a reverse-complement palindrome. Its first $L$ characters are $x$, so its last $L$ characters must be $\mathrm{revcomp}(x)$.

The existing portion of this last block must therefore satisfy:

$$
x[t:L]=\mathrm{revcomp}(x)[0:L-t]
$$

This is a suffix-prefix overlap of length $L-t$. Since $q$ is the maximum possible overlap:

$$
L-t\leq q
$$

Therefore:

$$
\boxed{t\geq L-q}
$$

No palindrome can occur at the next $L-q-1$ candidate lengths. The next possible candidate length is:

$$
\boxed{L_{\text{next}}=L+(L-q)}
$$

**Algorithm:**

- Read the DNA sequence using [`fasta.py`](./fasta.py).
- Start at every position in the DNA sequence.
- Initially consider a substring of length four.
- Check whether the substring is equal to its reverse complement using [`revc.py`](./revc.py).
- If it is, record its starting position and length, then increase the length by two.
- Otherwise, calculate the maximum overlap between the substring and its reverse complement using `overlap()` from [`long.py`](./long.py).
- Increase the candidate length by $L-q$, skipping lengths that cannot form a reverse-complement palindrome.
- Continue until the maximum allowed length or the end of the sequence is reached.

**Learning:**

- Restriction sites can exhibit reverse-complement symmetry.
- The maximum suffix-prefix overlap provides a lower bound on how many additional characters are needed before a longer reverse-complement palindrome can become possible.
- This allows candidate lengths to be skipped without checking each one individually.

---

### 42. Counting Subsets

[**Problem Statement**](https://rosalind.info/problems/sset/)

**Code:** [`sset.py`](./sset.py)

**Mathematics:**

For a set containing $n$ distinct elements, each element has two independent possibilities: either it belongs to a subset or it does not.

Therefore, the total number of subsets is:

$$
\lvert\mathcal{P}(S)\rvert=2^n
$$

**Algorithm:**

- Calculate $2^n$.
- Take the result modulo $10^6$.

**Learning:** The power set of a set with $n$ elements has $2^n$ elements, as every element independently contributes two choices.

---

### 43. Transitions and Transversions

[**Problem Statement**](https://rosalind.info/problems/tran/)

**Code:** [`tran.py`](./tran.py)

**Mathematics:**

Nucleotide substitutions are classified into two categories:

- **Transition:** A purine is replaced by another purine, or a pyrimidine by another pyrimidine.
- **Transversion:** A purine is replaced by a pyrimidine, or vice versa.

Purines:

$$
\lbrace A,G\rbrace 
$$

Pyrimidines:

$$
\lbrace C,T\rbrace 
$$

The transition/transversion ratio is:

$$
R=\frac{\text{Number of transitions}}{\text{Number of transversions}}
$$

**Algorithm:**

- Read the two DNA sequences using [`fasta.py`](./fasta.py).
- Compare the nucleotides at corresponding positions.
- If the nucleotides differ, check whether they form a transition using the `transit` dictionary.
- If they do, increment the transition counter. Otherwise, increment the transversion counter.
- Divide the total number of transitions by the total number of transversions.

**Learning:**

- Transitions and transversions represent different classes of point mutations.
- Transitions preserve the chemical category of the nucleotide, whereas transversions change it.
- The transition/transversion ratio is useful in studying patterns of nucleotide substitution.
