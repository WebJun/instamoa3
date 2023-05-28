from Requests import Requests
from Config import Config

class HttpFactory:
    
    def create(self, method):
        config = Config()
        if method == 'requests':
            if config.MOBILE_IP:
                return Requests(config.MOBILE_IP)
            return Requests()
        