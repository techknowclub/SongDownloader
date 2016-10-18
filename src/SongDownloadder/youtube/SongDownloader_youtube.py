# Designed for Python2.7
# BeautifulSoup, Requests libraries should be installed
# youtube-dl should be installed


import requests
import os
import sys
from bs4 import BeautifulSoup
import time


media = "default"
search = raw_input()
if search[::-1][:3] == 'v- ':
    url = 'https://www.youtube.com/results?search_query=' + \
          search[::-1][4:][::-1]
    media = "defvideo"
# Enter the name of the video/song. Append ' -v' after the
# name to download the video, By default, audio is downloaded

else:
    url = 'https://www.youtube.com/results?search_query=' + search
sc = requests.get(url)
soup = BeautifulSoup(sc.content, 'html.parser')
title = soup.findAll('h3', {'class': 'yt-lockup-title '})
link = []
for i in range(len(title)):
    link.append(title[i].find('a')['href'])
for i in range(len(title)):
    print (str(i+1)+'. '+title[i].find('a').text)

while True:
    try:
        # enter the index of song from displayed list of songs
        user_input = int(raw_input())
        if user_input not in range(1, 20):
            print ('!')
            continue
        break
    except NameError:
        print ('!')
        continue
f_link = 'https://www.youtube.com'+link[user_input-1]


# print ('Downloading...')
if media == "default":
    os.system("youtube-dl -f 140 " + f_link)
if media == "defvideo":
    os.system("youtube-dl " + f_link)
print "Download Complete"

# File gets downloaded to your Python directory
# Use os.rename() to rename the file if required

# ChangeLog
# v1.0 Working application, html parser changed
# v1.1 Added more download options, code more organized
# v1.2 Added resolution choice for videos
# v1.3 Downloaded files are moved to specified location
# automatically, name changed
