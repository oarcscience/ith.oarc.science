import sys
import pypandoc
import os
import re

filename=sys.argv[1]
print(filename)

with open(filename, "r") as fin:
    source=fin.read()

pattern_string0="\[([^\[]+)\]\((.*(?<!.md))\)"

with open(sys.argv[2], "w+") as fout:
    fout.write(re.sub(pattern_string0, r'[\1](\2.md)', source))
