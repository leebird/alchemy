from sqlalchemy import create_engine

from db.base import Base

# CREATE DATABASE alchemy
# DEFAULT CHARACTER SET utf8
# DEFAULT COLLATE utf8_unicode_ci;

if __name__ == '__main__':
    engine = create_engine('mysql+pymysql://root:198884@localhost/alchemy')
    Base.metadata.create_all(engine, checkfirst=True)