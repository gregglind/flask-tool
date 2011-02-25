# Flask Tool 
Tooling for Flask.

## Install

    pip install -e git+git://github.com/imlucas/flask-tool#egg=flasktool


## Create a new extension skeleton
Creates setup.py, flaskext.__init__.py, test suite, readme, and sets up gitignore.

    flasktool create ext

## Create a new app

All apps created with flasktool come with a ton of stuff for free.
All you have to do is write your app, write some tests, change a few settings
in your fabfile and hit `fab deploy`

Some of the things included are:

* Default templates with HTML5 Boilerplate included
* Ready to go manage.py that uses the excellent Flask-Script package
* Supervisord config to run your app on uwsgi
* Nginx config and required dependencies
* Pre built fabfile for deployment on ec2 via Fabric
* Default .gitignore for .DS_Store, *.pyc and supervisord logs
* Base requirements.txt

To create an app using the factory pattern (currently being updated with more hotness):

    flasktool create app MyApp

To create a simple app (models, views, etc in a single app.py):

    flasktool create app MyApp --layout=simple

Check out exampleappsimple/ to see what you get just from this one command.