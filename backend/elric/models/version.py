from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from .user import User
from .entity import Entity
from .event import Event
from .category import Category
from elric import db

class Version(db.Model):
    __tablename__ = 'versions'
    __table_args__ = {'mysql_engine': 'InnoDB'}

    id = Column(Integer, primary_key=True)
    user = Column(Integer, ForeignKey(User.id))
    version = Column(String(50))
    
    entities = relationship('Entity')
    events = relationship('Event')
    categories = relationship('Category')
    
    def __repr__(self):
        return "<Version(name='%s', version='%s')>" % self.name, self.version