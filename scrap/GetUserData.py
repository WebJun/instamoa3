from Util import Util
from createLogger import createLogger
from HttpHandler import HttpHandler
from ParseUser import ParseUser


class GetUserData:

    def __init__(self):
        self.logger = createLogger('user')
        self.util = Util()
        self.http = HttpHandler()
        self.parse = ParseUser()
        self.max_id = ''

    def setUserName(self, userName):
        self.userName = userName

    def first(self):
        userHtml = self.http.getUserHtml(self.userName)
        self.userId = self.parse.userId(userHtml)
        self.xIgAppID = self.parse.xIgAppID(userHtml)

    def repeat(self):
        user = self.http.getUserJson3(self.userId, self.xIgAppID, self.max_id)
        self.max_id = user.next_max_id
        next = False
        if user.more_available:
            next = True
        return user, next
