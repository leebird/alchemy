from .version import Version
from .document import Document
from .event_category import EventCategory
from elric import db

class Event(db.Model):
    __tablename__ = 'events'
    __table_args__ = {'mysql_engine': 'InnoDB'}

    id = db.Column(db.Integer, primary_key=True)
    document = db.Column(db.Integer, db.ForeignKey(Document.id))
    category = db.Column(db.Integer, db.ForeignKey(EventCategory.id))
    arguments_entity = db.relationship('ArgumentEntity')
    arguments_event = db.relationship('ArgumentEvent', foreign_keys="ArgumentEvent.event")
    properties = db.relationship('EventProperty')
    version = db.Column(db.Integer, db.ForeignKey(Version.id))

    def __repr__(self):
        return "<Entity(category='%s', start='%s', end='%s', text='%s')>" % (
            self.category, self.start, self.end, self.text)