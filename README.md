# MonophylyPENA
This repository contains the scripts used for the analyses described in this manuscript

For OneKP data, 
1. Download the gene sequences from the paftol tree of life website into a text editor
2. Run the following scripts
   i. 'createfoldersfromtxt.py' - This script creates a folder containing each gene as a separate file
   ii. 'convertgenesfromtxttofasta.py' - This script converts genes from text format to fasta format
   iii. 'concatgenes.bash' - This script concatenates genes from one file with another, and writes the results of the concatenated genes into a new folder. 

Usage:
Run 'createfoldersfromtxt.py' script by running ```python createfoldersfromtxt.py``` on the command line
Run 'convertgenesfromtxttofasta.py' script by running ```python convertgenesfromtxttofasta.py``` on the command line
Run 'concatgenes.bash' script by running ```bash concatgenes.bash``` on the command line

