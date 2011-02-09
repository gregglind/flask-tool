import os
from flask import Flask
import settings
import models

def create_app(environment=None):
    app = Flask('{{app.package_name}}')

    # Config app for environment
    if not environment:
        environment = os.environ.get('{{app.environment_var}}', 'Dev')

    app.config.from_object('{{app.package_name}}.settings.%s' % environment)

    # Init models
    models.init(app)

    # Import modules
    {% for module_name in app.module_names %}
    from {{app.package_name}}.views.{{module_name}} import {{module_name}}
    {% endfor %}
    
    # Register modules with app
    {% for module_name in app.module_names %}
    app.register_module({{module_name}})
    {% endfor %}
    
    return app
