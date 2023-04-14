#BIMM 182 Assignment 1
#Jisoo Kim
#April 12, 2023

#Platform : Linux
#Scripting Language : Python
#Editor : Visual Studio Code
import re

def sayHi():
    return "Hello Bioinformatics"
#print(sayHi())

def cat(infile):
    inf = open(infile, 'r')
    data = inf.readlines()

    count = 0
    for i in range(len(data)):
        if '>' in data[i] :
            if count != 0:
                print("sequence length : %s"%count)
            print(data[i].strip('\n'))
            count = 0 
        else:
            count += len(data[i].strip())
        
        if i == len(data) -1 : 
            print("sequence length : %s"%count)

    inf.close()
#cat("/Users/jisookim/Documents/BIMM182/datafile.txt")

import re
def filter(infile):
    inf = open(infile, 'r')
    data = inf.readlines()

    rat = False
    temp = ''
    while len(data) != 0:
        d = data.pop(0).strip('\n')
        #print(d)
        if '>' in d:
            if len(temp) != 0:
                chunks = [temp[i:i+60] for i in range(0, len(temp), 60)]
                for c in chunks:
                    print(c)
                temp = ''
            #if ('Mus musculus' in d) or ('RAT' in d):
            if (re.search('Mus musculus',d, re.IGNORECASE)) or (re.search('Rat',d, re.IGNORECASE)):
                print(d)
                rat = True
            else:
                rat = False
        else:
            if rat == True:
                temp += d

    inf.close()
#filter("/Users/jisookim/Documents/BIMM182/datafile.txt")

def dataSeq(infile, outfile):
    inf = open(infile, 'r')
    data = inf.readlines()
    out = open(outfile, 'w')

    SequenceEnd = False
    while len(data) != 0:
        d = data.pop(0).strip('\n')
        #print(d)
        if '>' in d:
            if SequenceEnd == True:
                out.write('@')
                SequenceEnd = False
        else:
            out.write(d)
            SequenceEnd = True

    inf.close()
    out.close()
#dataSeq("/Users/jisookim/Documents/BIMM182/datafile.txt", "/Users/jisookim/Documents/BIMM182/data.seq")

def dataIn(infile, outfile):
    inf = open(infile, 'r')
    data = inf.readlines()
    out = open(outfile, 'w')
 
    count=0
    while len(data) != 0:
        d = data.pop(0).strip('\n')
        #print(d)
        curr_gi = ''
        if '>' in d:
            gi = d.split('|')[1]
            out.write('%s\t%s\n'%(gi, count))           
        else:
            count += len(d) + 1

    inf.close()
    out.close()
#dataIn("/Users/jisookim/Documents/BIMM182/datafile.txt", "/Users/jisookim/Documents/BIMM182/data.in")

def getSeq(seq_file, in_file, query):#
    ### create dictionary of index for each gi number
    inf = open(in_file, 'r')
    data = inf.readlines()
    index_dict = {}
    index = []
    while len(data) != 0:
        d = data.pop(0).split()
        index_dict[int(d[1])] = d[0]
        index.append(int(d[1]))     
    inf.close()

    ### get the entire sequence
    seqf = open(seq_file, 'r')
    data = seqf.readlines()
    sequences = data[0].strip()
    index.append(len(sequences)-1)
    seqf.close()

    L = 0
    R = len(index) - 1
    while L != R-1:
        m = int((L + R) / 2)
        m_idx = index[m]
        L_idx = index[L]
        R_idx = index[R]
        if query in sequences[L_idx : m_idx]: #check left half for a match
            R = m
        elif query in sequences[m_idx: R_idx]: #check right half for a match
            L = m
        else:
            return "Query not in sequence"
    return index_dict[index[m-1]]
    
print(getSeq("/Users/jisookim/Documents/BIMM182/data.seq", "/Users/jisookim/Documents/BIMM182/data.in", "MHIQITDFGTAKVLSPDS"))
