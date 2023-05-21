import requests  # pip install requests
from dotmap import DotMap  # pip install dotmap


class Requests:

    def getUserHtml(self, userName):
        apple = DotMap()
        apple.url = f'https://www.instagram.com/{userName}/'
        apple.allow_redirects = False
        apple.timeout = 5
        return requests.get(**apple)

    def getUserJson(self, userId, xIgAppID):
        apple = DotMap()
        apple.url = f'https://test2.cono.kr/request/{userId}/'
        apple.params = {
            'count': '50',
        }
        apple.headers = {
            'X-IG-App-ID': xIgAppID,
        }
        apple.allow_redirects = False
        return requests.get(**apple)

    def getUserJson2(self, userId, xIgAppID, max_id):
        apple = DotMap()
        apple.url = f'https://www.instagram.com/api/v1/feed/user/{userId}/'
        apple.params = {
            'count': '33',
            'max_id': max_id,
        }
        apple.headers = {
            'X-IG-App-ID': xIgAppID,
        }
        return requests.get(**apple)
