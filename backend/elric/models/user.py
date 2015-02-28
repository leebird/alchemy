from sqlalchemy import Column, Integer, String
from elric import db

class User(db.Model):
    __tablename__ = 'users'
    __table_args__ = {'mysql_engine': 'InnoDB'}
    
    id = Column(Integer, primary_key=True)
    name = Column(String(20))

    def __repr__(self):
        return "<User(name='%s')>" % self.name