from flask import Flask  # pip install flask
from flask import render_template
import os
import webbrowser
import glob

app = Flask(__name__, template_folder='', static_folder='appdata')


@app.route('/')
def index():
    return render_template('/index.html', files=getFiles())


@app.route('/getFiles')
def getFiles():
    currentPath = os.path.abspath(__file__)
    basePath = os.path.dirname(currentPath)
    jpgGlob = f'{basePath}/appdata/*/*/*/*'
    files = glob.glob(jpgGlob, recursive=True)

    basePathLen = len(basePath) + 1
    files = [file[basePathLen:1000]
             for file in files if os.path.splitext(file)[1] == '.jpg']
    files.reverse()
    return files


if __name__ == '__main__':
    # webbrowser.open('http://127.0.0.1:18000') # 브라우저 열기 WSL에서 안됨
    app.run(debug=True, host='0.0.0.0', port=18000)
    # app.run()
