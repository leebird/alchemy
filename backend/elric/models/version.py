from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from db.base import Base
from db.user import User
from db.entity import Entity
from db.event import Event
from db.category import Category

class Version(Base):
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