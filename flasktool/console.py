from __future__ import absolute_import 


from .extensions import FlaskExtension
from .apps import FlaskApplication
from flask import Flask
from flaskext.script import prompt, prompt_choices, Manager, Option
import string


def create_app(*args, **kwargs):
        app = Flask(__name__)
        return app

manager = Manager(create_app, False)

whatnext = """
###################
Your new Flask app is ready.
###################
What to do now:
$ cd %(name)s  # then...

    - $ pip install -r requirements.txt
    - $ ./manage.py runserver
    - Add more commands to manage.py
    - Write your app and tests
    - Check in your code
    - setup an EC2 instance
    - Add credentials and hosts to fabfile.py
    - Run fab deploy
    - ???????
    - Profit!
"""


@manager.option('-l', '--layout', default='factory',choices=['factory','heavy','simple'])
@manager.option(nargs=1, dest='name',help='name of the app/directory')
@manager.option(nargs=1, dest='what',help='what sort of thing to make',choices=['ext','app'])
def create(what='app', name='MyAwesomeApp', layout='factory'):
    """(ext|app) <name>  # create an app or extension"""
    """
    flasktool create ext 'Flask-MongoEngine'

    flasktool create app MyAwesomeApp
    flasktool create app MyAwesomeApp --layout=factory
        - Create new folder.
        - Make app.yaml and  add to new folder.
        - Look at layout for template to use.
        - cd to new app directory
        - Create tasks, settings, etc.

    flasktool create view account
    flasktool create view api.account
        - Check we're in an app and load app yaml.
        - Default view imports in app.yaml
        - Create tests.views.test_account.py

    flasktool create view api.account
        - Check we're in an app and load app yaml.

    flasktool create model Account
        - Check we're in an app and load app yaml.
        - Create models.account.py.
        - Create tests.models.account.py
    """
    what = what[0]
    name = name[0]
    if what == 'app':
        _app = FlaskApplication(name, layout=layout)
        _app.bootstrap()

        print whatnext % {'name':name}
    
    elif what == 'ext':
        if not url:
            url = prompt('URL')
        
        if not author_name:
            author_name = prompt('Author Name')
        
        if not author_email:
            author_email = prompt('Author Email')
        
        license = prompt_choices('License', ('BSD','MIT','WTFPL'), 
            default='BSD', resolve=string.upper)
            
        if not short_description:
            short_description = prompt('Short Description')
        
        if not requires:
            requires = prompt('Dependencies (comma separated, exclude Flask)')
            
        extension = FlaskExtension(name, url, author_name, author_email, 
            short_description, requires, license)

        print "###################"
        print "Makin' the donuts..."
        print "###################"
        extension.boostrap()
        print "###################"
        print "Flask-%s created in %s" % (extension.name, extension.dir)
        print "###################"


@manager.option(nargs=1, dest='name',help='name of the app/directory')
def next(what='app', name='MyAwesomeApp'):
    """help for what to do next on <yourapp>"""
    print whatnext % {'name':name[0]} 


def run():
    manager.run()

if __name__ == '__main__':
    run()
