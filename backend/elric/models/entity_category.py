from elric import db
from .version import Version
from sqlalchemy import Column, Integer, String, ForeignKey


class EntityCategory(db.Model):
    __tablename__ = 'entity_category'
    __table_args__ = {'mysql_engine': 'InnoDB'}

    id = Column(Integer, primary_key=True)
    category = Column(String(20))
    version = Column(Integer, ForeignKey(Version.id))

    def __repr__(self):
        return "<Entity Category (category='%s')>" % self.category