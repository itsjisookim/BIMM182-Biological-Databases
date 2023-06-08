Question1.py
This file creates a table of expected and observed frequency of chrA.fasta dinucleotides
Input:
chrA.fasta
Output:
table of expected and observed frequency of all possible dinucleotides

Question2.py
This file calculates CpG potential scores to determine the classification of the known CpG and non-CpG regions. It creates Markov models for each CpG and non-CpG regions and calculates the probability(frequency) of each region. Then CpG potential score is calculated via proportionate comparison and classification is performed.
Input:
chrA.fasta
chrA.islands
Output:
CPG_stat.txt
CPG_stat.csv (hold all intermidiate columns as well)



Question3.py
This file utilizes isotopes provided at (https://www.britannica.com/science/isotope) and calculates Isotope profile of a given peptide, which for this assignment is SLAMMER
Input:
SLAMMER
Output:
SLAMMER_isotopeProfile.csv

Question4.py
This file is an edited algorithm of Question3.py where abundance dictionary is altered so that 50% of C-12 is modified to C-13
Input:
SLAMMER
Output:
SLAMMER_isotopeProfile_0.5_C-12.csv



