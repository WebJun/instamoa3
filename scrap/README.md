python -m venv .venv
.venv\Scripts\activate

python3 -m venv .venv
source .venv/bin/activate

pip list
pip freeze > requirements.txt
pip install -r requirements.txt

.venv\Scripts\activate

vim ~/.bashrc
source /scrap/www.instagrammoa.com/.venv/bin/activate