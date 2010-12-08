from __future__ import absolute_import
from __future__ import with_statement

from os.path import exists, isfile, join
from contextlib import closing
from subprocess import Popen

from .util import _mkdir, _cd, _create_file

class FlaskApplication(object):
    def __init__(self, name):
        self.name = name
        self.package_name = name.lower()
        self.dir = name.lower()
        self.environment_var = '%s_ENVIRONMENT' % name.upper()
        
    def bootstrap(self):
        _mkdir(self.dir)
        with _cd(self.dir):
            # Create requirements file
            _create_file('requirements.txt', 'apps/requirements.txt.tpl')
            
            # Create manage.py
            _create_file('manage.py', 'apps/manage.py.tpl', app=self)
            
            # Create tests
            _create_file('tests.py', 'apps/tests.py.tpl', app=self)
            
            
            _mkdir(self.package_name)
            with _cd(self.package_name):
                # Create __init__
                _create_file('__init__.py', 'apps/__init__.py.tpl', app=self)
                
                # Create models
                _create_file('models.py', 'apps/models.py.tpl', app=self)
                
                # Create views
                _mkdir('views')
                with _cd('views'):
                    _create_file('__init__.py', 'apps/views/__init__.py.tpl', app=self)
                    _create_file('api.py', 'apps/views/api.py.tpl', app=self)
                    _create_file('main.py', 'apps/views/main.py.tpl', app=self)
        
        
        
        
