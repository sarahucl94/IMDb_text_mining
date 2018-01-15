def job():
    title = input("Select year of production and movie title: ")
    file = open(title + "_critic_reviews.txt", "w+")
    import google  # for google searches
    import re
    import requests
    # can access info on the web and extrapolate it
    from bs4 import BeautifulSoup
    # gets HTML info


    for url in google.search(title + "External Reviews IMDb", lang='eng', num=1, start=0, stop=1):
        # open google.co.uk for "title, year IMDb user reviews" in english, open first URL only
        print(url)
        r = requests.get(url)
        # open URL
        soup = BeautifulSoup(r.text, "html.parser")
        # parse HTML


        for ul in soup.find_all('ul', class_="simpleList"):
            for li in ul.find_all('li'):
                a = li.find('a')
                link = a.get('href')
                print(link)
                new_soup = BeautifulSoup(requests.get('http://www.imdb.com'+link).text, "html.parser")
                for words in new_soup.find_all("p"):
                # inspect HTML of webpage and find article main body ("p")
                    if words:
                        b = str(words.text.replace("\n", " ").encode('ascii', 'ignore').decode('utf-8').strip())
                        file.write(b)
                    # remove formatting and make uniform text- print
                    else:
                        c = str(words.a.contents[0].strip())
                        file.write(c)
                    # remove links and add to text- print
                        file.close()


job()
