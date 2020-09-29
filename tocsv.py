#!/usr/bin/python

import sys

inputFile = './test.txt'

if len(sys.argv) > 1:
  inputFile = sys.argv[1]


file = open(inputFile, mode = 'r')
allfile = file.read()

replaceChars = [ '(', ')', '{', '}', '[', ']', '=', '/', '\\', '-', ';', ',', '.', '>', '<', ':', '\'', '"' ];
for replaceChar in replaceChars:
  allfile = allfile.replace(replaceChar, ' ');


vector = allfile.split()
file.close()

listall = list(set(vector))

file1 = open("output.txt","a") 
file1.write('|'.join(str(x) for x in listall))
file1.close() 

print 'ok...'