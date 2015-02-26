from db.base import Base
from db.version import Version
from db.category import Category
from sqlalchemy import Column, Integer, String, Text, ForeignKey
from sqlalchemy.orm import relationship

class Entity(Base):
    __tablename__ = 'entities'
    __table_args__ = {'mysql_engine': 'InnoDB'}

    id = Column(Integer, primary_key=True)
    document = Column(String(40))
    category = Column(Integer, ForeignKey(Category.id))
    start = Column(Integer)
    end = Column(Integer)
    text = Column(Text)
    properties = relationship('Property')
    version = Column(Integer, ForeignKey(Version.id))

    def __repr__(self):
        return "<Entity(category='%s', start='%s', end='%s', text='%s')>" % (
            self.category, self.start, self.end, self.text)