from Requests import Requests

class HttpFactory:
    
    def create(self, method):
        if method == 'requests':
            return Requests()
        