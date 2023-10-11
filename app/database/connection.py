from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.utils.environment import get_db_uri

engine = create_engine(
    get_db_uri(with_driver=True),
    echo=True
)
# distributed to application
Session = sessionmaker(engine)

# yields a new session
def yield_db_session():
    session = Session()
    yield session
    # close session
    session.close()
