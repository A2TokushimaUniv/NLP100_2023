import urllib
url = 'https://www.mediawiki.org/w/api.php?action=query&titles=File:' + urllib.parse.quote(inf_dic4['国旗画像']) + '&format=json&prop=imageinfo&iiprop=url'
connection = urllib.request.urlopen(urllib.request.Request(url))
response = json.loads(connection.read().decode())
print(response['query']['pages']['-1']['imageinfo'][0]['url'])