from __future__ import absolute_import 

from .extensions import FlaskExtension
from flaskext.script import prompt, prompt_choices

def flaskext_create():
    name = prompt('Extension Name: (ie CouchDBKit)')
    url = prompt('URL:')
    author_name = prompt('Author Name:')
    author_email = prompt('Author Email:')
    license = prompt_choices('License:', ['BSD','MIT','WTFPL'], 'BSD')
    short_description = prompt('Short Description:')
    deps = prompt('Dependencies: (comma separated, exclude Flask)')
    extension = FlaskExtension(name, url, author_name, author_email, 
        short_description, deps, license)
        
    extension.boostrap()

def run():
    flaskext_create()

if __name__ == '__main__':
    run()