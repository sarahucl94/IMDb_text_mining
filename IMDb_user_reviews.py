def job():
    title = input("Select year of production and movie title: ")
    file = open(title + "_reviews.txt", "w+")
    import google
    #for google searches
    import requests
    #can access info on the web and extrapolate it
    from bs4 import BeautifulSoup
    #gets HTML
    for url in google.search(title + "reviews and ratings IMDb", tld='co.uk', lang='eng', num=1, start=0, stop=1):
        #open google.co.uk for "title, year IMDb user reviews" in english, open first URL only
        print(url)
        r = requests.get(url)
        #open URL
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
