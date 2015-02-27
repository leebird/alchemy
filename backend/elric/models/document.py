from db.base import Base
from sqlalchemy import Column, Integer, String, Text

class Document(Base):
    __tablename__ = 'documents'
    __table_args__ = {'mysql_engine': 'InnoDB'}

    id = Column(Integer, primary_key=True)
    document_id = Column(String(40))
    text = Column(Text)

    def __repr__(self):
        return "<Document(id='%s', text='%s')>" % self.doc_id, self.text