from .user import User
from elric import db
import datetime

class Version(db.Model):
    __tablename__ = 'versions'
    __table_args__ = {'mysql_engine': 'InnoDB'}

    id = db.Column(db.Integer, primary_key=True)
    # TODO: how to get the user from a version object, currently it is just user id not user object
    user = db.Column(db.Integer, db.ForeignKey(User.id))
    datetime = db.Column(db.DateTime, default=datetime.datetime.utcnow())
    version = db.Column(db.String(64))
    
    entities = db.relationship('Entity')
    events = db.relationship('Event')
    entity_categories = db.relationship('EntityCategory')
    event_categories = db.relationship('EventCategory')

    def __init__(self, user, version):
        self.user = user
        self.version = version

    def __repr__(self):
        return "<Version(user='%s', version='%s')>" % self.user.username, self.version