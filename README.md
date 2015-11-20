# PyConES-backbone

Material para el taller *Single-Page Applications con Django y Backbone* en PyConES Valencia 2015.

En el taller intentaremos replicar una pequeña aplicación Django usando la librería de JavaScript *Backbone* para el front-end y *django-tastypie* para la API REST.

Hemos creado dos ramas: **master** tiene un ligero *boilerplate* que durante el taller intentaremos *javascriptizar*; **single_page** tiene una versión un poco (muy poco) más avanzada de dicha *javascriptización* para aquel que quiera echar un vistazo.

## Requisitos para el taller.
Se recomienda a todos los asistentes que intenten llevar todo configurado en su propio ordenador de antemano.

* Python 2.7+ (https://www.python.org/downloads/)
* git (https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
* Pip (http://pip.readthedocs.org/en/stable/installing/)
* Virtualenvwrapper (https://virtualenvwrapper.readthedocs.org/en/latest/)
* SQLite (recomendado) o Postgresql (http://www.postgresql.org/download/)
* nodejs (https://nodejs.org/en/download/)
* npm (https://docs.npmjs.com/getting-started/installing-node)


## Instalación del entorno

1. `$ git clone http://github.com/MiguelSR/pycones_project`
2. `$ mkvirtualenv pycones_spa`
3. `$ cd pycones_project/ && pip install -r requirements.txt`
4. `$ cd pycones/ && ./manage.py migrate`
5. `$ ./manage.py createsuperuser`
6. `$ cd static/js && npm install`
7. `$ sudo npm install -g bower`
8. `$ bower install`
9. `$ cd ../.. && ./manage.py runserver`
