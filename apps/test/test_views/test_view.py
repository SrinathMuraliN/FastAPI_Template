import os
import sys
from fastapi import status
from fastapi.testclient import TestClient
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..')))
import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from test_dbconnect import engine,override_get_db
from main import app
from utility.db_connection import Base, get_db

# claint = TestClient(app)

  
    
# # Create an in-memory SQLite database for testing
# SQLALCHEMY_DATABASE_URL = "sqlite:///./testdb.db"

# engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
# TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# # Dependency override for the test database
# def override_get_db():
#     try:
#         db = TestingSessionLocal()
#         yield db
#     finally:
#         db.close()


app.dependency_overrides[get_db] = override_get_db


client = TestClient(app)

@pytest.fixture(scope="module")
def setup_db():
    
    Base.metadata.create_all(bind=engine)
    yield
    
    Base.metadata.drop_all(bind=engine)


def test_get_users():
    response = client.get("api/get_user/", headers={"Authorization": "Bearer testtoken"})
    assert response.status_code == 200
    

def test_read_item(setup_db):
    response = client.get("api/items/1", headers={"Authorization": "Bearer testtoken"})
    assert response.status_code == 200
    assert response.json() == {"item_id": 1, "q": None}

def test_read_item_name(setup_db):
    response = client.get("/db_item/1", headers={"Authorization": "Bearer testtoken"})
    assert response.status_code in [200, 404] 

def test_create_user(setup_db):
    new_user = {
        "name": "testuser",
        "email_id": "testuser@example.com",
        "role": "user"  
    }
    response = client.post("api/user/", json=new_user) 
    assert response.json() == new_user

#     

def test_update_user(setup_db):
    updated_user = {
        "username": "updateduser",
        "email": "updateduser@example.com"
    }
    response = client.put("/user/1", json=updated_user)
    assert response.status_code in [200, 404] 

def test_delete_user(setup_db):
    response = client.delete("/user/1")
    assert response.status_code in [200, 404]  

    
    
    
    
    
    