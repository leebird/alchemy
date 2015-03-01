from elric import db
from .version import Version
from .document import Document
from .entity_category import EntityCategory

class Entity(db.Model):
    __tablename__ = 'entities'
    __table_args__ = {'mysql_engine': 'InnoDB'}

    id = db.Column(db.Integer, primary_key=True)
    document = db.Column(db.Integer, db.ForeignKey(Document.id))
    category = db.Column(db.Integer, db.ForeignKey(EntityCategory.id))
    start = db.Column(db.Integer)
    end = db.Column(db.Integer)
    text = db.Column(db.Text)
    properties = db.relationship('EntityProperty')
    version = db.Column(db.Integer, db.ForeignKey(Version.id))

    def __repr__(self):
        return "<Entity(category='%s', start='%s', end='%s', text='%s')>" % (
            self.category, self.start, self.end, self.text)