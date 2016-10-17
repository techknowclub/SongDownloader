import requests
from bs4 import BeautifulSoup
import os
import dryscrape
import urllib





def youtubedl(search):
    media = "audio"
    url = 'https://www.youtube.com/results?search_query='+search[:len(search)-3]
    sc =requests.get(url)
    soup = BeautifulSoup(sc.content,'html.parser')
    title = soup.findAll('h3',{'class':'yt-lockup-title '})
    link = []
    for i in range(len(title)):
        link.append(title[i].find('a')['href'])
    for i in range(len(title)):
        print (str(i+1)+'. '+title[i].find('a').text)

    while True:
        try:
            user_input = int(raw_input(">"))
            if user_input == 999: #override code
                continue
            if user_input not in range(1,20):
                print ('!')
                continue
            break
        except NameError:
            print ('!')
            continue
    f_link = 'https://www.youtube.com'+link[user_input-1]

    if search[::-1][:3] == 'v- ':
        media = "defvideo"
    if search[::-1][:3] == "r- ":
        res = ListRes(f_link)
        media = "video"

    if media == "video":
        os.system("youtube-dl -f {} ".format(res) + f_link)
    if media == "defvideo":
        os.system("youtube-dl " + f_link)
    if media == "audio":
        os.system("youtube-dl -f 140 " + f_link)
    print "Downlod Complete"
    os.system("say Download complete")




flag = ""
headers = {"User-agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.80 Safari/537.36"}
search = raw_input(">")
for song in search.split(', '):
    if song[len(song) -3:] == ' -y':
        youtubedl(song)
    else:
        base_url = "http://mp3brainz.cc/v1/"
        query_url = "http://mp3brainz.cc/v1/#!q=" + song
        session = dryscrape.Session()
        session.visit(query_url)
        response = session.body()
        soup = BeautifulSoup(response, 'lxml')
        links = soup.findAll('a')
        link_ = []
        link__ = []
        for link in links:
            try:
                if len(link['href']) == 71:

                    link_.append(link)
                    link__.append(link['href'][2:])
            except:
                pass
        if len(links) > 10:
            for i in range(20):
                temp = link_[i].text.split('\n')
                print str(i+1)+ ".", temp[2],temp[3],temp[5]
            n =int(raw_input(">"))
            if n == 0:
                    youtubedl(search)
            if n == 999:
                continue
            else:
                download = base_url + link__[n-1]
                session2 = dryscrape.Session()
                session2.visit(download)
                response2 = session2.body()
                soup1 = BeautifulSoup(response2, 'lxml')
                final_link = soup1.findAll('span' , {'class':'url'})
                final_link = str(final_link)[19:].split('<')
                print "Downloading from: \n",final_link[0], "\n\n"
                #urllib.urlretrieve(g[0], "{}.mp3".format(names[n-1].text))
                os.system("curl -O " + final_link[0])
                os.system("say download complete")
                print "Download complete"

        else:
            youtubedl(search)
