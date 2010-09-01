import sys
from os.path import dirname, abspath, join
TEST_DIR = dirname(abspath(__file__))

DEBUG = True

ROOT_URLCONF = 'urls'

DATABASE_ENGINE = 'sqlite3'
DATABASE_NAME = 'tests.db'
 
INSTALLED_APPS = [
    'core',
]