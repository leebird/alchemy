from elric import db
from .version import Version


class EntityCategory(db.Model):
    __tablename__ = 'entity_category'
    __table_args__ = {'mysql_engine': 'InnoDB'}

    id = db.Column(db.Integer, primary_key=True)
    category = db.Column(db.String(32))
    version = db.Column(db.Integer, db.ForeignKey(Version.id))

    def __repr__(self):
        return "<Entity Category (category='%s')>" % self.category