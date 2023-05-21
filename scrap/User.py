from dotmap import DotMap  # pip install dotmap
import selenium
from selenium.webdriver.common.by import By
import time
import json
import sys
import logging
# from BrowserFactory import BrowserFactory
from Util import Util
from Model import Model
from IpManager import IpManager
import traceback
from createLogger import createLogger
from func_timeout import func_set_timeout, FunctionTimedOut  # pip install func-timeout


class InstaCrawling:

    # userId = None
    bs = None  # browser
    postsAllIds = []
    orders = 0
    user = None
    logger = None

    def __init__(self, logger):
        self.logger = logger
        self.util = Util()
        self.ipManager = IpManager('192.168.42.36')
        self.bf = BrowserFactory()

    def runFireFox(self):
        if not self.bs:
            self.bs = self.bf.create('firefox')
            self.bs.set_page_load_timeout(60)

    def quitFireFox(self):
        self.bs.quit()
        self.bs = None

    def login(self):
        cookies = self.util.readFile('appdata/cookies.json')
        cookies = json.loads(cookies)
        self.bs.delete_all_cookies()
        for cookie in cookies:
            self.bs.add_cookie(cookie)

        self.bs.get(f'https://www.instagram.com/{self.user.id}/')

    # 수동 로그인 필요
    def createLoginCookie(self):
        time.sleep(100)
        cookies = self.bs.get_cookies()
        print(cookies)
        self.util.saveFile('appdata/cookies.json', json.dumps(cookies))
        sys.exit()

    def getIsScrollBottom(self):
        return self.bs.execute_script(
            'return document.scrollingElement.scrollTop+window.innerHeight==document.body.scrollHeight;'
        )

    def waitNextPosts(self):
        try:
            while True:
                self.waitNextPostsinner()
                break
        except FunctionTimedOut:
            self.moveScrollTop()

    @func_set_timeout(10)
    def waitNextPostsinner(self):
        while self.getIsScrollBottom():
            time.sleep(0.2)

    def moveScrollTop(self):
        self.bs.execute_script('window.scrollTo(0, 0);')

    def moveScrollBottom(self):
        self.bs.execute_script(
            'window.scrollTo(0, document.body.scrollHeight);')

    def getIsExistLoading(self):
        return self.bs.find_element(By.TAG_NAME, 'article').find_elements(
            By.XPATH, 'div[2]')

    # BeautifulSoup로 가져와서 파싱하는건 어떨까?
    def getPosts(self):
        postsNew = []
        postsNewIds = []
        script = '''
            function getXpath (aNode, aExpr)
            {
                return document.evaluate(aExpr, aNode, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null).singleNodeValue;
            }
            function evaluateXPath (aNode, aExpr) 
            {
                const xpe = new XPathEvaluator();
                const nsResolver = xpe.createNSResolver(aNode.ownerDocument === null ? aNode.documentElement : aNode.ownerDocument.documentElement);
                const result = xpe.evaluate(aExpr, aNode, nsResolver, 0, null);
                const found = [];
                let res;
                while (res = result.iterateNext()) {
                    found.push(res);
                }
                return found;
            }
            var article = document.getElementsByTagName('article')[0];
            var baseDiv = evaluateXPath(article, "div/div");
            var rowDivs = evaluateXPath(baseDiv[0], "div");
            var itemDivs = [];
            for (rowDiv of rowDivs) {
                // rowDiv.style.display = "none";
                itemDivs = itemDivs.concat(evaluateXPath(rowDiv, "div"))
            }
            var hrefs = [];
            for (itemDiv of itemDivs) {
                try {
                    href = getXpath(itemDiv, "a").getAttribute("href")
                    hrefs.push(href)
                } catch (e) {
                    
                }
            }
            return hrefs;
        '''
        postsIds = self.bs.execute_script(script)
        postNowIds = [
            self.util.extraxtText(postsId, '/', '/', 2, 1)
            for postsId in postsIds
        ]
        postsNewIds = [
            ele for ele in postNowIds if ele not in self.postsAllIds
        ]
        self.postsAllIds = set().union(self.postsAllIds, postNowIds)

        for postId in postsNewIds:
            self.orders = self.orders + 1
            apple = DotMap()
            apple.userId = self.user.id
            apple.postId = postId
            apple.orders = self.orders
            postsNew.append(apple)
        return postsNew

    # def waitLoading(self):
    #     while True:
    #         try:
    #             WebDriverWait(self.bs, 10).until(
    #                 EC.presence_of_element_located((
    #                     By.TAG_NAME, 'article'
    #                     #    By.XPATH,
    #                     #    '/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/section/main/div/div'
    #                 )))
    #             break
    #         except selenium.common.exceptions.TimeoutException:
    #             print('치명적오류')
    #             sys.exit()
    def waitLoading(self):
        while True:
            try:
                self.bs.find_element(By.TAG_NAME, 'article')
                break
            except selenium.common.exceptions.NoSuchElementException:
                pass
            # if not self.getIsShowByJs('splash-screen'):
            #    break
            try:
                h2 = self.bs.find_element(
                    By.XPATH,
                    '/html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]/div[1]/div[2]/section/main/div/div/div/h2'
                )
                if h2.text == '죄송합니다. 페이지를 사용할 수 없습니다.':
                    raise Exception('페이지를 찾을 수 없습니다. 404')
            except selenium.common.exceptions.NoSuchElementException:
                pass
            time.sleep(0.1)

    # 요소가 보이는지
    def getIsShowByJs(self, ele):
        return self.bs.execute_script(
            f'return document.getElementById("{ele}").style.display;'
        ) != 'none'

    def getElement(self, path):
        try:
            # section = '/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/section'
            # section = '/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/div[2]/div[2]/section'
            # section = '/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/div[1]/div[2]/section'
            # section = '/html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]/div[1]/div[2]/section'
            # section = '/html/body/div[2]/div/div/div[1]/div/div/div/div[1]/div[1]/div[2]/section'
            # section = '/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[2]/section'
            section = '/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[2]/div[2]/section'
            # section = '/html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]/section'
            return self.bs.find_element(By.XPATH, f'{section}/{path}')
        except selenium.common.exceptions.NoSuchElementException:
            pass

    def getUserIdText(self):
        h = self.getElement('main/div/header/section/div[1]').find_elements(
            By.TAG_NAME, 'h1')
        if not h:
            h = self.getElement(
                'main/div/header/section/div[1]').find_elements(
                    By.TAG_NAME, 'h2')
        return h[0].text

    def getFollowing(self):
        return self.getElement(
            'main/div/header/section/ul/li[3]').find_element(
                By.TAG_NAME, 'span').text

    def getFollowers(self):
        return self.getElement(
            'main/div/header/section/ul/li[2]').find_element(
                By.TAG_NAME, 'span').text

    # def getBiography(self):
    #     div = self.getElement('main/div/header/section/div[3]/div')
    #     if div:
    #         return div.text
    #     return ''

    # def getName(self):
    #     span = self.getElement('main/div/header/section/div[3]/span')
    #     if not span:
    #         span = self.getElement('main/div/header/section/div[3]')
    #     if span:
    #         return span.text
    #     return ''

    # def getFollowers(self):
    #     span = self.getElement('main/div/header/section/ul/li[2]/a/div/span')
    #     if not span:
    #         span = self.getElement('main/div/header/section/ul/li[2]/div/span')
    #     if span:
    #         return span.get_attribute('title').replace(',', '')
    #     return ''
    def getBiography(self):
        '''
        요소갸 존재하지않는 경우가 있고
        다른 곳에 존재하는 경우가 있어서 어려움
        요소가 존재하지 않은 경우에는 빈값이지만
        다른 곳에 존재하는 경우에는 그 값을 찾아야함
        '''
        div = self.getElement('main/div/header/section/div[3]/div')
        if div:
            return div.text
        return ''

    def getName(self):
        span = self.getElement('main/div/header/section/div[3]/span')
        if not span:
            span = self.getElement('main/div/header/section/div[3]')
        return span.text

    def getProfileUrl(self):
        return self.getElement('main/div/header/div/div').find_element(
            By.TAG_NAME, 'img').get_attribute('src')

    # 2.9만
    def getPostsCntStr(self):
        result = self.getElement(
            # 'main/div/header/section/ul/li[1]/div/span'
            # 'main/div/header/section/ul/li[1]/span/span/span'
            'main/div/header/section/ul/li[1]/span/span'
        ).text
        return result.replace(',', '')

    # 29000
    def getPostsCnt(self):
        text = self.user.postsCntStr
        textLen = len(text)
        if text[textLen - 1:textLen] != '만':
            return int(text)
        textNum = text[0:textLen - 1]
        return int(float(textNum) * 10000)

    def getProfile(self):
        self.user.id = self.getUserIdText()
        self.user.postsCntStr = self.getPostsCntStr()
        self.user.postsCnt = self.getPostsCnt()

        self.user.followers = self.getFollowers()
        self.user.following = self.getFollowing()
        self.user.name = self.getName()
        self.user.biography = self.getBiography()
        # self.user.content3 = self.getElement(
        #    'main/div/header/section/div[3]/a/div').text
        self.user.profileUrl = self.getProfileUrl()
        self.user.idNum = self.util.extraxtText(self.bs.page_source,
                                                '{"page_id":"profilePage_',
                                                '","profile_id":"')

    def getIsClosed(self):
        try:
            h2 = self.getElement(
                # 'main/div/div/article/div[1]/div/h2'
                'main/div/div/article/div/div/h2')
            if h2.text == '비공개 계정입니다':
                return True
        except AttributeError as err:
            pass
        return False


