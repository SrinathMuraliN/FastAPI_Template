import sys
import os
from fastapi.testclient import TestClient
from fastapi import status

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..')))

from  main import app
import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from utility.db_connection import Base, get_db



claint = TestClient(app)

  
    
# Create an in-memory SQLite database for testing
SQLALCHEMY_DATABASE_URL = "sqlite:///./testdb.db"

engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Dependency override for the test database
def override_get_db():
    try:
        db = TestingSessionLocal()
        yield db
    finally:
        db.close()

# Override the get_db dependency with the test database
app.dependency_overrides[get_db] = override_get_db

# Create the test client
client = TestClient(app)

@pytest.fixture(scope="module")
def setup_db():
    # Create tables in the test database
    Base.metadata.create_all(bind=engine)
    yield
    # Drop tables after tests complete
    Base.metadata.drop_all(bind=engine)

# def test_get_users(setup_db):
#     response = client.get("/get_user", headers={"Authorization": "Bearer testtoken"})
#     assert response.status_code == 200
#     # Add additional checks for the response content

# def test_read_item(setup_db):
#     response = client.get("/items/1", headers={"Authorization": "Bearer testtoken"})
#     assert response.status_code == 200
#     assert response.json() == {"item_id": 1, "q": None}

def test_read_item_name(setup_db):
    response = client.get("/db_item/1", headers={"Authorization": "Bearer testtoken"})
    assert response.status_code in [200, 404]  # Depending on test data
    # If using test data, add checks for the response content

def test_create_user(setup_db):
    new_user = {
        "name": "testuser",
        "email_id": "testuser@example.com",
        "role": "user"  # Assuming "user" is a valid role
    }
    response = client.post("/users/", json=new_user)  # Update the endpoint if necessary
    assert response.status_code == 200
    assert response.json() == new_user  # Optional: Assert the response matches the input

    # Add additional checks for the response content

def test_update_user(setup_db):
    updated_user = {
        "username": "updateduser",
        "email": "updateduser@example.com"
    }
    response = client.put("/user/1", json=updated_user)
    assert response.status_code in [200, 404]  # Depending on test data
    # If using test data, add checks for the response content

def test_delete_user(setup_db):
    response = client.delete("/user/1")
    assert response.status_code in [200, 404]  # Depending on test data
    # If using test data, add checks for the response content

    
    
    
    
    
    