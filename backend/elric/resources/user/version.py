from flask import jsonify
from flask.ext.restful import reqparse, abort, Api, Resource
from elric import db
from elric.models.user import User
from elric.models.version import Version


class VersionAPI(Resource):
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('username', type=str)
        parser.add_argument('version', type=str)
        args = parser.parse_args()
        
        username = args.get('username')
        version = args.get('version')
        
        user = User.query.filter_by(username=username).first()
        
        if user is None:
            abort(400, message='user not exists')
        
        if version is None:
            abort(400, message='version cannot be null')
        
        curr_version = Version.query.filter_by(user=user.id, version=version).first()
        
        if curr_version is None:
            abort(400, message='version not exists for the user %s' % username)
        
        return jsonify({'version': curr_version.version})

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('username', type=str)
        parser.add_argument('password', type=str)
        parser.add_argument('version', type=str)
        args = parser.parse_args()

        username = args.get('username')
        password = args.get('password')
        version = args.get('version')

        if username is None or password is None or version is None:
            abort(400, message='username, password or version is null')

        user = User.query.filter_by(username=username, password=password).first()

        # user already exsits
        curr_version = None
        if user is None:
            abort(400, message='username or password invalid')
        else:
            # retrieve version
            curr_version = Version.query.filter_by(user=user.id, version=version).first()
            if curr_version is None:
                curr_version = Version(user=user, version=version)
                db.session.add(curr_version)
                db.session.commit()

        return jsonify({'version': curr_version.version})
