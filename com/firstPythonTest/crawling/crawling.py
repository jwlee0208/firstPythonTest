'''
Created on 2016. 2. 22.

@author: leejinwon
'''
# -*- coding: euc-kr -*-
import urllib

from bs4 import BeautifulSoup


html = urllib.urlopen("http://linkednest.net/player/playerDetailView/jwlee")
soup = BeautifulSoup(html, "lxml")

data = soup.findAll("div", {"class" : "form-group"})
print "totalData : ", data
data = str(data)
data = data.split("<")
for i in range(len(data)):
    if i % 5 == 2:
        print data[i].split(">")[1]
        
        
        