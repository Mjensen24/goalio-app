import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import SQLAlchemyError
import logging

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Import all models, removing TaskTag
from models import Base, User, Project, Task, Comment, Tag

DATABASE_URL = "sqlite:///./task_manager.db"
engine = create_engine(DATABASE_URL, echo=True)  # echo=True will log all SQL commands
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def init_db():
    try:
        Base.metadata.create_all(bind=engine)
        logger.info("Tables created successfully!")
    except SQLAlchemyError as e:
        logger.error(f"An error occurred while creating tables: {e}")

if __name__ == "__main__":
    init_db()
    
    # Check if the database file was created
    if os.path.exists("./task_manager.db"):
        logger.info("Database file 'task_manager.db' was created successfully.")
    else:
        logger.warning("Database file 'task_manager.db' was not created.")

    # Try to create a session and make a simple query for each model
    try:
        session = SessionLocal()
        for model in [User, Project, Task, Comment, Tag]:
            count = session.query(model).count()
            logger.info(f"Number of {model.__name__} entries: {count}")
    except SQLAlchemyError as e:
        logger.error(f"An error occurred while querying the database: {e}")
    finally:
        session.close()