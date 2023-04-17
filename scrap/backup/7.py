import requests # pip install requests
from Util import Util
import sys
import json
from dotmap import DotMap  # pip install dotmap
from pprint import pprint
from bs4 import BeautifulSoup  # pip install bs4

headers = {
    'X-IG-App-ID': '936619743392459',
} 

util = Util()
now = util.now()
response = requests.get(
    'https://www.instagram.com/dlwlrma/'
)
# print(response.content)
#util.saveFile(f'appdata/html/{now}.html', response.text)

def searchJson(self, script):
    start = script.find('{')
    end = script.rfind('}')
    temp = script[start:end+1]
    return json.loads(temp)


s = util.readFile('appdata/html/20230413220515705802.html')
# print(s)

# temp = BeautifulSoup(s, 'html.parser')
# c = temp.find('body').find_all('script')[0].string
# print(c)
# temp2 = searchJson(c)

a = util.extraxtText(s, '","user_id":"','","include_chaining"')
print(a)

# s = json.loads(response.content)
# s = DotMap(s)

# pprint(s.user)
# print(s.status)
