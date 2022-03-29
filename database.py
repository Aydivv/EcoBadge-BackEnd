import sqlalchemy as _sql
import sqlalchemy.ext.declarative as _declarative
import sqlalchemy.orm as _orm
from sqlalchemy.exc import SQLAlchemyError

SQL_ALCHEMY_DATABASE_URL = "mysql+pymysql://b14a34d3a49e5b:aa7154b7@us-cdbr-east-05.cleardb.net/heroku_c46436a436c08a3"

engine = _sql.create_engine(SQL_ALCHEMY_DATABASE_URL)



session = _orm.sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = _declarative.declarative_base()
