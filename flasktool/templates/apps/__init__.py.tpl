from os import environ
from os.path import dirname
from pkgutil import iter_modules

from flask import Flask
import settings
import models

def create_app(environment=None):
    app = Flask('{{app.package_name}}')

    # Config app for environment
    if not environment:
        environment = environ.get('{{app.environment_var}}', 'Dev')
    app.config.from_object('{{app.package_name}}.settings.%s' % environment)

    # Init models
    models.init(app)

    # Wire modules to app
    from {{app.package_name}}.views.api import api
    from {{app.package_name}}.views.main import main
    
    app.register_module(api)
    app.register_module(main)
    
    return app
