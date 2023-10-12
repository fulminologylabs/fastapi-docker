from sqlalchemy import create_engine
from typing import Generator
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy.orm.session import Session
from app.utils.environment import get_db_uri

def db_dep_injector():
    """
    Used to dependency inject a database session, per API request
    """
    session = _get_session_factory()
    db = session()
    try:
        yield db
    finally:
        db.close()

def _get_session_factory() -> sessionmaker:
    """
        Called by scoped sessions and dependency injection
        connection generators
    """
    engine = create_engine(
        get_db_uri(with_driver=True),
        pool_pre_ping=True,
    )
    return sessionmaker(autocommit=False, autoflush=False, bind=engine)

# def db_scoped_session():
#     """
#         Used to provide client/service class instances
        
#         with their own thread-local connection: 
#         https://docs.sqlalchemy.org/en/13/orm/contextual.html#thread-local-scope
#     """
#     session_factory = _get_session_factory()
#     session = scoped_session(session_factory)
#     try:
#         yield session()
#     finally:
#         session.remove()
