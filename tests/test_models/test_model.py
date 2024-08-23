from sqlalchemy import inspect, Integer, String
from apps.models.models import Item


def test_item_model_columns():
    # Get the inspector for the Item model
    mapper = inspect(Item)

    # Get all column names
    column_names = [column.name for column in mapper.columns]

    # Test if the columns exist
    assert "id" in column_names
    assert "name" in column_names
    assert "description" in column_names


def test_item_model_column_types():
    # Get the inspector for the Item model
    mapper = inspect(Item)

    # Test if the columns have the correct types
    id_column = mapper.columns["id"]
    name_column = mapper.columns["name"]
    description_column = mapper.columns["description"]

    assert isinstance(id_column.type, Integer)
    assert isinstance(name_column.type, String)
    assert isinstance(description_column.type, String)


def test_item_model_primary_key():
    # Get the inspector for the Item model
    mapper = inspect(Item)

    # Test if the primary key is set correctly
    id_column = mapper.columns["id"]
    assert id_column.primary_key is True


def test_item_model_indexes():
    # Get the inspector for the Item model
    mapper = inspect(Item)

    # Test if the indexed columns are correct
    indexed_columns = [index.name for index in mapper.columns if index.index]

    assert "id" in indexed_columns
    assert "name" in indexed_columns
    assert "description" in indexed_columns
