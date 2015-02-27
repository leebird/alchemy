from db.base import Base
from db.version import Version
from db.document import Document
from db.event_category import EventCategory
from sqlalchemy import Column, Integer, ForeignKey, Table
from sqlalchemy.orm import relationship

association_table = Table('association', Base.metadata,
                          Column('event_id', Integer, ForeignKey('left.id')),
                          Column('entity_id', Integer, ForeignKey('right.id'))
)

class Event(Base):
    __tablename__ = 'events'
    __table_args__ = {'mysql_engine': 'InnoDB'}

    id = Column(Integer, primary_key=True)
    document = Column(Integer, ForeignKey(Document.id))
    category = Column(Integer, ForeignKey(EventCategory.id))
    arguments_entity = relationship('ArgumentEntity')
    arguments_event = relationship('ArgumentEvent')
    properties = relationship('EventProperty')
    version = Column(Integer, ForeignKey(Version.id))

    def __repr__(self):
        return "<Entity(category='%s', start='%s', end='%s', text='%s')>" % (
            self.category, self.start, self.end, self.text)