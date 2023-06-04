Question_1a.py
This file creates a table of E-values(divided by n length database) dependent to various l-mer value

Question_1c.py
This file calculated the E-value of 5-mer of a given query (AATAAGCCGC) aligned with 85% GC content
Input:
query = "AATAAGCCGC"
m = 10
l = 5
Output:
E-value (rounded to tenthousandth place)


Question_2.py
Calculates the speedup and sensitivity with given parameters and database with >=85% sequence identity with the query
Input:
l=[5,11,15,20,25,30,35,40]
n = 10e7
m = 10e7
r = 100
Output:
table of speedup sensitivity by l-mer value

Question_4.py
This file uses the Aho-Corasick automaton to create Trie of query dictionaries without failure links and align with the given database and count the number of exact matches. Then, a table will be created of each query with its E-value, observed count and the change
Input:
DNA.txt
Query file
Output:
Query statistics table


