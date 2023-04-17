python -m venv .venv
.venv\Scripts\activate

python3 -m venv .venv
source .venv/bin/activate

pip list
pip freeze > requirements.txt
pip install -r requirements.txt

.venv\Scripts\activate
python main.py user dlwlrma
python main.py post dlwlrma
python main.py file dlwlrma
python main.py copy dlwlrma

