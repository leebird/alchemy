from sqlalchemy import Column, Integer, String, ForeignKey
from db.base import Base
from db.entity import Entity
from db.event import Event


class Property(Base):
    """key-value property pairs for entity or event
    """
    __tablename__ = 'properties'
    __table_args__ = {'mysql_engine': 'InnoDB'}

    id = Column(Integer, primary_key=True)
    label = Column(String(40))
    value = Column(String(40))
    entity = Column(ForeignKey(Entity.id))
    event = Column(ForeignKey(Event.id))

    def __repr__(self):
        return "<Property(key='%s', value='%s')>" % self.key, self.value