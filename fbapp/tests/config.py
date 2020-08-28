import os
# To generate a new secret key:
#import random, string
#"".join([random.choice(string.printable) for _ in range(24)])
SECRET_KEY = '8S"6R\tPW\tPt</6p&8+k">Y/A'

# Remplacez par l'id de l'app TEST que vous avez créée précédemment.
FB_APP_ID = 230849604942548

basedir = os.path.abspath(os.path.dirname(__file__))

# Nouvelle base de données pour les tests.
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app_test.db')

# Active le debogueur
DEBUG = True
TESTING = True
LIVESERVER_PORT = 8943
LIVESERVER_TIMEOUT = 10

# Facebook test user
FB_USER_NAME = "Barbara "
FB_USER_PW = "demoniark"
FB_USER_EMAIL = "barbara_lvjfspl_carrierostein@tfbnw.net"
FB_USER_ID = 106722641159052
FB_USER_GENDER = 'undefined'