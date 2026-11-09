# Rosalind Bioinformatics Stronghold Problems

This repository contains 36 problems I solved from Rosalind, and few reusable utility files. 
I have shared the algorithms used and things I learned from each problem.
I have tried not using the predefined modules for bioinformatics as algorithm designing was the main focus.

## Utility Files
<table>
  <colgroup>
    <col width="15%">
    <col width="45%">
    <col width="40%">
  </colgroup>
  <thead>
    <tr>
      <th align="center">File</th>
      <th align="center">Description</th>
      <th align="center">Returns</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td align="center"><a href="./fasta.py"><code>fasta.py</code></a></td>
      <td>Reads input in fasta format.</td>
      <td>A dictionary with ID as keys and DNA strands as values.</td>
    </tr>
    <tr>
      <td align="center"><a href="./Motif.py"><code>Motif.py</code></a></td>
      <td>
        To treat motifs equivalent to strings. It also stores the information of the positions that allow for multiple codons.<br>
        Subclass <code>Inc</code> of <code>Motif</code> accounts for [XY]: "either X or Y".<br>
        Subclass <code>Exc</code> of <code>Motif</code> accounts for {X}: "any amino acid except X".
      </td>
      <td>
        An object of class <code>Motif</code> with behaviours such as <code>len</code>, <code>==</code> operation with strings and indexing defined.
      </td>
    </tr>
    <tr>
      <td align="center"><a href="./Streak.py"><code>Streak.py</code></a></td>
      <td>
        To maintain character streaks while finding substrings.<br>
        <code>streak</code> function finds all occurrences of a substring.<br>
        <code>istreak</code> function allows for streaking interactively, allowing you to update the substring in each iteration and also get some output each iteration according to some query.<br>
        <code>multi</code> function finds all occurrences of multiple substrings in a given string.
      </td>
      <td>
        <code>streak</code> returns a set of all starting indices of the substring.<br>
        <code>istreak</code> returns a generator object which yields the output to a query (a function on the streak set passed while calling) after checking each character of the string.<br>
        <code>multi</code> returns a dictionary containing substrings as keys and sets of their initial indices of occurrence as values.
      </td>
    </tr>
    <tr>
      <td align="center"><a href="./uniprot.py"><code>uniprot.py</code></a></td>
      <td>Fetches protein data from the UniProt database using the ID of the protein. [Credits: Gemini] </td>
      <td>
        A dictionary containing all data about the protein.<br>
        <code>uniprot(f"{ID}")["sequence"]["value"]</code> returns the string containing the protein sequence.
      </td>
    </tr>
    <tr>
      <td align="center"><a href="./RNA_Codon_Table.txt"><code>RNA_Codon_Table.txt</code></a></td>
      <td>A table indicating the translation of individual RNA codons into amino acids in JSON format.</td>
      <td><code>json.loads(open("RNA_Codon_Table.txt").read())</code> returns a dictionary having RNA codons as keys and corresponding amino acids as values.</td>
    </tr>
    <tr>
      <td align="center"><a href="./Monoisotopic_Mass_Table.txt"><code>Monoisotopic_Mass_Table.txt</code></a></td>
      <td>A table storing the mass of all amino acids in JSON format.</td>
      <td><code>json.loads(open("Monoisotopic_Mass_Table.txt").read())</code> returns a dictionary having amino acids as keys and their masses as values.</td>
    </tr>
  </tbody>
</table>

## Problems Solved