from bs4 import BeautifulSoup as bs
import urllib
import requests
from urllib import re

max_options_limit = 20
url_prefix = r'http://mp3clan.ws/mp3/'
url_suffix = r'.html'
song_name = raw_input()
url = url_prefix + song_name + url_suffix
r = requests.get(url)
soup = bs(r.content, 'lxml')
titles = soup.find_all('div', {'class': 'unselectable'})[0:max_options_limit]
download_links = soup.find_all('div', {'title': 'Download'})[0:max_options_limit]
links = []
for (count,title,download_link) in zip(range(1,max_options_limit + 1),titles,download_links):
  print str(count) + '. ' + title.text
  links.append(download_link.find('a')['href'])
choice = int(raw_input())
# Download
response = urllib.urlopen(links[choice - 1])
mp3 = response.read()
f = open("thisshouldwork.mp3", "w")
f.write(mp3)
f.close()
print "Done"
