
import re

with open("/Volumes/Macintosh HD/Users/sarah/Downloads/part3.txt", "r+") as file:
    with open("/Volumes/Macintosh HD/Users/sarah/Downloads/part3_modified.txt", "w+") as a:
        for line in file.readlines():
            # remove digits
            result = ''.join(i for i in line if not i.isdigit())
            # remove dollar signs
            result = result.replace('#', '')
            result = result.replace(']', '')
            result = result.replace('?', '')
            result = result.replace('!', '')
            result = result.replace('Chuckling', '')
            result = result.replace('  ', '')
            # some other regex, removes all y's
            result = re.sub(r"([-|:[{}"",.])", " ", result)
            a.write(result)
            print(result)
    a.close()
