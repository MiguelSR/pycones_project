# PyConES-backbone

Se recomienda linux con firefox o chrome como navegador.

* Python 2.7+ (https://www.python.org/downloads/)
* Pip (http://pip.readthedocs.org/en/stable/installing/)
* Virtualenvwrapper (sudo pip install virtualenvwrapper)
* Postgresql (http://www.postgresql.org/download/)

1º workon pycones (SI)
2º pip install -r requirements.txt (SI)
3º django-admin startproject pycones
4º cd pycones && ./manage.py syncdb (SI)
5º ./manage.py startapp talks
5º ./manage.py startapp authors
6º editar pycones/settings.py y añadir a INSTALLED APPS nuestro talks
7º ./manage.py makemigrations
8º ./manage.py migrate
