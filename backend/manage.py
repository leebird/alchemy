
"""
  Usage:
    manage.py serve
    manage.py create_db
    manage.py drop_db
"""


def serve(app):
    """start to serve the
    :type app: flask.Flask
    """
    app.run(host='127.0.0.1', port=3456, debug=True)


if __name__ == '__main__':
    from docopt import docopt
    from elric import create_app

    args = docopt(__doc__)
    app = create_app()
    if args['serve']:
        serve(app)
    else:
        print(args)