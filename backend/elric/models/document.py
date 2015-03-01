from elric import db

class Document(db.Model):
    __tablename__ = 'documents'
    __table_args__ = {'mysql_engine': 'InnoDB'}

    id = db.Column(db.Integer, primary_key=True)
    document_id = db.Column(db.String(64))
    text = db.Column(db.Text)

    def __repr__(self):
        return "<Document(id='%s', text='%s')>" % self.doc_id, self.text