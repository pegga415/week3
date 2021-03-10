import ssl
ssl._create_default_https_context = ssl._create_unverified_context

import urllib.request as req
url = "https://padax.github.io/taipei-day-trip-resources/taipei-attractions.json"

import json
with req.urlopen(url) as response:
    data = json.load(response)

clist = data['result']['results']

with open('data.txt','w',encoding='utf-8') as file:
    for attraction in clist:
        imgUrl = ''
        for x in range(len(attraction['file'])):
            imgUrl += attraction['file'][x]
            y = attraction['file'][x+1] + attraction['file'][x+2] + attraction['file'][x+3] + attraction['file'][x+4]
            if y == 'http':
                break
            if x+5 == len(attraction['file']):
                imgUrl += attraction['file'][x+1] + attraction['file'][x+2] + attraction['file'][x+3] + attraction['file'][x+4]
                break
        file.write(attraction['stitle']+','+attraction['longitude']+','+attraction['latitude']+','+imgUrl+'\n')