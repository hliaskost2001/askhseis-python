import urllib.request
import json
import  datetime
d = datetime.datetime(2021, 1, 30)
print(d)

url="https://api.opap.gr/draws/v3.0/1100/draw-date/2021-01-30/2021-01-30"
r=urllib.request.urlopen(url)
html=r.read()
html=html.decode()
data=json.loads(html,strict=False)
for draw in data["content"]:
    t=draw["winningNumbers"]["list"]
    print([max(t),min(t)])
