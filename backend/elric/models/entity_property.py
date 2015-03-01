from elric import db
from .entity import Entity


class EntityProperty(db.Model):
    """key-value property pairs for entity or event
    """
    __tablename__ = 'entity_properties'
    __table_args__ = {'mysql_engine': 'InnoDB'}

    id = db.Column(db.Integer, primary_key=True)
    label = db.Column(db.String(64))
    value = db.Column(db.String(64))
    entity = db.Column(db.ForeignKey(Entity.id), nullable=False)

    def __repr__(self):
        return "<Entity Property(key='%s', value='%s')>" % self.key, self.value