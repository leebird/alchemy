from .event import Event
from elric import db

class EventProperty(db.Model):
    """key-value property pairs for entity or event
    """
    __tablename__ = 'event_properties'
    __table_args__ = {'mysql_engine': 'InnoDB'}

    id = db.Column(db.Integer, primary_key=True)
    label = db.Column(db.String(64))
    value = db.Column(db.String(64))
    event = db.Column(db.ForeignKey(Event.id), nullable=False)

    def __repr__(self):
        return "<Event Property(key='%s', value='%s')>" % self.key, self.value