# Author: Sarah Aliko. 
# Date last modified: 16/07/2018
# Copyright: UCL, Jeremy Skipper Lab
# This code translates audio file with DVS data into text using a Google API, and applies the movie timings to the text
# Save subs as Adobe txt, but need to modify text (remove single digits at start of each line and add last time point of audio???



# Open subtitle file – contains both timings and text
# open new text file to write timings of subs only and remove text

import numpy as np
import scipy.io.wavfile
import json
import decimal



with open("subs.txt", "r+") as file:
    with open("subs_part3_times.txt", "w+") as a:
        for line in file.read().split():
            result = ''.join(i for i in line if i.isdigit() or i== ';')
            new_list = [result]
            a.write(repr(new_list))
    a.close()


# Modify subtitle file to adapt format for analysis
# Remove characters that are not timings (eg. commas, dots, brakets)

def subs():
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
subs()


# Open audio file for the movie- has to be in mono audio channel
# If audio channel is not originally mono, modify it using ffmpeg command
# In the terminal.

fs1, y1 = scipy.io.wavfile.read('audio_mono.wav')


time_str = open('subs_part3_times.txt').read().replace(' ', "").split(',')


# Write the timings as seconds instead of hh:mm:ss format
# Select the inter-subtitle timings (ie the ones that should have DVS audio)
# Print the start:end timings of the dvs audio into a file

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

# Split audio file based on dvs timing intervals above and merge them into new audio file

dvs = obtain_sec(time_str)
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

# Open the dvs timings and duration file and calculate the difference between each start:end pair
# This means calculate (end-start) = duration of each dvs audio chunk

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

# Calculate the expected start times of each dvs fragment from the Google API. Since the dvs chunks are all attached together
# The start times will be as follows: interval1+interval2 = start_time3. Eg. if one interval is 2.15sec long, and the second interval is 9.98sec
# Long, then the start time for the third interval from Google API is 2.15+9.98 = 12.13sec.
# Create a file with Google API start times of dvs fragments

durations = duration(dvs_interval)

with open('start_times_dvs_expected_googleAPI.json', 'w') as file:
    start_times_googleAPI = []
    i = 0
    for values in dvs_interval:
        while i < len(dvs_interval):
            start_times_googleAPI.append(dvs_interval[i])
            i += 2
    file.write(str(durations))
file.close()

# Open the file derived from Google API (data.json). NB: How to combine these two codes??
# Separate the text of the Google API from the timing information - save these into two different files

with open("data.json",'r') as dvs_data:
    with open('dvs_text_only.txt', 'w+') as simple_text:
        dvs_txt = json.load(dvs_data)
        for i in range(len(dvs_txt['transcript'])):
            simple_text.write(dvs_txt['transcript'][i]['content']+'\n')
        simple_text.close()


with open('data.json', 'r+') as file:
    numList =[]
    dvs_num = json.load(file)
    for i in range(len(dvs_num['transcript'])):
        numList.append(dvs_num['transcript'][i]['start'])

# Create a list (called times) that contains both dvs start times from Google API itself and those precedently calculated
# In durations. Sort the list so that all timings are in increasing order, and create a file with list values

times = sorted(numList + durations)
with open('dvs_combined_times.json', 'w') as file:
     file.write(str(times))
file.close()

# Calculate the actual movie timings of the dvs file and save them onto a json file.

numList_to_decimal = [decimal.Decimal(x) for x in numList]
start_to_decimal = [decimal.Decimal(x) for x in start_times_googleAPI]
i = 0
j = 0
y = 0
dvs_movie_times = []

with open('dvs_adapted_movie_time.json', 'w') as file:
    while i < len(numList_to_decimal):
        while j < len(numList_to_decimal):
            while y < len(numList_to_decimal):
                if numList_to_decimal[i] >= durations[j] and numList_to_decimal[i] <= durations[j+1]:
                    x = numList_to_decimal[i] - durations[j] + start_to_decimal[y]
                    dvs_movie_times.append(x)
                    i = i+1
                elif numList_to_decimal[i] <= durations[j] or numList_to_decimal[i] >= durations[j+1]:
                    j = j+1
                    y = y+1
                    continue
                else:
                    break
            print(dvs_movie_times)
        file.write(str(dvs_movie_times))




# Dec(0) 0 Dec(2.15)
# Dec(2.15) 3.9 7.65 10.4 Dec(12.13)
# Dec(12.13) 16.6 Dec(18.12)
# These DVS audio file timings correspond to the below movie timings
#
#
# 2sec(movie start)  2sec  4.15sec(movie end)
# 5.12sec (movie start)   6.91sec    10.62sec   13.37sec   15.18sec (movie end)
# 18.22sec(movie start)  22.69sec   24.21sec(movie end)
#
# Calculated as follows: 16.6(dvs speech) - 12.13 (dvs start fragment) + 18.22 (movie start fragment) = 22.69sec in movie
