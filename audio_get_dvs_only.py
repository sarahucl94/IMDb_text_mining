#Author: Sarah Aliko. This code modifies the text file containing subtitles and timings of subtitles obtained online.
# The timings are grouped into pairs (in the format start:end), but rather than use the start:end of subtitles,
# it uses the inter-subtitle timings that correspond to DVS timings. Then it accesses the audio file of the movie (mono audio channel)
# and splits the DVS timings out of the audio, merging them into a new audio file in .wav format.
#Save subs as Adobe txt, but need to modify text (remove single digits at start of each line and add last time point of audio

#Open subtitle file – contains both timings and text
#open new text file to write timings of subs only and remove text

import decimal
import numpy as np
import scipy.io.wavfile
import re
import decimal

with open("subs.txt", "r+") as file:
    with open("subs_part3_times.txt", "w+") as a:
        for line in file.read().split():
            result = ''.join(i for i in line if i.isdigit() or i== ';')
            new_list = [result]
            a.write(repr(new_list))
    a.close()


#modify subtitle file to adapt format for analysis
#removes characters that are not timings (eg. commas, dots, brakets)

def new():
    with open("subs_part3_times.txt", "r+") as a:
        for line in a.read().split():
            timings = ''.join(i for i in line if not i==']' or not i=="'" or not i=='[')
            timings = timings.replace("['']", '')
            timings = timings.replace('[', '\n')
            timings = timings.replace(']', ' ')
            timings = timings.replace("'", ' ')
            timings = timings.replace(". ", ' ')
            timings = timings.replace("..", ' ')
            timings = timings.replace("::", ' ')
            timings = timings.replace(": ", ' ')


    with open("subs_part3_times.txt", "w+") as a:
        a.write(timings)
        a.close()
new()


#open audio file for the movie- has to be in mono audio channel
#if audio channel is not originally mono, modify it using ffmpeg command
#in the terminal.

fs1, y1 = scipy.io.wavfile.read('audio_mono.wav')


time_str = open('subs_part3_times.txt').read().replace(' ', "").split(',')


#write the timings as seconds instead of hh:mm:ss format
#select the inter-subtitle timings (ie the ones that should have DVS audio)
#print the start:end timings of the dvs audio into a file

def obtain_sec(time_str):
    lst=[]
    subs=[]
    subs_1 = []
    for element in time_str:
        lst.append(element)
    time2 = [i.split() for i in lst]
    flat_time = [item for sublist in time2 for item in sublist if item is not '.']
    flat_time = [s.replace(";", ".") for s in flat_time]
    for timing in flat_time:
        c = int(timing[0:2]) * 3600 + int(timing[3:5]) * 60 + float(timing[6:11])
        subs.append(c)
    for element in subs:
        if element not in subs_1:
            subs_1.append(element)
    bits = [subs_1[x:x + 2] for x in range(1, len(subs_1), 2)]
    with open("dvs_timings.txt", "w+") as new_file:
        new_file.write(str(bits))
    return (bits)
    new_file.close()

#split audio file based on dvs timing intervals above and merge them into new audio file

dvs = obtain_sec(time_str)
print(dvs)
l1 = np.array(dvs)
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
scipy.io.wavfile.write("dvs_audio_only.wav", fs1, newWavFile)

#open the dvs timings and duration file and calculate the difference between each start:end pair
#this means calculate (end-start) = duration of each dvs audio chunk

dvs_interval = open("dvs_timings.txt").read().replace("[", '')
dvs_interval = dvs_interval.replace("]",'')
dvs_interval = dvs_interval.replace(",",'')
dvs_interval = dvs_interval.replace("'",'').split()

def duration(dvs_interval):
    l = []
    for element in dvs_interval:
        l.append(element)
    i = 0
    j = 1
    intervals = []
    intervals.append(decimal.Decimal(0))
    while i < len(l):
        while j < len(l):
            intervals.append(decimal.Decimal(l[j]) - decimal.Decimal(l[i]))
            j += 2
            i += 2
    y = [sum(intervals[:i + 1]) for i in range(len(intervals))]
    return y

durations = duration(dvs_interval)
print(durations)

# start_times = []
# i = 0
# for values in dvs_interval:
#     while i < len(dvs_interval):
#         start_times.append(dvs_interval[i])
#         i += 2
# print(start_times)



with open("data.txt",'r') as dvs_data:
    with open('dvs_text_only.txt', 'w+') as simple_text:
        for line in dvs_data.readlines():
            dvs_text = ''.join(i for i in line if i.isalpha() or i == "'" or i == ' ' or i == '.')
            dvs_text = dvs_text.replace("transcript", '')
            dvs_text = dvs_text.replace("content", '')
            dvs_text = dvs_text.replace("start", '')
            dvs_text = dvs_text.replace('.', '\n')
            simple_text.write(dvs_text)
        simple_text.close()


with open('data.txt', 'r+') as file:
    for line in file.readlines():
        dvs_num = ''.join(i for i in line if i.isdigit() or i == '.' or i == ' ')
    numList = re.sub("[^\d.]", " ", dvs_num).split()
    new_list=[]
    for element in numList:
        new_list.append(decimal.Decimal(element))
    print(new_list)

i = 0
j = 0
correlation = []
while j < len(durations):
    while i < len(new_list):
        if new_list[i] == durations[j] or new_list[i] < durations[j+1]:
            correlation.append(new_list[i])
            i = i+1
