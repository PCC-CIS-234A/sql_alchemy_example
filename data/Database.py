from sqlalchemy import create_engine, select
from sqlalchemy.orm import sessionmaker
from data.models import Names, NameCounts, YearGenderTotals

# Connects to the database and includes a method that fetches data. Reuses the database connection for efficiency.
USES_PYODBC = False  # change this to True to use pyodbc instead of pymssql.
MS_ODBC_17 = False  # False means use MSODBC 18 instead of the older version 17 with pyodbc

class Database:
    USERNAME = "275student"
    PASSWORD = "275student"
    SERVER = "cisdbss.pcc.edu"
    DATABASE = "NAMES"
    engine = None
    SessionLocal = None

    @classmethod
    def connect(cls):
        if cls.engine is None:
            if USES_PYODBC:
                driver = "pyodbc"
                if MS_ODBC_17:
                    odbc_driver = "?driver=ODBC Driver 17 for SQL Server"
                else:
                    odbc_driver = "?driver=ODBC Driver 18 for SQL Server&TrustServerCertificate=Yes"
            else:
                driver = "pymssql"
                odbc_driver = ""  # pymssql doesn't use MS ODBC at all

            connection_string = (f"mssql+{driver}://{cls.USERNAME}:{cls.PASSWORD}@{cls.SERVER}/{cls.DATABASE}"
                                 + odbc_driver)

            cls.engine = create_engine(connection_string)
            cls.SessionLocal = sessionmaker(bind=cls.engine)
        return cls.engine

    @classmethod
    def read_names(cls, name, gender):
        engine = cls.connect()
        stmt = (
            select(Names.Name, YearGenderTotals.Gender, YearGenderTotals.Year, NameCounts.NameCount)
            .join(NameCounts, Names.name_counts)
            .join(YearGenderTotals, NameCounts.year_gender_total)
            .filter(Names.Name == name, YearGenderTotals.Gender == gender)
            .order_by(YearGenderTotals.Year.asc())
        )

        with cls.SessionLocal() as session:
            results = session.execute(stmt).all()

        return results

