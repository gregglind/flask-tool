from __future__ import absolute_import
from __future__ import with_statement

from os.path import exists, isfile, join
from os import chmod, remove, removedirs
from contextlib import closing
from subprocess import Popen
from shutil import copytree
import stat

from .util import _mkdir, _cd, _create_file, tool_path

class FlaskApplication(object):
    def __init__(self, name, layout='factory', wsgi_server='uwsgi'):
        self.name = name
        self.layout = layout
        self.package_name = name.lower()
        self.dir = name.lower()
        self.environment_var = '%s_ENVIRONMENT' % name.upper()
        self.module_names = ['api', 'main']
        self.wsgi_server = wsgi_server

        
    def bootstrap(self):
        if self.layout == 'factory':
            return self._bootstrap_factory_app()
        
        elif self.layout == 'heavy':
            return self._bootstrap_heavy_factory_app()
 
        return self._bootstrap_simple_app()
    
    def _bootstrap_simple_app(self):
        self.callable = '%s'
        _mkdir(self.dir)
        with _cd(self.dir):

            dirs_to_make = ['logs', 'tmp', 'etc']
            for d in dirs_to_make:
                _mkdir(d)

            files_to_create = [
            ('requirements.txt', 'apps/requirements.txt.tpl'),
            ('tests.py', 'apps/tests.py.tpl'),
            ('logs/placeholder', 'placeholder.tpl'),
            ('etc/placeholder', 'placeholder.tpl'),
            ('tmp/placeholder', 'placeholder.tpl'),
            ('supervisord.conf', 'apps/supervisord.conf.tpl'),
            ('etc/mime.types', 'apps/mime_types.tpl'),
            ('etc/uwsgi_params', 'apps/uwsgi_params.tpl'),
            ('etc/nginx.conf', 'apps/nginx.conf.tpl'),
            ('app.py', 'apps/app.py.tpl'),
            ('fabfile.py', 'apps/fabfile.py.tpl'),
            ('manage.py', 'apps/manage.py.tpl'),
            ('app.yaml', 'apps/app.yaml.tpl'),
            ('.gitignore', 'apps/gitignore.tpl'),
            ('settings.py', 'apps/settings.py.tpl'),]

            dirs_to_copy = [('templates/apps/static', 'static'),
            ('templates/apps/templates','templates')]

            for name, tpl in files_to_create:
                _create_file(name, tpl, app=self)    
            
            for _dir, dest in dirs_to_copy:
                copytree(join(tool_path, _dir), dest)
            
            chmod('manage.py', 0755)

    def _bootstrap_factory_app(self):
        self.callable = '%s:uwsgi'

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

    def _bootstrap_heavy_factory_app(self):
        # it's a normal factory app, with extra!
        self._bootstrap_factory_app()

        self.callable = '%s:uwsgi'
        
        with _cd(self.dir):
            with _cd(self.package_name):
                _mkdir('utils')
                _mkdir('apis')
                _mkdir('adhoc')
                _mkdir('tests')
                _mkdir('docs')

                with _cd('tests'):
                    # Create tests
                    _create_file('tests.py', 'apps/tests.py.tpl', app=self)

        with _cd(self.dir):
            # Create requirements file
            _create_file('requirements.txt', 'apps/requirements.txt.heavy.tpl')

            # remove test file, directory is better
            remove('tests.py')

