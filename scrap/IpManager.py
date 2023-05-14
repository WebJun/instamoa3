import time
import re
import logging
from math import ceil
import requests  # pip install requests
from ppadb.client import Client as AdbClient  # pip install pure-python-adb
import sys
from createLogger import createLogger


class Adb:

    client = None
    device = None
    modelName = None

    def __init__(self):
        self.client = AdbClient()
        devices = self.client.devices()
        self.device = devices[0]

    def getDevice(self):
        modelName = self.device.shell('getprop ro.product.model')
        return modelName.strip()

    def dataEnable(self):
        self.device.shell('svc data enable')
        # subprocess.check_output([f'platform-tools/adb','shell','svc','data','enable'])

    def dataDisable(self):
        self.device.shell('svc data disable')
        # subprocess.check_output([f'platform-tools/adb','shell','svc','data','disable'])


class IpManager:

    logger = None
    nic = None
    ipConfirmUrls = [
        'http://icanhazip.com',
        'http://ipv4.icanhazip.com',
        'https://httpbin.org/ip',
        'http://checkip.dyndns.org',
        'http://ifconfig.me',
    ]

    def __init__(self, nic):
        self.logger = createLogger('IpManager')
        self.setNic(nic)

    # Network Interface Card
    def setNic(self, nic):
        if not nic:
            self.requests = requests
        else:
            self.requests = self.session_for_src_addr(nic)

    def changeIP(self):
        try:
            adb = Adb()
            adb.dataDisable()
            adb.dataEnable()
            ip = self.getExternalIP()
            self.logger.info(f'changeIP-end : {ip}')
        except IndexError as err:  # Adb서버 꺼져있을 때
            print(err)
            print('ADB서버 꺼져있음')
            sys.exit()

    # https://stackoverflow.com/questions/48996494/send-http-request-through-specific-network-interface
    def session_for_src_addr(self, nic):
        session = requests.Session()
        for prefix in ('http://', 'https://'):
            session.get_adapter(prefix).init_poolmanager(
                connections=requests.adapters.DEFAULT_POOLSIZE,
                maxsize=requests.adapters.DEFAULT_POOLSIZE,
                source_address=(nic, 0),
            )
        return session

    def getExternalIP(self):
        result = ''
        for url in self.ipConfirmUrls:
            try:
                requ = self.requests.get(url, timeout=1)
                result = re.findall(r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}",
                                    requ.text)[0]
                break
            except Exception as err:
                pass
        return result
