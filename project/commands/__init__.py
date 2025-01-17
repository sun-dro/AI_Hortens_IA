from project import create_app
from flask_script import Manager
from flask_migrate import MigrateCommand
from .db_init import InitDbCommand


manager = Manager(create_app())

manager.add_command('db', MigrateCommand)
manager.add_command('db_init', InitDbCommand)
