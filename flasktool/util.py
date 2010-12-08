from __future__ import absolute_import

from os import mkdir, chdir, getcwd
from os.path import dirname, abspath, join
from subprocess import Popen, STDOUT
from jinja2 import Environment, FileSystemLoader
from contextlib import contextmanager, closing

tool_path = abspath(dirname(__file__))
jinja_env = Environment(loader=FileSystemLoader(join(tool_path, 'templates')))


@contextmanager
def _cd(path):
    original_wd = getcwd()
    chdir(path)
    yield
    chdir(original_wd)


def _local(cmd, cwd=getcwd()):
    print "Executing: `%s` from `%s`" % (cmd, cwd)
    p = Popen(cmd, shell=True, cwd=cwd, stderr=STDOUT)
    if (p.wait() != 0):
        raise Exception('Error executing: %s' % (cmd))


def _mkdir(d):
    full_path = abspath(d)
    try:
        print "Creating %s directory %s" % (d, full_path)
        mkdir(d)
        return True
    except OSError, e:
        if e.errno != 17:
            raise e
        print "** %s directory already exists" % d
        return False


def _create_file(dest, tpl=None, **ctx):
    print "Creating %s at %s" % (dest, abspath(dest))
    _contents = jinja_env.get_template(tpl).render(**ctx) if tpl else ''
    with closing(open(dest, 'w')) as fp:
        fp.write(_contents)
