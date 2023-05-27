import os
import asyncio
import aiohttp
import aiofiles
import traceback
import time
from dotmap import DotMap
from createLogger import createLogger
from Model import Model
from Config import Config
from pprint import pprint


def get_file_list(directory):
    file_list = []
    for file_name in os.listdir(directory):
        if os.path.isfile(os.path.join(directory, file_name)):
            file_list.append(file_name)
    return file_list


if __name__ == '__main__':
    MAX_REQUEST = 5
    a = DotMap()
    a.priority = 0
    a.status = 0

    '''
    비동기가 아니라
    멀티프로세스를 해야함
    
    큐 시스템
    나는  http user post file image video 순서대로 함

    나는 평소에 처음부터 다시 받을거임

    근데 중간에 진짜 사용자가 와서 요청하면

    그게 1순위로 되야함

    근데 또 다른 사용자가 오면

    그것도 1순위로 되어야함

    그 2개가 번갈아가면서 되어야함

    내꺼는 다 끝나고 해야함

    1. 우선순위가 있다
    2. 상태가 있다
    3. 요청을 받아야한다
    4. 그 요청의 최대 수가 있다.


    priority 클수록 먼저해야함
    priority 기본값 0


    파일이 생기는 것을 요청이라 생각하자
    user 1개 후
    post 1개
    file 2개
    post 1개
    ...반복
    프로세스 관리를 해야함.
    프로세스를 만들고 지우고를 반복해야할까?
    
    http post file image video를 한사이클로 해서 반복을 해야할까?
    좀 크면 시간이 오래걸릴수있음..
    1초씩 걸린다쳐도 5초..
    도중에 요청이 오면 끊어야함.
    프로세스를 종료시켜야함
    프로세스 번호를 디비에 저장시킨다음에 kill하고
    롤백 시켜야함
    
    pid
    post_count
    status
    priority
    
    Flask 써도 될거 같음
    
    '''
    while True:
        files = get_file_list('/scrap/server')
        pprint(files)
        time.sleep(1)