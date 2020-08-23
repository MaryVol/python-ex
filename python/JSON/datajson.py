import json
import urllib.request, urllib.parse, urllib.error

sum = 0
x = 0

with urllib.request.urlopen('http://py4e-data.dr-chuck.net/comments_447450.json') as url:
    data = json.loads(url.read().decode())
    for item in data['comments']:
        print(item)
        num = int(data['comments'][x]['count'])
        sum += num
        x += 1
print(sum)

