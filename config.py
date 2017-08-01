import os

basedir = os.path.abspath(os.path.dirname(__file__))

# forms
WTF_CSRF_ENABLED = True

# database
SQLALCHEMY_DATABASE_URI = 'postgres://postgres:postgres@localhost/microblog'
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db', 'db_repository')
SQLALCHEMY_TRACK_MODIFICATIONS = True

# pagination
POSTS_PER_PAGE = 3

TEMPLATE_PATH = os.path.join(basedir, 'templates')
STATIC_PATH = os.path.join(basedir, 'static')

secret_key = b'\x19)z\x94\xa8[\xd1?x\xca\xb5\x1e\xfb\x80N\xd1\xf9@\xc9\xdeAw/`\xbb\x1bA3-rM\x96'


