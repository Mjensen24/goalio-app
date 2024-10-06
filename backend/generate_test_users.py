from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, User
from datetime import datetime
import random
import sys

# Database connection
DATABASE_URL = "sqlite:///./task_manager.db"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def create_test_users(num_users=10):
    session = SessionLocal()
    
    try:
        # Create the specific user you requested
        grace = User(
            username="gracebrown39",
            email="gracebrown39@example.com",
            role="User",
            created_at=datetime.utcnow()
        )
        grace.set_password("password123")
        session.add(grace)
        print(f"Created user: {grace.username}")

        # Create additional random users
        for i in range(num_users - 1):
            username = f"user{random.randint(1000, 9999)}"
            email = f"{username}@example.com"
            role = random.choice(["Admin", "User", "Manager"])
            
            new_user = User(
                username=username,
                email=email,
                role=role,
                created_at=datetime.utcnow()
            )
            new_user.set_password("password123")
            session.add(new_user)
            print(f"Created user: {new_user.username}")

        session.commit()
        print(f"{num_users} test users created successfully.")
    
    except Exception as e:
        print(f"An error occurred: {e}")
        print(f"Error type: {type(e).__name__}")
        print(f"Error details: {str(e)}")
        print("Traceback:")
        import traceback
        traceback.print_exc()
        session.rollback()
    finally:
        session.close()

if __name__ == "__main__":
    print(f"Python version: {sys.version}")
    create_test_users()