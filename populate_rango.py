import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','tango_with_django_project.settings')

import django
django.setup

from rango.models import Category, page
def populate():
    python_pages = [
        {'title':'Official Python Tutorial', 'url': 'http://docs.python.org/3/tutorial/'},
        {'title':'How to Think like a Computer scientist','url':'http://www.greenteapress.com/thinkpython/'}
        {'title':'Learn Python in 10 Minutes0','url':'http://www.Korokithakis.net/tutorials/pyhton/'}
    ]


    django_pages = [
        {'title':'Official Django Tutorial','url':'https://docs.djangoproject.com/en/2.1/intro/tutorial01/'},
        {'title':'Django Rocks','url':'http://www.djangorocks.com/'},
        {'title':'How to Tango with Django','url':'http://www.tangowithdjango.com/'}
    ]

    other_pages = [
        {'title':'Bottle','url':'http://bottlepy.org/docs/dev/'},
        {'title':'Flask','url':'http://flask.pocoo.org'}

    ]
    
    cats = {'Python': {'pages': python_pages},
            'Django': {'pages': django_pages},
            'Other Frameworks': {'pages': other_pages} }
        