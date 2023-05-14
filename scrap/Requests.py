import requests  # pip install requests


class Requests:

    def getUserHtml(self, userName):
        response = requests.get(
            f'https://www.instagram.com/{userName}/', allow_redirects=False, timeout=5)
        return response

    def getUserJson(self, userId, xIgAppID):
        params = {
            'count': '50',
            # 'max_id': max_id,
        }
        headers = {
            'X-IG-App-ID': xIgAppID,
        }
        response = requests.get(
            f'https://www.instagram.com/api/v1/feed/user/{userId}/',
            params=params,
            headers=headers,
            allow_redirects=False,
        )
        return response

    def getUserJson2(self, userId, xIgAppID, max_id):
        params = {
            # 'count': '50',
            'count': '33',
            'max_id': max_id,
        }
        headers = {
            'X-IG-App-ID': xIgAppID,
        }
        response = requests.get(
            f'https://www.instagram.com/api/v1/feed/user/{userId}/',
            params=params,
            headers=headers,
            allow_redirects=False,
        )
        return response
