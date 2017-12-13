
import re

with open("/Volumes/Macintosh HD/Users/sarah/Downloads/SUBS_part3.txt", "r+") as file:
    with open("/Volumes/Macintosh HD/Users/sarah/Downloads/part3_times.txt", "w+") as a:
        for line in file.read().split():
            # remove letters
            result = ''.join(i for i in line if i.isdigit() or i==':' or i =='.' or i=='[' or i==']')

            a.write(result)
            print(result)
    a.close()
