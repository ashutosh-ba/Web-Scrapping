# -*- coding: utf-8 -*-
"""
Created on Sat Apr 22 13:46:44 2017

@author: Ashutosh
"""


from urllib.request import urlopen

from lxml.html import fromstring

import pandas as pd
import os


def get_page(url):
    html = urlopen(url).read()
    print(html)
    dom = fromstring(html)
    dom.make_links_absolute(url)
    print(dom)
    return dom

dom = get_page("http://www.chicagoreader.com/chicago/best-of-chicago-2011/BestOf?oid=4100483")

#%%
dom.cssselect("#storyBody p a")
#%%

#%%
[link.attrib['href'] for link in _]
#%%

#%%
secns = _
#%%

fan =get_page("https://fantasycricket.dream11.com/in/my-team/indian-t20-league/669/7462/1")
print(fan.attrib)

for child in fan:
    print (fan.tag, fan.attrib)
    
for neighbor in fan.iter('neighbor'):
    print (neighbor.attrib)

name =fan.cssselect(".thPlName")
point =fan.cssselect(".thPlPoint")
credit=fan.cssselect(".thPlCr")
team=fan.cssselect(".plyrTeam")



out =pd.DataFrame()

for i in range(1,len(name)):
   out = out.append({'Player':name[i].text_content(),'Point':point[i].text_content(),'Credit':credit[i].text_content(),'Team':team[i-1].text_content()}, ignore_index=True)

os.chdir("C:\\Users\Ashutosh\Desktop\CBA\Optimization\Project")

out.to_csv("PlayerData.csv")

