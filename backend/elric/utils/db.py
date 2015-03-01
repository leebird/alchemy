# CREATE DATABASE alchemy
# DEFAULT CHARACTER SET utf8
# DEFAULT COLLATE utf8_unicode_ci;
"""
  Usage:
    db.py create_db
    db.py drop_db
    db.py create_table <table>
    db.py drop_table <table>
"""
from flask import Flask

from elric import db


def create_db(app: Flask):
    with app.app_context():
        # only valid if the user is superuser
        #db.session.execute("CREATE EXTENSION IF NOT EXISTS hstore;")
        # db.session.commit()
        db.create_all()


def drop_db(app: Flask):
    with app.app_context():
        db.drop_all(app=app)
        db.session.commit()


def create_table(app: Flask, table):
    # to create a single table, use following
    with app.app_context():
        db.metadata.tables[table].create(db.engine)


def drop_table(app: Flask, table):
    with app.app_context():
        db.metadata.tables[table].drop(db.engine)


def ask_for_confirmation() -> bool:
    from random import randint
    confirmation = str(randint(0, 100))
    if input('you are about to perform a dangerous task, are you sure what you are doing?\n' +
                    'enter %s if you are sure, or press enter to cancel.\n' % confirmation) == confirmation:
        print('mission confirmed')
        return True
    else:
        print('mission canceled')
        return False


if __name__ == '__main__':
    from docopt import docopt
    from elric import create_app

    args = docopt(__doc__)
    app = create_app()
    if args['create_db']:
        create_db(app)
    elif args['drop_db']:
        if ask_for_confirmation():
            drop_db(app)
    elif args['create_table']:
        create_table(app, args['<table>'])
    elif args['drop_table']:
        if ask_for_confirmation():
            drop_table(app, args['<table>'])
    else:
        print(args)
