__author__ = 'anthonymcclay'
__project__ = 'FlaskWebServices'
__date__ = '6/14/17'
__revision__ = '$'
__revision_date__ = '$'

from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from models import db
from run import app

migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()

