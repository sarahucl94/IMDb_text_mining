import difflib
import sys
import re
from tkinter import *

with open("/Volumes/Macintosh HD/Users/sarah/Downloads/data_modified1.txt") as dvs:
    a = dvs.read().split()
    with open("/Volumes/Macintosh HD/Users/sarah/Downloads/part3_modified1.txt") as sub:
        b = sub.read().split()
        d = difflib.Differ()
        diff = d.compare(a,b)
        x = ' '.join(diff)


with open("/Volumes/Macintosh HD/Users/sarah/Downloads/subs_unique.txt", 'w+') as file:
    new = re.findall(r'\+ (\w+)', x)
    y = str("\n".join(new))
    file.write(y.lower() + '\n')
    file.close()



with open("/Volumes/Macintosh HD/Users/sarah/Downloads/part3_modified1.txt", 'r') as file:
    with open("/Volumes/Macintosh HD/Users/sarah/Downloads/data_modified1.txt", 'r') as file1:
        sub = file.read().split()
        dvs = file1.read().split()
        for words in sub:
            for terms in b:
                print(terms)
                def search(c):
                    try:
                        k = terms.index(c)
                        #print(terms[k])
                    except ValueError:
                        print('')

                m = search(words)

            #final = m.replace('None', '')
            #print(final)
            #for terms in b:
                #if words == terms:
                    #new = [terms.replace(r'(\w+)', words.upper()) for line in b]
        #print(new)

