import sys
import pypandoc
import os
from bs4 import BeautifulSoup

filename=sys.argv[1]
print(filename)

with open(filename, "r") as fin:
    source=fin.read()

# if the file contains a yaml frontmatter, don't treat it
yaml_string="\n---\n"
if source.find(yaml_string)==-1:
    content=source
    frontmatter=""
else:
    frontmatter,content=source.split(yaml_string, 1)
    

content = pypandoc.convert_text(content, 'gfm', format='html')#, extra_args=["--type=gfm"])

if frontmatter=="":
    output=content
else:
    output=frontmatter+yaml_string+content


with open(sys.argv[2], "w+") as fout:
    fout.write(output)
