
import re

with open("/Volumes/Macintosh HD/Users/sarah/Downloads/data.txt", "r+") as file:
    with open("/Volumes/Macintosh HD/Users/sarah/Downloads/DVS_script.txt", "w+") as a:
        for line in file.readlines():
            result = ''.join(i for i in line if not i.isdigit())
            result = result.replace("content", "")
            result = result.replace("start", "\n")
            result = result.replace("transcript", "")
            result = result.replace('"', '')
            result = result.replace('cuz', 'cause')
            result = result.replace(']', '')
            result = re.sub(r"[-|:[{}"",.]", " ", result)
            a.write(result)

        a.close()

