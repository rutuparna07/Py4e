import json
import urllib.request

count = 0
sum = 0
url = "http://py4e-data.dr-chuck.net/comments_716296.json"
data = urllib.request.urlopen(url).read()

info = json.loads(data)

for i in info['comments']:
    count = count+1
    sum = sum+i['count']

print ("Sum:",sum)
print ("Count:",count)
