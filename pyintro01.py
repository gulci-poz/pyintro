# coding: utf-8

import json
from urllib.request import urlopen

# zmieniło się API
url = "https://gdata.youtube.com/feeds/api/standardfeeds/top_rated?alt=json"
response = urlopen(url)
contents = response.read()
text = contents.decode("utf-8")
data = json.loads(text)

for video in data["feed"]["entry"][0:6]:
    print(video["title"]["$t"])
