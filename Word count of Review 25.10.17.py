dictionary_1 = {} 
dictionary_2 = {}
data = []
final_list = []

def noun():
    with open('/Volumes/MY DATA/Users/Sarah/Documents/LIDo rotation 1/Review extrapolation code/Birdman_reviews.txt') as a:
        line_1 = a.read()
        with open('/Volumes/MY DATA/Users/Sarah/Documents/LIDo rotation 1/Review extrapolation code/Neurosynth_words.txt') as b:
            line_2 = b.read()
            for word in line_1.replace('\n', ' ').split():
                for term in line_2.replace('\n', ' ').split():
                    dictionary_1[word] = dictionary_1.setdefault(word, 0) +1
                    dictionary_2[term] = dictionary_2.setdefault(word, 0) +1
                    if [word] == [term]:
                        data.append(word)
                        for noun in data:
                            if noun not in final_list:
                                final_list.append(noun)
noun()


def count():
    from collections import Counter
    with open('/Volumes/MY DATA/Users/Sarah/Documents/LIDo rotation 1/Review extrapolation code/Birdman_reviews.txt') as a:
        line_1 = a.read().split(' ')
        cnt = Counter()
        for word in line_1:
            if word in final_list:
                cnt[word] += 1
        print('{:20}{:3}'.format('Word', 'Count'))
        print('-'*23)
        for (word, occurance) in cnt.items():
            print('{:20}{:3}'.format(word, occurance))
            
count()
