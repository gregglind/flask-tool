from setuptools import setup

setup(
    name='Flask-{{extension.name}}',
    version='0.1',
    url='{{extension.url}}',
    license='{{extension.license}}',
    author='{{extension.author_name}}',
    author_email='{{extension.author_email}}',
    description='{{extension.short_description}}',
    long_description=__doc__,
    packages=['flaskext'],
    namespace_packages=['flaskext'],
    zip_safe=False,
    platforms='any',
    install_requires=[{% for dep in extension.deps %}
        '{{dep}}'{% if not loop.last %},{% endif %}{% endfor %}
    ],
    test_suite='{{extension.test_suite}}',
    classifiers=[{% for classifier in extension.classifiers %}
        '{{classifier}}'{% if not loop.last %},{% endif %}{% endfor %}
    ]
)