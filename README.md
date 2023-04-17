### window
python -m venv .venv  
.venv\Scripts\activate

### linux
python3 -m venv .venv  
source .venv/bin/activate

### package
pip list  
pip freeze > requirements.txt  
pip install -r requirements.txt

### django
cd /web/mysite  
python manage.py runserver 0.0.0.0:8000  

python manage.py migrate  
python manage.py makemigrations insta  
python manage.py createsuperuser
