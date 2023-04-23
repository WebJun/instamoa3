import requests  # pip install requests
from HttpFactory import HttpFactory
from bs4 import BeautifulSoup
from createLogger import createLogger
import traceback
from Util import Util

class HttpHandler:
     
    def __init__(self):
        self.logger = createLogger('HttpHandler')
        httpFactory = HttpFactory()
        self.http = httpFactory.create('requests')
        self.util = Util()
        self.mode = True

    def getUserHtml(self, userName):
        if self.mode:
            return self.util.readFile('appdata/html/dlwlrma.html')
        result = ''
        try:
            response = self.http.getUserHtml(userName)
            if response.status_code != 200:
                raise Exception(response.status_code)
            if self.check404(response.text):
                raise Exception('aaaa')
            result = response.text
        except:
            self.logger.info(traceback.format_exc())
        return result
    
    def getUserJson(self, userId, xIgAppID):
        if self.mode:
            return self.util.readFile('appdata/json/dlwlrma.json')
        result = ''
        try:
            response = self.http.getUserJson(userId, xIgAppID)
            result = response.text
        except:
            self.logger.error(traceback.format_exc())
        return result

    def check404(self, html):
        #a = self.util.readFile('aaa.html')
        html = BeautifulSoup(html, 'html.parser')
        title = html.find('title').string.strip()
        print(title)
        if title == 'Instagram':
            return True
        return False