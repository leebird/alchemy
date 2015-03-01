from flask import jsonify
from flask.ext.restful import reqparse, abort, Api, Resource
from elric import db
from elric.models.user import User


class UserAuthAPI(Resource):
    def get(self):
        return jsonify({1: [], 2: []})

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('username', type=str)
        parser.add_argument('password', type=str)
        args = parser.parse_args()

        username = args.get('username')
        password = args.get('password')

        if username is None or password is None:
            abort(400, message='username or password is null')

        user = User.query.filter_by(username=username).first()

        # user already exsits
        if user is not None:
            abort(200, message='user exists')
        else:
            # add new user
            user = User(username, password)
            db.session.add(user)
            db.session.commit()

        return jsonify({'create_user': True})
