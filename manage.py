import os
from logging import FileHandler, Formatter

import logging
from flask_script import Manager

from api.main import create_app

app = create_app(os.getenv('BOILERPLATE_ENV') or 'dev')

app.app_context().push()

manager = Manager(app)


@manager.command
def run():
    file_handler = FileHandler('app.log')
    file_handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(
        Formatter('%(asctime)s %(levelname)s : %(message)s'))
    app.logger.addHandler(file_handler)
    app.run()


if __name__ == '__main__':
    manager.run()
