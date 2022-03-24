import sqlalchemy as _sql
import sqlalchemy.ext.declarative as _declarative
import sqlalchemy.orm as _orm
from sqlalchemy.exc import SQLAlchemyError

SQL_ALCHEMY_DATABASE_URL = "mysql+pymysql://root:jabalpur@localhost:3306/ecobadge"

engine = _sql.create_engine(SQL_ALCHEMY_DATABASE_URL)



session = _orm.sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = _declarative.declarative_base()
