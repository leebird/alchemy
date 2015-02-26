from db.base import Base
from db.version import Version
from db.category import Category
from sqlalchemy import Column, Integer, String, ForeignKey, Table
from sqlalchemy.orm import relationship

association_table = Table('association', Base.metadata,
                          Column('event_id', Integer, ForeignKey('left.id')),
                          Column('entity_id', Integer, ForeignKey('right.id'))
)

class Event(Base):
    __tablename__ = 'events'
    __table_args__ = {'mysql_engine': 'InnoDB'}

    id = Column(Integer, primary_key=True)
    document = Column(String(40))
    category = Column(Integer, ForeignKey(Category.id))
    arguments = Column(50)
    properties = relationship('Property')
    version = Column(Integer, ForeignKey(Version.id))

    def __repr__(self):
        return "<Entity(category='%s', start='%s', end='%s', text='%s')>" % (
            self.category, self.start, self.end, self.text)