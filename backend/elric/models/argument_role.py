from .version import Version
from elric import db

class ArgumentRole(db.Model):
    __tablename__ = 'argument_roles'
    __table_args__ = {'mysql_engine': 'InnoDB'}

    id = db.Column(db.Integer, primary_key=True)
    role = db.Column(db.String(32))
    version = db.Column(db.Integer, db.ForeignKey(Version.id))

    def __repr__(self):
        return "<Argument Role(role='%s', start='%s', end='%s', text='%s')>" % self.role