import urllib.request, urllib.parse, urllib.error
import json


url = 'http://py4e-data.dr-chuck.net/comments_1997283.json'
uh = urllib.request.urlopen(url)
data = uh.read().decode()

info = json.loads(data)
lst = info['comments']
sum = 0

for item in lst:
    sum = sum + int(item['count'])
    
print(sum)
