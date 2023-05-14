import requests  # pip install requests
from HttpFactory import HttpFactory
from bs4 import BeautifulSoup
from createLogger import createLogger
import traceback
from Util import Util
from dotmap import DotMap  # pip install dotmap


class HttpHandler:

    def __init__(self):
        self.logger = createLogger('HttpHandler')
        httpFactory = HttpFactory()
        self.http = httpFactory.create('requests')
        self.util = Util()
        self.mode = False
        self.saveMode = True

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
            if self.saveMode:
                self.util.saveFile(
                    f'appdata/html/{self.util.now()}.html', result)
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
            if self.saveMode:
                self.util.saveFile(
                    f'appdata/json/{self.util.now()}.json', result)
        except:
            self.logger.error(traceback.format_exc())
        return result

    def getUserJson2(self, userId, xIgAppID, max_id):
        if self.mode:
            return self.util.readFile('appdata/json/dlwlrma.json')
        result = ''
        try:
            response = self.http.getUserJson2(userId, xIgAppID, max_id)
            result = response.text
            if self.saveMode:
                self.util.saveFile(
                    f'appdata/json/{self.util.now()}.json', result)
        except:
            self.logger.error(traceback.format_exc())
        return result

    def getUserJson3(self, userId, xIgAppID, max_id):
        for i in range(0, 3):
            if self.mode:
                return self.util.readFile('appdata/json/dlwlrma.json')
            result = {}
            try:
                response = self.http.getUserJson2(userId, xIgAppID, max_id)
                result = DotMap(response.json())
                if self.saveMode:
                    self.util.saveFile(
                        f'appdata/json/{self.util.now()}.json', result)
            except:
                self.logger.error(traceback.format_exc())
            if result.status == 'ok':
                break
            print(i, '무야호')
        return result

    def check404(self, html):
        # a = self.util.readFile('aaa.html')
        html = BeautifulSoup(html, 'html.parser')
        title = html.find('title').string.strip()
        print(title)
        if title == 'Instagram':
            return True
        return False
