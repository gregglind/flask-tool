from __future__ import absolute_import
from __future__ import with_statement

from os.path import exists, isfile, join
from contextlib import closing
from subprocess import Popen
from shutil import copytree

from .util import _mkdir, _cd, _create_file, tool_path

class FlaskApplication(object):
    def __init__(self, name):
        self.name = name
        self.package_name = name.lower()
        self.dir = name.lower()
        self.environment_var = '%s_ENVIRONMENT' % name.upper()
        self.module_names = ['api', 'main']
        
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
            
                _create_file('settings.py', 'apps/settings.py.tpl', app=self)
            
                # Create models
                _create_file('models.py', 'apps/models.py.tpl', app=self)
                
                # Create static
                copytree(join(tool_path, 'templates/apps/static'), 'static')    
                
                # Create templates
                copytree(join(tool_path, 'templates/apps/templates'), 'templates')    

                # Create views
                _mkdir('views')
                with _cd('views'):
                    _create_file('__init__.py', 'apps/views/__init__.py.tpl', app=self)
                    for module_name in self.module_names:
                        _create_file('%s.py' % module_name, 'apps/views/module.py.tpl', app=self, module_name=module_name)
        
        
        
        
