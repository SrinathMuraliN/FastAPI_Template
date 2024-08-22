import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
# from apps.user_management.db_connection import Base, get_db
# from FastAPI_Template.apps.user_management.db_connection import Base, get_db

from main import app

# Configure test database
SQLALCHEMY_DATABASE_URL = "sqlite:///./testone.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create test client
client = TestClient(app)

# Override the get_db dependency with the test database
def override_get_db():
    try:
        db = TestingSessionLocal()
        yield db
    finally:
        db.close()

app.dependency_overrides[get_db] = override_get_db

# Create the database tables for testing
@pytest.fixture(autouse=True)
def setup_db():
    Base.metadata.create_all(bind=engine)
    yield
    Base.metadata.drop_all(bind=engine)


def test_get_users():
    response = client.get("/get_user")
    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_read_item_valid():
    response = client.get("/items/1")
    assert response.status_code == 200
    assert response.json() == {"item_id": 1, "q": None}


def test_read_item_invalid():
    response = client.get("/items/0")
    assert response.status_code == 400
    assert response.json() == {"detail": "Invalid ID"}


def test_read_item_name_found():
    # Add item to the database before running the test
    db = next(override_get_db())
    db_item = Item(name="Test Item")
    db.add(db_item)
    db.commit()
    db.refresh(db_item)

    response = client.get(f"/db_item/{db_item.id}")
    assert response.status_code == 200
    assert response.json()["name"] == "Test Item"


def test_read_item_name_not_found():
    response = client.get("/db_item/999")
    assert response.status_code == 404
    assert response.json() == {"detail": "Item not found"}


def test_create_user():
    user_data = {
        "username": "testuser",
        "email": "testuser@example.com",
        "password": "password"
    }
    response = client.post("/user/", json=user_data)
    assert response.status_code == 200
    assert response.json()["username"] == "testuser"
    assert response.json()["email"] == "testuser@example.com"


def test_update_user():
    # Create a user to update
    user_data = {
        "username": "updateuser",
        "email": "updateuser@example.com",
        
    }
    response = client.post("/user/", json=user_data)
    user_id = response.json()["id"]

    # Update the user
    updated_data = {
        "username": "updateduser",
        "email": "updateduser@example.com"
    }
    response = client.put(f"/user/{user_id}", json=updated_data)
    assert response.status_code == 200
    assert response.json()["username"] == "updateduser"
    assert response.json()["email"] == "updateduser@example.com"


def test_delete_user():
    # Create a user to delete
    user_data = {
        "username": "deleteuser",
        "email": "deleteuser@example.com",
        
    }
    response = client.post("/user/", json=user_data)
    user_id = response.json()["id"]

    # Delete the user
    response = client.delete(f"/user/{user_id}")
    assert response.status_code == 200

    # Ensure the user is deleted
    response = client.get(f"/user/{user_id}")
    assert response.status_code == 404
