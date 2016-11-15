from bs4 import BeautifulSoup
from urllib.request import  urlopen,urlretrieve,ContentTooShortError
import re
import os
import random
import datetime
random.seed(datetime.datetime.now())

base="http://updates.jenkins-ci.org/download/plugins/"
html=urlopen(base)
bsobj=BeautifulSoup(html)
links=bsobj.findAll("a",href=re.compile("^([^?|/download/])"))
def auto_down(url,filename):
    try:
        urlretrieve(url,filename)
    except ContentTooShortError:
        print("network condition is not good!!!")
        auto_down(url,filename)
for link in links:
    local = os.path.join("D:\jenkins",link.attrs['href'].split('/')[0])
    page=base+link.attrs['href']+"/latest/"+link.attrs['href'].split('/')[0]+".hpi"
    auto_down(page,local)