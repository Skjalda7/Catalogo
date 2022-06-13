from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, Integer, String, VARCHAR
from datos import bbdd

engine = create_engine('postgresql://postgres:password@localhost/pelis')
Base = declarative_base()

class catalogo(Base):
    __tablename__ = 'catalogo'

    id = Column(Integer(), primary_key=True)
    type = Column(VARCHAR())
    title = Column(VARCHAR())
    director = Column(VARCHAR())
    cast = Column(VARCHAR())
    country = Column(VARCHAR())
    release_year = Column(Integer())
    rating = Column(VARCHAR())
    duration = Column(VARCHAR())
    genre = Column(VARCHAR())
    description = Column(String())
    plataforma = Column(VARCHAR())

    def __str__(self):
        return self.type


Session = sessionmaker(engine)
session = Session()

if __name__ == '__main__':
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)

bbdd.to_sql('catalogo', if_exists='append', con=engine, index=False)