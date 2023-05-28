import requests  # pip install requests
from dotmap import DotMap  # pip install dotmap


class Requests:

    def __init__(self, nic = None):
        if nic:
            self.setNic(nic)
           

    # Network Interface Card
    def setNic(self, nic):
        if not nic:
            self.requests = requests
        else:
            self.requests = self.session_for_src_addr(nic)

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
        
    def getUserHtml(self, userName):
        apple = DotMap()
        apple.url = f'https://www.instagram.com/{userName}/'
        apple.allow_redirects = False
        #apple.headers = {
        #    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36',
        #}
        apple.timeout = 5
        return self.requests.get(**apple)

    def getUserJson(self, userId, xIgAppID):
        apple = DotMap()
        apple.url = f'https://test2.cono.kr/request/{userId}/'
        apple.params = {
            'count': '50',
        }
        apple.headers = {
            'X-IG-App-ID': xIgAppID,
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36',
        }
        apple.allow_redirects = False
        return self.requests.get(**apple)

    def getUserJson2(self, userId, xIgAppID, max_id):
        apple = DotMap()
        apple.url = f'https://www.instagram.com/api/v1/feed/user/{userId}/'
        apple.params = {
            'count': '33',
            'max_id': max_id,
        }
        apple.headers = {
            'X-IG-App-ID': xIgAppID,
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36',
        }
        return self.requests.get(**apple)
