import requests  # pip install requests

class Requests:
     
    def getUserHtml(self, userName):
        response = requests.get(
            f'https://www.instagram.com/{userName}/', allow_redirects=False, timeout=1)
        return response
        
    def getUserJson(self, userId, xIgAppID):
        response = requests.get(
            f'https://www.instagram.com/api/v1/feed/user/{userId}/',
            headers={
                'X-IG-App-ID': xIgAppID,
            },
            allow_redirects=False,
        )
        return response