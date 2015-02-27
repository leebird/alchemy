from db.base import Base
from db.version import Version
from sqlalchemy import Column, Integer, String, ForeignKey


class EventCategory(Base):
    __tablename__ = 'event_category'
    __table_args__ = {'mysql_engine': 'InnoDB'}

    id = Column(Integer, primary_key=True)
    category = Column(String(20))
    version = Column(Integer, ForeignKey(Version.id))

    def __repr__(self):
        return "<Event Category(category='%s')>" % self.category