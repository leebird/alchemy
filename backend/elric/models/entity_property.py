from elric import db
from sqlalchemy import Column, Integer, String, ForeignKey
from .entity import Entity


class EntityProperty(db.Model):
    """key-value property pairs for entity or event
    """
    __tablename__ = 'properties'
    __table_args__ = {'mysql_engine': 'InnoDB'}

    id = Column(Integer, primary_key=True)
    label = Column(String(40))
    value = Column(String(40))
    entity = Column(ForeignKey(Entity.id), nullable=False)

    def __repr__(self):
        return "<Entity Property(key='%s', value='%s')>" % self.key, self.value