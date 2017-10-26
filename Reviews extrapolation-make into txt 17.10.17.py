def job():
    file = open("Birdman_reviews.txt", "w+")
    import google
    #for google searches
    import requests
    #can access info on the web and extrapolate it
    from bs4 import BeautifulSoup
    #gets HTML
    for url in google.search("birdman movie reviews", tld='co.uk', lang='eng', num=5, start=0, stop=5):
        #open google.co.uk for "birdman movie reviews" in english, open 2 URLs and stop at the 3rd
        print(url)
        r = requests.get(url)
        #extrapolate URL
        soup = BeautifulSoup(r.text, "html.parser")
        #parse HTML
        for words in soup.find_all("p"):
            #inspect HTML of webpage and find article main body ("p")
            if words:
                b = str(words.text.replace("\n", " ").encode('ascii', 'ignore').decode('utf-8').strip())
                file.write(b)
                #remove formatting and make uniform text- print
            else:
                c = str(words.a.contents[0].strip())
                file.write(c)
                #remove links and add to text- print
                file.close()
job()
