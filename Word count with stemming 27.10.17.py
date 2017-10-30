dictionary_1 = {} 
dictionary_2 = {}
data = []
final_list = []
new = []


from stemming.porter2 import stem

with open('/Users/sarah/Downloads/Birdman_reviews.txt') as a:
    line_1 = a.read()
    with open('/Users/sarah/Downloads/Neurosynth_words.txt') as b:
        line_2 = b.read()

        
def noun():
    for word in line_1.replace('\n', ' ').split():
        for term in line_2.replace('\n', ' ').split():
            dictionary_1[word] = dictionary_1.setdefault(word, 0) +1
            dictionary_2[term] = dictionary_2.setdefault(word, 0) +1
            if stem([word]) == stem([term]):
                data.append(stem(word))
                for noun in data:
                    if noun not in final_list:
                        final_list.append(noun)
                        
noun()



def count():
    from collections import Counter
    cnt = Counter()
    for noun in line_1.split(' '):
        if stem(noun) in final_list:
            new.append(stem(noun))
    for term in new:
        cnt[term] += 1
    print('{:20}{:3}'.format('Word', 'Count'))
    print('-'*23)
    for (term, occurance) in cnt.items():
        print('{:20}{:3}'.format(term, occurance))
            
count()
