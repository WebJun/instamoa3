import time
from datetime import timezone, timedelta, datetime


class Util:

    def now(self):
        return datetime.fromtimestamp(time.time(), timezone(
            timedelta(hours=9))).strftime('%Y%m%d%H%M%S%f')
    
    # 자동 확장자
    def info(self, data):
        #f = open(file_name, 'w', encoding='utf8')
        ext = 'txt'
        if data[0:1] == '<':
            ext = 'html'
        elif data[0:1] == '{':
            ext = 'json'
        f = open(f'appdata/{ext}/{self.now()}.{ext}', 'w', encoding='utf8')
        f.write(data)
        f.close()
        return 200
    
    def saveFile(self, file_name, data):
        #f = open(file_name, 'w', encoding='utf8')
        f = open(f'{file_name}', 'w', encoding='utf8')
        f.write(data)
        f.close()
        return 200

    def readFile(self, file_name):
        result = ''
        f = open(file_name, 'r', encoding='utf8')
        result = f.read()
        f.close()
        return result

    def extraxtText(self, book, text1, text2, n=1, m=1):
        temp1 = 0
        temp2 = 0
        text1 = str(text1)
        text2 = str(text2)

        for i in range(0, n):
            temp1 = book.find(text1, temp1)
            if temp1 == -1:
                return ''
            temp1 = temp1 + 1

        temp2 = temp1 + len(text1) - 1
        for i in range(0, m):
            temp2 = book.find(text2, temp2)
            if temp2 == -1:
                return ''
            temp2 = temp2 + 1

        return book[temp1 - 1 + len(text1):temp2 - 1]

    def zfill3(self, text):
        return str(text).zfill(3)