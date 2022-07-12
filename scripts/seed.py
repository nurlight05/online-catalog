import os
from employee.models import Employer

def run():
    Employer.objects.all().delete()
    os.system('python manage.py loaddata scripts/json/ceo.json')
    os.system('python manage.py loaddata scripts/json/dir.json')
    os.system('python manage.py loaddata scripts/json/mgr.json')
    os.system('python manage.py loaddata scripts/json/tml.json')
    os.system('python manage.py loaddata scripts/json/dvp.json')
