from .version import Version
from elric import db

class EventCategory(db.Model):
    __tablename__ = 'event_category'
    __table_args__ = {'mysql_engine': 'InnoDB'}

    id = db.Column(db.Integer, primary_key=True)
    category = db.Column(db.String(32))
    version = db.Column(db.Integer, db.ForeignKey(Version.id))

    def __repr__(self):
        return "<Event Category(category='%s')>" % self.category