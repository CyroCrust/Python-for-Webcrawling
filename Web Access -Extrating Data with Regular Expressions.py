name = input("Enter file:")
if len(name) < 1 : name = "regex_sum_372585.txt"
handle = open(name)
counts = dict()
total = 0
totalsum = 0
import re

for line in handle:
    line = line.rstrip()
    stuff=re.findall( '([0-9]+)', line)
    if len(stuff) == 0 : continue
    for number in stuff:
        sum = (int(number))
        total = total + sum
totalsum = totalsum + total
print(totalsum)
