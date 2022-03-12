import sqlalchemy as _sql
import sqlalchemy.ext.declarative as _declarative
import sqlalchemy.orm as _orm
from sqlalchemy.exc import SQLAlchemyError

SQL_ALCHEMY_DATABASE_URL = "mysql+pymysql://root:jabalpur@localhost:3306/ecobadge"

engine = _sql.create_engine(SQL_ALCHEMY_DATABASE_URL)

try:
    engine.connect()
    print("SQL connected")
except SQLAlchemyError as err:
    print("error", err.__cause__)

session = _orm.sessionmaker(autocommit=False, autoFlush=False, bind=engine)

Base = _declarative.declarative_base()
