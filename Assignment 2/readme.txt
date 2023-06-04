#Jisoo Kim
#BIMM 182
#April 28, 2023


#### Question 1
>locAL.py
usage: locAL.py [-h] -m MATCH -s MISMATCH -d INDEL [-a] file

Align 2 DNA sequences

positional arguments:
  file

optional arguments:
  -h, --help            show this help message and exit
  -m MATCH, --Match MATCH
                        [required] Match score
  -s MISMATCH, --Mismatch MISMATCH
                        [required] Mismatch score
  -d INDEL, --Indel INDEL
                        [required] Indel score
  -a, --Alignment       [optional] Print aligned sequences


#### Question 2
>randomDNA.py
usage: randomDNA.py [-h] Number Length

Generate random DNA sequences with the given number and length of the
sequences and they nucleotide composition summary

positional arguments:
  Number      Number of Sequence (e.g. 500)
  Length      Length of Sequence (e.g. 1000)

optional arguments:
  -h, --help  show this help message and exit


#### Question 3
>histGen.py
usage: histGen.py [-h] file

Generate Histogram of given alignment length data

positional arguments:
  file        File containing alignment lengths
optional arguments:
  -h, --help  show this help message and exit

#### Question 3
>lineGen.py
usage: lineGen.py [-h] file [file ...]

Generate Line plot of given set alignment length data mean values

positional arguments:
  files        Files containing alignment lengths with the same mismatch score

optional arguments:
  -h, --help  show this help message and exit


#### Question 4
>locAL_Q4.py
usage: locAL_Q4.py [-h] -m MATCH -s MISMATCH -d INDEL [-a] file

Align 2 DNA sequences

positional arguments:
  file

optional arguments:
  -h, --help            show this help message and exit
  -m MATCH, --Match MATCH
                        [required] Match score
  -s MISMATCH, --Mismatch MISMATCH
                        [required] Mismatch score
  -d INDEL, --Indel INDEL
                        [required] Indel score
  -a, --Alignment       [optional] Print aligned sequences
