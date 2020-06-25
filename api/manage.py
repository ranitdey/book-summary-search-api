import os

from flask_script import Manager
from flask import g


from api.main import create_app
from core_search.search import Search

app = create_app(os.getenv('BOILERPLATE_ENV') or 'dev')


app.app_context().push()

manager = Manager(app)


@manager.command
def run():
    app.run()


if __name__ == '__main__':
    manager.run()