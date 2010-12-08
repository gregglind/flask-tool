from __future__ import absolute_import
from __future__ import with_statement

from os.path import exists, isfile, join
import datetime
from contextlib import closing
from subprocess import Popen

from .util import _mkdir, _cd, _create_file

DEFAULT_CLASSIFIERS = ['Environment :: Web Environment',
    'Intended Audience :: Developers',
    'Operating System :: OS Independent',
    'Programming Language :: Python',
    'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    'Topic :: Software Development :: Libraries :: Python Modules']


class FlaskExtension(object):

    def __init__(self, name, url, author_name, author_email,
        short_description, deps_csv_string, license):
        self.name = name
        self.url = url
        self.author_name = author_name
        self.author_email = author_email
        self.short_description = short_description
        self.deps = ['Flask']
        self.deps.extend(map(lambda x: x.strip(), deps_csv_string.split(',')))

        self.classifiers = DEFAULT_CLASSIFIERS
        self.module_name = self.name.lower()
        self.test_suite = 'test_%s' % self.module_name
        self.dir = 'flask-%s' % self.module_name
        self.license = license

    def boostrap(self):
        # Make dirs
        _mkdir(self.dir)
        with _cd(self.dir):
            for d in ['docs', 'examples', 'flaskext', 'docs/_themes']:
                _mkdir(d)

            # Make gitignore
            _create_file('.gitignore', '.gitignore.tpl', extension=self)

            # Make setup.py
            _create_file('setup.py', 'setup.py.tpl', extension=self)

            # Make readme
            _create_file('README.md', 'README.md.tpl', extension=self)

            # Make __init__
            _create_file('flaskext/__init__.py',
                'extensions/__init__.py.tpl', extension=self)

            # Make module
            if not exists('flaskext/%s.py' % self.module_name):
                _create_file('flaskext/%s.py' % self.module_name)

            # Make test suite
            _create_file('%s.py' % self.test_suite,
                'extensions/test_suite.py.tpl', extension=self)

            # Make license
            _create_file('LICENSE', 'licenses/%s.tpl' % (self.license),
                year=datetime.datetime.today().year, author_name=self.author_name)
                
            # Make docs
            with _cd('docs'):
                # From the original extension wizard
                # https://github.com/mitsuhiko/flask-extension-wizard/blob/master/make-flaskext.py
                Popen(['sphinx-quickstart']).wait()
                if isfile(join('source', 'conf.py')):
                    sphinx_conf_py = join('source', 'conf.py')
                else:
                    sphinx_conf_py = join('conf.py')
                    
                with closing(open(sphinx_conf_py, 'r')) as f:
                    config = f.read().splitlines()
                    for idx, line in enumerate(config):
                        if line.startswith('#sys.path.append'):
                            config[idx] = "sys.path.append(os.path.abspath('_themes'))"
                        elif line.startswith('html_theme ='):
                            config[idx] = 'html_theme = flask'
                        elif line == '#html_theme_path = []':
                            config[idx] = "html_theme_path = ['_themes']"
                        elif line.startswith('pygments_style ='):
                            config[idx] = "#pygments_style = 'sphinx'"
                with closing(open(sphinx_conf_py, 'w')) as f:
                    f.write('\n'.join(config))
                
                # Get flask themes
                with _cd('_themes'):
                    Popen("wget http://download.github.com/mitsuhiko-flask-sphinx-themes-3d964b6.tar.gz").wait() 
                    Popen("tar -zxvf  mitsuhiko-flask-sphinx-themes-3d964b6.tar.gz --strip 1").wait()
