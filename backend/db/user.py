from db.base import Base
from sqlalchemy import Column, Integer, String

class User(Base):
    __tablename__ = 'users'
    __table_args__ = {'mysql_engine': 'InnoDB'}
    
    id = Column(Integer, primary_key=True)
    name = Column(String(20))

    def __repr__(self):
        return "<User(name='%s')>" % self.name