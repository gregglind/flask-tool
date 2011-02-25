CSRF_SECRET_KEY = ''
SESSION_KEY = ''

class _Config(object):
    DEBUG = True
    TESTING = False
    DATABASE_URI = 'sqlite://:memory:'
    SECRET_KEY = CSRF_SECRET_KEY
    CSRF_SESSION_LKEY = SESSION_KEY
    CSRF_ENABLED = True

class Prod(_Config):
    DATABASE_URI = ''
    DEBUG = False
    TESTING = False

class Dev(_Config):
    NAME = "Dev"
    DEBUG = True
    DATABASE_URI = ''
    
    
class Testing(_Config):
    TESTING = True