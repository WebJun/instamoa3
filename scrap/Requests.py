import requests  # pip install requests


class Requests:

    def getUserHtml(self, userName):
        response = requests.get(
            f'https://www.instagram.com/{userName}/', allow_redirects=False, timeout=1)
        return response

    def getUserJson(self, userId, xIgAppID):
        headers = {
            'X-IG-App-ID': xIgAppID,
        }
        print(77)
        response = requests.get(
            f'https://www.instagram.com/api/v1/feed/user/{userId}/',
            headers=headers,
            allow_redirects=False,
        )
        print(7711)
        return response

    def getUserJson2(self, userId, xIgAppID, max_id):
        params = {
            'count': '50',
            'max_id': max_id,
        }
        headers = {
            'X-IG-App-ID': xIgAppID,
        }
        print(99)
        response = requests.get(
            f'https://www.instagram.com/api/v1/feed/user/{userId}/',
            params=params,
            headers=headers,
            allow_redirects=False,
        )
        print(9911)
        return response
