from .version import Version
from .argument_role import ArgumentRole
from .event import Event
from elric import db

class ArgumentEvent(db.Model):
    __tablename__ = 'arguments_event'
    __table_args__ = {'mysql_engine': 'InnoDB'}

    id = db.Column(db.Integer, primary_key=True)
    role = db.Column(db.Integer, db.ForeignKey(ArgumentRole.id), nullable=False)
    event = db.Column(db.Integer, db.ForeignKey(Event.id), nullable=False)
    argument = db.Column(db.Integer, db.ForeignKey(Event.id), nullable=False)
    version = db.Column(db.Integer, db.ForeignKey(Version.id))

    def __repr__(self):
        return "<Entity(category='%s', start='%s', end='%s', text='%s')>" % (
            self.category, self.start, self.end, self.text)