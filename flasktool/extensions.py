from __future__ import absolute_import

from .util import _mkdir, _cd, _create_file

DEFAULT_CLASSIFIERS = ['Environment :: Web Environment',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: BSD License',
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
            for d in ['docs', 'examples']:
                _mkdir(d)
        
            # Make setup.py
            _create_file('setup.py', 'setup.py.tpl', extension=self)
            
            # Make readme
            _create_file('README.md', 'README.md.tpl', extension=self)
        
            # Make __init__
            _create_file('flaskext/__init__.py', '__init__.py.tpl', extension=self)
        
            # Make module
            _create_file('flaskext/%s.py' % self.module_name)
            
            # Make test suite
            _create_file('%s.py' % self.test_suite, 'test_suite.py.tpl', extension=self)
            
            # Make docs assets
            # @todo (lucas) See sphinx/quickstart.  Setup docs w Sphinx then copy in Flask templates. 