# import pytest
# from fastapi.testclient import TestClient
# from sqlalchemy.orm import Session
# from unittest.mock import MagicMock

# from main import app  # Import your FastAPI app from your main file
# from apps.repository.repository import UserRepository
# from apps.serializer.serializer import UserCreate, UserUpdate


# # Create a TestClient instance for making requests to your FastAPI app
# client = TestClient(app)


# def test_get_users():
#     response = client.get("/get_user", headers={"Authorization": "Bearer testtoken"})
#     assert response.status_code == 200
#     assert isinstance(response.json(), list)


# def test_read_item():
#     response = client.get("/items/1", headers={"Authorization": "Bearer testtoken"})
#     assert response.status_code == 200
#     assert response.json() == {"item_id": 1, "q": None}

#     response = client.get("/items/0", headers={"Authorization": "Bearer testtoken"})
#     assert response.status_code == 400
#     assert response.json() == {"detail": "Invalid ID"}


# def test_read_item_name(monkeypatch):
#     # Mocking the database query
#     mock_db_item = {"item_id": 1, "name": "Item Name", "description": "Item Description"}
#     mock_get_item = MagicMock(return_value=mock_db_item)
#     monkeypatch.setattr(UserRepository, "get_item", mock_get_item)

#     response = client.get("/db_item/1", headers={"Authorization": "Bearer testtoken"})
#     assert response.status_code == 200
#     assert response.json() == mock_db_item

#     # Test item not found
#     mock_get_item.return_value = None
#     response = client.get("/db_item/99", headers={"Authorization": "Bearer testtoken"})
#     assert response.status_code == 404
#     assert response.json() == {"detail": "Item not found"}


# def test_create_user(monkeypatch):
#     mock_db_item = {"id": 1, "name": "Test User", "email": "test@example.com"}
#     mock_create_user = MagicMock(return_value=mock_db_item)
#     monkeypatch.setattr(UserRepository, "create_user", mock_create_user)

#     user_data = {"name": "Test User", "email": "test@example.com", "password": "password123"}
#     response = client.post("/user/", json=user_data)
#     assert response.status_code == 200
#     assert response.json() == mock_db_item


# def test_update_user(monkeypatch):
#     mock_db_item = {"id": 1, "name": "Updated User", "email": "updated@example.com"}
#     mock_update_user = MagicMock(return_value=mock_db_item)
#     monkeypatch.setattr(UserRepository, "update_user", mock_update_user)

#     user_data = {"name": "Updated User", "email": "updated@example.com"}
#     response = client.put("/user/1", json=user_data)
#     assert response.status_code == 200
#     assert response.json() == mock_db_item

#     # Test user not found
#     mock_update_user.return_value = None
#     response = client.put("/user/99", json=user_data)
#     assert response.status_code == 404
#     assert response.json() == {"detail": "Item not found"}


# def test_delete_user(monkeypatch):
#     mock_delete_user = MagicMock(return_value={"msg": "User deleted"})
#     monkeypatch.setattr(UserRepository, "delete_user", mock_delete_user)

#     response = client.delete("/user/1")
#     assert response.status_code == 200

#     # Test user not found
#     mock_delete_user.return_value = None
#     response = client.delete("/user/99")
#     assert response.status_code == 404
#     assert response.json() == {"detail": "Item not found"}
