import re
with open("/Volumes/Macintosh HD/Users/sarah/Downloads/subs_timings.txt", "r+") as file:
    with open("/Volumes/Macintosh HD/Users/sarah/Downloads/subs_part3_times.txt", "w+") as a:
        for line in file.read().split():
            result = ''.join(i for i in line if i.isdigit() or i== ';' or i=='.')
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



    with open("/Volumes/Macintosh HD/Users/sarah/Downloads/subs_part3_times.txt", "w+") as a:
        a.write(timings)
        a.close()
new()

import numpy as np
import scipy.io.wavfile
fs1, y1 = scipy.io.wavfile.read('/Volumes/Macintosh HD/Users/sarah/Downloads/audio_mono.wav')


time_str = open('/Volumes/Macintosh HD/Users/sarah/Downloads/subs_part3_times.txt').read().replace(' ', "").split(',')


def obtain_sec(time_str):
    lst=[]
    subs=[]
    for element in time_str:
        lst.append(element)
    time2 = [i.split() for i in lst]
    flat_time = [item for sublist in time2 for item in sublist if item is not '.']
    indices = [487, 488, 515, 100, 103, 230, 231, 234, 277, 288, 291, 326, 361, 410, 449, 454, 518, 537, 560, 705, 714]
    for i in sorted(indices, reverse=True):
         del flat_time[i]
    for timing in flat_time:
        c = int(timing[0:2]) * 3600 + int(timing[3:5]) * 60 + float(timing[6:11])
        subs.append(c)
        bits = [subs[x:x + 2] for x in range(0, len(subs), 2)]
    return (bits)


subtitles = obtain_sec(time_str)


l1 = np.array(subtitles)
#print(l1)
l1 = np.ceil(l1*fs1)
newWavFileAsList = []
for elem in l1:
    startRead = elem[0]
    endRead = elem[1]
    if startRead >= y1.shape[0]:
      startRead = y1.shape[0]-1
    if endRead >= y1.shape[0]:
      endRead = y1.shape[0]-1
    newWavFileAsList.extend(y1[int(startRead):int(endRead)])


newWavFile = np.array(newWavFileAsList)
scipy.io.wavfile.write("sub_audio_only.wav", fs1, newWavFile)