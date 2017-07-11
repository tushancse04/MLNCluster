import os
import sys

fname = sys.argv[1]
ifile = open(fname)
ifile1 = open("mln.txt")
ln = ifile1.readline()
parts = ln.strip().split()
preds = []
for p in parts:
    p1 = p.split(":")
    preds.append(p1[0])
ifile1.close()
ofile = open("cl-"+fname,'w')

for line in ifile:
    if len(line)<2:
        continue
    prts = line.split("(")
    if prts[0] not in preds:
        continue
    ofile.write(line)
ofile.close()
ifile.close()
