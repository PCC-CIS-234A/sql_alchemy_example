from sqlalchemy import Column, Integer, String, CHAR, ForeignKey
from sqlalchemy.orm import declarative_base, relationship

# SQL Alchemy Models, match the NAMES database on cisdbss.pcc.edu (excluding some columns we don't need
# for this example).

Base = declarative_base()


class Names(Base):
    __tablename__ = 'names'
    NameID = Column(Integer, primary_key=True)
    Name = Column(String)

    name_counts = relationship("NameCounts", back_populates="name")


class NameCounts(Base):
    __tablename__ = 'name_counts'
    ID = Column(Integer, primary_key=True)
    FK_NameID = Column(Integer, ForeignKey('names.NameID'))
    FK_YearGenderTotalID = Column(Integer, ForeignKey('year_gender_totals.YearGenderTotalID'))
    NameCount = Column(Integer)

    name = relationship("Names", back_populates="name_counts")
    year_gender_total = relationship("YearGenderTotals", back_populates="name_counts")


class YearGenderTotals(Base):
    __tablename__ = 'year_gender_totals'
    YearGenderTotalID = Column(Integer, primary_key=True)
    Year = Column(Integer)
    Gender = Column(CHAR(1))

    name_counts = relationship("NameCounts", back_populates="year_gender_total")
