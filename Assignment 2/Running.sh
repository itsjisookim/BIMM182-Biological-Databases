#!/bin/bash



##mismatch -30
#python locAL.py -m 1 -s -30 -d -30 Q2_1000.txt > P3.30_30.txt
#python locAL.py -m 1 -s -30 -d -20 Q2_1000.txt > P3.30_20.txt
#python locAL.py -m 1 -s -30 -d -10 Q2_1000.txt > P3.30_10.txt
#python locAL.py -m 1 -s -30 -d -1 Q2_1000.txt > P3.30_1.txt
#python locAL.py -m 1 -s -30 -d -0.5 Q2_1000.txt > P3.30_0_5.txt
#python locAL.py -m 1 -s -30 -d -0.33 Q2_1000.txt > P3.30_0_33.txt
#python locAL.py -m 1 -s -30 -d -0.25 Q2_1000.txt > P3.30_0_25.txt
#python locAL.py -m 1 -s -30 -d 0 Q2_1000.txt > P3.30_0.txt
#
##mismatch -20
#python locAL.py -m 1 -s -20 -d -30 Q2_1000.txt > P3.20_30.txt
#python locAL.py -m 1 -s -20 -d -20 Q2_1000.txt > P3.20_20.txt
#python locAL.py -m 1 -s -20 -d -10 Q2_1000.txt > P3.20_10.txt
#python locAL.py -m 1 -s -20 -d -1 Q2_1000.txt > P3.20_1.txt
#python locAL.py -m 1 -s -20 -d -0.5 Q2_1000.txt > P3.20_0_5.txt
#python locAL.py -m 1 -s -20 -d -0.33 Q2_1000.txt > P3.20_0_33.txt
#python locAL.py -m 1 -s -20 -d -0.25 Q2_1000.txt > P3.20_0_25.txt
#python locAL.py -m 1 -s -20 -d 0 Q2_1000.txt > P3.20_0.txt
#
##mismatch -10
#python locAL.py -m 1 -s -10 -d -30 Q2_1000.txt > P3.10_30.txt
#python locAL.py -m 1 -s -10 -d -20 Q2_1000.txt > P3.10_20.txt
#python locAL.py -m 1 -s -10 -d -10 Q2_1000.txt > P3.10_10.txt
#python locAL.py -m 1 -s -10 -d -1 Q2_1000.txt > P3.10_1.txt
#python locAL.py -m 1 -s -10 -d -0.5 Q2_1000.txt > P3.10_0_5.txt
#python locAL.py -m 1 -s -10 -d -0.33 Q2_1000.txt > P3.10_0_33.txt
#python locAL.py -m 1 -s -10 -d -0.25 Q2_1000.txt > P3.10_0_25.txt
#python locAL.py -m 1 -s -10 -d 0 Q2_1000.txt > P3.10_0.txt
#
##mismatch -5
#python locAL.py -m 1 -s -5 -d -30 Q2_1000.txt > P3.5_30.txt
#python locAL.py -m 1 -s -5 -d -20 Q2_1000.txt > P3.5_20.txt
#python locAL.py -m 1 -s -5 -d -10 Q2_1000.txt > P3.5_10.txt
#python locAL.py -m 1 -s -5 -d -1 Q2_1000.txt > P3.5_1.txt
#python locAL.py -m 1 -s -5 -d -0.5 Q2_1000.txt > P3.5_0_5.txt
#python locAL.py -m 1 -s -5 -d -0.33 Q2_1000.txt > P3.5_0_33.txt
#python locAL.py -m 1 -s -5 -d -0.25 Q2_1000.txt > P3.5_0_25.txt
#python locAL.py -m 1 -s -5 -d 0 Q2_1000.txt > P3.5_0.txt
#
##mismatch 0
#python locAL.py -m 1 -s -0 -d -30 Q2_1000.txt > P3.0_30.txt
#python locAL.py -m 1 -s -0 -d -20 Q2_1000.txt > P3.0_20.txt
#python locAL.py -m 1 -s -0 -d -10 Q2_1000.txt > P3.0_10.txt
#python locAL.py -m 1 -s -0 -d -1 Q2_1000.txt > P3.0_1.txt
#python locAL.py -m 1 -s -0 -d -0.5 Q2_1000.txt > P3.0_0_5.txt
#python locAL.py -m 1 -s -0 -d -0.33 Q2_1000.txt > P3.0_0_33.txt
#python locAL.py -m 1 -s -0 -d -0.25 Q2_1000.txt > P3.0_0_25.txt
#python locAL.py -m 1 -s -0 -d 0 Q2_1000.txt > P3.0_0.txt


#
#python lineGen.py P3.30*
#python lineGen.py P3.20*
#python lineGen.py P3.10*
#python lineGen.py P3.5*
#python lineGen.py P3.0*

python3 locAl_Q4.py -m 1 -s 10 -d -1 -a p4pairs.txt > Q4_alignment.txt 
