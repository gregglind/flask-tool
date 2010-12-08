from os import environ
from os.path import dirname
from pkgutil import iter_modules

from flask import Flask
import settings
import models
import util

def create_app(environment=None):
    app = Flask('{{app.package_name}}')

    # Config app for environment
    if not environment:
        environment = environ.get(environment_var, 'Dev')
    app.config.from_object('settings.%s' % environment)

    # Init models
    models.init(app)

    # Wire modules to app
    pkg_path = dirname('views')
    for module_name in [name for _, name, _ in iter_modules([pkg_path])]:
        qualified_name = '%s.views.%s' % (app.logger_name, module_name)
        module = __import__(qualified_name)
        app.register_module(fgetattr(module, module_name))

    return app
