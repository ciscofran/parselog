#
# Author: Francisco Londono
# Date: March 4 2016
# Revision 1.0
# This script searches in a log file for all the occurences of the word 'error'
#

import sys
import re

def find_keyword(filename):
  try:
    f = open(filename, 'rU')
  except:
    print ("Cannot open file:" , filename)
    exit()

  counts = dict()
  for line in f:
     m = re.findall('error\d*', line)
     if m:
      for word in m:
        if word not in counts:
           counts[word] = 1
        else:
           counts[word] += 1

  for k, v in counts.items():
      print(k, v)

def main():

  if len(sys.argv) != 2:
    print ('usage: ./wordfreq.py filename')
    sys.exit(1)

  filename = sys.argv[1]
  find_keyword(filename)

if __name__ == '__main__':
  main()