class User:

    userId = None

    def __init__(self, userId):
        self.user = DotMap()
        self.user.id = userId

    def run(self):
        try:
            mylogger = createLogger('User')
            mylogger.info(f'start user : {self.user.id}')
            model = Model()
            ic = InstaCrawling(mylogger)
            ic.user = self.user
            # 이미 있으면 진행x
            users = model.getUsers(ic.user)
            if users:
                mylogger.info(users)
                mylogger.info('이미 존재하는 User입니다.')
                sys.exit()
            ic.runFireFox()
            ic.bs.get(f'https://www.instagram.com/{self.user.id}/')
            # ic.createLoginCookie()
            ic.login()
            ic.waitLoading()
            ic.getProfile()
            ic.user.isClosed = ic.getIsClosed()
            ic.user.state = 200
            if ic.user.postsCnt == 0:
                ic.user.state = 602
            elif ic.user.isClosed:
                ic.user.state = 601
            mylogger.info(ic.user)
            model.saveUser(ic.user)
            if ic.user.postsCnt == 0:
                raise Exception('포스트가 없습니다.')
            if ic.user.isClosed:
                raise Exception('비공개 계정입니다.')
            postCnt = 0
            while True:
                if not ic.getIsScrollBottom():
                    ic.moveScrollBottom()
                posts = ic.getPosts()
                postCnt = postCnt + len(posts)
                model.savePosts(posts)
                mylogger.info(json.dumps([dict(post) for post in posts]))
                if not ic.getIsExistLoading():
                    break
                ic.waitNextPosts()

            # 로딩이 먼저 없어져서 한 번 더 내려줘야함
            ic.moveScrollBottom()
            posts = ic.getPosts()
            postCnt = postCnt + len(posts)
            model.savePosts(posts)
            mylogger.info(json.dumps([dict(post) for post in posts]))
            mylogger.info(f'총 {postCnt}개')
            mylogger.info(f'end user success : {self.user.id}')
            ic.quitFireFox()
        except Exception as err:
            mylogger.info(traceback.format_exc())
            mylogger.info(err)
            mylogger.info(f'end user error : {self.user.id}')
            ic.quitFireFox()
