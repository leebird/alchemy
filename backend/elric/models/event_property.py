from sqlalchemy import Column, Integer, String, ForeignKey
from .event import Event
from elric import db

class EventProperty(db.Model):
    """key-value property pairs for entity or event
    """
    __tablename__ = 'properties'
    __table_args__ = {'mysql_engine': 'InnoDB'}

    id = Column(Integer, primary_key=True)
    label = Column(String(40))
    value = Column(String(40))
    event = Column(ForeignKey(Event.id), nullable=False)

    def __repr__(self):
        return "<Event Property(key='%s', value='%s')>" % self.key, self.value