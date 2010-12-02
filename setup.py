from setuptools import setup
"""
`flasktool create ext`
    Console prompts to create a skeleton for a new extension.
"""

setup(
    name='Flask-Tool',
    version='0.1',
    url='http://imlucas.com/',
    license='BSD',
    author='Lucas Hrabovsky',
    author_email='hrabovsky.lucas@gmail.com',
    description='Some tooling for developing with flask.',
    long_description=__doc__,
    packages=['flaskext'],
    namespace_packages=['flaskext'],
    zip_safe=False,
    platforms='any',
    install_requires=[
        'Flask',
        'Flask-Script',
        'Jinja2'
    ],
    test_suite='test_tool',
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ],
    entry_points = {
        'console_scripts': [
            'flasktool = flasktool:console'
        ],
    }
)

