from .version import Version
from .argument_role import ArgumentRole
from .event import Event
from sqlalchemy import Column, Integer, String, Text, ForeignKey
from sqlalchemy.orm import relationship
from elric import db

class ArgumentEvent(db.Model):
    __tablename__ = 'arguments'
    __table_args__ = {'mysql_engine': 'InnoDB'}

    id = Column(Integer, primary_key=True)
    role = Column(Integer, ForeignKey(ArgumentRole.id), nullable=False)
    event = Column(Integer, ForeignKey(Event.id), nullable=False)
    argument = Column(Integer, ForeignKey(Event.id), nullable=False)
    version = Column(Integer, ForeignKey(Version.id))

    def __repr__(self):
        return "<Entity(category='%s', start='%s', end='%s', text='%s')>" % (
            self.category, self.start, self.end, self.text)