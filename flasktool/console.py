from __future__ import absolute_import 


from .extensions import FlaskExtension
from flask import Flask
from flaskext.script import prompt, prompt_choices, Manager
import string


def create_app(*args, **kwargs):
        app = Flask(__name__)
        return app

manager = Manager(create_app, False)
    
@manager.option('--name', dest='name', required=False)
@manager.option('--url', dest='url', required=False)
@manager.option('--authorname', dest='author_name', required=False)
@manager.option('--authoremail', dest='author_email', required=False)
@manager.option('--license', dest='license', required=False,
    help="BSD, MIT, or WTFPL", default="BSD")
@manager.option('--requires', dest='requires', required=False,
    help="Comma separated list of required packages")
@manager.option('--description', dest='author_email', required=False)
def create_ext(name=None, url=None, author_name=None, author_email=None, 
    license='BSD', requires=None, short_description=None):
    """
    Create the skeleton of a new Flask Extension.
    
    `flasktool create_ext`
    `flasktool create_ext --name=MyExtension`
    `flasktool create_ext --name=MyExtension --url=http://imlucas.com/flask-myextension`
    `flasktool create_ext --name=MyExtension --authorname="Lucas"`
    """
    if not name:
        name = prompt('Extension Name: (ie CouchDBKit)')
    
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

def run():
    manager.run()

if __name__ == '__main__':
    run()