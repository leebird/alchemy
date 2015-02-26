from db.base import Base
from db.version import Version
from sqlalchemy import Column, Integer, String, ForeignKey


class Category(Base):
    __tablename__ = 'events'
    __table_args__ = {'mysql_engine': 'InnoDB'}

    id = Column(Integer, primary_key=True)
    category = Column(String(20))
    owner = Column(String(10))
    version = Column(Integer, ForeignKey(Version.id))

    def __repr__(self):
        return "<Entity(category='%s', start='%s', end='%s', text='%s')>" % (
            self.category, self.start, self.end, self.text)