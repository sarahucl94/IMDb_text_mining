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


with open("/Volumes/Macintosh HD/Users/sarah/Downloads/DVS_unique.txt", 'w+') as file:
    new = re.findall(r'- (\w+)', x)
    y = str("\n".join(new))
    file.write(y.lower() + '\n')
    file.close()


list_1 = []
with open("/Volumes/Macintosh HD/Users/sarah/Downloads/part3_modified1.txt", 'r') as file:
    with open("/Volumes/Macintosh HD/Users/sarah/Downloads/data_modified1.txt", 'r') as file1:
        a = file.read().split()
        b = file1.read().split()



root = Tk()
root.title('Full DVS')
t = Text(root)
t.pack()
t.insert(END, b)
t.tag_config('subtitle', background='yellow', foreground='black')


def search(text_widget, keyword, tag):
    pos = '1.0'
    while True:
        idx = text_widget.search(keyword, pos, END)
        if not idx:
            break
        pos = '{}+{}c'.format(idx, len(keyword))
        text_widget.tag_add(tag, idx, pos)

for words in a:
    search(t, 'she', 'subtitle')
root.mainloop()











