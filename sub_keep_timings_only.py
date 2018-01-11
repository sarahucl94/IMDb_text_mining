
with open("/Volumes/Macintosh HD/Users/sarah/Downloads/subs_timings.txt", "r+") as file:
    with open("/Volumes/Macintosh HD/Users/sarah/Downloads/subs_part3_times.txt", "w+") as a:
        for line in file.read().split():
            result = ''.join(i for i in line if i.isdigit() or i== ';')
            result = result.replace(';', ':')
            new = [result]
            a.write(repr(new))
    a.close()

def new():
    with open("/Volumes/Macintosh HD/Users/sarah/Downloads/subs_part3_times.txt", "r+") as a:
        for line in a.read().split():
            timings = ''.join(i for i in line if not i==']' or not i=="'" or not i=='[')
            timings = timings.replace("['']", '')
            timings = timings.replace('[', '\n')
            timings = timings.replace(']', ' ')
            timings = timings.replace("'", ' ')


        print(timings)

    with open("/Volumes/Macintosh HD/Users/sarah/Downloads/subs_part3_times.txt", "w+") as a:
        a.write(timings)
        a.close()
new()