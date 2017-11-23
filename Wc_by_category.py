dictionary_1 = {}
dictionary_2 = {}
# create two dictionaries
data = []
final_list = []
new = []
term_count = []
# create various lists

from stemming.porter2 import stem

# package for word stemming

with open('/Volumes/MY DATA/Users/Sarah/Documents/'
          'LIDo rotation 1/Review extrapolation code/'
          'Reviews/Codes/2016 La La Land_critic_reviews.txt') as a:
    line_1 = a.read()
    with open('/Volumes/MY DATA/Users/Sarah/Documents/'
              'LIDo rotation 1/Review extrapolation code/'
              'Key word by category/Neutral.txt') as b:
        lines = b.readlines()
        line_2 = [item.replace('\n', '') for item in lines]
        print(line_2)


# open neurosynth words and reviews of movie files and read the file

def noun():
    for word in line_1.replace('\n', ' ').split():
        # read each word in the first file
        for term in line_2:
            # read each word in the second file
            dictionary_1[word] = dictionary_1.setdefault(word, 0) + 1
            dictionary_2[term] = dictionary_2.setdefault(word, 0) + 1
            # save words in two separate dictionaries
            if [word] == [term]:
                data.append(word)
                # if the stem of the words in reviews is the same as the stem of terms in neurosynth
                for noun in data:
                    if noun not in final_list:
                        final_list.append(noun)
                        # append the words in common to a list (this removes duplicates present in the data list)


noun()


def count():
    from collections import Counter
    cnt = Counter()
    # start the counter package for word count
    for noun in line_1.split(' '):
        if noun in final_list:
            new.append(noun)
            # read each word in the review file and compare to those in the list of common words (append the stemmed words)
    for term in new:
        cnt[term] += 1
        # count occurence of each word
    print('{:20}{:3}'.format('Word', 'Count'))
    print('-' * 23)
    for (term, occurance) in cnt.items():
        print('{:20}{:3}'.format(term, occurance))
        term_count.append(cnt.items())
        # create a list with format (word, count)



count()
