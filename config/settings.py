from datetime import timedelta

DEBUG = True

SERVER_NAME = 'localhost:8000'
SECRET_KEY = 'insecurekeyfordev'

# SQLAlchemy.
db_uri = 'postgresql://pierre:devpassword@postgres:5432/captur'
SQLALCHEMY_DATABASE_URI = db_uri
SQLALCHEMY_TRACK_MODIFICATIONS = False

# User.
SEED_ADMIN_EMAIL = 'dev@local.host'
SEED_ADMIN_PASSWORD = 'devpassword'
REMEMBER_COOKIE_DURATION = timedelta(days=90)
