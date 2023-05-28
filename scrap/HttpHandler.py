import requests  # pip install requests
from HttpFactory import HttpFactory
from bs4 import BeautifulSoup
from createLogger import createLogger
import traceback
from Util import Util
from dotmap import DotMap  # pip install dotmap
from IpManager import IpManager
from Config import Config
import time
from pprint import pprint


class HttpHandler:

    def __init__(self):
        self.logger = createLogger('HttpHandler')
        config = Config()
        httpFactory = HttpFactory()
        self.http = httpFactory.create('requests')
        self.util = Util()
        self.ipManager = IpManager(config.MOBILE_IP)

    def getUserHtml(self, userName):
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
        result = ''
        try:
            response = self.http.getUserJson(userId, xIgAppID)
            result = response.text
        except:
            self.logger.error(traceback.format_exc())
        return result

    def getUserJson2(self, userId, xIgAppID, max_id):
        result = ''
        try:
            response = self.http.getUserJson2(userId, xIgAppID, max_id)
            result = response.text
        except:
            self.logger.error(traceback.format_exc())
        return result

    def getUserJson3(self, userId, xIgAppID, max_id):
        for i in range(0, 10):
            result = {}
            try:
                response = self.http.getUserJson2(userId, xIgAppID, max_id)
                result = DotMap(response.json())
            except:
                self.logger.error(traceback.format_exc())
            pprint(result)
            if result.status == 'ok':
                break
            pprint(i, '무야호')
            self.ipManager.changeIP()
            time.sleep(1)
        return result

    def check404(self, html):
        html = BeautifulSoup(html, 'html.parser')
        title = html.find('title').string.strip()
        print(title)
        if title == 'Instagram':
            return True
        return False
