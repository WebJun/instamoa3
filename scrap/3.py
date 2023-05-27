from flask import Flask, request
from multiprocessing import Process
import time

app = Flask(__name__)


def run_program(program):
    print('시작')
    time.sleep(3)
    # 여기에 프로그램 실행 로직을 추가하세요.
    print("Running program:", program)


@app.route('/execute', methods=['GET'])
def execute():
    # data = request.json
    program = 'aaa'
    # program = data['program']
    process = Process(target=run_program, args=(program,))
    process.start()
    return "Program execution started"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=18000, debug=True)
